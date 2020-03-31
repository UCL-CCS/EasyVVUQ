from easyvvuq.decoders.simple_csv import SimpleCSV
import os
import numpy as np


def test_simple_csv():
    decoder = SimpleCSV('test.csv', output_columns=['Step', 'Value'])
    df = decoder.parse_sim_output({'run_dir': os.path.join('tests', 'simple_csv')})
    assert(df['Step'][1] == 1)
    assert(df['Value'][5] == 25.950662)
    restart_dict = decoder.get_restart_dict()
    assert(restart_dict['target_filename'] == 'test.csv')
    assert(restart_dict['output_columns'] == ['Step', 'Value'])
    assert(restart_dict['header'] == 0)
    assert(decoder.sim_complete({'run_dir': os.path.join('tests', 'simple_csv')}))
