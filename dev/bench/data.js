window.BENCHMARK_DATA = {
  "lastUpdate": 1622038071051,
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
          "id": "f549b8ae0a3831da623ff88c317e96d0aa6cb7da",
          "message": "gp stuff",
          "timestamp": "2021-05-25T16:32:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/345/commits/f549b8ae0a3831da623ff88c317e96d0aa6cb7da"
        },
        "date": 1622037639260,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07767128106719047,
            "unit": "iter/sec",
            "range": "stddev: 0.07053211820897316",
            "extra": "mean: 12.8747715534 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08689943424242548,
            "unit": "iter/sec",
            "range": "stddev: 0.0876319815487725",
            "extra": "mean: 11.50755478120002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.15056572477664,
            "unit": "iter/sec",
            "range": "stddev: 0.0003467152492049448",
            "extra": "mean: 12.026376384617029 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07790636847803913,
            "unit": "iter/sec",
            "range": "stddev: 0.04879114513120218",
            "extra": "mean: 12.835921113199982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08706061270677849,
            "unit": "iter/sec",
            "range": "stddev: 0.05482158826341066",
            "extra": "mean: 11.48625042839999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.74421496460403,
            "unit": "iter/sec",
            "range": "stddev: 0.000486261747601849",
            "extra": "mean: 23.39497873169709 msec\nrounds: 41"
          }
        ]
      },
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
          "id": "484be1570a2cf7ed472d7475d2b386abb3ea91a5",
          "message": "Merge pull request #345 from UCL-CCS/gp-improvements\n\ngp stuff",
          "timestamp": "2021-05-26T15:59:11+02:00",
          "tree_id": "dd1c1f33f7f2e096391ebc34fe407d104fb1273e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/484be1570a2cf7ed472d7475d2b386abb3ea91a5"
        },
        "date": 1622038069482,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05776112966464457,
            "unit": "iter/sec",
            "range": "stddev: 0.770965423825617",
            "extra": "mean: 17.312680790799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07308248717655498,
            "unit": "iter/sec",
            "range": "stddev: 0.5048871894264578",
            "extra": "mean: 13.683168685599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.72921314438366,
            "unit": "iter/sec",
            "range": "stddev: 0.0009211126443374985",
            "extra": "mean: 11.53014035000221 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05510423561987556,
            "unit": "iter/sec",
            "range": "stddev: 0.603325701120653",
            "extra": "mean: 18.147425306800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0707773530996987,
            "unit": "iter/sec",
            "range": "stddev: 0.25795524807214154",
            "extra": "mean: 14.12881318960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.521932110848404,
            "unit": "iter/sec",
            "range": "stddev: 0.001566724969037143",
            "extra": "mean: 24.0836576999925 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}