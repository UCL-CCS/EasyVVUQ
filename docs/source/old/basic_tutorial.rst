.. _basic_tutorial:

Basic Tutorial
==============

This tutorial shows a simple EasyVVUQ workflow in action.
The example is slightly daft (it uses a program, `gauss.py` program which
simply samples values from a Gaussian distribution),
but illustrates how EasyVVUQ samples from a parameter space, wraps an
application and analyses output.

The input files for this tutorial are the *gauss* application
(:download:`gauss.py <../../tutorials/gauss.py>`), an input template
(:download:`gauss.template <../../tutorials/gauss.template>`) and the EasyVVUQ workflow
script (:download:`easyvvuq_gauss_tutorial.py <../../tutorials/easyvvuq_gauss_tutorial.py>`).
In preparation for this tutorial download the files and place them in
an empty directory, then change into this directory.

Important Note About the CSV File Format
----------------------------------------

Please note that when creating CSV files to be used with EasyVVUQ
and in the examples below, special care needs to be taken to respect
RFC 4180. One common issue is that people leave spaces around
attribute names in the first row of the text file. These spaces are
not trimmed and become part of the attribute name which causes
confusion later.

For example::

  attr1,attr2,attr3

is correct, while::

   attr1, attr2, attr3

Is wrong (unless your attribute names are meant to have a space at the
start).

Gauss Application
-----------------

The usage of the `gauss.py` application is::

    gauss.py <input_file>

It outputs a single file called `output.csv`, which has two columns
'Steps' and 'Value'.

The `gauss.template` is a template input file, in JSON format ::

    {"outfile": "$out_file", "num_steps": "$num_steps", "mu": "$mu", "sigma": "$sigma"}

The values for each key are tags (signified by the ``$`` delimiter) which will
be substituted by EasyVVUQ with values to sample the parameter space.
In the following tutorial, the template will be used to generate files called
`in_file.json` that will be the input to each run of `gauss.py`.

Uncertainty Quantification Workflow
-----------------------------------

In this dummy workflow we will use the *gauss* application to produce values
from normal distributions centred on 3 different means `mu`), using 5 repeat
('replica') runs for each one.
The output will be collected for each run and bootstrap statistics calculated
for each set of runs.

EasyVVUQ Script Overview
------------------------

The script `easyvvuq_gauss_tutorial.py` implements the workflow described above using
EasyVVUQ.
The commands are split into sections which are indicated by numbered comments.
Sections 1 to 9 contain the core EasyVVUQ workflow, section 0 sets up
convenience variables related to the application.

.. note:: In this tutorial application execution is handled locally and by
          EasyVVUQ functions. In real world applications (especially for HPC
          applications the run step is beyond the scope of EasyVVUQ.

To run the workflow execute the following command ::

    python3 easyvvuq_gauss_tutorial.py

If this works you should see 15 lines that look something like:

    Applying easyvvuq.actions.execute_local to <run-location>/EasyVVUQ_Campaign_zxe7_cb2/runs/Run_1...

where `<run-location>` is the directory in which you ran the script and
`EasyVVUQ_Campaign_zxe7_cb2` is an example of the unique directory that
EasyVVUQ created to hold all of the files created relating to a campaign.

Followed by a results table that looks like:

.. code-block:: text

    stats:
                    Value
                    boot       high        low
    mu
    44.539790  44.490930  44.372364  44.553067
    57.115719  57.128225  57.015388  57.175946
    61.319723  61.319182  61.225901  61.392122

The 'mu' values are chosen at random so your output values will be different.
The statistics represent the variation across the 5 replica runs executed for
each of the 3 'mu' values sampled.

Below we go through each section of the workflow, explaining each step and the
EasyVVUQ elements used to perform them.

Section 0: Application Setup
-----------------------------------

This section contains no EasyVVUQ functionality.
It sets up variables to store the command used to run the *gauss* application,
the names of the input and output filenames and the template used to generate
the specific input for each run. ::
  
    import os
    cwd = os.getcwd()
    input_filename = "gauss_in.json"
    cmd = f"{cwd}/tutorial_files/gauss.py {input_filename}"
    out_file = "output.csv"
    # Template input to substitute values into for each run
    template = f"{cwd}/tutorial_files/gauss.template"

Section 1: Campaign Creation
-----------------------------------

The organizing principle within EasyVVUQ is the *Campaign*, this object
coordinates the workflow.
The *Campaign* acts as an interface to a database (*CampaignDB*) which will
store information about the application, the parameters it takes,
how these should be sampled and the runs used to perform the sampling.
Consequently, the first step of an EasyVVUQ workflow is to create a
*Campaign*, specifying a name and working directory::

    import easyvvuq as uq
    my_campaign = uq.Campaign(name='gauss', work_dir=".")

The reason for having a name is that in some cases it may be necessary to
combine the output of multiple *Campaigns* in a single analysis and having a
name allows the data from each to be identified easily.

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

The parameter space for *gauss* reflects the options we saw in the `gauss.template`
template input::


    params = {
        "sigma": {
            "type": "float",
            "min": 0.0,
            "max": 100000.0,
            "default": 0.25
        },
        "mu": {
            "type": "float",
            "min": 0.0,
            "max": 100000.0,
            "default": 1
        },
        "num_steps": {
            "type": "integer",
            "min": 0,
            "max": 100000,
            "default": 10
        },
        "out_file": {
            "type": "string",
            "default": "output.csv"
        }
    }

The only two parameters which could (somewhat) sensibly be sampled are 'mu'
(the mean of the gaussian) and 'sigma' the variance.
Nonetheless we need to provide a range for 'num_steps'.
Notice that the keys in the parameter description match the tags in the template.

.. note:: The names of parameters here does not need to match the input of the
          application directly. In the next section we will see how *Decoder*
          elements map the parameter space to the application inputs.


Section 3: Wrap Application
---------------------------

In order for an application to be used in an EasyVVUQ workflow two processes
have to be accounted for:

1. the parameters being sampled need to be converted into a format that
the application can understand; we call this process *encoding*,
2. the application output must be converted into a standard form that can be
analysed (we use `panda.DataFrame` by default); we call this process *decoding*.

Within EasyVVUQ these actions are performed by *Encoders* and *Decoders*
respectively.
Both the *Encoder* and *Decoder* have to be executed for each run (sample).
The *gauss* application is simple and the input and output formats can be
interpreted by inbuilt classes.

The appropriate encoder here is the `GenericEncoder`, this takes a template file
and substitutes in values from the parameter space description (outputting to a
specified file).
We create the encoder using the following code::

    encoder = uq.encoders.GenericEncoder(template_fname=template,
                                         target_filename=input_filename)

.. note:: The tags in the template here use the default $ delimiter.
          Different delimiters can be specified using the `delimiter` keyword.

The output of *gauss* is a CSV format files, so we use a *Decoder* called *SimpleCSV*.
This requires us to specify the file to be read, the location of the header (line 0)
and the columns to keep in the data for analysis::

    decoder = uq.decoders.SimpleCSV(
                target_filename=out_file,
                output_columns=['Step', 'Value'])

These choices are then added to the *Campaign*::

    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder)

