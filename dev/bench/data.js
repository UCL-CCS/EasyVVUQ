window.BENCHMARK_DATA = {
  "lastUpdate": 1623663798560,
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
          "id": "bf60e028b242fe574a87ce52bd12d4bbb61a1ad1",
          "message": "Integration with QCG-PJ",
          "timestamp": "2021-06-11T15:35:48Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/343/commits/bf60e028b242fe574a87ce52bd12d4bbb61a1ad1"
        },
        "date": 1623663796960,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05277896699610108,
            "unit": "iter/sec",
            "range": "stddev: 0.08694197288038678",
            "extra": "mean: 18.946941498 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07263450057712086,
            "unit": "iter/sec",
            "range": "stddev: 0.057635025844814225",
            "extra": "mean: 13.767562137199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 79.74716842678421,
            "unit": "iter/sec",
            "range": "stddev: 0.0005597804735437229",
            "extra": "mean: 12.539630180325446 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053297753267192556,
            "unit": "iter/sec",
            "range": "stddev: 0.10296763574032032",
            "extra": "mean: 18.762516967400018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07220817891146604,
            "unit": "iter/sec",
            "range": "stddev: 0.15985491881958439",
            "extra": "mean: 13.8488466968 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.38217644581825,
            "unit": "iter/sec",
            "range": "stddev: 0.0009538513570896146",
            "extra": "mean: 24.164992900006155 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}