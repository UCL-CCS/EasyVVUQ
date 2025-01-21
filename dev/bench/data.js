window.BENCHMARK_DATA = {
  "lastUpdate": 1737467420433,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "committer": {
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "distinct": true,
          "id": "7a1f08ce02b6dd98d7838a1bbe2747be4d668d0c",
          "message": "Added Twine command to upload.",
          "timestamp": "2025-01-21T13:45:45Z",
          "tree_id": "5289a33d314c04a79a9f34d5fb7210f837329e2e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7a1f08ce02b6dd98d7838a1bbe2747be4d668d0c"
        },
        "date": 1737467418640,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11533431867112484,
            "unit": "iter/sec",
            "range": "stddev: 0.08713290322188803",
            "extra": "mean: 8.670446156199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19325135310673477,
            "unit": "iter/sec",
            "range": "stddev: 0.03112970510948948",
            "extra": "mean: 5.174608011399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.16126843972697,
            "unit": "iter/sec",
            "range": "stddev: 0.00026170807873816197",
            "extra": "mean: 8.915733692307324 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11595669619138288,
            "unit": "iter/sec",
            "range": "stddev: 0.10639550464592827",
            "extra": "mean: 8.623909035400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1968171125237099,
            "unit": "iter/sec",
            "range": "stddev: 0.05666259290284772",
            "extra": "mean: 5.080859012600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.38317688763281,
            "unit": "iter/sec",
            "range": "stddev: 0.00021278582275106143",
            "extra": "mean: 17.735786722215398 msec\nrounds: 54"
          }
        ]
      }
    ]
  }
}