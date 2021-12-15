UQI : EasyVVUQ + QCG-PilotJob
=============================
For most VVUQ scenarios, a large number of jobs is required to be executed and analysed.
For execution side, users mostly use the HPC resources.
Within VECMAtk, we introduced the QCG-PilotJob (QCG-PJ) toolkit to flexibly and efficiently execute
a large number of simulations on the HPC resources.
In order to make it straightforward for EasyVVUQ users to use the QCG-PilotJob functionality and benefit from
efficient processing of their jobs on HPC resources, the two tools has been integrated.

Preparation:
------------
In order to use QCG-PilotJob as the job executor within EasyVVUQ, you need to import the following module::

    from easyvvuq.actions import QCGPJPool

and then to use ``QCGPJPool`` object as an execution engine for the campaign, which is done by the passing it to the
``execute`` method. ``QCGPJPool`` will submit all the jobs directly to the QCG-PilotJob toolkit::

    with QCGPJPool() as qcgpj:
        app_campaign.execute(pool=qcgpj).collate()

Advance Usage:
--------------
By default, using ``QCGPJPool()`` without any input arguments will load the default setting for QCG-PilotJob pool.
For more advanced execution scenarios, such as setting the number of cores to execute the target application,
or set the total number of requested compute nodes to be used during the execution of jobs,
you need to provide extra input parameters to the ``QCGPJPool()`` constructor.

For more information see:
 * `Jupyter Notebook tutorial displaying QCG-PilotJob usage
   from EasyVVUQ <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/tutorials/basic_tutorial_qcgpj.ipynb>`_
 * `QCG-PilotJob documentation <https://qcg-pilotjob.readthedocs.io>`_






 
