window.BENCHMARK_DATA = {
  "lastUpdate": 1622476195944,
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
          "id": "9213f4801d1d1d80835e46da366bfccbe53f7395",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-31T17:42:34+02:00",
          "tree_id": "7fe7b9c90ab8b9b959bb4787b419e92c6bf12f51",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9213f4801d1d1d80835e46da366bfccbe53f7395"
        },
        "date": 1622476194888,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07328837869124843,
            "unit": "iter/sec",
            "range": "stddev: 0.4586383047472748",
            "extra": "mean: 13.644728098200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07882532374150544,
            "unit": "iter/sec",
            "range": "stddev: 0.06249603600486896",
            "extra": "mean: 12.686278375200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.06708797420937,
            "unit": "iter/sec",
            "range": "stddev: 0.00021233888394210429",
            "extra": "mean: 13.321417241382372 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07038748118090496,
            "unit": "iter/sec",
            "range": "stddev: 0.10641613171319597",
            "extra": "mean: 14.207071814799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0804611317771726,
            "unit": "iter/sec",
            "range": "stddev: 0.04512769295787682",
            "extra": "mean: 12.42836109699997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.660266396553276,
            "unit": "iter/sec",
            "range": "stddev: 0.0006195476850730718",
            "extra": "mean: 24.00368712195115 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}