window.BENCHMARK_DATA = {
  "lastUpdate": 1733336728987,
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
          "id": "71005d5cec9a61469927b01379d8d667e9858922",
          "message": "Merge pull request #435 from mzrghorbani/dev\n\nFix issue #391 with database dump.",
          "timestamp": "2024-12-04T14:20:17Z",
          "tree_id": "5cd1ef52b1bc41fdc276c7f50f0ebbb293b2320f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/71005d5cec9a61469927b01379d8d667e9858922"
        },
        "date": 1733322277154,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11872301855001743,
            "unit": "iter/sec",
            "range": "stddev: 0.1018809475498958",
            "extra": "mean: 8.422966432400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19798332376057998,
            "unit": "iter/sec",
            "range": "stddev: 0.0670745914185555",
            "extra": "mean: 5.050930457199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.74604213651365,
            "unit": "iter/sec",
            "range": "stddev: 0.00018863224744407127",
            "extra": "mean: 9.456618704547282 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11927917601874193,
            "unit": "iter/sec",
            "range": "stddev: 0.05144954760354987",
            "extra": "mean: 8.383693058400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1984479614105786,
            "unit": "iter/sec",
            "range": "stddev: 0.024122999600444953",
            "extra": "mean: 5.039104422599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.168326530886205,
            "unit": "iter/sec",
            "range": "stddev: 0.00015537045496653954",
            "extra": "mean: 18.460972750003837 msec\nrounds: 52"
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
          "id": "dbdf9e8e45f63df0068ed89583d7cec8257e2819",
          "message": "Hackathon2024",
          "timestamp": "2024-12-04T14:20:22Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/432/commits/dbdf9e8e45f63df0068ed89583d7cec8257e2819"
        },
        "date": 1733336727664,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1200090355590133,
            "unit": "iter/sec",
            "range": "stddev: 0.06348891268448274",
            "extra": "mean: 8.33270591119999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19695050219881868,
            "unit": "iter/sec",
            "range": "stddev: 0.0635063187410515",
            "extra": "mean: 5.077417873200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.5415993759928,
            "unit": "iter/sec",
            "range": "stddev: 0.0001282202066183518",
            "extra": "mean: 9.474936952940157 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12023125083722849,
            "unit": "iter/sec",
            "range": "stddev: 0.07277750699999255",
            "extra": "mean: 8.317305135200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19702265351555523,
            "unit": "iter/sec",
            "range": "stddev: 0.04824573380325992",
            "extra": "mean: 5.075558480999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.31201847062492,
            "unit": "iter/sec",
            "range": "stddev: 0.0013369384632465617",
            "extra": "mean: 18.412131019230262 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}