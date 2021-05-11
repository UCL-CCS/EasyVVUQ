window.BENCHMARK_DATA = {
  "lastUpdate": 1620730976580,
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
          "id": "c218465732cc171e2e85eb9fe53de245fd7c5809",
          "message": "remove base action class",
          "timestamp": "2021-05-11T12:54:14+02:00",
          "tree_id": "6b19f8587d06c0cf567caf59e9171e15e9566eb5",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c218465732cc171e2e85eb9fe53de245fd7c5809"
        },
        "date": 1620730975610,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05582349747023596,
            "unit": "iter/sec",
            "range": "stddev: 0.16121213301256604",
            "extra": "mean: 17.91360350599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07224890593023689,
            "unit": "iter/sec",
            "range": "stddev: 0.07010414113810257",
            "extra": "mean: 13.841040042400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.81428208763414,
            "unit": "iter/sec",
            "range": "stddev: 0.0009234771948408748",
            "extra": "mean: 13.19012687931404 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05581363745110036,
            "unit": "iter/sec",
            "range": "stddev: 0.1044471884537277",
            "extra": "mean: 17.916768117400046 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07486020742981635,
            "unit": "iter/sec",
            "range": "stddev: 0.25103176223600215",
            "extra": "mean: 13.358231754000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.61562592828981,
            "unit": "iter/sec",
            "range": "stddev: 0.0014229980912471216",
            "extra": "mean: 25.242564684201863 msec\nrounds: 38"
          }
        ]
      }
    ]
  }
}