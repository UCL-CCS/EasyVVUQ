import easyvvuq as uq
from easyvvuq.actions import Actions, Encode, Decode, CreateRunDirectory, ExecuteQCGPJ, QCGPJPool
import chaospy as cp
import os

__license__ = "LGPL"


def test_qcgpj(tmpdir):
    params = {
        "temp_init": {
            "type": "float",
            "min": 0.0,
            "max": 100.0,
            "default": 95.0},
        "kappa": {
            "type": "float",
            "min": 0.0,
            "max": 0.1,
            "default": 0.025},
        "t_env": {
            "type": "float",
            "min": 0.0,
            "max": 40.0,
            "default": 15.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"}}
    output_filename = params["out_file"]["default"]
    output_columns = ["te"]

    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cooling/cooling.template',
        delimiter='$',
        target_filename='cooling_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                output_columns=output_columns)

    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }

    cooling_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)
    cooling_stats = uq.analysis.PCEAnalysis(sampler=cooling_sampler, qoi_cols=output_columns)

    cooling_action = uq.actions.ExecuteLocal(os.path.abspath("tests/cooling/cooling_model.py") +
                                         " cooling_in.json")

    qcgpj_action = ExecuteQCGPJ(cooling_action)
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), qcgpj_action, Decode(decoder))

    campaign = uq.Campaign(name='beam', params=params, actions=actions)
    campaign.set_sampler(cooling_sampler)

    with QCGPJPool() as qcgpj:
        campaign.execute(pool=qcgpj).collate()

    campaign.apply_analysis(cooling_stats)

if __name__ == "__main__":
    test_qcgpj("/tmp/")
