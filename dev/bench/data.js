window.BENCHMARK_DATA = {
  "lastUpdate": 1621956769432,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "344f461afcf61addde61c8becd42a01e933e0dce",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-25T17:24:44+02:00",
          "tree_id": "7eac9458889bc5fcbd442e0918f3d4e375dcbe03",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/344f461afcf61addde61c8becd42a01e933e0dce"
        },
        "date": 1621956767840,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0663108905511089,
            "unit": "iter/sec",
            "range": "stddev: 0.07256190364457046",
            "extra": "mean: 15.0804791142 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07395355890200116,
            "unit": "iter/sec",
            "range": "stddev: 0.0395577075505215",
            "extra": "mean: 13.5219996826 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.02337737761833,
            "unit": "iter/sec",
            "range": "stddev: 0.000188088491154912",
            "extra": "mean: 13.884380827588842 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06675461436332614,
            "unit": "iter/sec",
            "range": "stddev: 0.09243112665834828",
            "extra": "mean: 14.980237838799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07396979957087921,
            "unit": "iter/sec",
            "range": "stddev: 0.03468373457428476",
            "extra": "mean: 13.51903081800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.17627537122458,
            "unit": "iter/sec",
            "range": "stddev: 0.00020415050147161153",
            "extra": "mean: 26.19427878377448 msec\nrounds: 37"
          }
        ]
      }
    ]
  }
}