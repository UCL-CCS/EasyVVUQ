.. _mcmc_tutorial:

MCMC With EasyVVUQ
=====================

In this tutorial we will show how to perform Markov Chain Monte Carlo sampling with EasyVVUQ.

MCMC Setup
----------

MCMC setup::
  
    campaign = uq.Campaign(name="mcmc", work_dir=tmp_path)
    params = {
        "x1": {"type": "float", "default": 0.0},
        "x2": {"type": "float", "default": 0.0},
        "out_file": {"type": "string", "default": "output.json"}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname=os.path.abspath("tutorials/rosenbrock.template"), delimiter="$", target_filename="input.json")
    decoder = uq.decoders.JSONDecoder("output.json", ["value"])
    campaign.add_app(name="mcmc", params=params, encoder=encoder, decoder=decoder)
    action = uq.actions.ExecutePython(rosenbrock)


MCMC Sampling
-------------

Sampling stage::

    vary_init = {
        "x1": -3.0,
        "x2": 2.0
    }
    def q(x, b=0.1):
        return cp.J(cp.Normal(x['x1'], b), cp.Normal(x['x2'], b))
    sampler = uq.sampling.MCMCSampler(vary_init, q, 'value')
    campaign.set_sampler(sampler)
    sampler.mcmc_sampling(campaign, action, 2000)


MCMC Analysis
----------------------------------

Analysis stage::
  
    df = campaign.get_collation_result()
    analysis = uq.analysis.MCMCAnalysis(sampler, 'value')
    result = analysis.analyse(df)

  
