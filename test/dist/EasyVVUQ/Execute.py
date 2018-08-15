import os, sys
import json
import glob

def execute_local(dirname):
    cmd = "cd " + dirname + "\nbash run_cmd.sh"
    r = os.system(cmd)
    if r != 0:
        sys.exit("Non-zero exit code from command '" + cmd + "'")
