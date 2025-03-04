from easyvvuq.actions import ExecuteKubernetes

if __name__ == '__main__':
    action = ExecuteKubernetes("orbitfold/easyvvuq:latest", "python3 /EasyVVUQ/docs/epidemic/epidemic.py /config/epidemic_in.json out.csv && cat out.csv", ['input.json'], 'output.csv')
    action.start({'rundir': '.'})
    
