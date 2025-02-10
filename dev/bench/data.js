window.BENCHMARK_DATA = {
  "lastUpdate": 1739208202481,
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
          "id": "e455582c290eca1df5d7fa7a8044865ab8d69836",
          "message": "Merge pull request #440 from UCL-CCS/hackathon2025\n\nHackathon Jan 2025",
          "timestamp": "2025-02-10T17:18:52Z",
          "tree_id": "faddd6143c818ace39cf34a60bb4e2f9fc709975",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e455582c290eca1df5d7fa7a8044865ab8d69836"
        },
        "date": 1739208200726,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11586028371867195,
            "unit": "iter/sec",
            "range": "stddev: 0.10282297317799423",
            "extra": "mean: 8.631085372000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1968516787392463,
            "unit": "iter/sec",
            "range": "stddev: 0.022299494021146303",
            "extra": "mean: 5.079966837999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.04484816407926,
            "unit": "iter/sec",
            "range": "stddev: 0.00040389438407863215",
            "extra": "mean: 9.799612797620972 msec\nrounds: 84"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11603972343543774,
            "unit": "iter/sec",
            "range": "stddev: 0.11971992675811768",
            "extra": "mean: 8.617738567399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20458299138900846,
            "unit": "iter/sec",
            "range": "stddev: 0.05134523077316515",
            "extra": "mean: 4.887991876599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.939924819901066,
            "unit": "iter/sec",
            "range": "stddev: 0.0002392409812725469",
            "extra": "mean: 18.53914337735694 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}