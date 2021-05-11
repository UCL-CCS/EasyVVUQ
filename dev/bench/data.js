window.BENCHMARK_DATA = {
  "lastUpdate": 1620731712060,
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "181f87d83d8033f45d085e193072317005168509",
          "message": "updated docstrings in yaml.py",
          "timestamp": "2021-05-11T13:07:22+02:00",
          "tree_id": "f7ae1383106b543dddab8a08d70db569fab85ebe",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/181f87d83d8033f45d085e193072317005168509"
        },
        "date": 1620731711127,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06293728031952439,
            "unit": "iter/sec",
            "range": "stddev: 0.39797027598354306",
            "extra": "mean: 15.888834009399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08005480576211035,
            "unit": "iter/sec",
            "range": "stddev: 0.2789713890819612",
            "extra": "mean: 12.491442462200018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 92.09626756666627,
            "unit": "iter/sec",
            "range": "stddev: 0.0009347563766044013",
            "extra": "mean: 10.858203338980314 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06152529568856662,
            "unit": "iter/sec",
            "range": "stddev: 0.2341219007561046",
            "extra": "mean: 16.25347735119999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08163218287317874,
            "unit": "iter/sec",
            "range": "stddev: 0.19783934460605052",
            "extra": "mean: 12.250070558000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.9647113814899,
            "unit": "iter/sec",
            "range": "stddev: 0.0022682184284605464",
            "extra": "mean: 22.745514949997414 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}