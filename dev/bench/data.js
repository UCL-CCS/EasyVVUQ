window.BENCHMARK_DATA = {
  "lastUpdate": 1623244629748,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "committer": {
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "59aa8d84eba45f3672bc9e044e65d3ed779f6ef2",
          "message": "make some cells not evaluate",
          "timestamp": "2021-06-09T15:09:11+02:00",
          "tree_id": "4823519742371ea66d5a51add65793aa047f2870",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/59aa8d84eba45f3672bc9e044e65d3ed779f6ef2"
        },
        "date": 1623244628192,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.060439780117438925,
            "unit": "iter/sec",
            "range": "stddev: 0.902179780714924",
            "extra": "mean: 16.545394408400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07889790644275384,
            "unit": "iter/sec",
            "range": "stddev: 0.6614507453224772",
            "extra": "mean: 12.674607541400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 90.61142206185511,
            "unit": "iter/sec",
            "range": "stddev: 0.0018049790264537007",
            "extra": "mean: 11.036136253521754 msec\nrounds: 71"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06222806768385143,
            "unit": "iter/sec",
            "range": "stddev: 0.30270324908124174",
            "extra": "mean: 16.0699188842 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07978590686213448,
            "unit": "iter/sec",
            "range": "stddev: 0.5521458808540562",
            "extra": "mean: 12.533541816199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.080062490242,
            "unit": "iter/sec",
            "range": "stddev: 0.0008957346893555801",
            "extra": "mean: 18.491102893611416 msec\nrounds: 47"
          }
        ]
      }
    ]
  }
}