window.BENCHMARK_DATA = {
  "lastUpdate": 1741238542507,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
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
          "id": "9fdf22bdec4846b0a9bee452bed73a7d012972d9",
          "message": "Bump jinja2 from 3.1.5 to 3.1.6",
          "timestamp": "2025-02-28T13:41:31Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/443/commits/9fdf22bdec4846b0a9bee452bed73a7d012972d9"
        },
        "date": 1741238531182,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11482799222700424,
            "unit": "iter/sec",
            "range": "stddev: 0.10989878644331072",
            "extra": "mean: 8.708677915599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1893125882251681,
            "unit": "iter/sec",
            "range": "stddev: 0.058626566107546324",
            "extra": "mean: 5.282268914999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.87566369187847,
            "unit": "iter/sec",
            "range": "stddev: 0.00043022000793692405",
            "extra": "mean: 9.626893965907678 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11577570779168662,
            "unit": "iter/sec",
            "range": "stddev: 0.0408424132658578",
            "extra": "mean: 8.637390512000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19602183248217833,
            "unit": "iter/sec",
            "range": "stddev: 0.0448798470468709",
            "extra": "mean: 5.101472562200013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.02064406252605,
            "unit": "iter/sec",
            "range": "stddev: 0.00033180180807720124",
            "extra": "mean: 18.511441641505655 msec\nrounds: 53"
          }
        ]
      },
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
          "id": "f6c2c3a7ba07d030335df83384482f43514f4352",
          "message": "Merge pull request #443 from UCL-CCS/dependabot/pip/jinja2-3.1.6\n\nBump jinja2 from 3.1.5 to 3.1.6",
          "timestamp": "2025-03-06T05:18:00Z",
          "tree_id": "1eaff843fd5bc2adc2fa82a25c18f15512c76af8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f6c2c3a7ba07d030335df83384482f43514f4352"
        },
        "date": 1741238540732,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1170305299883491,
            "unit": "iter/sec",
            "range": "stddev: 0.10109633513217299",
            "extra": "mean: 8.544778871799986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19386110479261456,
            "unit": "iter/sec",
            "range": "stddev: 0.03660635947587113",
            "extra": "mean: 5.158332307399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.98918183875467,
            "unit": "iter/sec",
            "range": "stddev: 0.00010891089535786978",
            "extra": "mean: 9.09180324175891 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1185710318416999,
            "unit": "iter/sec",
            "range": "stddev: 0.07783048123166286",
            "extra": "mean: 8.433763158399984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20140141992691327,
            "unit": "iter/sec",
            "range": "stddev: 0.043083940393508074",
            "extra": "mean: 4.96520829079999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.4751087394768,
            "unit": "iter/sec",
            "range": "stddev: 0.0001724689213488541",
            "extra": "mean: 18.026102566039444 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}