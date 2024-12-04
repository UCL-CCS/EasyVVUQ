window.BENCHMARK_DATA = {
  "lastUpdate": 1733309053655,
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
          "id": "20bad93776a9be31d972ebfcafde02f3e19466ae",
          "message": "Merge pull request #429 from PlasmaFAIR/pyproject\n\nSwitch packaging to `pyproject.toml`",
          "timestamp": "2024-12-04T10:36:01Z",
          "tree_id": "fcedf45fa56e718dae43fcd9f16255234dd90847",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/20bad93776a9be31d972ebfcafde02f3e19466ae"
        },
        "date": 1733308822671,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11671069263555665,
            "unit": "iter/sec",
            "range": "stddev: 0.08032845519344628",
            "extra": "mean: 8.568195230600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18972670039978848,
            "unit": "iter/sec",
            "range": "stddev: 0.05675433473272348",
            "extra": "mean: 5.270739426199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 100.73447997368952,
            "unit": "iter/sec",
            "range": "stddev: 0.0001850657464780936",
            "extra": "mean: 9.927087530120636 msec\nrounds: 83"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11800671208097739,
            "unit": "iter/sec",
            "range": "stddev: 0.047108186019940476",
            "extra": "mean: 8.474094247400012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19506960111574842,
            "unit": "iter/sec",
            "range": "stddev: 0.035559606173689536",
            "extra": "mean: 5.1263753772000085 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.259275845956566,
            "unit": "iter/sec",
            "range": "stddev: 0.0004979004624800529",
            "extra": "mean: 18.776072038462004 msec\nrounds: 52"
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
          "id": "1acc205634a3c640a73753bdc5aae7d92aff82ba",
          "message": "Hackathon2024",
          "timestamp": "2024-12-04T10:36:41Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/432/commits/1acc205634a3c640a73753bdc5aae7d92aff82ba"
        },
        "date": 1733308916125,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1178779429860812,
            "unit": "iter/sec",
            "range": "stddev: 0.11683880305170143",
            "extra": "mean: 8.483351292599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19204370061644693,
            "unit": "iter/sec",
            "range": "stddev: 0.060820170767618933",
            "extra": "mean: 5.207148148000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 101.8577207888783,
            "unit": "iter/sec",
            "range": "stddev: 0.00015137177772812954",
            "extra": "mean: 9.817616104651622 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11832926411694716,
            "unit": "iter/sec",
            "range": "stddev: 0.05236766499751529",
            "extra": "mean: 8.450994835999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19383177924979503,
            "unit": "iter/sec",
            "range": "stddev: 0.07492397352010552",
            "extra": "mean: 5.159112731000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.377777337948785,
            "unit": "iter/sec",
            "range": "stddev: 0.001365708322359823",
            "extra": "mean: 19.092066346150187 msec\nrounds: 52"
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
          "id": "41d1a7f67eb571ca2621d50c4e90f56c449fd68b",
          "message": "Code scanning alerts",
          "timestamp": "2024-12-04T10:36:41Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/433/commits/41d1a7f67eb571ca2621d50c4e90f56c449fd68b"
        },
        "date": 1733309052483,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11931506105534062,
            "unit": "iter/sec",
            "range": "stddev: 0.0839961491493196",
            "extra": "mean: 8.381171590200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1970448881997622,
            "unit": "iter/sec",
            "range": "stddev: 0.055046716989705015",
            "extra": "mean: 5.074985751400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.85765390238056,
            "unit": "iter/sec",
            "range": "stddev: 0.00019479365794273715",
            "extra": "mean: 9.72217391764616 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12008784952754159,
            "unit": "iter/sec",
            "range": "stddev: 0.10617670899524617",
            "extra": "mean: 8.327237134599988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19832970117898238,
            "unit": "iter/sec",
            "range": "stddev: 0.024085827318121478",
            "extra": "mean: 5.042109144800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.84051666117036,
            "unit": "iter/sec",
            "range": "stddev: 0.00025247701666113924",
            "extra": "mean: 18.924871730765 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}