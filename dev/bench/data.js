window.BENCHMARK_DATA = {
  "lastUpdate": 1621960834344,
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
          "id": "0441d5494f9f9de9b100ae440ea3910c399e1508",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-25T18:32:44+02:00",
          "tree_id": "197ee7c0402e5d94b3b4a47b50305b9184bdd8c7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0441d5494f9f9de9b100ae440ea3910c399e1508"
        },
        "date": 1621960833112,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06893441786384197,
            "unit": "iter/sec",
            "range": "stddev: 0.08336337328934211",
            "extra": "mean: 14.506541593999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0761008972925815,
            "unit": "iter/sec",
            "range": "stddev: 0.06580595244521042",
            "extra": "mean: 13.140449529199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.90209733511108,
            "unit": "iter/sec",
            "range": "stddev: 0.00021579961624478027",
            "extra": "mean: 14.103955137936307 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06928743135037722,
            "unit": "iter/sec",
            "range": "stddev: 0.022073423073399132",
            "extra": "mean: 14.432632015800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07588348903432324,
            "unit": "iter/sec",
            "range": "stddev: 0.05256939182944068",
            "extra": "mean: 13.17809727419999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.71147463079201,
            "unit": "iter/sec",
            "range": "stddev: 0.0003079191054790602",
            "extra": "mean: 25.832133999994323 msec\nrounds: 38"
          }
        ]
      }
    ]
  }
}