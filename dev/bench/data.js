window.BENCHMARK_DATA = {
  "lastUpdate": 1623252633505,
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
          "id": "4b7b2bc211223e5ea0e31bde35e7504dc091a4e0",
          "message": "remove restartable_campaign_tutorial.rst",
          "timestamp": "2021-06-09T17:23:24+02:00",
          "tree_id": "a26a0d511462a07338e61526847cc854861b3be0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4b7b2bc211223e5ea0e31bde35e7504dc091a4e0"
        },
        "date": 1623252632029,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07506642935430319,
            "unit": "iter/sec",
            "range": "stddev: 0.09353045095964799",
            "extra": "mean: 13.321534121200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08806415454707352,
            "unit": "iter/sec",
            "range": "stddev: 0.09689396430580743",
            "extra": "mean: 11.355357978999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.47276781398557,
            "unit": "iter/sec",
            "range": "stddev: 0.00024177134303478935",
            "extra": "mean: 11.176585059702257 msec\nrounds: 67"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07487460449251762,
            "unit": "iter/sec",
            "range": "stddev: 0.15948948211257938",
            "extra": "mean: 13.355663202200049 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08807804985753805,
            "unit": "iter/sec",
            "range": "stddev: 0.09205692923449443",
            "extra": "mean: 11.353566542600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.69482756959306,
            "unit": "iter/sec",
            "range": "stddev: 0.0003414148087468053",
            "extra": "mean: 20.96663413953783 msec\nrounds: 43"
          }
        ]
      }
    ]
  }
}