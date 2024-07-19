.. _fusion_tutorial:

A Reduced Version of the Fusion Workflow using Polynomial Chaos Expansion
=========================================================================

Within VECMA the fusion contributors (from the Max Planck Institute of
Plasma Physics) are building a multi-scale workflow looking at coupling
small space scale and fast time scale turbulence models with a larger
space and slower time scale transport model [FUSION-WF]_.

The following tutorial is designed to provide a simplified version of
the workflow that can show key aspects of the uncertainty
quantification applied to the full fusion workflow.

For the purposes of this tutorial, we introduce some simplifications
from the full fusion workflow:

- We replace the turbulence code with a simple specification of the
  transport coefficient specifying the thermal diffusivity.

- Instead of implementing the toroidal geometry used by the tokamak,
  we implement a cylindrical geometry which corresponds to
  straightening out the torus and increasing the aspect ratio (ratio
  of major radius of the torus to the minor radius of the torus).

  - This removes one code that is a part of the fusion workflow which
    is the calculation of the equilibrium geometry.

- Instead of doing a time-dependent analysis, we look for the steady
  state (or, more exactly, the long time) solution

.. figure:: ../images/cyl_jet.svg

We will perform a Polynomial Chaos Expansion for this cylindrical
model of a tokamak.

The model solves for the temperature, :math:`T(\rho, t)`, across the
cross-section of the cylinder, (:math:`\rho`), in the presence of a
specified thermal diffusivity and sources:

.. math:: \frac{3}{2}\;\;\frac{\partial}{\partial t}\left(n(\rho,t) T(\rho,t)\right) =
    \nabla_\rho \left[ n(\rho,t) \chi(\rho,t) \nabla_\rho
    (T(\rho,t))\right] + S(\rho, t)

with a boundary condition given by :math:`Te_{bc}` and an initial
uniform temperature of 1000 eV; the quantities are

:math:`n(\rho,t)` characterizes the plasma density

:math:`\chi(\rho,t)` characterizes the thermal conductivity

:math:`S(\rho,t)` characterizes the source

The geometry of the simulation is characterized by the minor radius
:math:`a_0`, major radius :math:`R_0` and elongation :math:`E_0`
(while the geometry is solved in the cylindrical approximation, the
actual radius used, :math:`a`, is adjusted on the basis of :math:`a_0`
and :math:`E_0`).

The density is specified by a modified tanh function (:math:`mtanh`) [MTANH]_ given by

.. math::
   n(\rho_{norm},t) = \frac{b_{height} - b_{sol}}{2} \; mtanh\left(\frac{b_{pos} - \rho_{norm}}{2 b_{width}}, b_{slope}\right)+1)+b_{sol}

Where

:math:`b_{height}` is the density at the top of the pedestal


:math:`b_{sol}` is the density at the base of the pedestal


:math:`b_{pos}` is the position of the pedestal


:math:`b_{width}` is the pedestal width

and

.. math::
   mtanh(x, b_{slope}) = \frac{(1 + x \cdot b_{slope}) exp(x) - exp(-x)}{exp(x) + exp(-x)}

A typical density profile used in these simulation is shown below:

.. figure:: ../images/ne.svg

The source is given by

.. math::
   S(\rho,t) = \alpha \cdot exp\left(-\left(\frac{\rho/a-H_0}{H_w}\right)^2\right)

where :math:`\alpha` is chosen so that :math:`\int\; S(\rho,t) dV =
Qe_{tot}`, the total heating power.

In this example we will analyze this model using the polynomial chaos
expansion (PCE) UQ algorithm.  The parameters that can be varied are:

==================    =======    =======   =========
    Quantity            Min        Max      Default
==================    =======    =======   =========
:math:`Qe_{tot}`       1.0e6      50.0e6      2e6
:math:`H_0`            0.00       1.0         0 
:math:`H_w`            0.01       100.0       0.1 
:math:`Te_{bc}`        10.0       1000.0      100
:math:`\chi`           0.01       100.0       1
:math:`a_0`            0.2        10.0        1
:math:`R_0`            0.5        20.0        3
:math:`E_0`            1.0        10.0        1.5
:math:`b_{pos}`        0.95       0.99        0.98
:math:`b_{height}`     3e19       10e19       6e19
:math:`b_{sol}`        2e18       3e19        2e19
:math:`b_{width}`      0.005      0.02        0.01
:math:`b_{slope}`      0.0        0.05        0.01
==================    =======    =======   =========

though we will restrict the variation to

================  ============  ================
   Quantity       Distribution        Range
