window.BENCHMARK_DATA = {
  "lastUpdate": 1621960048872,
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
          "id": "4dc4fc0bd4b7846cdeaf5a0a39d763826586eb9f",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-25T18:18:23+02:00",
          "tree_id": "92679718a24ce83c3bd642a0fde761b5d5de7e63",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4dc4fc0bd4b7846cdeaf5a0a39d763826586eb9f"
        },
        "date": 1621960047769,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05340103205625502,
            "unit": "iter/sec",
            "range": "stddev: 0.09456074634356039",
            "extra": "mean: 18.726229840400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06866499571493648,
            "unit": "iter/sec",
            "range": "stddev: 0.11674273871308496",
            "extra": "mean: 14.56346118700002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.43345809845562,
            "unit": "iter/sec",
            "range": "stddev: 0.0008226553057179469",
            "extra": "mean: 12.91431410345271 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.052880574402744414,
            "unit": "iter/sec",
            "range": "stddev: 0.1332216417357263",
            "extra": "mean: 18.9105358876 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06879356466920798,
            "unit": "iter/sec",
            "range": "stddev: 0.11759117982386241",
            "extra": "mean: 14.536243394399946 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.822163699425246,
            "unit": "iter/sec",
            "range": "stddev: 0.00188641589445258",
            "extra": "mean: 25.75848187500185 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}