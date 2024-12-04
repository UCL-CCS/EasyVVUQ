.. _dask_tutorial:

A Cooling Coffee Cup - Using Dask Jobqueue to Run on Clusters
=============================================================

In this tutorial we expand the previous :doc:`example
<cooling\_coffee\_cup>` and move our computations to computing
clusters. In order to run it you will need access to one. And if you
have access to one you most likely don't need explaining what they are
or how they fit in the work you do. So we will skip that part. We will
also skip the parts that are the same as in the previous tutorial. We
only outline the parts that will be different from when you ran it on
your laptop. Luckily there aren't that many differences.


Import necessary libraries
--------------------------

In addition we need to import the relevant Dask classes that will let us
set-up our cluster. Here we assume a SLURM cluster, however, other
options (PBS and so on) are possible. Please refer to Dask JobQueue
`documentation <https://jobqueue.dask.org/en/latest/>`_. ::

    from dask.distributed import Client
    from dask_jobqueue import SLURMCluster

Create a new Campaign
---------------------

As in the :doc:`Basic Tutorial <basic\_tutorial>`, we start by creating the
campaign, the only difference is that we instantiate the CampaignDask class
instead of Campaign ::

    my_campaign = uq.CampaignDask(name='coffee_pce')

Initialize Cluster
------------------

Provided that you have access to a computing cluster you can now run
your UQ workflow on it. You will need to know some technical details
about the compute nodes of your cluster. Most importantly you need to
know how many CPU cores does this node have and how much RAM. This
information is used to figure out the amount of resources we will
need, namely, how many nodes to reserve.

Here we describe a single node of an example cluster. Please note that
you don't need to specify the resources you need for your run as
such. Only the resources available on a single node. Unless the
resources the job needs are fewer than the node provides. For example,
if the node has 48 cores and 64 gigabytes of memory ::

    cluster = SLURMCluster(job_extra=['--cluster=mycluster'],
                           queue='myqueue', 
                           cores=48, memory='64 GB')

Now you can allocate the resources needed for your UQ run using the
``scale`` method. For full documentation refer to the `API
<https://jobqueue.dask.org/en/latest/api.html>`_. To ask for 96 cores,
for example, we can use ::

     cluster.scale(96)

At this stage you can print the batch file that will be used to submit the
worker processes. ::

    print(cluster.job_script())

Then we create a Dask client associated with this cluster. ::

    client = Client(cluster)

Please note that after this point the jobs will be submitted to the
batch scheduler. They will take some time to actually start
executing. The code in the following section will block until the job
starts.


Execute Runs
------------

The only difference here is that you will need to supply the client argument
to the call to apply_for_each_run_dir. The remainder is exactly the same as
before. ::

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal("python3 cooling_model.py cooling_in.json"), client)

At this stage the computation will block until the requested resources are
allocated and all the computations are completed.


Notes and Workarounds
---------------------

Note that Dask JobQueue will want to establish a TCP connection
between the compute and login nodes. It is possible that the admins on
your system don't allow this. The reasons for this are unclear but we
suspect they are mad with power. If that is the case, there is a quick
workaround. You should try running your script in interactive mode and
see if that solves the problem. For example, on SLURM it could be
something like this: ::

    salloc --partition=interactivequeue

The system will then try to allocate resources for you to run the
interactive job and this might take a couple of moments. After that an
interactive mode prompt will appear. Commands that you execute there
will be run on compute nodes. You would then execute the script
normally, e.g. :: 

    python tutorial_files/easyvvuq_dask_tutorial.py


