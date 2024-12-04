import ruamel.yaml
import numpy as np
from scipy.stats.mstats import gmean
import os
import sys

def deserialize_yaml(file_name=None):
    with open(file_name) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
        data = ruamel.yaml.load(file, Loader=ruamel.yaml.Loader)
    return data

def serialize_yaml(my_campaign=None,
        output_name="sobols.yml", output_columns=None,
        params_dist=None, vary=None,
        my_sampler=None, polynomial_order=0, regression=None,
        time=None, mu=None, stddev=None, cov=None, mean=None, variance=None,
        p10=None, p90=None,
        derivatives_first=None,
        sobols_first=None, sobols_total=None, sobols_first_conf=None,
        ROUND_NDIGITS=8):
    S = ruamel.yaml.scalarstring.DoubleQuotedScalarString
    yml_results = ruamel.yaml.comments.CommentedMap()
    yml_results.update({"campaign_info": {}})
    yml_results["campaign_info"].update({
        "name": S(my_campaign._active_app_name),
        "work_dir": S(my_campaign.work_dir),
        "output_column": S(output_columns),
        "params": S(list(vary)),
        "distribution_type": S(params_dist),
        "mu":
            np.around(mu, ROUND_NDIGITS).tolist(),
        "stddev":
            np.around(stddev, ROUND_NDIGITS).tolist(),
        "cov":
            np.around([c for cov_r in cov for c in cov_r], ROUND_NDIGITS).tolist(),
        "sampler": S(type(my_sampler)),
        "num_runs": my_campaign.campaign_db.get_num_runs(),
        "polynomial_order": polynomial_order,
        "PCE_regression": S(regression)
        })

    for output_column in output_columns:
        yml_results.update({output_column: {}})

        yml_results[output_column].update({"model": {}})
        yml_results[output_column]["model"].update({
            "time":
                np.around(time, ROUND_NDIGITS).tolist(),
            "mean":
                np.around(mean[output_column].ravel(), ROUND_NDIGITS).tolist(),
            "variance":
                np.around(variance[output_column].ravel(), ROUND_NDIGITS).tolist(),
            "p10":
                np.around(p10[output_column].ravel(), ROUND_NDIGITS).tolist(),
            "p90":
                np.around(p90[output_column].ravel(), ROUND_NDIGITS).tolist()
            })

        for param in vary:
            # I used CommentedMap for adding comments
            yml_results[output_column][param] = ruamel.yaml.comments.CommentedMap()
            # yml_results.update({param: {}})
            yml_results[output_column][param].update({
                "sobols_first_mean":
                    round(float(np.mean(sobols_first[output_column][param].ravel())),
                        ROUND_NDIGITS),
                "sobols_first_gmean":
                    round(float(gmean(sobols_first[output_column][param].ravel())),
                        ROUND_NDIGITS),
                "sobols_first":
                    np.around(sobols_first[output_column][param].ravel(),
                            ROUND_NDIGITS).tolist(),
                "derivatives_first":
                    np.around(derivatives_first[output_column][param].ravel(),
                            ROUND_NDIGITS).tolist()
            })
            yml_results[output_column][param].yaml_set_comment_before_after_key(
                "sobols_first_gmean",
                before="geometric mean, i.e., n-th root of (x1 * x2 * ... * xn)",
                indent=2)
            yml_results[output_column][param].yaml_set_comment_before_after_key(
                "sobols_first_mean",
                before="arithmetic mean i.e., (x1 + x2 + ... + xn)/n", indent=2)

            yml_results[output_column][param].update({
                "sobols_total_mean":
                    round(float(np.mean(sobols_total[output_column][param].ravel())),
                        ROUND_NDIGITS),
                "sobols_total_gmean":
                    round(float(gmean(sobols_total[output_column][param].ravel())),
                        ROUND_NDIGITS),
                "sobols_total":
                    np.around(sobols_total[output_column][param].ravel(),
                            ROUND_NDIGITS).tolist()
            })
            yml_results[output_column][param].yaml_set_comment_before_after_key(
                "sobols_total_gmean",
                before="geometric mean, i.e., n-th root of (x1 * x2 * ... * xn)",
                indent=2)
            yml_results[output_column][param].yaml_set_comment_before_after_key(
                "sobols_total_mean",
                before="arithmetic mean i.e., (x1 + x2 + ... + xn)/n", indent=2)

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = None
    # to Prevent long lines getting wrapped in ruamel.yaml
    # we set the yaml.width to a big enough value to prevent line-wrap
    yaml.width = sys.maxsize

    res_file_name = os.path.join(my_campaign.work_dir, output_name)
    print(res_file_name)
    with open(res_file_name, "w") as outfile:
        yaml.dump(yml_results, outfile)
        
    return yml_results