window.BENCHMARK_DATA = {
  "lastUpdate": 1733307672487,
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
          "id": "bb55d476774693dfe7d90f8aef3a2ef95e0a98c8",
          "message": "Merge pull request #426 from UCL-CCS/feature_support_for_modules_in_qcgpj\n\nadded suppport for modules in QCG-PJ templates",
          "timestamp": "2024-12-04T11:15:19+01:00",
          "tree_id": "0ef12ff1c10d6ced0b4505a7975d191a534cc59b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bb55d476774693dfe7d90f8aef3a2ef95e0a98c8"
        },
        "date": 1733307671235,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1185117911473581,
            "unit": "iter/sec",
            "range": "stddev: 0.10031261246215466",
            "extra": "mean: 8.437978958199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19801263069202757,
            "unit": "iter/sec",
            "range": "stddev: 0.010338961047539261",
            "extra": "mean: 5.0501828924000165 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 101.94299576869949,
            "unit": "iter/sec",
            "range": "stddev: 0.0004033555610315059",
            "extra": "mean: 9.809403701151966 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11905535800022041,
            "unit": "iter/sec",
            "range": "stddev: 0.13660181221814752",
            "extra": "mean: 8.399453975000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19681531405208488,
            "unit": "iter/sec",
            "range": "stddev: 0.05850944466264784",
            "extra": "mean: 5.080905440800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.181687524093626,
            "unit": "iter/sec",
            "range": "stddev: 0.00020390513374698207",
            "extra": "mean: 18.803464999995654 msec\nrounds: 51"
          }
        ]
      }
    ]
  }
}