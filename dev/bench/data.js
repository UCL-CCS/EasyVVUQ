window.BENCHMARK_DATA = {
  "lastUpdate": 1719383233842,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "David Coster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "156b37cd6822b658f2d5e0290176ac1f36fdcee6",
          "message": "Merge pull request #416 from UCL-CCS/dpc/fusion-aleatoric-sobol\n\nAdd aleatoric uncertainty impact on Sobols",
          "timestamp": "2024-06-26T08:22:31+02:00",
          "tree_id": "bc36042a03166e23e19e5663484313f90430245d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/156b37cd6822b658f2d5e0290176ac1f36fdcee6"
        },
        "date": 1719383217512,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11759466043857768,
            "unit": "iter/sec",
            "range": "stddev: 0.07963263877837214",
            "extra": "mean: 8.503787470199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20123003817595872,
            "unit": "iter/sec",
            "range": "stddev: 0.037981272219017",
            "extra": "mean: 4.969437013800018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.21985734548744,
            "unit": "iter/sec",
            "range": "stddev: 0.00008513644536959311",
            "extra": "mean: 9.503909482755889 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11860637571444349,
            "unit": "iter/sec",
            "range": "stddev: 0.08331673458999374",
            "extra": "mean: 8.431249955800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20025640502479958,
            "unit": "iter/sec",
            "range": "stddev: 0.012580820333373493",
            "extra": "mean: 4.993598081799985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.63754684969561,
            "unit": "iter/sec",
            "range": "stddev: 0.0006188640610658295",
            "extra": "mean: 18.64365651923313 msec\nrounds: 52"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "UCL-CCS",
            "username": "UCL-CCS"
          },
          "committer": {
            "name": "UCL-CCS",
            "username": "UCL-CCS"
          },
          "id": "5e599a9664d7a132dd8a191c8ab70b446efdc59f",
          "message": "Update conf.py",
          "timestamp": "2024-06-26T06:22:36Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/417/commits/5e599a9664d7a132dd8a191c8ab70b446efdc59f"
        },
        "date": 1719383232618,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1182711792593881,
            "unit": "iter/sec",
            "range": "stddev: 0.07889732834513133",
            "extra": "mean: 8.455145254000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20162778912905208,
            "unit": "iter/sec",
            "range": "stddev: 0.07969150078072362",
            "extra": "mean: 4.959633810000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.14928509925225,
            "unit": "iter/sec",
            "range": "stddev: 0.00047681766295652934",
            "extra": "mean: 9.510288149425671 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11795584529226842,
            "unit": "iter/sec",
            "range": "stddev: 0.1025122181875005",
            "extra": "mean: 8.477748580599984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20304984139816729,
            "unit": "iter/sec",
            "range": "stddev: 0.030220895430452806",
            "extra": "mean: 4.924899192799989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.484283370239844,
            "unit": "iter/sec",
            "range": "stddev: 0.0006789950337628435",
            "extra": "mean: 18.697081403850838 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}