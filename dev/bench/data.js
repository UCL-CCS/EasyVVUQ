window.BENCHMARK_DATA = {
  "lastUpdate": 1733305577368,
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
          "id": "d607845fdeef9b98b8026dfb63b8e686f5be1ea1",
          "message": "Merge pull request #425 from UCL-CCS/djgroen-actions-update\n\nDjgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-12-04T09:37:20Z",
          "tree_id": "f63059454c5a98dda94f0aa51387479748c5e3d2",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d607845fdeef9b98b8026dfb63b8e686f5be1ea1"
        },
        "date": 1733305303321,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11684369586868891,
            "unit": "iter/sec",
            "range": "stddev: 0.13076636578456075",
            "extra": "mean: 8.558442050000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18943382157089414,
            "unit": "iter/sec",
            "range": "stddev: 0.051366426982805434",
            "extra": "mean: 5.278888382799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 95.50079377589628,
            "unit": "iter/sec",
            "range": "stddev: 0.0009087193431055693",
            "extra": "mean: 10.47111715476016 msec\nrounds: 84"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1175468871447201,
            "unit": "iter/sec",
            "range": "stddev: 0.10901622541567087",
            "extra": "mean: 8.507243571399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.18962339525198268,
            "unit": "iter/sec",
            "range": "stddev: 0.028785128111414163",
            "extra": "mean: 5.273610878400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.10928032992714,
            "unit": "iter/sec",
            "range": "stddev: 0.00023271241355299425",
            "extra": "mean: 19.565918235292543 msec\nrounds: 51"
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
          "id": "ca59500b0d0d7a7a38487bb0bc508b2dbcd70a6e",
          "message": "Full Integration Tests",
          "timestamp": "2024-12-04T09:37:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/ca59500b0d0d7a7a38487bb0bc508b2dbcd70a6e"
        },
        "date": 1733305575793,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11949859035060488,
            "unit": "iter/sec",
            "range": "stddev: 0.10562039058513142",
            "extra": "mean: 8.368299551200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20153255597447478,
            "unit": "iter/sec",
            "range": "stddev: 0.025632895843363784",
            "extra": "mean: 4.961977459000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.60710560735964,
            "unit": "iter/sec",
            "range": "stddev: 0.00013999934652351848",
            "extra": "mean: 9.469059816087897 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1200749304529892,
            "unit": "iter/sec",
            "range": "stddev: 0.12419969368207495",
            "extra": "mean: 8.32813307680001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20154252201720332,
            "unit": "iter/sec",
            "range": "stddev: 0.03999431080975945",
            "extra": "mean: 4.961732094999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.12068434614045,
            "unit": "iter/sec",
            "range": "stddev: 0.00018960787183577488",
            "extra": "mean: 18.14200987999925 msec\nrounds: 50"
          }
        ]
      }
    ]
  }
}