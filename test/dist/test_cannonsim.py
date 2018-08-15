import os, sys
import EasyVVUQ as uq

campaign = uq.Campaign(state_fname="test_input/test_cannonsim.json")
uq.UQP.basicUQP(campaign)
uq.populate_runs_dir(campaign)
uq.apply_for_each_run(campaign, uq.execute_local)
uq.apply_for_each_run(campaign, uq.UQP.statsUQP(reader=uq.Reader.csvReader('output.csv', 0)))
campaign.print()
campaign.save_state("out_cannonsim.json")

