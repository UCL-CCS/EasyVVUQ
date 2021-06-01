window.BENCHMARK_DATA = {
  "lastUpdate": 1622532194882,
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
          "id": "0a0928ff2cae70d086283eaa1ca14353006b4191",
          "message": "Update requirements.txt",
          "timestamp": "2021-06-01T09:16:20+02:00",
          "tree_id": "09eef4d7fab8166658838393b2b9946a04119425",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0a0928ff2cae70d086283eaa1ca14353006b4191"
        },
        "date": 1622532193975,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07516846267447519,
            "unit": "iter/sec",
            "range": "stddev: 0.07480448265242592",
            "extra": "mean: 13.303451532999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08878994087997001,
            "unit": "iter/sec",
            "range": "stddev: 0.03613894400519578",
            "extra": "mean: 11.26253706320001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.59755258255781,
            "unit": "iter/sec",
            "range": "stddev: 0.00021928924988108867",
            "extra": "mean: 11.547670461548547 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07523379504206318,
            "unit": "iter/sec",
            "range": "stddev: 0.11867926716643867",
            "extra": "mean: 13.291898932399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08870200251049176,
            "unit": "iter/sec",
            "range": "stddev: 0.07608308332529773",
            "extra": "mean: 11.273702641399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.10272168053543,
            "unit": "iter/sec",
            "range": "stddev: 0.0003867275945978243",
            "extra": "mean: 21.69069338095499 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}