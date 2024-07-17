window.BENCHMARK_DATA = {
  "lastUpdate": 1721211052553,
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
          "id": "e74eed20eb0951b92f9a7bb7d943233f94d30557",
          "message": "Merge pull request #422 from UCL-CCS/dpc/further-doc-fixes\n\nadd some more libraries to autodoc_mock_imports",
          "timestamp": "2024-07-01T11:06:55+01:00",
          "tree_id": "5ddc38c2bbe3ed8923132328f54620f14af3890e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e74eed20eb0951b92f9a7bb7d943233f94d30557"
        },
        "date": 1719828676317,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11721470975752726,
            "unit": "iter/sec",
            "range": "stddev: 0.0802701950422126",
            "extra": "mean: 8.531352439199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19750978195853766,
            "unit": "iter/sec",
            "range": "stddev: 0.03421538676473527",
            "extra": "mean: 5.063040372400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.13997414161894,
            "unit": "iter/sec",
            "range": "stddev: 0.0006153536133071009",
            "extra": "mean: 9.602460613636314 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11795994359658793,
            "unit": "iter/sec",
            "range": "stddev: 0.13094116761331726",
            "extra": "mean: 8.477454036599976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19714473334900687,
            "unit": "iter/sec",
            "range": "stddev: 0.03860307413505523",
            "extra": "mean: 5.072415493999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.56530070045482,
            "unit": "iter/sec",
            "range": "stddev: 0.0002925020542568863",
            "extra": "mean: 19.023956615382733 msec\nrounds: 52"
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
          "id": "1f6592088514aed2faeedb17d3e43237479ad076",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/1f6592088514aed2faeedb17d3e43237479ad076"
        },
        "date": 1721211051024,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11790730721665138,
            "unit": "iter/sec",
            "range": "stddev: 0.09592585995246657",
            "extra": "mean: 8.481238555999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19288345684496896,
            "unit": "iter/sec",
            "range": "stddev: 0.04424728767678711",
            "extra": "mean: 5.184477800000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 101.68458511037065,
            "unit": "iter/sec",
            "range": "stddev: 0.00016241760862616657",
            "extra": "mean: 9.834332302330568 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11768461980827623,
            "unit": "iter/sec",
            "range": "stddev: 0.06509037598798263",
            "extra": "mean: 8.497287084999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1924789827302092,
            "unit": "iter/sec",
            "range": "stddev: 0.05401697444192741",
            "extra": "mean: 5.195372428799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.646794185352306,
            "unit": "iter/sec",
            "range": "stddev: 0.0016684231240068057",
            "extra": "mean: 19.362286000001387 msec\nrounds: 51"
          }
        ]
      }
    ]
  }
}