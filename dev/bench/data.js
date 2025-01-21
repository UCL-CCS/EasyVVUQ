window.BENCHMARK_DATA = {
  "lastUpdate": 1737466736181,
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
          "id": "16c3d298df0ff797e57306cc021b36be75a761cd",
          "message": "Hackathon Jan 2025",
          "timestamp": "2025-01-13T13:49:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/440/commits/16c3d298df0ff797e57306cc021b36be75a761cd"
        },
        "date": 1737466734262,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11639172174196084,
            "unit": "iter/sec",
            "range": "stddev: 0.08170631533489923",
            "extra": "mean: 8.591676323999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18934629969997424,
            "unit": "iter/sec",
            "range": "stddev: 0.013489581808397901",
            "extra": "mean: 5.281328452599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.57262665110127,
            "unit": "iter/sec",
            "range": "stddev: 0.00014569965333372512",
            "extra": "mean: 9.043829655556438 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11664047612434468,
            "unit": "iter/sec",
            "range": "stddev: 0.1020110715017469",
            "extra": "mean: 8.57335320659999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19747709072348357,
            "unit": "iter/sec",
            "range": "stddev: 0.06354912257314614",
            "extra": "mean: 5.063878530600016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.749777456170534,
            "unit": "iter/sec",
            "range": "stddev: 0.0003842810732404091",
            "extra": "mean: 17.937291333336386 msec\nrounds: 54"
          }
        ]
      }
    ]
  }
}