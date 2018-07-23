import os, sys
import json

def wrap_gauss(input_json, basedir, target_filename='gauss_in.json'):
    """

    TODO: Fix API - for example should we use named inputs
    TODO: Fix API - Will need standard for *args/**kwargs
    TODO: Need someway of doing validation checks on input params
    """

    if hasattr(input_json, 'read'):
        json_stream = input_json
    else:
        json_stream = file(input_json, 'r')

    # Open file and parse either
    user_inputs = json.load(json_stream)

    # Check for required inputs
    if 'run_name' not in user_inputs:
        raise Exception("EasyVVUQ wrapper requires a run_name in input JSON")

    run_name = user_inputs['run_name']
    
    gauss_params = {x: y for x, y in user_inputs.items() if x != 'run_name'}

    # Write target input file
    target_path = os.path.join(basedir, run_name)
    os.makedirs(target_path)
    target_file_path = os.join_path(target_path, target_filename)
    with open(target_file_path, 'w') as fp:
        json.dump(gauss_params, fp)
    
    # Write execution file
    run_cmd_file_path = os.path.join(target_path, 'run_cmd.txt')
    with open(run_cmd_file_path, 'w') as fp:
        fp.write(f"python3 gauss_json.py {target_filename}")

if __name__ == "__main__":

    input_json_file = sys.argv[0]
    output_basedir = sys.argv[1]

    wrap_gauss(input_json_file, output_basedir)
