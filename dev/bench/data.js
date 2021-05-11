window.BENCHMARK_DATA = {
  "lastUpdate": 1620737304783,
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
          "id": "a4490aa7c4a7c5e5ae9f7ba1ac8920b5313dc19d",
          "message": "added unique constraints to some columns in the database",
          "timestamp": "2021-05-11T14:40:48+02:00",
          "tree_id": "4c470819dbf830e5d4b7f6987674b5c8c70be8d7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/a4490aa7c4a7c5e5ae9f7ba1ac8920b5313dc19d"
        },
        "date": 1620737303498,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07099293112406452,
            "unit": "iter/sec",
            "range": "stddev: 0.07280926507013454",
            "extra": "mean: 14.0859094584 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07974679120523168,
            "unit": "iter/sec",
            "range": "stddev: 0.051658602483876576",
            "extra": "mean: 12.539689495800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.8725395386873,
            "unit": "iter/sec",
            "range": "stddev: 0.0003262731748525116",
            "extra": "mean: 12.678683935484235 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07094249250581923,
            "unit": "iter/sec",
            "range": "stddev: 0.11469111390665919",
            "extra": "mean: 14.095924243399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07960417582295364,
            "unit": "iter/sec",
            "range": "stddev: 0.09369063515375727",
            "extra": "mean: 12.56215505859999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.8800699187287,
            "unit": "iter/sec",
            "range": "stddev: 0.0005822230817435209",
            "extra": "mean: 23.877706076913725 msec\nrounds: 39"
          }
        ]
      }
    ]
  }
}