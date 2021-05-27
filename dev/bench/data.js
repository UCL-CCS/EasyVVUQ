window.BENCHMARK_DATA = {
  "lastUpdate": 1622114314505,
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
          "id": "96272c8337482ff01f5a1e9302e9c434244cc815",
          "message": "Merge pull request #344 from UCL-CCS/versions\n\nbump up chaospy",
          "timestamp": "2021-05-27T13:10:20+02:00",
          "tree_id": "5ea20c3537fc4518b1b2088f9181dc0e48b91d75",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/96272c8337482ff01f5a1e9302e9c434244cc815"
        },
        "date": 1622114313063,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05802968198048259,
            "unit": "iter/sec",
            "range": "stddev: 0.22590669685583045",
            "extra": "mean: 17.232560404799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07996493966519529,
            "unit": "iter/sec",
            "range": "stddev: 0.11548407569405345",
            "extra": "mean: 12.505480579200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.87784803526864,
            "unit": "iter/sec",
            "range": "stddev: 0.0012253363607107651",
            "extra": "mean: 12.065950355931664 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05794511303797481,
            "unit": "iter/sec",
            "range": "stddev: 0.05097946130243059",
            "extra": "mean: 17.257710746800022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08108744798071107,
            "unit": "iter/sec",
            "range": "stddev: 0.2429066439656572",
            "extra": "mean: 12.332364933199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.375390688134104,
            "unit": "iter/sec",
            "range": "stddev: 0.00122936845831468",
            "extra": "mean: 21.10800534781585 msec\nrounds: 46"
          }
        ]
      }
    ]
  }
}