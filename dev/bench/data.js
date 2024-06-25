window.BENCHMARK_DATA = {
  "lastUpdate": 1719319796767,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "j.mccullough@ucl.ac.uk",
            "name": "JonMcCullough",
            "username": "JonMcCullough"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4b259fcc6893ce9f2ff7f3c2cee49773b4f9adcd",
          "message": "Merge pull request #414 from UCL-CCS/code_scanning_alerts\n\nCode scanning alerts",
          "timestamp": "2023-12-05T13:04:15Z",
          "tree_id": "aa7be13df4b5b09fcb7dedb01b35a7649a2148fa",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4b259fcc6893ce9f2ff7f3c2cee49773b4f9adcd"
        },
        "date": 1701781714523,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11888069326279814,
            "unit": "iter/sec",
            "range": "stddev: 0.08622529380442127",
            "extra": "mean: 8.411794821800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19965507215979353,
            "unit": "iter/sec",
            "range": "stddev: 0.05273649314623863",
            "extra": "mean: 5.008638093600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 116.02708436108317,
            "unit": "iter/sec",
            "range": "stddev: 0.0005070681793514711",
            "extra": "mean: 8.618677315788965 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11909249271324045,
            "unit": "iter/sec",
            "range": "stddev: 0.06166583974381248",
            "extra": "mean: 8.396834907200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1989787398270291,
            "unit": "iter/sec",
            "range": "stddev: 0.06761537259616823",
            "extra": "mean: 5.025662545 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.690051365840496,
            "unit": "iter/sec",
            "range": "stddev: 0.00022425717274585707",
            "extra": "mean: 16.75321057894551 msec\nrounds: 57"
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
          "id": "ac39d615ed4d205b71f935cfbeb3972968d35d1c",
          "message": "Add aleatoric uncertainty impact on Sobols",
          "timestamp": "2024-05-15T08:27:18Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/416/commits/ac39d615ed4d205b71f935cfbeb3972968d35d1c"
        },
        "date": 1719242044694,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11786578392012496,
            "unit": "iter/sec",
            "range": "stddev: 0.06940492188324773",
            "extra": "mean: 8.4842264374 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19821487605715568,
            "unit": "iter/sec",
            "range": "stddev: 0.01988022529723284",
            "extra": "mean: 5.045030019399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.59434971451287,
            "unit": "iter/sec",
            "range": "stddev: 0.00013431824602882028",
            "extra": "mean: 9.294168352272823 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1186319647190671,
            "unit": "iter/sec",
            "range": "stddev: 0.060735917303876244",
            "extra": "mean: 8.429431328799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19815889162896264,
            "unit": "iter/sec",
            "range": "stddev: 0.040038398407301855",
            "extra": "mean: 5.04645535599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.48640332462169,
            "unit": "iter/sec",
            "range": "stddev: 0.0002720730662092116",
            "extra": "mean: 18.35320261537823 msec\nrounds: 52"
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
          "id": "80219659afc58c6eb6fe1c41cc43477e84ee8c96",
          "message": "Update conf.py",
          "timestamp": "2024-05-15T08:27:18Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/417/commits/80219659afc58c6eb6fe1c41cc43477e84ee8c96"
        },
        "date": 1719319795857,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1150113651978016,
            "unit": "iter/sec",
            "range": "stddev: 0.06929731418021959",
            "extra": "mean: 8.694792886599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19670629535796075,
            "unit": "iter/sec",
            "range": "stddev: 0.04298080244618933",
            "extra": "mean: 5.083721383599988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.28364692112774,
            "unit": "iter/sec",
            "range": "stddev: 0.00020346798015555617",
            "extra": "mean: 9.408785160920308 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11629385584426716,
            "unit": "iter/sec",
            "range": "stddev: 0.09380635628994889",
            "extra": "mean: 8.598906560800014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19803643955873276,
            "unit": "iter/sec",
            "range": "stddev: 0.01697280914012459",
            "extra": "mean: 5.0495757357999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.61047623677198,
            "unit": "iter/sec",
            "range": "stddev: 0.00027519498860153156",
            "extra": "mean: 18.65307063461767 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}