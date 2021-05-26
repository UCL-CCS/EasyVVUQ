window.BENCHMARK_DATA = {
  "lastUpdate": 1622037640383,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
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
          "id": "f549b8ae0a3831da623ff88c317e96d0aa6cb7da",
          "message": "gp stuff",
          "timestamp": "2021-05-25T16:32:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/345/commits/f549b8ae0a3831da623ff88c317e96d0aa6cb7da"
        },
        "date": 1622037639260,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07767128106719047,
            "unit": "iter/sec",
            "range": "stddev: 0.07053211820897316",
            "extra": "mean: 12.8747715534 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08689943424242548,
            "unit": "iter/sec",
            "range": "stddev: 0.0876319815487725",
            "extra": "mean: 11.50755478120002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.15056572477664,
            "unit": "iter/sec",
            "range": "stddev: 0.0003467152492049448",
            "extra": "mean: 12.026376384617029 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07790636847803913,
            "unit": "iter/sec",
            "range": "stddev: 0.04879114513120218",
            "extra": "mean: 12.835921113199982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08706061270677849,
            "unit": "iter/sec",
            "range": "stddev: 0.05482158826341066",
            "extra": "mean: 11.48625042839999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.74421496460403,
            "unit": "iter/sec",
            "range": "stddev: 0.000486261747601849",
            "extra": "mean: 23.39497873169709 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}