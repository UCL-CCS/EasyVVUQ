window.BENCHMARK_DATA = {
  "lastUpdate": 1620736506610,
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
          "id": "9b7de20cf1a59df5f401ec6755ebc8874a107657",
          "message": "remove base encoder",
          "timestamp": "2021-05-11T14:27:01+02:00",
          "tree_id": "9e7ce44b19eec06270a9f93fc1718bb254ec5386",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9b7de20cf1a59df5f401ec6755ebc8874a107657"
        },
        "date": 1620736503558,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06772382220412787,
            "unit": "iter/sec",
            "range": "stddev: 0.17916144116031438",
            "extra": "mean: 14.765852951800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0752929934527238,
            "unit": "iter/sec",
            "range": "stddev: 0.051133598378228604",
            "extra": "mean: 13.281448301400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.11106377990264,
            "unit": "iter/sec",
            "range": "stddev: 0.0001420810021131434",
            "extra": "mean: 14.469463285714872 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06833577058758795,
            "unit": "iter/sec",
            "range": "stddev: 0.09194698375483851",
            "extra": "mean: 14.633624401999986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0753823777954625,
            "unit": "iter/sec",
            "range": "stddev: 0.03799523745238108",
            "extra": "mean: 13.26569987900001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.13224087582628,
            "unit": "iter/sec",
            "range": "stddev: 0.00021682832223776736",
            "extra": "mean: 26.224527513512705 msec\nrounds: 37"
          }
        ]
      }
    ]
  }
}