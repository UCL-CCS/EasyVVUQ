window.BENCHMARK_DATA = {
  "lastUpdate": 1622117385162,
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
          "id": "69c9b2379d2f1f8e2f301e1f4dce531dea04254d",
          "message": "added add_collation_callback to action_statuses",
          "timestamp": "2021-05-27T14:00:37+02:00",
          "tree_id": "7c5ec1421facabe417d9eddd11e0218a877cdf41",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/69c9b2379d2f1f8e2f301e1f4dce531dea04254d"
        },
        "date": 1622117383648,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05174746937125652,
            "unit": "iter/sec",
            "range": "stddev: 0.5801332694149912",
            "extra": "mean: 19.324616491399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07835194725137574,
            "unit": "iter/sec",
            "range": "stddev: 0.14466339545778828",
            "extra": "mean: 12.762924663400009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.10358834401113,
            "unit": "iter/sec",
            "range": "stddev: 0.0021535110703544955",
            "extra": "mean: 13.494623166663663 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05181525670678513,
            "unit": "iter/sec",
            "range": "stddev: 0.3191741960545512",
            "extra": "mean: 19.299335052200014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07701786613098685,
            "unit": "iter/sec",
            "range": "stddev: 0.26990937266908427",
            "extra": "mean: 12.984000339599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.316066596713384,
            "unit": "iter/sec",
            "range": "stddev: 0.001853494820603443",
            "extra": "mean: 22.067228581408397 msec\nrounds: 43"
          }
        ]
      }
    ]
  }
}