.. _basic_tutorial:

Basic Tutorial
==============

This tutorial shows a simple EasyVVUQ workflow in action.
The example is slightly daft (it uses a program, `gauss.py` program which
simply samples values from a Gaussian distribution),
but illustrates how EasyVVUQ samples from a parameter space, wraps an
application and analyses output.

The input files for this tuorial are the gauss application (here), an
input template (here) and the EasyVVUQ workflow script (here).

Gauss Application
-----------------

The usage of the `gauss.py` application is::

    gauss.py input.json

It outputs a single file called `output.csv`, which has two columns
'Steps' and 'Value'.

The `gauss.template` is a template input file, in JSON format ::

    {"outfile": "$out_file", "num_steps": "$num_steps", "mu": "$mu", "sigma": "$sigma"}

The values for each key are tags (signified by the $ delimiter) which will 
be substituted by EasyVVUQ with values to sample the parameter space.

EasyVVUQ Workflow
-----------------

In this dummy workflow we will use the gauss application to produce values
from normal distributions centred on 3 different means `mu`), using 5 repeat 
runs for each one.
The output will be collected for each run and bootstrap statistics calculated
for each set of runs.
