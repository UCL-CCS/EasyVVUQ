import os, sys
import easyvvuq as uq

my_campaign = uq.Campaign(state_filename="test_input/test_gauss.json")
uq.uqp.basicUQP(my_campaign)
my_campaign.populate_runs_dir()
my_campaign.apply_for_each_run(uq.execute_local)
my_campaign.apply_for_each_run(uq.uqp.statsUQP(reader=uq.reader.csvReader('output.csv', 0)))
my_campaign.print()
my_campaign.save_state("out_gauss.json")

