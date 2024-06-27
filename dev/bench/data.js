window.BENCHMARK_DATA = {
  "lastUpdate": 1719500581392,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "David Coster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b2810f152aa958246ccfd41d29d09c06e8a7d2b2",
          "message": "Merge pull request #418 from UCL-CCS/dpc/improve-docs\n\nimprove the documentation, adding in a reference to Diana's paper",
          "timestamp": "2024-06-27T13:43:39+02:00",
          "tree_id": "a3e1046e46c08eced9b2f07c205613340eb49181",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/b2810f152aa958246ccfd41d29d09c06e8a7d2b2"
        },
        "date": 1719488875221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11809391111440316,
            "unit": "iter/sec",
            "range": "stddev: 0.09875012297230529",
            "extra": "mean: 8.467837084600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19795476962056943,
            "unit": "iter/sec",
            "range": "stddev: 0.06201696868765437",
            "extra": "mean: 5.051659032599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.07034860585497,
            "unit": "iter/sec",
            "range": "stddev: 0.00011517834240595094",
            "extra": "mean: 9.427705415732 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11804787919528771,
            "unit": "iter/sec",
            "range": "stddev: 0.0777914458667359",
            "extra": "mean: 8.471139056599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19698503993210037,
            "unit": "iter/sec",
            "range": "stddev: 0.013958444521924088",
            "extra": "mean: 5.076527640599989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.22734180948195,
            "unit": "iter/sec",
            "range": "stddev: 0.0006310540134006864",
            "extra": "mean: 18.787336846151867 msec\nrounds: 52"
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
          "id": "1618e1054049a1dc8f445a5ca204a9447708c7a3",
          "message": "Update Dockerfile",
          "timestamp": "2024-06-27T11:43:43Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/419/commits/1618e1054049a1dc8f445a5ca204a9447708c7a3"
        },
        "date": 1719500580470,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11919428435654253,
            "unit": "iter/sec",
            "range": "stddev: 0.07112791376090119",
            "extra": "mean: 8.38966402960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20283269681308105,
            "unit": "iter/sec",
            "range": "stddev: 0.03891619568522959",
            "extra": "mean: 4.930171593199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.93650169651589,
            "unit": "iter/sec",
            "range": "stddev: 0.0001089788635620443",
            "extra": "mean: 9.351343873563252 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1198434644493743,
            "unit": "iter/sec",
            "range": "stddev: 0.1039623021897812",
            "extra": "mean: 8.344218056399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2026769407873354,
            "unit": "iter/sec",
            "range": "stddev: 0.028641189034424083",
            "extra": "mean: 4.933960400800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.981812752847674,
            "unit": "iter/sec",
            "range": "stddev: 0.00014253020682896856",
            "extra": "mean: 18.52475767307847 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}