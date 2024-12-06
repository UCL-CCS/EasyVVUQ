window.BENCHMARK_DATA = {
  "lastUpdate": 1733496418053,
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
          "id": "5624a2e2d5a5a2812466b3239cfbdb570608b2f7",
          "message": "Merge pull request #432 from UCL-CCS/hackathon2024\n\nHackathon2024",
          "timestamp": "2024-12-06T15:42:36+01:00",
          "tree_id": "ae835c818ae0c1d01c2fb7fcc1831617c91dfe93",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5624a2e2d5a5a2812466b3239cfbdb570608b2f7"
        },
        "date": 1733496416913,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1203822963983597,
            "unit": "iter/sec",
            "range": "stddev: 0.06633665084257066",
            "extra": "mean: 8.306869281599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19524074759908525,
            "unit": "iter/sec",
            "range": "stddev: 0.08049567887820311",
            "extra": "mean: 5.121881637399985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.33569880197867,
            "unit": "iter/sec",
            "range": "stddev: 0.0003653899929664167",
            "extra": "mean: 9.40417951136267 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12024096122890127,
            "unit": "iter/sec",
            "range": "stddev: 0.05816295225964996",
            "extra": "mean: 8.316633448200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19530444509539063,
            "unit": "iter/sec",
            "range": "stddev: 0.056750479976298535",
            "extra": "mean: 5.120211163199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.86759240112265,
            "unit": "iter/sec",
            "range": "stddev: 0.00040705896891819884",
            "extra": "mean: 18.915179499998658 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}