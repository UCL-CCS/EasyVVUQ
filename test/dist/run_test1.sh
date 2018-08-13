# Run UQP
python3 UQP/UQP_basic.py test_input/test1.json uqp_runs.json || exit

# Run splitter
python3 splitter.py uqp_runs.json runs_dir.json
