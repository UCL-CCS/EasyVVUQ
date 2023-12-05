window.BENCHMARK_DATA = {
  "lastUpdate": 1701781715656,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "j.mccullough@ucl.ac.uk",
            "name": "JonMcCullough",
            "username": "JonMcCullough"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4b259fcc6893ce9f2ff7f3c2cee49773b4f9adcd",
          "message": "Merge pull request #414 from UCL-CCS/code_scanning_alerts\n\nCode scanning alerts",
          "timestamp": "2023-12-05T13:04:15Z",
          "tree_id": "aa7be13df4b5b09fcb7dedb01b35a7649a2148fa",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4b259fcc6893ce9f2ff7f3c2cee49773b4f9adcd"
        },
        "date": 1701781714523,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11888069326279814,
            "unit": "iter/sec",
            "range": "stddev: 0.08622529380442127",
            "extra": "mean: 8.411794821800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19965507215979353,
            "unit": "iter/sec",
            "range": "stddev: 0.05273649314623863",
            "extra": "mean: 5.008638093600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 116.02708436108317,
            "unit": "iter/sec",
            "range": "stddev: 0.0005070681793514711",
            "extra": "mean: 8.618677315788965 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11909249271324045,
            "unit": "iter/sec",
            "range": "stddev: 0.06166583974381248",
            "extra": "mean: 8.396834907200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1989787398270291,
            "unit": "iter/sec",
            "range": "stddev: 0.06761537259616823",
            "extra": "mean: 5.025662545 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.690051365840496,
            "unit": "iter/sec",
            "range": "stddev: 0.00022425717274585707",
            "extra": "mean: 16.75321057894551 msec\nrounds: 57"
          }
        ]
      }
    ]
  }
}