window.BENCHMARK_DATA = {
  "lastUpdate": 1622046447631,
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
          "id": "c971eab20c0e7f4a35dfe1e21a292b1a16b7fec7",
          "message": "change get_params",
          "timestamp": "2021-05-26T13:59:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/346/commits/c971eab20c0e7f4a35dfe1e21a292b1a16b7fec7"
        },
        "date": 1622046446134,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06482108014000995,
            "unit": "iter/sec",
            "range": "stddev: 1.1933735410333313",
            "extra": "mean: 15.4270801696 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0847974853088379,
            "unit": "iter/sec",
            "range": "stddev: 0.2793530969702726",
            "extra": "mean: 11.792802538399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.75284104613763,
            "unit": "iter/sec",
            "range": "stddev: 0.0019364820660447099",
            "extra": "mean: 11.267244949152174 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06279542563571132,
            "unit": "iter/sec",
            "range": "stddev: 0.5581833516458158",
            "extra": "mean: 15.924726839200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08325381330369933,
            "unit": "iter/sec",
            "range": "stddev: 1.076347109848095",
            "extra": "mean: 12.011461821600017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.97591715996058,
            "unit": "iter/sec",
            "range": "stddev: 0.0014722254705387787",
            "extra": "mean: 18.189782938779388 msec\nrounds: 49"
          }
        ]
      }
    ]
  }
}