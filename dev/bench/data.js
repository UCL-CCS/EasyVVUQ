window.BENCHMARK_DATA = {
  "lastUpdate": 1719383763070,
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
          "id": "5d4a4cacd9b14713949646cebcc370509be99ff6",
          "message": "Merge pull request #417 from UCL-CCS/module-index-fix\n\nUpdate conf.py",
          "timestamp": "2024-06-26T08:31:45+02:00",
          "tree_id": "5e6950cd820254ad240073d63a4b517502df470c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5d4a4cacd9b14713949646cebcc370509be99ff6"
        },
        "date": 1719383761105,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11734007271203396,
            "unit": "iter/sec",
            "range": "stddev: 0.08692521383708937",
            "extra": "mean: 8.522237773400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19983194456390538,
            "unit": "iter/sec",
            "range": "stddev: 0.029586010681161692",
            "extra": "mean: 5.004204919200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.56612648674745,
            "unit": "iter/sec",
            "range": "stddev: 0.0001802620773612944",
            "extra": "mean: 9.749807604650156 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11722904327483696,
            "unit": "iter/sec",
            "range": "stddev: 0.08052922479788575",
            "extra": "mean: 8.530309316399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19989115285476186,
            "unit": "iter/sec",
            "range": "stddev: 0.04005421175062335",
            "extra": "mean: 5.002722660400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.83422195276727,
            "unit": "iter/sec",
            "range": "stddev: 0.0003255057244326405",
            "extra": "mean: 18.575544769224557 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}