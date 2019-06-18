from .base import BaseSamplingElement, Vary
import itertools

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


class SweepSampler(BaseSamplingElement, sampler_name="sweep_sampler"):

    def __init__(self, vary=None):
        """
            Expects dict of var names, and their corresponding distributions
        """
        self.vary = Vary(vary)

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def __next__(self):
#        run_dict = {}
#        for param_name, dist in self.vary.get_items():
#            run_dict[param_name] = dist.sample(1)[0]
#        return run_dict


    params = campaign.params_info

    # Extract static and dynamic variables from input
    static_params = []
    gens = []
    for key in params.keys():
        value = params[key]
        func, args = value[0], value[1]
        if func == "static":
            static_params.append((key, args))
        else:
            if func == "range":
                # TODO: Change to use numpy linspace
                gens.append(range_float(key, args[0], args[1], args[2]))
            elif func == "normal":
                gens.append(normal_dist(key, args[0], args[1], args[2]))
            else:
                sys.exit("Unrecognised function " + func + " for parameter " + key)

    # Combine all the iterables/generators into one
    mega_iter = itertools.product(*gens)

    # Build runs
    for dynamic_params in mega_iter:
        run_dict = {}
        for dp in dynamic_params:
            key, value = dp
            run_dict[key] = value
        for sp in static_params:
            key, value = sp
            run_dict[key] = value

        # Add run to Application's run list
        campaign.add_run(run_dict)

    campaign.sample_uqps.append(('random_sampler'))


    def is_restartable(self):
        return False

    def get_restart_dict(self):
        return {"vary": self.vary.serialize()}
