window.BENCHMARK_DATA = {
  "lastUpdate": 1614938578311,
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
          "id": "63e0ef3a17702e294e559223e02e254d14ef0beb",
          "message": "switch to random sampler in the benchmark",
          "timestamp": "2021-03-05T10:36:11+01:00",
          "tree_id": "12bbfb4786ec32dded71e2f06ee12567c31d266f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/63e0ef3a17702e294e559223e02e254d14ef0beb"
        },
        "date": 1614937979811,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.016968405793070566,
            "unit": "iter/sec",
            "range": "stddev: 1.6657898172267298",
            "extra": "mean: 58.933055479400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.12581519660829585,
            "unit": "iter/sec",
            "range": "stddev: 0.04407669845616022",
            "extra": "mean: 7.948165459799975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.8837793767907066,
            "unit": "iter/sec",
            "range": "stddev: 0.019093985161128556",
            "extra": "mean: 1.1315041131999806 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.017861498281560688,
            "unit": "iter/sec",
            "range": "stddev: 0.6876158411863663",
            "extra": "mean: 55.98634471960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.13678770683100816,
            "unit": "iter/sec",
            "range": "stddev: 0.08577785617245892",
            "extra": "mean: 7.31059846799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.8788672877017757,
            "unit": "iter/sec",
            "range": "stddev: 0.023556023549316057",
            "extra": "mean: 1.1378282182000248 sec\nrounds: 5"
          }
        ]
      },
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
          "id": "5c50000306784e571e642b17fe8bc737d151ef90",
          "message": "another typo in the benchmark",
          "timestamp": "2021-03-05T10:46:12+01:00",
          "tree_id": "c78908feec592add4ae406bf7df8c04bce42e47b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5c50000306784e571e642b17fe8bc737d151ef90"
        },
        "date": 1614938577631,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.017482682938384297,
            "unit": "iter/sec",
            "range": "stddev: 0.18012740520735981",
            "extra": "mean: 57.19945866 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10844356823695446,
            "unit": "iter/sec",
            "range": "stddev: 0.08016638635136153",
            "extra": "mean: 9.22138598219999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7280318465556737,
            "unit": "iter/sec",
            "range": "stddev: 0.042578129239668874",
            "extra": "mean: 1.3735662865999756 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.018192478490293547,
            "unit": "iter/sec",
            "range": "stddev: 0.4976523526012892",
            "extra": "mean: 54.967771463000055 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.12147321030897262,
            "unit": "iter/sec",
            "range": "stddev: 0.30325163100790237",
            "extra": "mean: 8.232267818200034 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7852006277666463,
            "unit": "iter/sec",
            "range": "stddev: 0.051753611805625876",
            "extra": "mean: 1.2735598579999987 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}