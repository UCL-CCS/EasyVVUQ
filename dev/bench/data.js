window.BENCHMARK_DATA = {
  "lastUpdate": 1719383219182,
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
      }
    ]
  }
}