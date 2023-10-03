window.BENCHMARK_DATA = {
  "lastUpdate": 1696332417428,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "DavidPCoster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "0d27a6381b1019596a3118a000083c39ec8ae49b",
          "message": "Merge pull request #405 from UCL-CCS/feature/decrease_needed_memory\n\nFeature/decrease needed memory (Issue 404)",
          "timestamp": "2023-10-03T13:20:17+02:00",
          "tree_id": "3c4cd6d17200ddfe6ff3a4a5611930f322193562",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0d27a6381b1019596a3118a000083c39ec8ae49b"
        },
        "date": 1696332415328,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08094409373872408,
            "unit": "iter/sec",
            "range": "stddev: 0.14249084540885787",
            "extra": "mean: 12.3542058946 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11467444459059077,
            "unit": "iter/sec",
            "range": "stddev: 0.08056124292395488",
            "extra": "mean: 8.720338725599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 67.86138045529297,
            "unit": "iter/sec",
            "range": "stddev: 0.00017029841610480265",
            "extra": "mean: 14.735921864407095 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0806325109493175,
            "unit": "iter/sec",
            "range": "stddev: 0.10499664710661842",
            "extra": "mean: 12.401945421599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.11402539885852998,
            "unit": "iter/sec",
            "range": "stddev: 0.07213734277034899",
            "extra": "mean: 8.769975900199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.959268038103694,
            "unit": "iter/sec",
            "range": "stddev: 0.00019887361353020265",
            "extra": "mean: 27.80924236111717 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}