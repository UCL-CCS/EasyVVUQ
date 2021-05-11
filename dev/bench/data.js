window.BENCHMARK_DATA = {
  "lastUpdate": 1620730437210,
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
          "id": "bdc62328dce7ec9cde6ebc83d9bb99d517281283",
          "message": "updated the docstring in action_statuses.py",
          "timestamp": "2021-05-11T12:46:20+02:00",
          "tree_id": "1a37969ea32ee3775989908b375f741846a1da04",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bdc62328dce7ec9cde6ebc83d9bb99d517281283"
        },
        "date": 1620730435774,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07042430787540761,
            "unit": "iter/sec",
            "range": "stddev: 0.38282145467371403",
            "extra": "mean: 14.199642569000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07761221117179681,
            "unit": "iter/sec",
            "range": "stddev: 0.16030599273808482",
            "extra": "mean: 12.884570416199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.60710394924851,
            "unit": "iter/sec",
            "range": "stddev: 0.0005216372186293777",
            "extra": "mean: 12.253835163932548 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07142169635159318,
            "unit": "iter/sec",
            "range": "stddev: 0.1927115174086003",
            "extra": "mean: 14.001347644800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07798460125658804,
            "unit": "iter/sec",
            "range": "stddev: 0.36300221567393726",
            "extra": "mean: 12.823044343200014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.12916665330394,
            "unit": "iter/sec",
            "range": "stddev: 0.0010463631911273598",
            "extra": "mean: 24.91953069047018 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}