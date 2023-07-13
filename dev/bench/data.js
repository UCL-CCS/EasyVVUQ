window.BENCHMARK_DATA = {
  "lastUpdate": 1689266393286,
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
          "id": "422260cf783b1b5e3fb15b7d98de7d1992490d60",
          "message": "Goghino dev",
          "timestamp": "2023-06-15T13:39:42Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/400/commits/422260cf783b1b5e3fb15b7d98de7d1992490d60"
        },
        "date": 1689020012409,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07281069321360141,
            "unit": "iter/sec",
            "range": "stddev: 0.23396163415673252",
            "extra": "mean: 13.734246384199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10244492601125575,
            "unit": "iter/sec",
            "range": "stddev: 0.14415968294670337",
            "extra": "mean: 9.761342400599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.99999345384757,
            "unit": "iter/sec",
            "range": "stddev: 0.0015156633075615051",
            "extra": "mean: 12.04819372131702 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07317516927981632,
            "unit": "iter/sec",
            "range": "stddev: 0.16036624803779387",
            "extra": "mean: 13.66583787699999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10371989579340783,
            "unit": "iter/sec",
            "range": "stddev: 0.08084390892627602",
            "extra": "mean: 9.641351761400028 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.2648032756529,
            "unit": "iter/sec",
            "range": "stddev: 0.00261379706589478",
            "extra": "mean: 26.834973274992535 msec\nrounds: 40"
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
          "id": "dbb30d2f4869682ff5c1409ea5e6c4e4ad9292b3",
          "message": "Goghino dev",
          "timestamp": "2023-06-15T13:39:42Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/400/commits/dbb30d2f4869682ff5c1409ea5e6c4e4ad9292b3"
        },
        "date": 1689266391366,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08032958985358227,
            "unit": "iter/sec",
            "range": "stddev: 0.09441741236777637",
            "extra": "mean: 12.448712881799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1118066247305517,
            "unit": "iter/sec",
            "range": "stddev: 0.05458225501618616",
            "extra": "mean: 8.944013848999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.45943924205392,
            "unit": "iter/sec",
            "range": "stddev: 0.00017281559674173748",
            "extra": "mean: 14.396891350003216 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08007142310727468,
            "unit": "iter/sec",
            "range": "stddev: 0.09673861251461466",
            "extra": "mean: 12.488850093999986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.11069957440773305,
            "unit": "iter/sec",
            "range": "stddev: 0.05170551930565745",
            "extra": "mean: 9.03345839719998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.597117695453356,
            "unit": "iter/sec",
            "range": "stddev: 0.000234535031195094",
            "extra": "mean: 28.092162083328592 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}