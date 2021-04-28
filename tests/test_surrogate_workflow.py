import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
import math
from tests.sc.sobol_model import sobol_g_func
from easyvvuq.analysis.sc_analysis import SCAnalysisResults
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions

def test_surrogate_workflow(tmpdir):
    campaign = uq.Campaign(name='sc', work_dir=tmpdir)
    params = {
        "Pe": {
            "type": "float",
            "min": 1.0,
            "max": 2000.0,
            "default": 100.0},
        "f": {
            "type": "float",
            "min": 0.0,
            "max": 10.0,
            "default": 1.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"
        }
    }

    output_filename = params["out_file"]["default"]
    output_columns = ["u"]
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/sc/sc.template',
        delimiter='$',
        target_filename='ade_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    execute = ExecuteLocal("{} ade_in.json".format(os.path.abspath('tests/sc/sc_model.py')))
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))
    campaign.add_app(name="sc", params=params, actions=actions)

    vary = {
        "Pe": cp.Uniform(100.0, 200.0),
        "f": cp.Uniform(0.95, 1.05)
    }
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=[2, 5], quadrature_rule="G")
    campaign.set_sampler(sampler)

    campaign.execute().collate()

    results = campaign.analyse(qoi_cols=output_columns)


