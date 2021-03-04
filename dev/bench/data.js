window.BENCHMARK_DATA = {
  "lastUpdate": 1614884970923,
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
          "id": "caf20a4cbcd8e736f242d4ff0b77eb70f5ba0b6f",
          "message": "set run_name as index",
          "timestamp": "2021-03-04T15:39:14+01:00",
          "tree_id": "ca84d056735f7f957aaa0a1842cb97137e80ab1b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/caf20a4cbcd8e736f242d4ff0b77eb70f5ba0b6f"
        },
        "date": 1614868904991,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_draw",
            "value": 0.01870826160772363,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 53.4523207430002 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_store_results",
            "value": 0.1382887083272835,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 7.2312483939999765 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_get_collation_result",
            "value": 0.9460002097961505,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.0570822180002324 sec\nrounds: 1"
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
          "id": "6263ce8a737dbcafd9e61b0fc2bce4e8f0d240c9",
          "message": "add the dask tutorial planned for the tutorial paper",
          "timestamp": "2021-03-04T18:41:21Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/322/commits/6263ce8a737dbcafd9e61b0fc2bce4e8f0d240c9"
        },
        "date": 1614884970220,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_draw",
            "value": 0.022253955598358473,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 44.935831546 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_store_results",
            "value": 0.1630773432298923,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 6.132059672999986 sec\nrounds: 1"
          },
          {
            "name": "tests/test_db_benchmark.py::test_db_benchmark_get_collation_result",
            "value": 1.165033962440943,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 858.3440760000087 msec\nrounds: 1"
          }
        ]
      }
    ]
  }
}