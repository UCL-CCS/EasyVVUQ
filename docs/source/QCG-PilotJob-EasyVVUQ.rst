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
In order to use QCG-PilotJob as the job executor within EasyVVUQ, you need to import these two main modules::

    from easyvvuq.actions import QCGPJPool, ExecuteQCGPJ


Usage:
------
In order to setup the job submission with QCG-PilotJob, you need to follow these steps::

1. Wrap the task that need to be processed with QCG-PilotJob in the ExecuteQCGPJ decorator:

    qcg_pj_action = ExecuteQCGPJ(ExecuteLocal(app_exe_cmd))

where ``app_exe_cmd`` is the execution command for target application, e.g., ``app_exe_cmd = '{}/beam input.json'.format(os.getcwd())``

2. Pass this wrapped action as an ``action`` to EasyVVUQ ``campaign`` object::

    app_actions = Actions(...,qcg_pj_action)
    ...
    app_campaign = uq.Campaign(...,actions=app_actions)

3. The last step is submitting all campaign jobs to QCG-PilotJob for execution.
This can be done by crating a ``QCGPJPool`` object and use it as the campaign's execute method.
The ``QCGPJPool`` will submit all the jobs directly to the QCG-PilotJob toolkit.::
    
    with QCGPJPool() as qcgpj:
        app_campaign.execute(pool=qcgpj).collate()


Advance Usage:
--------------
By default, using ``QCGPJPool()`` without any input arguments will load the default setting for QCG-PilotJob pool.
For more advanced execution scenarios, such as setting the number of cores to execute the target application,
or set the total number of requested compute nodes to be used during the execution of jobs,
you need to provide extra input parameters to the ``QCGPJPool()`` constructor.

TODO: linkt to the Jupyter Notebook tutorial, links to the QCG-PilotJob webpage









 
