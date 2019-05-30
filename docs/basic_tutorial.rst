.. _basic_tutorial:

Basic Tutorial
==============

This tutorial shows a simple EasyVVUQ workflow in action.
The example is slightly daft (it uses a program, `gauss.py` program which
simply samples values from a Gaussian distribution),
but illustrates how EasyVVUQ samples from a parameter space, wraps an
application and analyses output.

The input files for this tutorial are the *gauss* application (here), an
input template (here) and the EasyVVUQ workflow script (here).
In preparation fo r this tutorial download the files and place them in 
an empty directory, then change into this directory.

Gauss Application
-----------------

The usage of the `gauss.py` application is::

    gauss.py in_file.json

It outputs a single file called `output.csv`, which has two columns
'Steps' and 'Value'.

The `gauss.template` is a template input file, in JSON format ::

    {"outfile": "$out_file", "num_steps": "$num_steps", "mu": "$mu", "sigma": "$sigma"}

The values for each key are tags (signified by the $ delimiter) which will 
be substituted by EasyVVUQ with values to sample the parameter space.

Uncertainty Quantification Workflow
-----------------------------------

In this dummy workflow we will use the *gauss* application to produce values
from normal distributions centred on 3 different means `mu`), using 5 repeat 
('replica') runs for each one.
The output will be collected for each run and bootstrap statistics calculated
for each set of runs.

EasyVVUQ Script Overview
------------------------

The script `gauss_tutorial.py` implements the workflow described above using
EasyVVUQ.
The commands are split into sections which are indicated by numbered comments.
Sections 1 to 9 contain the core EasyVVUQ workflow, section 0 sets up 
convenience variables related to the application.
Below we go through each section one by one.

.. note:: In this tutorial application execution is handled locally and by 
          EasyVVUQ functions. In real world applications (especially for HPC 
          applications teh run step is beyond the scope of EasyVVUQ.

To run the workflow execute the following command ::

    python3 gauss_tutorial.py


Section 0: Application Setup
-----------------------------------

This section contains no EasyVVUQ functionality.
It sets up variables to store the command used to run the *gauss* application, 
the names of the input and output filenames and the template used to generate 
the specific input for each run. ::

    cwd = os.cwd()
    input_filename = gauss_in.json
    cmd = f"{cwd}/gauss.py {input_filename}"
    out_file = "output.csv"
    # Template input to substitute values into for each run
    template = f"{cwd}/gauss_in.template"

Section 1: Campaign Creation
-----------------------------------

::

    my_campaign = uq.Campaign(name='gauss', work_dir=".")

Section 2: Define Parameter Space
-----------------------------------------

::

    params = {
        "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
                  "default": "0.25"},
        "mu": {"type": "real", "min": "0.0", "max": "100000.0",
               "default": "1"},
        "num_steps": {"type": "int", "min": "0", "max": "100000",
                      "default": "10"},
        "out_file": {"type": "str", "default": out_file}
    }

Section 3: Wrap Application
---------------------------

::

    # 3. Create and add elements to the campaign
    encoder = uq.encoders.GenericEncoder(template_fname=template,
                                        target_filename=input_filename)

    decoder = uq.decoders.SimpleCSV(
                target_filename=out_file, 
                output_columns=['Step', 'Value'], 
                header=0)

    collation = uq.collate.AggregateSamples(average=True)

    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collation=collation
                        )

Section 4: Specify Sampler
--------------------------

::

    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }

    my_sampler = uq.sampling.RandomSampler(vary=vary)

    my_campaign.set_sampler(my_sampler)

Section 5: Get Run Parameters
-----------------------------

::

    my_campaign.draw_samples(num_samples=3,
                             replicas=5)


Section 6: Create Input Directories
-----------------------------------

::

    my_campaign.populate_runs_dir()

Section 7: Run Application
--------------------------

::

    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd)

Section 8: Collate Output
-------------------------

::

    my_campaign.collate()

Section 9: Run Analysis
-----------------------

::

    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    my_campaign.apply_analysis(stats)

Conclusions
-----------

