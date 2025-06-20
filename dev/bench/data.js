window.BENCHMARK_DATA = {
  "lastUpdate": 1750423618219,
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
      }
    ]
  }
}