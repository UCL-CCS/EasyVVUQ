window.BENCHMARK_DATA = {
  "lastUpdate": 1620724828748,
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
          "id": "38e0a1406b0cd2db1ced34cb5c2f36816067f46e",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-05-11T11:11:44+02:00",
          "tree_id": "6c1677c361d443410c880554899d6e433b7411e5",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/38e0a1406b0cd2db1ced34cb5c2f36816067f46e"
        },
        "date": 1620724827333,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05645805295512876,
            "unit": "iter/sec",
            "range": "stddev: 0.340604278894253",
            "extra": "mean: 17.71226508279999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07174086790222087,
            "unit": "iter/sec",
            "range": "stddev: 0.24685520446398027",
            "extra": "mean: 13.939056346000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.59635640099341,
            "unit": "iter/sec",
            "range": "stddev: 0.0018469314962772597",
            "extra": "mean: 12.25544919047176 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05639192799251916,
            "unit": "iter/sec",
            "range": "stddev: 0.3961965407656874",
            "extra": "mean: 17.73303441820003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07842831744434531,
            "unit": "iter/sec",
            "range": "stddev: 0.09978497474800353",
            "extra": "mean: 12.750496664799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.093643753538295,
            "unit": "iter/sec",
            "range": "stddev: 0.0015608933505516197",
            "extra": "mean: 26.251098647057514 msec\nrounds: 34"
          }
        ]
      }
    ]
  }
}