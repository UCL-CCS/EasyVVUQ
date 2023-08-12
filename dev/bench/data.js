window.BENCHMARK_DATA = {
  "lastUpdate": 1691825939206,
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
          "id": "a3864a662ad85c5bf3e2a4c7fc6dea49ca23a134",
          "message": "Merge pull request #400 from UCL-CCS/goghino-dev\n\nGoghino dev",
          "timestamp": "2023-08-12T09:33:20+02:00",
          "tree_id": "63a6ceedd09418141ee7d22fb62efb6ab982744c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/a3864a662ad85c5bf3e2a4c7fc6dea49ca23a134"
        },
        "date": 1691825937886,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09440782063344193,
            "unit": "iter/sec",
            "range": "stddev: 0.010029744277847107",
            "extra": "mean: 10.592342808999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.12898970283364736,
            "unit": "iter/sec",
            "range": "stddev: 0.06266291542393096",
            "extra": "mean: 7.7525568168000065 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.93703182242469,
            "unit": "iter/sec",
            "range": "stddev: 0.0003002499638489595",
            "extra": "mean: 12.355283823528312 msec\nrounds: 68"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09432309108537376,
            "unit": "iter/sec",
            "range": "stddev: 0.10862906083319758",
            "extra": "mean: 10.601857811200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.12888733604292194,
            "unit": "iter/sec",
            "range": "stddev: 0.05457446784336495",
            "extra": "mean: 7.758714166200013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.13277630432733,
            "unit": "iter/sec",
            "range": "stddev: 0.00044120282012384066",
            "extra": "mean: 23.734490999998332 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}