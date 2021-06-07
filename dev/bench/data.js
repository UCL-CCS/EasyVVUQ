window.BENCHMARK_DATA = {
  "lastUpdate": 1623063024815,
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "c654d49e85ec15c8c58f473d0c91aba8963a7740",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-06-01T16:07:52+02:00",
          "tree_id": "4dbee7488d6c23a7469c6142aca69aec4826b460",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c654d49e85ec15c8c58f473d0c91aba8963a7740"
        },
        "date": 1622556887809,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0746663425693428,
            "unit": "iter/sec",
            "range": "stddev: 0.060799722190267094",
            "extra": "mean: 13.392915275999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09262693379501451,
            "unit": "iter/sec",
            "range": "stddev: 0.040334659722831685",
            "extra": "mean: 10.795995927199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.84341729426164,
            "unit": "iter/sec",
            "range": "stddev: 0.00024960617032071904",
            "extra": "mean: 12.218453640621796 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.074968240988911,
            "unit": "iter/sec",
            "range": "stddev: 0.09985502607076258",
            "extra": "mean: 13.338981771600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0920830739475458,
            "unit": "iter/sec",
            "range": "stddev: 0.03673796748506574",
            "extra": "mean: 10.859759097199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.32523248754653,
            "unit": "iter/sec",
            "range": "stddev: 0.00022027005004452983",
            "extra": "mean: 23.626568390244113 msec\nrounds: 41"
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
          "id": "862b53246fffbbe856db123f8276a6e70acaac8e",
          "message": "Integration with QCG-PJ",
          "timestamp": "2021-06-01T14:08:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/343/commits/862b53246fffbbe856db123f8276a6e70acaac8e"
        },
        "date": 1623063023351,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0570122712945347,
            "unit": "iter/sec",
            "range": "stddev: 0.3518333710821891",
            "extra": "mean: 17.540083516999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0784683712427505,
            "unit": "iter/sec",
            "range": "stddev: 0.10770568485613402",
            "extra": "mean: 12.743988235800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 90.31226084055265,
            "unit": "iter/sec",
            "range": "stddev: 0.0006526339153015746",
            "extra": "mean: 11.072693681819256 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05745449122978222,
            "unit": "iter/sec",
            "range": "stddev: 0.24448270333817393",
            "extra": "mean: 17.405079717799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07646246279120437,
            "unit": "iter/sec",
            "range": "stddev: 0.28407807302789234",
            "extra": "mean: 13.078312723600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.00497642528637,
            "unit": "iter/sec",
            "range": "stddev: 0.0021286307248336057",
            "extra": "mean: 22.219764999991042 msec\nrounds: 44"
          }
        ]
      }
    ]
  }
}