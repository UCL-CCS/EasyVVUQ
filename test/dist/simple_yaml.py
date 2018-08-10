import os,sys
import numpy as np
from pprint import pprint
import yaml

# Load YAML file
with open("test_input/test1.yml", "r") as infile:
	params = yaml.safe_load(infile)
pprint(params)

# Save as YAML
with open("output.yml", 'w') as outfile:
	yaml.dump(params, outfile, default_flow_style=False)
