.. _dask_tutorial:

A Cooling Coffee Cup - Using Dask Jobqueue to Run on Clusters
=============================================================

In this tutorial we expand the previous example and move on to supercomputing
clusters. In order to run it you need access to one. And if you have access to
one you most likely don't need explaining what they are or how they fit in
the work you do. So we will skip that part. We will also skip the parts that
are the same as in the previous tutorial. We only outline the parts that will
be different from when you ran it on your laptop. Luckily there aren't that
many differences.


Import necessary libraries
--------------------------

In addition we need to import the relavant Dask classes that will let us
set-up our cluster. ::

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

In order to run the jobs that correspond to each sample drawn on a cluster we
need to provide some information about. This assumes that you are executing
this code on a login node of a computing cluster. It also assumes that we are
using a SLURM cluster, but other options are possible and describe in the
dask_jobqueue documentation.

Here we ask ::

    cluster = SLURMCluster(job_extra=['--cluster=mpp2'], queue='mpp2_batch', 
                           cores=28, memory='1 GB')

We then ask to allocate a single nodes. ::

    cluster.scale(1)

At this stage you can print the batch file that will be used to submit the
worker processes. ::

    print(cluster.job_script())

Then we create a Dask client associated with this cluster. ::

    client = Client(cluster)


Execute Runs
------------

The only difference here is that you will need to supply the client argument
to the call to apply_for_each_run_dir. The remainder is exactly the same as
before and will work as before. ::

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal("python3
    cooling_model.py cooling_in.json"), client)

At this stage the computation will block until the requested resources are
allocated and all the comptutations are completed.
