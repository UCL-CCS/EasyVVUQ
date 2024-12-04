window.BENCHMARK_DATA = {
  "lastUpdate": 1733307712017,
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
          "id": "f816a25eefb8410e1b54d0694de0ca3a6aa88cee",
          "message": "added reference to QCG-PJ parallel tasks template",
          "timestamp": "2024-12-04T10:15:24Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/377/commits/f816a25eefb8410e1b54d0694de0ca3a6aa88cee"
        },
        "date": 1733307710150,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11824761714470189,
            "unit": "iter/sec",
            "range": "stddev: 0.108004028588617",
            "extra": "mean: 8.456830032999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1941897019023127,
            "unit": "iter/sec",
            "range": "stddev: 0.0530072439773998",
            "extra": "mean: 5.1496036618000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.95325284934617,
            "unit": "iter/sec",
            "range": "stddev: 0.0005383659261845304",
            "extra": "mean: 9.438124579543487 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11856035635561875,
            "unit": "iter/sec",
            "range": "stddev: 0.08477257764281242",
            "extra": "mean: 8.434522556599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19325390056909014,
            "unit": "iter/sec",
            "range": "stddev: 0.04874722187525585",
            "extra": "mean: 5.1745398000000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.392748400422114,
            "unit": "iter/sec",
            "range": "stddev: 0.0006578999355015374",
            "extra": "mean: 18.729135134614914 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}