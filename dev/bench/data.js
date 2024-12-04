window.BENCHMARK_DATA = {
  "lastUpdate": 1733305304414,
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
      }
    ]
  }
}