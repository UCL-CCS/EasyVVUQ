.. _basic_tutorial:

Basic Tutorial
==============

This tutorial shows a simple EasyVVUQ workflow in action.
The example is slightly daft (it uses a program, `gauss.py` program which
simply samples values from a Gaussian distribution),
but illustrates how EasyVVUQ samples from a parameter space, wraps an
application and analyses output.

The input files for this tutorial are the *gauss* application 
(:download:`here <tutorial_files/gauss.py>`), an input template 
(:download:`here <tutorial_files/gauss.template>`) and the EasyVVUQ workflow 
script (:download:`here <tutorial_files/gauss_tutorial.py>`).
In preparation for this tutorial download the files and place them in 
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
Below we go through each section one by one explaining each step and the 
EasyVVUQ elements used to perform them.

.. note:: In this tutorial application execution is handled locally and by 
          EasyVVUQ functions. In real world applications (especially for HPC 
          applications the run step is beyond the scope of EasyVVUQ.

To run the workflow execute the following command ::

    python3 gauss_tutorial.py

If this works you should see 15 lines that look something like:

    Applying easyvvuq.actions.execute_local to /tmp/tut_test/EasyVVUQ_Campaign_zxe7_cb2/runs/Run_1...

Followed by a table that looks like:

    stats:
                    Value                      
                    boot       high        low
    mu                                        
    44.539790  44.490930  44.372364  44.553067
    57.115719  57.128225  57.015388  57.175946
    61.319723  61.319182  61.225901  61.392122

Section 0: Application Setup
-----------------------------------

This section contains no EasyVVUQ functionality.
It sets up variables to store the command used to run the *gauss* application, 
the names of the input and output filenames and the template used to generate 
the specific input for each run. ::

    cwd = os.getcwd()
    input_filename = "gauss_in.json"
    cmd = f"{cwd}/gauss.py {input_filename}"
    out_file = "output.csv"
    # Template input to substitute values into for each run
    template = f"{cwd}/gauss.template"

Section 1: Campaign Creation
-----------------------------------

The organizing principle within EasyVVUQ is the *Campaign*, this object
coordinates the workflow.
The *Campaign* acts as an interface to a database (*CampaignDB*) which will 
store information about the application, the parameters it takes,
how these should be sampled and the runs used to perform the sampling.
Consequently, the first step of an EasyVVUQ workflow is to create a
*Campaign*, specifying a name and working directory::

    my_campaign = uq.Campaign(name='gauss', work_dir=".")

The reason for having a name is that in some cases it may be necessary to 
combine the output of multiple *Campaigns* in a single analysis and having a
name allows the data from each to be identfied easily.

Section 2: Define Parameter Space
-----------------------------------------

The basis of any uncertainty quantification workflow will be sampling in some
parameter space.
This space will be defined by the inputs of the applications which are being 
investigated.
EasyVVUQ uses a simple format to define the possible space to be explored, it 
is a Python dictionary with dictionary entries for each parameter.

All parameters require a 'type' (this is usually a standard Python data type) 
and 'default' to be specified.
For numerical parameters a range, given by 'min' and 'max' values,
should also be provided.
The range is only used if the parameter is varied during the sampling step.

The parameter space for *gauss* refelects the options we saw in the `gauss.template`
template input::

    params = {
        "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
                  "default": "0.25"},
        "mu": {"type": "real", "min": "0.0", "max": "100000.0",
               "default": "1"},
        "num_steps": {"type": "int", "min": "0", "max": "100000",
                      "default": "10"},
        "out_file": {"type": "str", "default": out_file}
    }

The only two parameters which could (somewhat) sensibly be sampled are 'mu' 
(the mean of the gaussian) and 'sigma' the variance.
Nonetheless we need to provide a range for 'num_steps'.
Notice that the keys in the parameter descrition match the tags in the template.

.. note:: The names of parameters here does not need to match the input of the
          application directly. In the next section we will see how *Decoder*
          elements map the parameter space to the application inputs.

Section 3: Wrap Application
---------------------------

In order for an application to be used in an EasyVVUQ workflow the parameters 
being sampled need to be converted into a format that the application can 
understand (we call the proccess of doing this *encoding*) and its output 
converted into a standard form that can be analysed (we call this process 
*decoding* the output).


::

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

    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd))

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

