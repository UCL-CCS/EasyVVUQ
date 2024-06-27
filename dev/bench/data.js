window.BENCHMARK_DATA = {
  "lastUpdate": 1719488876123,
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
          "id": "b2810f152aa958246ccfd41d29d09c06e8a7d2b2",
          "message": "Merge pull request #418 from UCL-CCS/dpc/improve-docs\n\nimprove the documentation, adding in a reference to Diana's paper",
          "timestamp": "2024-06-27T13:43:39+02:00",
          "tree_id": "a3e1046e46c08eced9b2f07c205613340eb49181",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/b2810f152aa958246ccfd41d29d09c06e8a7d2b2"
        },
        "date": 1719488875221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11809391111440316,
            "unit": "iter/sec",
            "range": "stddev: 0.09875012297230529",
            "extra": "mean: 8.467837084600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19795476962056943,
            "unit": "iter/sec",
            "range": "stddev: 0.06201696868765437",
            "extra": "mean: 5.051659032599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.07034860585497,
            "unit": "iter/sec",
            "range": "stddev: 0.00011517834240595094",
            "extra": "mean: 9.427705415732 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11804787919528771,
            "unit": "iter/sec",
            "range": "stddev: 0.0777914458667359",
            "extra": "mean: 8.471139056599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19698503993210037,
            "unit": "iter/sec",
            "range": "stddev: 0.013958444521924088",
            "extra": "mean: 5.076527640599989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.22734180948195,
            "unit": "iter/sec",
            "range": "stddev: 0.0006310540134006864",
            "extra": "mean: 18.787336846151867 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}