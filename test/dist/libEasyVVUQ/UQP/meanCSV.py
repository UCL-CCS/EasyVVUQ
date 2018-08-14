#TODO: For now this reads only csv files, and doesn't really do any analysis. Probably want to have an "output" wrapper for each application too?

import os, sys
import csv

# Use a closure so that user can specify the output file name to analyse from (TODO: Find a more elegant way to do this)
def meanCSV(fname):
    def func(dirname):
        infname = os.path.join(dirname, fname)
        with open(infname, "r") as infile:
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

    return func