================  ============  ================
:math:`Qe_{tot}`     Uniform    (1.8e6, 2.2e6)
:math:`H_0`          Uniform    (0.0,   0.2)
:math:`H_w`          Uniform    (0.1,   0.5),
:math:`\chi`         Uniform    (0.8,   1.2), 
:math:`Te_{bc}`      Uniform    (80.0,  120.0)
================  ============  ================

for this analysis.

Below we provide a commented script that shows how the Campaign is built up and then employed.
We also provide an outline of how each element is setup.

EasyVVUQ Script Overview
------------------------

We illustrate the intended workflow using the following basic example
script, a python implementation of the reduced fusion workflow model. 

The input files for this tutorial are

- the *fusion* application
  (:download:`fusion.py <../../tutorials/fusion.py>`),

- the *fusion* application interface to uq
  (:download:`fusion_model.py <../../tutorials/fusion_model.py>`),

- an input template
  (:download:`fusion.template <../../tutorials/fusion.template>`),

- the EasyVVUQ workflow script
  (:download:`easyvvuq_fusion_tutorial.py <../../tutorials/easyvvuq_fusion_tutorial.py>`)

- the EasyVVUQ workflow script demonstrating the use of dask
  (:download:`easyvvuq_fusion_dask_tutorial.py <../../tutorials/easyvvuq_fusion_dask_tutorial.py>`)

Note: the fusion tutorial uses the FiPy [FiPy]_ python package.

To run the script execute the following command

``python3 easyvvuq_fusion_tutorial.py``

Import necessary libraries
--------------------------

For this example we import both easyvvuq and chaospy (for the
distributions). EasyVVUQ will be referred to as 'uq' in the code. ::

    import easyvvuq as uq
    import chaospy as cp

Create a new Campaign
---------------------

As in the :doc:`Basic Tutorial <basic\_tutorial>`, we start by
creating an EasyVVUQ Campaign. Here we call it 'fusion_pce.'. ::

    my_campaign = uq.Campaign(name='fusion_pce.')

Parameter space definition
--------------------------

The parameter space is defined using a dictionary. Each entry in the
dictionary follows the format:

``"parameter_name": {"type" : "<value>", "min": <value>, "max": <value>, "default": <value>}``

With a defined type, minimum and maximum value and default. If the
parameter is not selected to vary in the Sampler (see below) then the
default value is used for every run. In this example, our full
parameter space looks like the following: ::

    params = {
              "Qe_tot":   {"type": "float",   "min": 1.0e6, "max": 50.0e6, "default": 2e6}, 
	      "H0":       {"type": "float",   "min": 0.00,  "max": 1.0,    "default": 0}, 
	      "Hw":       {"type": "float",   "min": 0.01,  "max": 100.0,  "default": 0.1}, 
	      "Te_bc":    {"type": "float",   "min": 10.0,  "max": 1000.0, "default": 100}, 
	      "chi":      {"type": "float",   "min": 0.01,  "max": 100.0,  "default": 1}, 
	      "a0":       {"type": "float",   "min": 0.2,   "max": 10.0,   "default": 1}, 
	      "R0":       {"type": "float",   "min": 0.5,   "max": 20.0,   "default": 3}, 
	      "E0":       {"type": "float",   "min": 1.0,   "max": 10.0,   "default": 1.5}, 
	      "b_pos":    {"type": "float",   "min": 0.95,  "max": 0.99,   "default": 0.98}, 
	      "b_height": {"type": "float",   "min": 3e19,  "max": 10e19,  "default": 6e19}, 
	      "b_sol":    {"type": "float",   "min": 2e18,  "max": 3e19,   "default": 2e19}, 
	      "b_width":  {"type": "float",   "min": 0.005, "max": 0.02,   "default": 0.01}, 
	      "b_slope":  {"type": "float",   "min": 0.0,   "max": 0.05,   "default": 0.01}, 
	      "nr":       {"type": "integer", "min": 10,    "max": 1000,   "default": 100}, 
	      "dt":       {"type": "float",   "min": 1e-3,  "max": 1e3,    "default": 100},
	      "out_file": {"type": "string",  "default": "output.csv"}
	     }

App Creation
------------

In this example the GenericEncoder and SimpleCSV, both included in the
core EasyVVUQ library, were used as the encoder/decoder pair for this
application. ::

    encoder = uq.encoders.GenericEncoder(
        template_fname='tutorial_files/fusion.template',
        delimiter='$',
        target_filename='fusion_in.json')

    decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                output_columns=["te", "ne", "rho", "rho_norm"])

