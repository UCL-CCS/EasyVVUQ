#TODO: For now this reads only csv files, and doesn't really do any analysis. Probably want to have an "output" wrapper for each application too?

import os, sys
import csv

if len(sys.argv) != 2:
    sys.exit("python3 UQP_analyse.py CSVFILE")

infile = sys.argv[1]
with open(infile, "r") as infile:
    csvreader = csv.reader(infile)
    total = 0
    n = 0
    for row in csvreader:
        if '#' in row[0]: # skip comment line
            continue
        total += float(row[1])
        n += 1
    mean = total/n
    print("Average = " + str(mean))
