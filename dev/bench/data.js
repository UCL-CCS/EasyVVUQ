window.BENCHMARK_DATA = {
  "lastUpdate": 1733319304574,
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
          "id": "c8968328cc175940f88127e9dbf997aecd457273",
          "message": "Merge pull request #433 from UCL-CCS/code_scanning_alerts\n\nCode scanning alerts",
          "timestamp": "2024-12-04T13:30:41Z",
          "tree_id": "66c3cc1497a8ab43c0e80b16ba9d1e4ca54d4806",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c8968328cc175940f88127e9dbf997aecd457273"
        },
        "date": 1733319302971,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11907551195045359,
            "unit": "iter/sec",
            "range": "stddev: 0.08892923361221217",
            "extra": "mean: 8.398032337800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19589480360909134,
            "unit": "iter/sec",
            "range": "stddev: 0.10899661510234598",
            "extra": "mean: 5.104780635200018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.97847629821857,
            "unit": "iter/sec",
            "range": "stddev: 0.0001323529961028476",
            "extra": "mean: 9.710767103448578 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11877261148942601,
            "unit": "iter/sec",
            "range": "stddev: 0.06572913295093577",
            "extra": "mean: 8.419449462799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19988579875088308,
            "unit": "iter/sec",
            "range": "stddev: 0.017784874848464693",
            "extra": "mean: 5.002856662399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.89176357030998,
            "unit": "iter/sec",
            "range": "stddev: 0.00039230147033311426",
            "extra": "mean: 18.217669372548325 msec\nrounds: 51"
          }
        ]
      }
    ]
  }
}