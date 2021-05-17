window.BENCHMARK_DATA = {
  "lastUpdate": 1621245066236,
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
          "id": "6a726fb6e53ca9132cace0626ef6cb4515f443c2",
          "message": "Merge pull request #341 from UCL-CCS/jsonpickle-test\n\nremoved jsonpickle",
          "timestamp": "2021-05-17T11:42:26+02:00",
          "tree_id": "0181ee64eb7e67419ea403da417fd5ee59bf407b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/6a726fb6e53ca9132cace0626ef6cb4515f443c2"
        },
        "date": 1621245065142,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05600432989116223,
            "unit": "iter/sec",
            "range": "stddev: 0.1702133711364724",
            "extra": "mean: 17.855762258800013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07460698455383877,
            "unit": "iter/sec",
            "range": "stddev: 0.09311152879655565",
            "extra": "mean: 13.40357080480003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.87025802520915,
            "unit": "iter/sec",
            "range": "stddev: 0.0007967509979174",
            "extra": "mean: 12.214447885239156 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05628766894378261,
            "unit": "iter/sec",
            "range": "stddev: 0.22807995066847186",
            "extra": "mean: 17.765880498599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07445630295422917,
            "unit": "iter/sec",
            "range": "stddev: 0.24250749803681487",
            "extra": "mean: 13.430696399399983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.125582053669305,
            "unit": "iter/sec",
            "range": "stddev: 0.0016849449344731183",
            "extra": "mean: 25.558725200005483 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}