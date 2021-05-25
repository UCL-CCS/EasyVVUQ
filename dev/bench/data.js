window.BENCHMARK_DATA = {
  "lastUpdate": 1621953927434,
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
          "id": "072e116382958d8eb7533ace2734bd5224b6ce66",
          "message": "move gpanalyse parameters",
          "timestamp": "2021-05-25T16:37:33+02:00",
          "tree_id": "92679718a24ce83c3bd642a0fde761b5d5de7e63",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/072e116382958d8eb7533ace2734bd5224b6ce66"
        },
        "date": 1621953926186,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06597750536496218,
            "unit": "iter/sec",
            "range": "stddev: 0.3647550613144021",
            "extra": "mean: 15.156680969800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07644257131875232,
            "unit": "iter/sec",
            "range": "stddev: 0.039026334312197195",
            "extra": "mean: 13.0817158914 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.52192865041694,
            "unit": "iter/sec",
            "range": "stddev: 0.00016248056246653578",
            "extra": "mean: 13.241187266666543 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06882856967237316,
            "unit": "iter/sec",
            "range": "stddev: 0.08695550075787836",
            "extra": "mean: 14.528850515999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0764789045917782,
            "unit": "iter/sec",
            "range": "stddev: 0.03728531718155203",
            "extra": "mean: 13.075501085400015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.77793683218754,
            "unit": "iter/sec",
            "range": "stddev: 0.00018248237256286275",
            "extra": "mean: 25.139564282047406 msec\nrounds: 39"
          }
        ]
      }
    ]
  }
}