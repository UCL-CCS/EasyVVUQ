window.BENCHMARK_DATA = {
  "lastUpdate": 1719824578795,
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
          "id": "8a7aadd59c5861cdd4aa192ed246fddd744ae041",
          "message": "Merge pull request #419 from UCL-CCS/DavidPCoster-patch-dockerfile\n\nUpdate Dockerfile",
          "timestamp": "2024-06-28T16:23:40+01:00",
          "tree_id": "1317718f13140536d2c7a81b77a5c462cd3b049a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/8a7aadd59c5861cdd4aa192ed246fddd744ae041"
        },
        "date": 1719588476995,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11914717417677866,
            "unit": "iter/sec",
            "range": "stddev: 0.07423269800423238",
            "extra": "mean: 8.392981259599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1989686414548223,
            "unit": "iter/sec",
            "range": "stddev: 0.038393192918015524",
            "extra": "mean: 5.02591761540001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.96995956846581,
            "unit": "iter/sec",
            "range": "stddev: 0.00013199089799989045",
            "extra": "mean: 9.348418977011512 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11940336958911957,
            "unit": "iter/sec",
            "range": "stddev: 0.07986591810483026",
            "extra": "mean: 8.374973030000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20031102461052527,
            "unit": "iter/sec",
            "range": "stddev: 0.009077989178033787",
            "extra": "mean: 4.9922364580000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.13373514196641,
            "unit": "iter/sec",
            "range": "stddev: 0.0002015996922133776",
            "extra": "mean: 18.47276928845732 msec\nrounds: 52"
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
          "id": "4e94fcaef79b12f970325bc7729dd390488f665a",
          "message": "add some more libraries to autodoc_mock_imports",
          "timestamp": "2024-06-28T15:23:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/422/commits/4e94fcaef79b12f970325bc7729dd390488f665a"
        },
        "date": 1719824577572,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11945112066426744,
            "unit": "iter/sec",
            "range": "stddev: 0.07123441988534068",
            "extra": "mean: 8.371625100199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20150081075416804,
            "unit": "iter/sec",
            "range": "stddev: 0.0361186961480456",
            "extra": "mean: 4.962759188200016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.02674795270597,
            "unit": "iter/sec",
            "range": "stddev: 0.00012846381813079298",
            "extra": "mean: 9.52138402352803 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11932531818124556,
            "unit": "iter/sec",
            "range": "stddev: 0.10818041316913686",
            "extra": "mean: 8.380451150199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20106154868788048,
            "unit": "iter/sec",
            "range": "stddev: 0.03667493084308729",
            "extra": "mean: 4.973601399800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.38506888572469,
            "unit": "iter/sec",
            "range": "stddev: 0.0002054994073385754",
            "extra": "mean: 18.73182934615268 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}