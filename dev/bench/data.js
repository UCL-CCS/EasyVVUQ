window.BENCHMARK_DATA = {
  "lastUpdate": 1688738809997,
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
          "id": "07d06050e9608b92ccf854e517b8b69081b83439",
          "message": "Merge pull request #398 from UCL-CCS/djgroen-patch-2\n\nUpdate execute_qcgpj.py",
          "timestamp": "2023-07-07T15:00:16+01:00",
          "tree_id": "4878fbdf360ec8a705171670fbd24c53dda6130c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/07d06050e9608b92ccf854e517b8b69081b83439"
        },
        "date": 1688738808597,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08081611103515803,
            "unit": "iter/sec",
            "range": "stddev: 0.01697703008619096",
            "extra": "mean: 12.373770368200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11606709286465554,
            "unit": "iter/sec",
            "range": "stddev: 0.10285783532454423",
            "extra": "mean: 8.615706444600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.55662660567076,
            "unit": "iter/sec",
            "range": "stddev: 0.0001486991634258608",
            "extra": "mean: 13.782338661288364 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08064825869856482,
            "unit": "iter/sec",
            "range": "stddev: 0.10991828915252438",
            "extra": "mean: 12.399523760800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.11495931225610187,
            "unit": "iter/sec",
            "range": "stddev: 0.046975737773083164",
            "extra": "mean: 8.698729840800013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.04297100087153,
            "unit": "iter/sec",
            "range": "stddev: 0.00017496100004916164",
            "extra": "mean: 26.995674833329986 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}