GenericEncoder performs simple text substitution into a supplied
template, using a specified delimiter to identify where parameters
should be placed.  The template is shown below (\$ is used as the
delimiter).  The template substitution approach is likely to suit most
simple applications but in practice many large applications have more
complex requirements, for example the multiple input files or the
creation of a directory hierarchy.  In such cases, users may write
their own encoders by extending the BaseEncoder class. ::

    {
       "Qe_tot": "$Qe_tot", 
       "H0": "$H0", 
       "Hw": "$Hw", 
       "Te_bc": "$Te_bc", 
       "chi": "$chi", 
       "a0": "$a0", 
       "R0": "$R0", 
       "E0": "$E0", 
       "b_pos": "$b_pos", 
       "b_height": "$b_height", 
       "b_sol": "$b_sol", 
       "b_width": "$b_width", 
       "b_slope": "$b_slope", 
       "nr": "$nr", 
       "dt": "$dt", 
       "out_file": "$out_file"
    }

As can be inferred from its name SimpleCSV reads CSV files produced by
the fusion model code. Again many applications output results in
different formats, potentially requiring bespoke Decoders. Having
created an encoder, decoder and parameter space definition for our
`fusion` app, we can add it to our campaign. ::

    # Add the app (automatically set as current app)
    my_campaign.add_app(name="fusion",
                        params=params,
                        encoder=encoder,
                        decoder=decoder)

The Sampler
-----------

The user specified which parameters will vary and their corresponding
distributions. In this case the :math:`Qe_{tot}`, :math:`H_0`,
:math:`H_w`, :math:`\chi` and :math:`Te_{bc}` parameters are varied, all
according to a uniform distribution: ::

    vary = {
            "Qe_tot":   cp.Uniform(1.8e6, 2.2e6),
	    "H0":       cp.Uniform(0.0,   0.2),
	    "Hw":       cp.Uniform(0.1,   0.5),
	    "chi":      cp.Uniform(0.8,   1.2), 
	    "Te_bc":    cp.Uniform(80.0,  120.0)
	   }

To perform a polynomial chaos expansion we will create a PCESampler,
informing it which parameters to vary, and what polynomial order to
use for the PCE. ::

    my_campaign.set_sampler(uq.sampling.PCESampler(vary=vary, polynomial_order=3))

Calling the campaign's draw\_samples() method will cause the specified
number of samples to be added as runs to the campaign database,
awaiting encoding and execution. If no arguments are passed to
draw\_samples() then all samples will be drawn, unless the sampler is
not finite. In this case PCESampler is finite (produces a finite
number of samples) and we elect to draw all of them at once: ::

    my_campaign.draw_samples()

Execute Runs
------------

my\_campaign.populate\_runs\_dir() will create a directory hierarchy
containing the encoded input files for every run that has not yet been
completed. Finally, in this example, a shell command is executed in
each directory to execute the simple test code. In practice (in a real
HPC workflow) this stage would be best handled using, for example, a
pilot job manager. ::

    import os
    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal("{} fusion_in.json".format(os.path.abspath('tutorial_files/fusion_model.py')), interpret="python3"))

Collation and analysis
----------------------

Calling my\_campaign.collate() at any stage causes the campaign to
aggregate decoded simulation output for all runs which have not yet
been collated. ::

    my_campaign.collate()

This collated data is stored in the campaign database. An analysis
element, here PCEAnalysis, can then be applied to the campaign's
collation result. ::

    my_campaign.apply_analysis(uq.analysis.PCEAnalysis(sampler=my_sampler, qoi_cols=["te", "ne", "rho", "rho_norm"]))

The output of this is dependent on the type of analysis element. ::

    # Get Descriptive Statistics
    results = my_campaign.get_last_analysis()
    stats = results['statistical_moments']['te']
    per = results['percentiles']['te']
    sobols = results['sobols_first']['te']

Typical results
---------------

The above workflow calculates the distribution of temeperatures as the
uncertain parameters are varied.  A typical results is shown below.

.. figure:: ../images/Te.svg

Here the mean temperature, the mean plus and minus one sigma, the 10
and 90 percentiles as well as the complete range are shown as a
function of :math:`\rho`.

The sensitivity of the results to the varying paramaters can be found
from the Sobol first

.. figure:: ../images/sobols_first.svg

and total coefficients

.. figure:: ../images/sobols_total.svg

Here it can be seen that the width of the heating source ("Hw") is the
most important determiner of the central temperature, the heat
diffusivity ("chi") at mid-radius and the boundary condition ("Te_bc")
at the edge.

Running with dask
-----------------

Only minor changes are necessary to run with dask.  These can be found
in easyvvuq_fusion_dask_tutorial.py and are basically:

- changes so that matplotlib is not activated with an interactive
  front-end if the code is run without an attached display

- allowing for an optional argument to specify whether to use dask
  locally ("-l") or in batch (the default)

