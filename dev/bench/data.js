window.BENCHMARK_DATA = {
  "lastUpdate": 1622490292634,
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
      },
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
          "id": "d1efc84c8a28c633abea43984dd4b0de2e7f62ff",
          "message": "Pce sc comparison",
          "timestamp": "2021-05-31T15:42:37Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/347/commits/d1efc84c8a28c633abea43984dd4b0de2e7f62ff"
        },
        "date": 1622490291283,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07526471627512858,
            "unit": "iter/sec",
            "range": "stddev: 0.06484332834044501",
            "extra": "mean: 13.286438180999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0890429339244112,
            "unit": "iter/sec",
            "range": "stddev: 0.0482795692303684",
            "extra": "mean: 11.230537403999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 91.06779665062676,
            "unit": "iter/sec",
            "range": "stddev: 0.00018105628618160353",
            "extra": "mean: 10.980830071429182 msec\nrounds: 70"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07549186150968734,
            "unit": "iter/sec",
            "range": "stddev: 0.07331821205715207",
            "extra": "mean: 13.246461009200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08932676663129863,
            "unit": "iter/sec",
            "range": "stddev: 0.060780308273167404",
            "extra": "mean: 11.1948527604 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.82085827008286,
            "unit": "iter/sec",
            "range": "stddev: 0.0001662481498271305",
            "extra": "mean: 20.91137708888861 msec\nrounds: 45"
          }
        ]
      }
    ]
  }
}