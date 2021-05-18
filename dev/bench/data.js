window.BENCHMARK_DATA = {
  "lastUpdate": 1621344894244,
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
          "id": "97f7219ef8af59a52735b71c73c3b5f383e2b9b2",
          "message": "execute_kubernetes docstrings",
          "timestamp": "2021-05-18T15:26:08+02:00",
          "tree_id": "e9a1948a287bea21f149c0a7a5bba99da9e31386",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/97f7219ef8af59a52735b71c73c3b5f383e2b9b2"
        },
        "date": 1621344892698,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055150166163129066,
            "unit": "iter/sec",
            "range": "stddev: 0.1419291163529441",
            "extra": "mean: 18.132311642400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07546768508117706,
            "unit": "iter/sec",
            "range": "stddev: 0.11760529019874456",
            "extra": "mean: 13.250704575400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 76.526740518934,
            "unit": "iter/sec",
            "range": "stddev: 0.000822428418545126",
            "extra": "mean: 13.067327749998489 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05497948517641362,
            "unit": "iter/sec",
            "range": "stddev: 0.1536840654918747",
            "extra": "mean: 18.1886024722 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07505556152839223,
            "unit": "iter/sec",
            "range": "stddev: 0.10674564315357789",
            "extra": "mean: 13.323463040399975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.95331129738836,
            "unit": "iter/sec",
            "range": "stddev: 0.0011666175400600217",
            "extra": "mean: 24.41804992857247 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}