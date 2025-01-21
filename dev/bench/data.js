window.BENCHMARK_DATA = {
  "lastUpdate": 1737467645578,
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
          "id": "546287531c57366ed7f6181af0755a7650e07ef7",
          "message": "Another attempted fix.",
          "timestamp": "2025-01-21T13:49:36Z",
          "tree_id": "512c419f0454894c52c1c5b9557c696b8770e149",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/546287531c57366ed7f6181af0755a7650e07ef7"
        },
        "date": 1737467644203,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11715510132053863,
            "unit": "iter/sec",
            "range": "stddev: 0.09561601238123801",
            "extra": "mean: 8.535693185600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19158114683388675,
            "unit": "iter/sec",
            "range": "stddev: 0.007080964486174515",
            "extra": "mean: 5.2197202936 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.44117652293693,
            "unit": "iter/sec",
            "range": "stddev: 0.0013025566385097692",
            "extra": "mean: 9.307418555552733 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11820724779088476,
            "unit": "iter/sec",
            "range": "stddev: 0.1011388509603096",
            "extra": "mean: 8.4597181534 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1984784226914822,
            "unit": "iter/sec",
            "range": "stddev: 0.040064144310440766",
            "extra": "mean: 5.038331051000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.737811892673406,
            "unit": "iter/sec",
            "range": "stddev: 0.0004171693467356305",
            "extra": "mean: 17.94114203703514 msec\nrounds: 54"
          }
        ]
      }
    ]
  }
}