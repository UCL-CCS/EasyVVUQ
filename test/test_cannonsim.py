import os, sys
import easyvvuq as uq

campaign = uq.Campaign(state_fname="test_input/test_cannonsim.json")
uq.uqp.basicUQP(campaign)
uq.populate_runs_dir(campaign)
uq.apply_for_each_run(campaign, uq.execute_local)
uq.apply_for_each_run(campaign, uq.uqp.statsUQP(reader=uq.reader.csvReader('output.csv', 0)))
campaign.print()
campaign.save_state("out_cannonsim.json")