Section 4: Specify Sampler
--------------------------

The backbone of EasyVVUQ workflows is the sampling of one or more parameters.
The type of element used to do this is (imaginatively) called a *Sampler*.
A *Sampler* implements an algorithm that chooses sets of parameters to span the
input parameter space.
The particular parameters to vary are specified by the user, along with the
distribution that they take.
The distributions are specified as `Chaospy <https://chaospy.readthedocs.io/>`_
distributions.
In this example we simply pick 'mu' values from a uniform distribution between
1 and 100::

    import chaospy as cp

    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }

    my_sampler = uq.sampling.RandomSampler(vary=vary)

    my_campaign.set_sampler(my_sampler)

Real world examples are likely to use more complicated algorithms (such as
quasi-Monte Carlo or stochastic collocation) but the way of specifying
parameters to vary remains the same.

Section 5: Get Run Parameters
-----------------------------

Now that the *Campaign* is setup it can provide sets of parameters to
input into runs.
We draw samples the number of samples we want from the *Sampler*::

    my_campaign.draw_samples(num_samples=3,
                             replicas=5)

Here we have chosen to have 5 replicas (repeats) of each sample drawn.
At this stage all that happens is the parameter sets are added to the
*CampaignDB*, no input files have been generated.

Section 6: Create Input Directories
-----------------------------------

We now need to create the input files for each run.
The `populate_runs_dir` method of *Campaign* creates a directory for each run
and uses the specified *Encoder* to produce the appropriate input files::

    my_campaign.populate_runs_dir()

Section 7: Run Application
--------------------------

To create our samples we need to execute all of the runs.
EasyVVUQ *Campaigns* provide a method `apply_for_each_run_dir` which allows
us to apply a function whilst in each run directory we have created.
Here we use the `ExecuteLocal` action to run the *gauss* application using the
command we specified in Step 0::

    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd))

Section 8: Collate Output
-------------------------

The collection of simulation output simply handled by the *Campaign*::

    my_campaign.collate()

Under the hood this method combines the use of the specified *Decoder* for
the current application, and the set *Collation* element to produce a summary
`pandas.DataFrame` including data from all runs. Each time this method is called,
it will append any new results to the dataframe.

Section 9: Run Analysis
-----------------------

The final element in the workflow is the analysis.
Here we apply bootstrapping analysis::

    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    my_campaign.apply_analysis(stats)

The `groupby` option specifies the parameters which should be used to group runs
together when calculating statistics, `qoi_cols` specifies which columns of the
output collected by the *Decoder* should analysed.

Some Final Points
-----------------

The last command in the script simply prints out the results of the analysis,
stored in
`my_campaign.get_last_analysis()`.
This is a `pandas.DataFrame` and can easily be output as a CSV or other file format.

It is instructive to look in the `EasyVVUQ_Campaign_<random_characters>` directory
to see the input and output files generated by each run.
