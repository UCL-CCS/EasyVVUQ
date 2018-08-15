import os, sys
import EasyVVUQ as uq

campaign = uq.Campaign(state_fname="test_input/test_cannonsim.json")
uq.UQP.Basic(campaign)
uq.populate_runs_dir(campaign)
campaign.save_state("out_state.json")
campaign.print()
uq.apply_for_each_run(campaign, uq.execute_local)
uq.apply_for_each_run(campaign, uq.UQP.meanCSV('output.csv', 0))

