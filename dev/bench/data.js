window.BENCHMARK_DATA = {
  "lastUpdate": 1733307442222,
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
          "id": "309d897a0d08336f4e3b4a91c03146bdac116905",
          "message": "Merge pull request #379 from UCL-CCS/fix_ndarray_qois\n\nFix ndarray qois in pce_analysis",
          "timestamp": "2024-12-04T11:12:45+01:00",
          "tree_id": "420cf168e9c0418e2a14081fd0dc09c1ba8745a3",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/309d897a0d08336f4e3b4a91c03146bdac116905"
        },
        "date": 1733307422711,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1208599123075221,
            "unit": "iter/sec",
            "range": "stddev: 0.08074983204858449",
            "extra": "mean: 8.2740420782 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19554787300769083,
            "unit": "iter/sec",
            "range": "stddev: 0.0771126486204634",
            "extra": "mean: 5.1138372646000105 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.17483906516978,
            "unit": "iter/sec",
            "range": "stddev: 0.00010873621375007403",
            "extra": "mean: 9.330548183906583 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12096925090689545,
            "unit": "iter/sec",
            "range": "stddev: 0.07116740842808117",
            "extra": "mean: 8.266563548199986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19698513032785747,
            "unit": "iter/sec",
            "range": "stddev: 0.043432518893168515",
            "extra": "mean: 5.076525310999989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.0260785088577,
            "unit": "iter/sec",
            "range": "stddev: 0.00021570176366922012",
            "extra": "mean: 18.509579588236218 msec\nrounds: 51"
          }
        ]
      },
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
          "id": "1159d3bb74830d4ed58b7eb956db51af83c18f3e",
          "message": "Merge pull request #428 from UCL-CCS/feature_enseble_boot_multiple\n\nAdded EnsebleBootMultiple class to enable analysis of many statistics…",
          "timestamp": "2024-12-04T11:13:05+01:00",
          "tree_id": "9958f04d6c0368d60ee400cfb088bd65b4792731",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1159d3bb74830d4ed58b7eb956db51af83c18f3e"
        },
        "date": 1733307440575,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11908927885631315,
            "unit": "iter/sec",
            "range": "stddev: 0.11650681596221217",
            "extra": "mean: 8.397061512199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19936722332986986,
            "unit": "iter/sec",
            "range": "stddev: 0.07435885963563618",
            "extra": "mean: 5.015869626400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.94068984072199,
            "unit": "iter/sec",
            "range": "stddev: 0.0010203870957589654",
            "extra": "mean: 10.005934535710383 msec\nrounds: 84"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11898621980114137,
            "unit": "iter/sec",
            "range": "stddev: 0.07211040779695906",
            "extra": "mean: 8.404334566399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19874932034951956,
            "unit": "iter/sec",
            "range": "stddev: 0.04813556470814143",
            "extra": "mean: 5.031463746600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.4739956612574,
            "unit": "iter/sec",
            "range": "stddev: 0.0010786194279962657",
            "extra": "mean: 19.05705840385088 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}