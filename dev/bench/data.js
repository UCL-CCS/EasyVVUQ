window.BENCHMARK_DATA = {
  "lastUpdate": 1614866894560,
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
          "id": "ba32edae1a0f6778a39ccf52c7a04497b597d41a",
          "message": "messing with the benchmark workflow",
          "timestamp": "2021-03-04T15:05:45+01:00",
          "tree_id": "86a9911d99e6351aae2010a6e9e5925a3e1e126e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ba32edae1a0f6778a39ccf52c7a04497b597d41a"
        },
        "date": 1614866894081,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_draw",
            "value": 0.0270036618940036,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 37.032014544000006 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_store_results",
            "value": 0.033494380397982776,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 29.855754551000018 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_get_collation_result",
            "value": 1.1985997689013383,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 834.3068519999974 msec\nrounds: 1"
          }
        ]
      }
    ]
  }
}