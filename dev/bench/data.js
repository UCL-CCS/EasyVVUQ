window.BENCHMARK_DATA = {
  "lastUpdate": 1737470374296,
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
          "id": "e99de2eee8ed3ee3e85d7d34eff61cf303c24188",
          "message": "Hackathon Jan 2025",
          "timestamp": "2025-01-21T13:49:49Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/440/commits/e99de2eee8ed3ee3e85d7d34eff61cf303c24188"
        },
        "date": 1737470372435,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11678111132233465,
            "unit": "iter/sec",
            "range": "stddev: 0.10115546458105679",
            "extra": "mean: 8.563028632600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1855322255287544,
            "unit": "iter/sec",
            "range": "stddev: 0.027391155089837003",
            "extra": "mean: 5.389899232599982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.53465841927513,
            "unit": "iter/sec",
            "range": "stddev: 0.000168749029120604",
            "extra": "mean: 9.21364672413624 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11675001758486447,
            "unit": "iter/sec",
            "range": "stddev: 0.11698094162455613",
            "extra": "mean: 8.565309202399987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.18413470952947028,
            "unit": "iter/sec",
            "range": "stddev: 0.03788122760470973",
            "extra": "mean: 5.430806622799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.24421767529125,
            "unit": "iter/sec",
            "range": "stddev: 0.0002096047746955481",
            "extra": "mean: 18.10144196226466 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}