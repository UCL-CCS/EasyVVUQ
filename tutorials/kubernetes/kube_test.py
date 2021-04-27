from easyvvuq.actions import ExecuteKubernetes

if __name__ == '__main__':
    action = ExecuteKubernetes("sir.yaml", ['input.json'], 'output.csv')
    status = action.act_on_dir('.')
    status.start()
