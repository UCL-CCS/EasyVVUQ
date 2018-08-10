import os, sys
import json

def generic_wrapper(input_json, targetdir):
    
    if hasattr(input_json, 'read'):
        json_stream = input_json
    else:
        json_stream = open(input_json, 'r')

    # Open file and extract the app and params blocks
    input_json = json.load(json_stream)
    app = input_json["app"]
    params = input_json["params"]

    # Check that a template and run_cmd have been supplied in the application info block
    if "template" not in app.keys():
        sys.exit("Generic wrapper needs the desired application template ('template') to have been specified in the 'app' block")
    if "run-cmd" not in app.keys():
        sys.exit("Generic wrapper needs the run command ('run-cmd') to have been specified in the 'app' block")
    if "inputfilename" not in app.keys():
        sys.exit("Generic wrapper needs the filename to give to the application input file ('inputfilename') to have been specified in the 'app' block")

    # Load template file
    with open(app["template"], "r") as in_template:
        template = in_template.readlines()

    # Perform substitution of variables
    output_string = ''
    for line in template:
        for param, value in params.items():
            pattern = '$' + param
            line = line.replace(pattern, str(value))
        output_string += line

    # Write target input file
    target_filename = app["inputfilename"]
    target_file_path = os.path.join(targetdir, target_filename)
    with open(target_file_path, 'w') as fp:
        fp.write(output_string)
    
    # Write execution file
    run_cmd_file_path = os.path.join(targetdir, 'run_cmd.txt')
    with open(run_cmd_file_path, 'w') as fp:
        fp.write(app["run-cmd"])

if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 generic.py INPUT_JSON_FILE TARGETDIR")

    input_json_file = sys.argv[1]
    targetdir = sys.argv[2]

    generic_wrapper(input_json_file, targetdir)
