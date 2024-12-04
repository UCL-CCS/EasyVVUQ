window.BENCHMARK_DATA = {
  "lastUpdate": 1733308416369,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
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
          "id": "8a776fcc28566501f1081dbfe45b3328806d80e6",
          "message": "Full Integration Tests",
          "timestamp": "2024-12-04T10:15:24Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/8a776fcc28566501f1081dbfe45b3328806d80e6"
        },
        "date": 1733308415153,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11863780902038795,
            "unit": "iter/sec",
            "range": "stddev: 0.09200858349120634",
            "extra": "mean: 8.429016080599984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19445226258995318,
            "unit": "iter/sec",
            "range": "stddev: 0.019712327890004776",
            "extra": "mean: 5.14265036920001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.84138227978053,
            "unit": "iter/sec",
            "range": "stddev: 0.00015570996639803608",
            "extra": "mean: 9.448100340910187 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11814342758758212,
            "unit": "iter/sec",
            "range": "stddev: 0.11236647246874473",
            "extra": "mean: 8.464288030399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19213670656402687,
            "unit": "iter/sec",
            "range": "stddev: 0.03879662577736774",
            "extra": "mean: 5.204627569000013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.561016474344065,
            "unit": "iter/sec",
            "range": "stddev: 0.0006640995629873741",
            "extra": "mean: 19.025507249999954 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}