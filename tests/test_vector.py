import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
import logging
from pprint import pformat, pprint
from .gauss.encoder_gauss import GaussEncoder
from .gauss.decoder_gauss import GaussDecoder
from easyvvuq.decoders.json import JSONDecoder

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


__license__ = "LGPL"


logging.basicConfig(level=logging.CRITICAL)


def test_gauss_vector_sc(tmpdir):
    # vector version of test_gauss
    # loads json output containing vector data from gauss test

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
        },
    }

    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }

    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                    output_columns=["numbers"],
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=4)
    my_campaign = uq.Campaign(name='gauss_vector', work_dir=tmpdir)
    my_campaign.add_app(name="gauss_vector",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)
    my_campaign.set_sampler(sampler)
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(actions)
    my_campaign.collate()

    data = my_campaign.get_collation_result()
    print("===== DATA:\n ", data)
    analysis = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=["numbers"])
    my_campaign.apply_analysis(analysis)
    results = my_campaign.get_last_analysis()


def test_gauss_vector_pce(tmpdir):
    # vector version of test_gauss
    # loads json output containing vector data from gauss test

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
        },
    }

    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }

    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    #decoder = JSONDecoder(target_filename='output.csv.json', output_columns=['numbers'])
    decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                    output_columns=["numbers"],
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
    sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=4)
    my_campaign = uq.Campaign(name='gauss_vector', work_dir=tmpdir)
    my_campaign.add_app(name="gauss_vector",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)
    my_campaign.set_sampler(sampler)
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(actions)
    my_campaign.collate()

    data = my_campaign.get_collation_result()
    print("===== DATA:\n ", data)
    analysis = uq.analysis.PCEAnalysis(sampler=sampler, qoi_cols=["numbers"])
    my_campaign.apply_analysis(analysis)
    results = my_campaign.get_last_analysis()


if __name__ == "__main__":
    # test_gauss_vector_pce("/tmp")
    test_gauss_vector_sc("/tmp")
