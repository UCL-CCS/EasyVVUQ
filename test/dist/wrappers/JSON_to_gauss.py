import os,sys
import json
from pprint import pprint

with open('UQ_in.json') as f:
	data = json.load(f)

pprint(data)
