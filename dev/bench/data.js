window.BENCHMARK_DATA = {
  "lastUpdate": 1622532326589,
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
          "id": "0a0928ff2cae70d086283eaa1ca14353006b4191",
          "message": "Update requirements.txt",
          "timestamp": "2021-06-01T09:16:20+02:00",
          "tree_id": "09eef4d7fab8166658838393b2b9946a04119425",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0a0928ff2cae70d086283eaa1ca14353006b4191"
        },
        "date": 1622532193975,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07516846267447519,
            "unit": "iter/sec",
            "range": "stddev: 0.07480448265242592",
            "extra": "mean: 13.303451532999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08878994087997001,
            "unit": "iter/sec",
            "range": "stddev: 0.03613894400519578",
            "extra": "mean: 11.26253706320001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.59755258255781,
            "unit": "iter/sec",
            "range": "stddev: 0.00021928924988108867",
            "extra": "mean: 11.547670461548547 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07523379504206318,
            "unit": "iter/sec",
            "range": "stddev: 0.11867926716643867",
            "extra": "mean: 13.291898932399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08870200251049176,
            "unit": "iter/sec",
            "range": "stddev: 0.07608308332529773",
            "extra": "mean: 11.273702641399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.10272168053543,
            "unit": "iter/sec",
            "range": "stddev: 0.0003867275945978243",
            "extra": "mean: 21.69069338095499 msec\nrounds: 42"
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
          "id": "2e74b10d07c7501ed97b1631e0eecced857e2e48",
          "message": "Merge pull request #347 from UCL-CCS/pce_sc_comparison\n\nPce sc comparison",
          "timestamp": "2021-06-01T09:17:42+02:00",
          "tree_id": "6129edcf09ea5daef1ac12929dc3e368437f4a42",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/2e74b10d07c7501ed97b1631e0eecced857e2e48"
        },
        "date": 1622532325526,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06709552416746781,
            "unit": "iter/sec",
            "range": "stddev: 0.06855540643564119",
            "extra": "mean: 14.9041238206 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07567178002437619,
            "unit": "iter/sec",
            "range": "stddev: 0.025354885003509065",
            "extra": "mean: 13.214965997600023 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.64091193496667,
            "unit": "iter/sec",
            "range": "stddev: 0.00022436017319823806",
            "extra": "mean: 13.397478327586386 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06740259675812878,
            "unit": "iter/sec",
            "range": "stddev: 0.09237074787956358",
            "extra": "mean: 14.836223648600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07574911210154436,
            "unit": "iter/sec",
            "range": "stddev: 0.04230616864132512",
            "extra": "mean: 13.201474872200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.83823161864976,
            "unit": "iter/sec",
            "range": "stddev: 0.00039150635803181076",
            "extra": "mean: 25.10151578946749 msec\nrounds: 38"
          }
        ]
      }
    ]
  }
}