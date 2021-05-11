window.BENCHMARK_DATA = {
  "lastUpdate": 1620723696466,
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
          "id": "efccd37d4e2c8b840b3903a1fb8a125b35a8ef16",
          "message": "Update pdocs.yml",
          "timestamp": "2021-05-11T10:54:04+02:00",
          "tree_id": "cf0e26733286da01338a73604b4ee16191976c20",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/efccd37d4e2c8b840b3903a1fb8a125b35a8ef16"
        },
        "date": 1620723695516,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06995609625718761,
            "unit": "iter/sec",
            "range": "stddev: 0.1446015098501605",
            "extra": "mean: 14.294679856400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07632670502988778,
            "unit": "iter/sec",
            "range": "stddev: 0.06575159299354867",
            "extra": "mean: 13.101574339 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.65912991771988,
            "unit": "iter/sec",
            "range": "stddev: 0.00026110322251573587",
            "extra": "mean: 13.394209135601729 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07016022228686969,
            "unit": "iter/sec",
            "range": "stddev: 0.14652563455477555",
            "extra": "mean: 14.253090532000034 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0812322090869418,
            "unit": "iter/sec",
            "range": "stddev: 0.07318116137009355",
            "extra": "mean: 12.310387852800023 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.73400868676936,
            "unit": "iter/sec",
            "range": "stddev: 0.0002783969105504185",
            "extra": "mean: 25.167357461543524 msec\nrounds: 39"
          }
        ]
      }
    ]
  }
}