#! /usr/bin/env python
"""
Simple solver for Te in cylindrical geometry

David.Coster@ipp.mpg.de
"""
import numpy as np

def F_ped(r, b_pos, b_height, b_sol, b_width, b_slope):
    """
    Create a density profile using an mtanh profile
    :param r: position in rho_norm where the density is wanted
    :type r: numpy float scalar or array
    :param b_pos: position of density pedestal (-)
    :type b_pos: numpy float
    :param b_height: height of density pedestal (m^-3)
    :type b_height: numpy float
    :param b_sol: sol value for density pedestal (m^-3)
    :type b_sol: numpy float
    :param b_width: width of density pedestal (-)
    :type b_width: numpy float
    :param b_slope: slope of density pedestal (?)
    :type b_slope: numpy float
    :return: value of density at r
    :rtype: numpy float scalar or array (sime dimensions as r)
    """
    return (b_height - b_sol)/2*(mtanh((b_pos - r)/(2 * b_width), b_slope)+1)+b_sol

def mtanh(x, b_slope):
    """
    modified tanh function
    :param x: position to evaluate function
    :type x: numpy float scalar or array
    :param b_slope: interior slope
    :type b_slope: numpy float
    :return: value of the mtanh function evaluated at x
    :rtype: numpy float scalar or array (sime dimensions as x)

    See https://pdfs.semanticscholar.org/5dc9/029eb9614a0128ae7c3f16ae6c4e54be4ac5.pdf
    for the mtanh definition
    """
    return ((1 + b_slope * x)*np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def solve_Te(Qe_tot=2e6, H0=0, Hw=0.1, Te_bc=100, chi=1, a0=1, R0=3, E0=1.5, b_pos=0.98, b_height=6e19, b_sol=2e19, b_width=0.01, b_slope=0.01, nr=100, dt=100, plots=True, output=True):
    """
    :param Qe_tot: heating power [W]
    :type Qe_tot: numpy float
    :param H0: position of Gaussian [-]
    :type H0: numpy float
    :param Hw: width of Gaussian [-]
    :type Hw: numpy float
    :param Te_bc: outer edge Te boundary condition [eV]
    :type Te_bc: numpy float
    :param chi: thermal diffusivity [?]
    :type chi: numpy float
    :param a0: minor radius [m]
    :type a0: numpy float
    :param R0: major radius [m]
    :type R0: numpy float
    :param E0: ellipticity
    :type E0: numpy float
    :param b_pos: position of density pedestal [-]
    :type b_pos:  numpy float
    :param b_height: height of density pedestal [m^-3]
    :type b_height: numpy float
    :param b_sol: sol value for density pedestal [m^-3]
    :type b_sol: numpy float
    :param b_width: width of density pedestal [-]
    :type b_width: numpy float
    :param b_slope: slope of density pedestal [?]
    :type b_slope: numpy float
    :param nr: number of radial grid points
    :type nr: inteher
    :param dt: time-step [s]
    :type dt: numpy float
    :param plots: enable plots
    :type plots: boolean
    :param output: enable output of some diagnostic information
    :type output: boolean
    :return: array of Te values [eV]
    :type: numpy float array
    :return: array of ne values [m^-3]
    :type: numpy float array
    :return: rho values corresponding to the Te and ne values [m]
    :type: numpy float array
    :return: rho_norm values corresponding to the Te and ne values [-]
    :type: numpy float array

    David.Coster@ipp.mpg.de
    """

    if plots:
        import os
        import matplotlib
        if not os.getenv("DISPLAY"): matplotlib.use('Agg')
        import matplotlib.pylab as plt

    import scipy.constants
    from fipy import Variable, FaceVariable, CellVariable, TransientTerm, DiffusionTerm, Viewer, meshes

    a = a0*np.sqrt(E0)
    V = 2*np.pi * 2*np.pi*R0
    mesh = meshes.CylindricalGrid1D(nr=nr, Lr=a)
    Te = CellVariable(name="Te", mesh=mesh, value=1e3)
    ne = CellVariable(name="ne", mesh=mesh, value=F_ped(mesh.cellCenters.value[0]/a, b_pos, b_height, b_sol, b_width, b_slope))
    Qe = CellVariable(name="Qe", mesh=mesh, value=np.exp(-((mesh.cellCenters.value/a-H0)/(Hw))**2)[0])
    Qe = Qe * Qe_tot/((mesh.cellVolumes*Qe.value).sum() * V)

    if output:
        print('Volume = %s m^3' % (mesh.cellVolumes.sum() * V))
        print('Heating power = %0.3e W' % ((mesh.cellVolumes*Qe).sum() * V))

    Te.constrain(Te_bc, mesh.facesRight)
    eqI = TransientTerm(coeff=scipy.constants.e*ne*1.5) == DiffusionTerm(coeff=scipy.constants.e*ne*chi) + Qe

    if plots: viewer = Viewer(vars=(Te), title='Heating power = %0.3e W\nchi = %s' % (Qe.cellVolumeAverage.value * V, chi), datamin=0, datamax=5000)

    eqI.solve(var=Te, dt=dt)
    if plots: viewer.plot()

    return Te.value, ne.value, mesh.cellCenters.value[0], mesh.cellCenters.value[0]/a

if __name__ == '__main__':
    solve_Te()

"""
to test:

  import fusion
  Te, ne, rho, rho_norm = fusion.solve_Te()

"""
