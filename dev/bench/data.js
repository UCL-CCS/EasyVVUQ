window.BENCHMARK_DATA = {
  "lastUpdate": 1623228146558,
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "108ac2e03cfef7a9a2f2592940de1a90caf260a9",
          "message": "Merge pull request #350 from UCL-CCS/dataframe-sampling\n\nadded dataframe_sampler",
          "timestamp": "2021-06-09T10:35:38+02:00",
          "tree_id": "7eeb0798077bc667571762c59abbda54e4036e5a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/108ac2e03cfef7a9a2f2592940de1a90caf260a9"
        },
        "date": 1623228145509,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07533434131457449,
            "unit": "iter/sec",
            "range": "stddev: 0.05759948189169888",
            "extra": "mean: 13.274158671200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09008746404862901,
            "unit": "iter/sec",
            "range": "stddev: 0.0889886076777143",
            "extra": "mean: 11.100323564000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.88105752037755,
            "unit": "iter/sec",
            "range": "stddev: 0.00023221173806533307",
            "extra": "mean: 11.125814800001471 msec\nrounds: 70"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07557316547074928,
            "unit": "iter/sec",
            "range": "stddev: 0.08765987165863696",
            "extra": "mean: 13.232210054600023 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09046030769435304,
            "unit": "iter/sec",
            "range": "stddev: 0.03519970027536819",
            "extra": "mean: 11.054572170799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.13261331374291,
            "unit": "iter/sec",
            "range": "stddev: 0.000250809832141325",
            "extra": "mean: 21.21673146666833 msec\nrounds: 45"
          }
        ]
      }
    ]
  }
}