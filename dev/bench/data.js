window.BENCHMARK_DATA = {
  "lastUpdate": 1701779399873,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "committer": {
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "distinct": true,
          "id": "b7890edb297ff603a90d8aedaca9df823412ab52",
          "message": "Fix to pdocs build command issue.",
          "timestamp": "2023-12-05T12:23:41Z",
          "tree_id": "91f2c231d7377042be0bf8ff1697df6b868579fc",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/b7890edb297ff603a90d8aedaca9df823412ab52"
        },
        "date": 1701779294290,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11883110630194745,
            "unit": "iter/sec",
            "range": "stddev: 0.08164586273204644",
            "extra": "mean: 8.415304974600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19917277122795404,
            "unit": "iter/sec",
            "range": "stddev: 0.05555647642937504",
            "extra": "mean: 5.020766613000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 119.12077063428526,
            "unit": "iter/sec",
            "range": "stddev: 0.00012104129580882628",
            "extra": "mean: 8.39484159374789 msec\nrounds: 96"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11882536726870638,
            "unit": "iter/sec",
            "range": "stddev: 0.08023741056890708",
            "extra": "mean: 8.415711417399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20053835207257195,
            "unit": "iter/sec",
            "range": "stddev: 0.050959855339839266",
            "extra": "mean: 4.986577328800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 61.410002888997454,
            "unit": "iter/sec",
            "range": "stddev: 0.0005065287346950841",
            "extra": "mean: 16.28399206897229 msec\nrounds: 58"
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
          "id": "41e3cfbac280ad199e3f92da62278ce950eb0858",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/414/commits/41e3cfbac280ad199e3f92da62278ce950eb0858"
        },
        "date": 1701779397231,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11849304174635711,
            "unit": "iter/sec",
            "range": "stddev: 0.0965286441825094",
            "extra": "mean: 8.439314117199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19821803944894018,
            "unit": "iter/sec",
            "range": "stddev: 0.05738346960470813",
            "extra": "mean: 5.044949504999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.81232639269011,
            "unit": "iter/sec",
            "range": "stddev: 0.00010194414093157319",
            "extra": "mean: 8.488076168420752 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11790894876445501,
            "unit": "iter/sec",
            "range": "stddev: 0.0847291674862285",
            "extra": "mean: 8.481120478800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19756207316700994,
            "unit": "iter/sec",
            "range": "stddev: 0.07049415764889014",
            "extra": "mean: 5.061700274600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 61.60756653339142,
            "unit": "iter/sec",
            "range": "stddev: 0.00018212077260383166",
            "extra": "mean: 16.231772431037314 msec\nrounds: 58"
          }
        ]
      }
    ]
  }
}