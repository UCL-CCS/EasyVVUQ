window.BENCHMARK_DATA = {
  "lastUpdate": 1733309390515,
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "9523da25a903151939f238d7399eb3c0d02df60e",
          "message": "Update pdocs.yml\n\nAttempt to fix docs build directly.",
          "timestamp": "2024-12-04T10:45:35Z",
          "tree_id": "6bf42bd5939afef547bb8c6b90941b3ed02ea418",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9523da25a903151939f238d7399eb3c0d02df60e"
        },
        "date": 1733309389537,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11891102686271311,
            "unit": "iter/sec",
            "range": "stddev: 0.08862935626213218",
            "extra": "mean: 8.409649015599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1953782255708891,
            "unit": "iter/sec",
            "range": "stddev: 0.06630967878825714",
            "extra": "mean: 5.118277623199981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.48625323343504,
            "unit": "iter/sec",
            "range": "stddev: 0.00012290012787365522",
            "extra": "mean: 9.570636988636945 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11875073741446993,
            "unit": "iter/sec",
            "range": "stddev: 0.06043409730760119",
            "extra": "mean: 8.42100033879999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19398248031780238,
            "unit": "iter/sec",
            "range": "stddev: 0.07558269325198012",
            "extra": "mean: 5.1551047206000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.72741471774233,
            "unit": "iter/sec",
            "range": "stddev: 0.0006359458809834306",
            "extra": "mean: 18.612471961539804 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}