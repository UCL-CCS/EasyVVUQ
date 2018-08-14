import os, sys
import libEasyVVUQ as easy

app = easy.Application()
app.load_state("test_input/test2.json")
easy.UQP.Basic(app)
easy.populate_runs_dir(app)
app.save_state("out_state.json")
app.print()
easy.apply_for_each_run(app, easy.execute_local)
easy.apply_for_each_run(app, easy.UQP.meanCSV('output.csv'))

