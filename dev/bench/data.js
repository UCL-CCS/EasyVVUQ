window.BENCHMARK_DATA = {
  "lastUpdate": 1750429319259,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "f63677e12ae6029f4577fec4aab38330b70c4182",
          "message": "Fix GitHub Actions workflows, no jobs run, and  Docker Hub failure",
          "timestamp": "2025-06-20T13:42:30+01:00",
          "tree_id": "2c07da9fba7954ffa2e0a4047f3aaf90c78b975a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f63677e12ae6029f4577fec4aab38330b70c4182"
        },
        "date": 1750423617625,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11403607944206584,
            "unit": "iter/sec",
            "range": "stddev: 0.09905930307445804",
            "extra": "mean: 8.769154506999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19454313292366465,
            "unit": "iter/sec",
            "range": "stddev: 0.029276374992779866",
            "extra": "mean: 5.14024825739998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.67118377215328,
            "unit": "iter/sec",
            "range": "stddev: 0.0001624037744285325",
            "extra": "mean: 8.954861641301626 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11431554506960502,
            "unit": "iter/sec",
            "range": "stddev: 0.12653335179005754",
            "extra": "mean: 8.747716676599975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19949376213155307,
            "unit": "iter/sec",
            "range": "stddev: 0.022308542939704506",
            "extra": "mean: 5.0126880626000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.39540256282185,
            "unit": "iter/sec",
            "range": "stddev: 0.00024977512375035164",
            "extra": "mean: 17.73194187036872 msec\nrounds: 54"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "3d7727de7ff106f2bdf27ef4166d5b5e7decc6a2",
          "message": "Add conditional logic for Docker Hub authentication (build for all, push only with secret)",
          "timestamp": "2025-06-20T14:26:10+01:00",
          "tree_id": "db8ce02e3983a105501bbede97b38bac53a89356",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3d7727de7ff106f2bdf27ef4166d5b5e7decc6a2"
        },
        "date": 1750426260821,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11416312098672363,
            "unit": "iter/sec",
            "range": "stddev: 0.09099308537735086",
            "extra": "mean: 8.759396128599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20170751945703008,
            "unit": "iter/sec",
            "range": "stddev: 0.0707002632168006",
            "extra": "mean: 4.957673381200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.72220971067127,
            "unit": "iter/sec",
            "range": "stddev: 0.00031508045633757496",
            "extra": "mean: 9.113925089887639 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1153866020445603,
            "unit": "iter/sec",
            "range": "stddev: 0.11815399604297513",
            "extra": "mean: 8.666517448999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20606748246555626,
            "unit": "iter/sec",
            "range": "stddev: 0.027070329633180495",
            "extra": "mean: 4.852779235399976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.409526706779424,
            "unit": "iter/sec",
            "range": "stddev: 0.00022818791544108223",
            "extra": "mean: 18.72325148077126 msec\nrounds: 52"
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
          "id": "26238b66446daea05350a475e306db4e7e09ce87",
          "message": "Bump urllib3 from 2.3.0 to 2.5.0",
          "timestamp": "2025-06-20T13:26:46Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/453/commits/26238b66446daea05350a475e306db4e7e09ce87"
        },
        "date": 1750429318178,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11377851844490476,
            "unit": "iter/sec",
            "range": "stddev: 0.13657537458409863",
            "extra": "mean: 8.789005285599956 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1932834610683154,
            "unit": "iter/sec",
            "range": "stddev: 0.020239566281131174",
            "extra": "mean: 5.173748413199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.19426570807794,
            "unit": "iter/sec",
            "range": "stddev: 0.0001726475438561635",
            "extra": "mean: 9.597457146074714 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11401131931891383,
            "unit": "iter/sec",
            "range": "stddev: 0.09365596612350635",
            "extra": "mean: 8.771058926200022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20105136856933925,
            "unit": "iter/sec",
            "range": "stddev: 0.03254953990442435",
            "extra": "mean: 4.973853235200022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.20713672198483,
            "unit": "iter/sec",
            "range": "stddev: 0.0001739324637540713",
            "extra": "mean: 18.44775541509886 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}