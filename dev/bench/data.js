window.BENCHMARK_DATA = {
  "lastUpdate": 1696330459854,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "wouteredeling@gmail.com",
            "name": "Wouter Edeling",
            "username": "wedeling"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "253386dd6f4fd6ba3ce4ce46d4e550293e442926",
          "message": "Update README.md",
          "timestamp": "2023-10-03T12:48:59+02:00",
          "tree_id": "1ad8781db3b7e77b4e44a86ab735de2a7e548a40",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/253386dd6f4fd6ba3ce4ce46d4e550293e442926"
        },
        "date": 1696330457821,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09753639601165566,
            "unit": "iter/sec",
            "range": "stddev: 0.07171517296222504",
            "extra": "mean: 10.252583044800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.15460088277073145,
            "unit": "iter/sec",
            "range": "stddev: 0.05843390226077615",
            "extra": "mean: 6.468268369999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 92.14457373044391,
            "unit": "iter/sec",
            "range": "stddev: 0.0001718995275358315",
            "extra": "mean: 10.852511000000504 msec\nrounds: 75"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09738228385214136,
            "unit": "iter/sec",
            "range": "stddev: 0.06934850309941858",
            "extra": "mean: 10.26880825180001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.15477391847928643,
            "unit": "iter/sec",
            "range": "stddev: 0.0144821791670536",
            "extra": "mean: 6.461036909999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.132114521993486,
            "unit": "iter/sec",
            "range": "stddev: 0.0001221539223060291",
            "extra": "mean: 21.216955999997946 msec\nrounds: 46"
          }
        ]
      }
    ]
  }
}