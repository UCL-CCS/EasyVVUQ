UQI : EasyVVUQ + QCG-PilotJob
=============================
For most VVUQ scenarios, a large number of jobs required to be executed and analysed. For execution side, users mostly use the HPC resources. Within VECMAtk, we introduced the QCG-PilotJob (QCG-PJ) toolkit to flexibly and efficiently execute a large number of simulations on the HPC resources. In order to use this functionality, users need to submit their jobs with the QCG-PJ Manager which may require some level of bash and SLURM scheduler scripting knowledge. To make this process much easier for users, we provide an integration between EasyVVUQ and QCG-PJ tools which make the VVUQ process much efficient and straightforward for users from different scientific domains.

Preparation:
------------
In order to use QCG-PJ as the job executor within easyvvuq, you need to import these two main modules::

    from easyvvuq.actions import QCGPJPool, ExecuteQCGPJ


Usage:
------
In order to setup the job submission with QCG-PJ, you need to follow these steps:

1. defines an QCG-PJ executor::

    qcg_pj_executor = ExecuteQCGPJ(ExecuteLocal(app_exe_cmd))

where ``app_exe_cmd`` is the execution command for target application, e.g., ``app_exe_cmd = '{}/beam input.json'.format(os.getcwd())``

2. Pass this QCG-PJ executor as an ``action`` to easyvvuq ``campaign`` object::

    app_actions = Actions(...,qcg_pj_executor)
    ...
    app_campaign = uq.Campaign(...,actions=app_actions)

3. The last step is submiting all campaign jobs to QCG-PJ for execution. This can be done by crating a ``QCGPJPool`` object and use it as the campaign's execute method. The ``QCGPJPool`` will submit all the jobs directly to QCG-PJ toolkit.::
    
    with QCGPJPool() as qcgpj:
        app_campaign.execute(pool=qcgpj).collate()


Advance Usage:
--------------
By default, using ``QCGPJPool()`` without any input arguments will load the default setting for QCG-PJ pool. For more advanced execution scenarios, such as setting the number of cores to execute the target application, or set the total number of requested compute node to be used during the execution of jobs, you need to provide extra input parameters to the ``QCGPJPool()`` constructor. 










 
