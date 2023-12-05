window.BENCHMARK_DATA = {
  "lastUpdate": 1701779295477,
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
      }
    ]
  }
}