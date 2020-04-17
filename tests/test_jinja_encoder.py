import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
from easyvvuq.encoders.jinja_encoder import JinjaEncoder

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


def test_jinjaencoder(tmpdir):
    """
    Set up a campaign using the jinja2 template.
    This example is based on the DALES model. The input file is a Fortran namelist.
    """

    params = {
        "Nc_0": {  # concentration of cloud condensation nuclei
            "type": "float",
            "min": 0.1e6,
            "max": 1000e6,
            "default": 70e6,
        },
        "cf": {  # cf subgrid filter constant
            "type": "float",
            "min": 1.0,
            "max": 4.0,
            "default": 2.5,
        },
        "cn": {  # subfilterscale parameter
            "type": "float",
            "min": 0.5,
            "max": 1.0,
            "default": 0.76,
        },
        "Rigc": {  # critical Richardson number
            "type": "float",
            "min": 0.1,
            "max": 1.0,
            "default": 0.25,
        },
        "Prandtl": {  # Prandtl number, subgrid.
            "type": "float",
            "min": 0.1,
            "max": 1.0,
            "default": 1.0 / 3,
        },
        "z0": {  # surface roughness
            "type": "float",
            "min": 1e-4,
            "max": 1.0,
            "default": 1.6e-4,
        },
        "l_sb": {  # flag for microphysics scheme: false - KK00 Khairoutdinov and Kogan, 2000
            "type": "integer",    # true - SB   Seifert and Beheng, 2001, 2006, Default
            "min": 0,
            "max": 1,
            "default": 1
        },
        "Nh": {  # number of grid points in the horizontal directions - itot, jtot
            "type": "integer",
            "min": 3,
            "max": 1024,
            "default": 10
        },
        "extent": {  # norizontal domain size in x, y  - xsize, ysize. unit: m
            "type": "float",
            "min": 1,
            "max": 1000000,
            "default": 1000,
        },
        "seed": {  # random seed
            "type": "integer",
            "min": 1,
            "max": 1000000,
            "default": 43
        },
        "nprocx": {  # number of MPI tasks in x
            "type": "integer",
            "min": 1,
            "max": 1000,
            "default": 1
        },
        "nprocy": {  # number of MPI tasks in y
            "type": "integer",
            "min": 1,
            "max": 1000,
            "default": 1
        },
    }

    vary = {
        "Nc_0": cp.Uniform(50e6, 100e6),
        # "cf": cp.Uniform(2.4, 2.6),
        # "cn": cp.Uniform(0.5, 0.9),
        # "Rigc": cp.Uniform(0.1, 0.4),
        # "Prandtl": cp.Uniform(0.2, 0.4),
        # "z0": cp.Uniform(1e-4, 2e-4),
        "l_sb": cp.DiscreteUniform(0, 1),
        # "Nh": cp.DiscreteUniform(10, 20),
        # "extent": cp.Uniform(1000, 2000),
        "seed": cp.Uniform(1, 2000),
    }

    output_columns = ['cfrac', 'lwp', 'rwp', 'zb', 'zi', 'prec', 'wq', 'wtheta', 'we', 'walltime']
    my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=2,
                                       quadrature_rule="C")
    my_campaign = uq.Campaign(name='dales', work_dir=tmpdir, db_location='sqlite:///')
    encoder = JinjaEncoder(template_fname='tests/jinjaencoder/namoptions.template',
                           target_filename='namoptions.001')
    decoder = uq.decoders.SimpleCSV(
        target_filename='results.csv',
        output_columns=output_columns,
        header=0)
    collater = uq.collate.AggregateSamples(average=False)
    my_campaign.add_app(name="dales",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)
    my_campaign.verify_all_runs = False  # to prevent errors on integer quantities
    my_campaign.set_sampler(my_sampler)
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()


if __name__ == "__main__":
    test_jinjaencoder("/tmp/")
