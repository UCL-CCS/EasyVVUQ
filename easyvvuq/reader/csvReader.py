import os, sys
import csv

# Extracts the specified column from the specified csv file. Returns it as a list. Ignores comment lines.
def csvReader(fname, column):
    def csvReaderSpecific(dirname):
        full_path = os.path.join(dirname, fname)
        ret = []
        with open(full_path, "r") as infile:
            csvreader = csv.reader(infile)
            for row in csvreader:
                if '#' in row[0]: # skip comment line
                    continue
                ret.append(float(row[column]))
        return ret

    return csvReaderSpecific