- the importing of the appropriate dask components (we use SLURM for
  the batch scheduler --- other options are available in dask)

- a conditioning on " __name__ == '__main__'" to prevent recursive
  invocations from within dask

- invoking uq.CampaignDask() rather than uq.Campaign()

- setting up the dask workers
  
  - with a local option, 
  - or using SLURM, here configured to use
    
    - p.tok.openmp.2h QOS
    - send a mail at completion of the SLURM job(s)
    - use the p.tok.openmp partition ("queue")
    - 8 cores per job
    - 8 processes per job
    - 8 GB per job
    - 32 workers (i.e. 4 SLURM jobs)
      
  - specify the client when requesting "apply_for_each_run_dir"
  - shutting down the dask workers

I don't want to use Polynomial Chaos
------------------------------------

If you wish to use something other than PCE, it is simply a matter of
changing the sampling and analysis element used. For example, to use a
Stochastic Collocation approach, replace the sampler line with: ::

    my_campaign.set_sampler(uq.sampling.SCSampler(vary=vary, polynomial_order=3))

And the analysis can be done with: ::

    my_campaign.apply_analysis(uq.analysis.SCAnalysis(sampler=my_campaign.get_active_sampler(), qoi_cols=["te", "ne", "rho", "rho_norm"]))

References
----------

.. |_| unicode:: 0xA0 
   :trim:


.. [FUSION-WF] |_| See

- Olivier Hoenen, Luis Fazendeiro, Bruce D. Scott, Joris Borgdoff,
  Alfons G. Hoekstra, Pär Strand, and David P. Coster:
  Designing and running turbulence transport simulations using a distributed multiscale computing approach.
  In 40th EPS Conference on Plasma Physics, EPS 2013; Espoo; Finland; 1 July 2013 through 5 July 2013, vol. 2, pp. 1094-1097. 2013.
  http://publications.lib.chalmers.se/records/fulltext/185427/local_185427.pdf
  
- Falchetto, G.L., Coster, D., Coelho, R., Scott, B., Figini, L., Kalupin,
  D., Nardon,E., Nowak, S., Alves, L.L., Artaud, J.F., et al.:
  The European Integrated Tokamak Modelling (ITM) effort: achievements and first physics results.
  Nuclear Fusion 54(4)(2014) 043018.
  https://doi.org/10.1088/0029-5515/54/4/043018

- Luk, O. O., O. Hoenen, A. Bottino, B. D. Scott, and D. P. Coster:
  Optimization of Multiscale Fusion Plasma Simulations within the ComPat Framework.
  In 45th EPS Conference on Plasma Physics. European Physical Society, 2018.
  http://ocs.ciemat.es/EPS2018PAP/pdf/P1.1102.pdf
  
- O. O. Luk,  O. Hoenen,  O. Perks, K. Brabazon, T. Piontek, P. Kopta, B. Bosak, A. Bottino,
  B. D. Scott and D. P. Coster:
  Application of the extreme scaling computing pattern on multiscale fusion plasma modelling
  Phil. Trans. R. Soc. A.37720180152 (2019).
  http://doi.org/10.1098/rsta.2018.0152
	  
- Luk, O., Hoenen, O., Bottino, A., Scott, B., Coster, D.:
  ComPat framework for multiscale simulations applied to fusion plasmas.
  Computer Physics Communications (2019).
  https://doi.org/10.1016/j.cpc.2018.12.021
	   
.. [MTANH] |_| See 
	   
- E. Stefanikova, M. Peterka, P. Bohm, P. Bilkova, M. Aftanas, M. Sos, J. Urban, M. Hron and R. Panek:
  Fitting of the Thomson scatteringdensity and temperature profiles on the COMPASS tokamak.
  Presented at 21st Topical Conference on High-Temperature Plasma Diagnostics
  (HTPD 2016) in Madison, Wisconsin, USA and published in
  Review of Scientific Instruments 87, 11E536 (2016); https://doi.org/10.1063/1.4961554.
  https://pdfs.semanticscholar.org/5dc9/029eb9614a0128ae7c3f16ae6c4e54be4ac5.pdf
  
- The article cites as the source of the function: R. J. Groebener and T. N. Carlstrom,
  Plasma Phys. Controlled Fusion 40, 673 (1998). https://doi.org/10.1088/0741-3335/40/5/021

.. [FiPy] |_| See 

- J. E. Guyer, D. Wheeler & J. A. Warren:
  FiPy: Partial Differential Equations with Python.
  Computing in Science & Engineering 11(3) pp. 6—15 (2009).
  https://doi.org/10.1109/MCSE.2009.52, http://www.ctcms.nist.gov/fipy
	     
