window.BENCHMARK_DATA = {
  "lastUpdate": 1733308495815,
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
      },
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
          "id": "ba0200413632f9368218ef790972146f0703ae14",
          "message": "Merge pull request #377 from UCL-CCS/qcgpj-parallel-template-patch-1\n\nadded reference to QCG-PJ parallel tasks template",
          "timestamp": "2024-12-04T10:30:42Z",
          "tree_id": "90fbbaf1b8ad68f9ad9192a7115be74fc6776644",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ba0200413632f9368218ef790972146f0703ae14"
        },
        "date": 1733308494838,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12010847632399144,
            "unit": "iter/sec",
            "range": "stddev: 0.08958386531975066",
            "extra": "mean: 8.325807058799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2010373999137255,
            "unit": "iter/sec",
            "range": "stddev: 0.054140479729594244",
            "extra": "mean: 4.974198832799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.96685447286463,
            "unit": "iter/sec",
            "range": "stddev: 0.00009642550879306053",
            "extra": "mean: 9.348690348314209 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12030427710690482,
            "unit": "iter/sec",
            "range": "stddev: 0.07805367465586704",
            "extra": "mean: 8.312256422200017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2012931760279322,
            "unit": "iter/sec",
            "range": "stddev: 0.021110985491262734",
            "extra": "mean: 4.967878294399986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.61111432837531,
            "unit": "iter/sec",
            "range": "stddev: 0.0007801043226753423",
            "extra": "mean: 18.31129088461781 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}