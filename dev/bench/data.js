window.BENCHMARK_DATA = {
  "lastUpdate": 1621351329179,
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "de9ca5581c5ae061b86e13ce270262ac7dabe7c3",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-05-18T17:15:10+02:00",
          "tree_id": "f5dbb5409a844c0b1dc3534590e0ec1b31e81e45",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/de9ca5581c5ae061b86e13ce270262ac7dabe7c3"
        },
        "date": 1621351328159,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07635770673800299,
            "unit": "iter/sec",
            "range": "stddev: 0.07283143840886648",
            "extra": "mean: 13.096255017599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08993181628980321,
            "unit": "iter/sec",
            "range": "stddev: 0.030471582783377395",
            "extra": "mean: 11.119535235199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.1023294689122,
            "unit": "iter/sec",
            "range": "stddev: 0.00013677926690988505",
            "extra": "mean: 12.4840314461529 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07657087829060252,
            "unit": "iter/sec",
            "range": "stddev: 0.09588847521120346",
            "extra": "mean: 13.059795346800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09009300960357693,
            "unit": "iter/sec",
            "range": "stddev: 0.04285298761524459",
            "extra": "mean: 11.099640298399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.021856071907976,
            "unit": "iter/sec",
            "range": "stddev: 0.0000734970813874104",
            "extra": "mean: 23.243999476186502 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}