window.BENCHMARK_DATA = {
  "lastUpdate": 1620740890731,
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
          "id": "3f80b999dc733d29c4a2e2e420e19776e1ab636e",
          "message": "remove base encoder class",
          "timestamp": "2021-05-11T15:41:20+02:00",
          "tree_id": "675cf024352892df377388bf69aff9933e8f4f45",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3f80b999dc733d29c4a2e2e420e19776e1ab636e"
        },
        "date": 1620740889772,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07751591770405786,
            "unit": "iter/sec",
            "range": "stddev: 0.08270374608571311",
            "extra": "mean: 12.900576160599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08869138780665867,
            "unit": "iter/sec",
            "range": "stddev: 0.09490039118412717",
            "extra": "mean: 11.275051893199976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.04060751293979,
            "unit": "iter/sec",
            "range": "stddev: 0.00015389974897773613",
            "extra": "mean: 11.358395043480645 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07778323141698996,
            "unit": "iter/sec",
            "range": "stddev: 0.07425609347833793",
            "extra": "mean: 12.856241400399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09028274899321197,
            "unit": "iter/sec",
            "range": "stddev: 0.21553996420789462",
            "extra": "mean: 11.076313151199974 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.03486138209725,
            "unit": "iter/sec",
            "range": "stddev: 0.00015505134360293014",
            "extra": "mean: 21.722667777791887 msec\nrounds: 45"
          }
        ]
      }
    ]
  }
}