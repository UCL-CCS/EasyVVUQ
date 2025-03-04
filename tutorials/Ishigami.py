#! /usr/bin/env python

import sys
import json
import numpy as np

"""
Three-dimensional test function of Ishigami, based on the code in pygpc

The Ishigami function of Ishigami & Homma (1990) [1] is used as an example
for uncertainty and sensitivity analysis methods, because it exhibits
strong nonlinearity and nonmonotonicity. It also has a peculiar
dependence on x3, as described by Sobol' & Levitan (1999) [2].
The values of a and b used by Crestaux et al. (2007) [3] and Marrel et al. (2009) [4] are: a = 7 and b = 0.1.

.. math:: y = \sin(x_1) + a \sin(x_2)^2 + b x_3^4 \sin(x_1)

Parameters
----------
p["x1"]: float or ndarray of float [n_grid]
    First parameter defined in [-pi, pi]
p["x2"]: float or ndarray of float [n_grid]
    Second parameter defined in [-pi, pi]
p["x3"]: float or ndarray of float [n_grid]
    Third parameter defined in [-pi, pi]
p["a"]: float
    shape parameter (a=7)
p["b"]: float
    shape parameter (b=0.1)

Returns
-------
y: ndarray of float [n_grid x 1]
    Output data

Notes
-----
.. plot::

   import numpy as np
   from pygpc.testfunctions import plot_testfunction as plot
   from collections import OrderedDict

   parameters = OrderedDict()
   parameters["x1"] = np.linspace(-np.pi, np.pi, 100)
   parameters["x2"] = np.linspace(-np.pi, np.pi, 100)

   constants = OrderedDict()
   constants["a"] = 7.
   constants["b"] = 0.1
   constants["x3"] = 0.

   plot("Ishigami", parameters, constants)

.. [1] Ishigami, T., Homma, T. (1990, December). An importance quantification
   technique in uncertainty analysis for computer models. In Uncertainty
   Modeling and Analysis, 1990. Proceedings., First International Symposium
   on (pp. 398-403). IEEE.

.. [2] Sobol', I.M., Levitan, Y.L. (1999). On the use of variance reducing
   multipliers in Monte Carlo computations of a global sensitivity index.
   Computer Physics Communications, 117(1), 52-61.

.. [3] Crestaux, T., Martinez, J.-M., Le Maitre, O., & Lafitte, O. (2007).
   Polynomial chaos expansion for uncertainties quantification and sensitivity analysis [PowerPoint slides].
   Retrieved from SAMO 2007 website: http://samo2007.chem.elte.hu/lectures/Crestaux.pdf.

.. [4] Marrel, A., Iooss, B., Laurent, B., & Roustant, O. (2009).
   Calculations of sobol indices for the gaussian process metamodel.
   Reliability Engineering & System Safety, 94(3), 742-751.
"""

def evaluate(x1, x2, x3, a, b):
    return np.sin(x1) + a * np.sin(x2) ** 2 + b * x3 ** 4 * np.sin(x1)



# author: David Coster (based on work from Jalal Lakhlili)

if __name__ == '__main__':
    json_input = sys.argv[1]
    with open(json_input, "r") as f:
        inputs = json.load(f)

    y_out = evaluate(x1 = float(inputs['x1']),
                     x2 = float(inputs['x2']),
                     x3 = float(inputs['x3']),
                     a = float(inputs['a']),
                     b = float(inputs['b']))

    output_filename = inputs['out_file']

    # output csv file
    header = 'Ishigami'
    np.savetxt(output_filename,  np.atleast_1d(np.array(y_out)),
               delimiter=",", comments='',
               header=header)
