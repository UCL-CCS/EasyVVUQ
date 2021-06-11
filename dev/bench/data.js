window.BENCHMARK_DATA = {
  "lastUpdate": 1623426262461,
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
          "id": "ce3bf5255cd9629e763e14101c81842aa63b2bce",
          "message": "typo",
          "timestamp": "2021-06-11T17:35:41+02:00",
          "tree_id": "a2737d0c8946223e7867624bf8372a0296c54a90",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ce3bf5255cd9629e763e14101c81842aa63b2bce"
        },
        "date": 1623426260826,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055133987488725056,
            "unit": "iter/sec",
            "range": "stddev: 0.059056890295497565",
            "extra": "mean: 18.137632439599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07672037721897779,
            "unit": "iter/sec",
            "range": "stddev: 0.06741153213780118",
            "extra": "mean: 13.034346757000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.9680593997937,
            "unit": "iter/sec",
            "range": "stddev: 0.0009348852118664085",
            "extra": "mean: 12.350549184615236 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05578647234744035,
            "unit": "iter/sec",
            "range": "stddev: 0.16190738734184293",
            "extra": "mean: 17.92549264940003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07636342826490818,
            "unit": "iter/sec",
            "range": "stddev: 0.1448394217090048",
            "extra": "mean: 13.095273781200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.989790302799605,
            "unit": "iter/sec",
            "range": "stddev: 0.0015513774041091492",
            "extra": "mean: 23.815313027017584 msec\nrounds: 37"
          }
        ]
      }
    ]
  }
}