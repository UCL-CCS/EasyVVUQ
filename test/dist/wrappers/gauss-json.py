import os, sys
import json

def wrap_gauss(input_json, targetdir, target_filename='gauss_in.json'):
    """

    TODO: Fix API - for example should we use named inputs
    TODO: Fix API - Will need standard for *args/**kwargs
    TODO: Need someway of doing validation checks on input params
    """

    if hasattr(input_json, 'read'):
        json_stream = input_json
    else:
        json_stream = open(input_json, 'r')

    # Open file and parse either
    input_json = json.load(json_stream)
    gauss_params = input_json["params"]

    # Check for required inputs
    #if 'run_name' not in user_inputs:
    #    raise Exception("EasyVVUQ wrapper requires a run_name in input JSON")

#    run_name = list(user_inputs.keys())[0]
    
    #gauss_params = {x: y for x, y in user_inputs.items() if x != 'run_name'}
 #   gauss_params = user_inputs[run_name]

    # Write target input file
    target_file_path = os.path.join(targetdir, target_filename)
    with open(target_file_path, 'w') as fp:
        json.dump(gauss_params, fp)
    
    # Write execution file
    run_cmd_file_path = os.path.join(targetdir, 'run_cmd.txt')
    with open(run_cmd_file_path, 'w') as fp:
        out_txt = "python3 gauss_json.py {target_filename}"
        fp.write(out_txt)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 gauss-json.py INPUT_JSON_FILE TARGETDIR")

    input_json_file = sys.argv[1]
    targetdir = sys.argv[2]

    wrap_gauss(input_json_file, targetdir)
