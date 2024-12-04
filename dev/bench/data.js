window.BENCHMARK_DATA = {
  "lastUpdate": 1733306171840,
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
          "id": "d607845fdeef9b98b8026dfb63b8e686f5be1ea1",
          "message": "Merge pull request #425 from UCL-CCS/djgroen-actions-update\n\nDjgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-12-04T09:37:20Z",
          "tree_id": "f63059454c5a98dda94f0aa51387479748c5e3d2",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d607845fdeef9b98b8026dfb63b8e686f5be1ea1"
        },
        "date": 1733305303321,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11684369586868891,
            "unit": "iter/sec",
            "range": "stddev: 0.13076636578456075",
            "extra": "mean: 8.558442050000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18943382157089414,
            "unit": "iter/sec",
            "range": "stddev: 0.051366426982805434",
            "extra": "mean: 5.278888382799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 95.50079377589628,
            "unit": "iter/sec",
            "range": "stddev: 0.0009087193431055693",
            "extra": "mean: 10.47111715476016 msec\nrounds: 84"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1175468871447201,
            "unit": "iter/sec",
            "range": "stddev: 0.10901622541567087",
            "extra": "mean: 8.507243571399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.18962339525198268,
            "unit": "iter/sec",
            "range": "stddev: 0.028785128111414163",
            "extra": "mean: 5.273610878400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.10928032992714,
            "unit": "iter/sec",
            "range": "stddev: 0.00023271241355299425",
            "extra": "mean: 19.565918235292543 msec\nrounds: 51"
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
          "id": "ca59500b0d0d7a7a38487bb0bc508b2dbcd70a6e",
          "message": "Full Integration Tests",
          "timestamp": "2024-12-04T09:37:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/ca59500b0d0d7a7a38487bb0bc508b2dbcd70a6e"
        },
        "date": 1733305575793,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11949859035060488,
            "unit": "iter/sec",
            "range": "stddev: 0.10562039058513142",
            "extra": "mean: 8.368299551200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20153255597447478,
            "unit": "iter/sec",
            "range": "stddev: 0.025632895843363784",
            "extra": "mean: 4.961977459000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.60710560735964,
            "unit": "iter/sec",
            "range": "stddev: 0.00013999934652351848",
            "extra": "mean: 9.469059816087897 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1200749304529892,
            "unit": "iter/sec",
            "range": "stddev: 0.12419969368207495",
            "extra": "mean: 8.32813307680001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20154252201720332,
            "unit": "iter/sec",
            "range": "stddev: 0.03999431080975945",
            "extra": "mean: 4.961732094999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.12068434614045,
            "unit": "iter/sec",
            "range": "stddev: 0.00018960787183577488",
            "extra": "mean: 18.14200987999925 msec\nrounds: 50"
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
          "id": "c418e0b050050ad6c9c35514f48a784b86b04107",
          "message": "added reference to QCG-PJ parallel tasks template",
          "timestamp": "2024-12-04T09:37:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/377/commits/c418e0b050050ad6c9c35514f48a784b86b04107"
        },
        "date": 1733305700540,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11875541981596159,
            "unit": "iter/sec",
            "range": "stddev: 0.08700192678588303",
            "extra": "mean: 8.420668307599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19659387446849935,
            "unit": "iter/sec",
            "range": "stddev: 0.04790189834160834",
            "extra": "mean: 5.086628475599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.32520096056126,
            "unit": "iter/sec",
            "range": "stddev: 0.00013852083539043933",
            "extra": "mean: 9.31747614772666 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11930255650734688,
            "unit": "iter/sec",
            "range": "stddev: 0.07433227598762197",
            "extra": "mean: 8.382050052199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1979987107968135,
            "unit": "iter/sec",
            "range": "stddev: 0.019821976486464957",
            "extra": "mean: 5.050537935199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.4533039287385,
            "unit": "iter/sec",
            "range": "stddev: 0.000502609748509614",
            "extra": "mean: 18.033190615388257 msec\nrounds: 52"
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
          "id": "8b234957810ba0924bf6d6af83410d11039f80de",
          "message": "Fix ndarray qois in pce_analysis",
          "timestamp": "2024-12-04T09:37:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/379/commits/8b234957810ba0924bf6d6af83410d11039f80de"
        },
        "date": 1733305744386,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11830650741586753,
            "unit": "iter/sec",
            "range": "stddev: 0.07623259108947034",
            "extra": "mean: 8.45262041659999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1962100266443116,
            "unit": "iter/sec",
            "range": "stddev: 0.04846522379138875",
            "extra": "mean: 5.096579502600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.13656533969947,
            "unit": "iter/sec",
            "range": "stddev: 0.00011113833028562497",
            "extra": "mean: 9.421823636363317 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11827955694531318,
            "unit": "iter/sec",
            "range": "stddev: 0.08413727733352806",
            "extra": "mean: 8.454546379999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19678680635967657,
            "unit": "iter/sec",
            "range": "stddev: 0.019807780610263396",
            "extra": "mean: 5.081641490599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.31681445047742,
            "unit": "iter/sec",
            "range": "stddev: 0.0007292342341011027",
            "extra": "mean: 18.410505294115428 msec\nrounds: 51"
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
          "id": "aa44cc52b7d53d5ff5d4bc8a9dcad6ce3ba77067",
          "message": "Added EnsebleBootMultiple class to enable analysis of many statistics…",
          "timestamp": "2024-12-04T09:37:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/428/commits/aa44cc52b7d53d5ff5d4bc8a9dcad6ce3ba77067"
        },
        "date": 1733306170654,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11991515678406921,
            "unit": "iter/sec",
            "range": "stddev: 0.08798176154413793",
            "extra": "mean: 8.339229392000016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19765368168589786,
            "unit": "iter/sec",
            "range": "stddev: 0.04830728861105164",
            "extra": "mean: 5.059354278000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.15655477781887,
            "unit": "iter/sec",
            "range": "stddev: 0.00010232818739761083",
            "extra": "mean: 9.332140269658963 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1203965826233883,
            "unit": "iter/sec",
            "range": "stddev: 0.08163002147094967",
            "extra": "mean: 8.305883590800022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1972908117510032,
            "unit": "iter/sec",
            "range": "stddev: 0.03827720221012087",
            "extra": "mean: 5.068659767400016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.055587895404265,
            "unit": "iter/sec",
            "range": "stddev: 0.00013544700372797896",
            "extra": "mean: 18.499475057693687 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}