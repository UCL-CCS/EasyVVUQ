window.BENCHMARK_DATA = {
  "lastUpdate": 1622474113158,
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
          "id": "5e56923d7f58ddfd461b99b1d54e10ffee648c18",
          "message": "Pce sc comparison",
          "timestamp": "2021-05-27T12:00:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/347/commits/5e56923d7f58ddfd461b99b1d54e10ffee648c18"
        },
        "date": 1622474112074,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06700668771408703,
            "unit": "iter/sec",
            "range": "stddev: 0.45977753336923183",
            "extra": "mean: 14.9238834826 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07631863931944632,
            "unit": "iter/sec",
            "range": "stddev: 0.06256945324012719",
            "extra": "mean: 13.102958974600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.41999143558506,
            "unit": "iter/sec",
            "range": "stddev: 0.00023611031365750466",
            "extra": "mean: 14.200512945457046 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06805199312314725,
            "unit": "iter/sec",
            "range": "stddev: 0.10622635733303926",
            "extra": "mean: 14.694646756199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07698565397758791,
            "unit": "iter/sec",
            "range": "stddev: 0.0550232301269657",
            "extra": "mean: 12.989433073999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.49815419242687,
            "unit": "iter/sec",
            "range": "stddev: 0.0003154431587813248",
            "extra": "mean: 26.667979305550997 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}