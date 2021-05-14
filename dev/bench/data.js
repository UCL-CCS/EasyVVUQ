window.BENCHMARK_DATA = {
  "lastUpdate": 1620999096233,
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
          "id": "da5719237ebef3cd912681662cd70573e3e08f9c",
          "message": "increase test coverage of action_pool",
          "timestamp": "2021-05-14T15:24:48+02:00",
          "tree_id": "75ccb1ae68c98f98004ce232b618f77e2f6c8fcd",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/da5719237ebef3cd912681662cd70573e3e08f9c"
        },
        "date": 1620999095274,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07672720135745476,
            "unit": "iter/sec",
            "range": "stddev: 0.06502076416400518",
            "extra": "mean: 13.033187478599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09060719895417349,
            "unit": "iter/sec",
            "range": "stddev: 0.030908304683874913",
            "extra": "mean: 11.036650636399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 84.31542491101571,
            "unit": "iter/sec",
            "range": "stddev: 0.0002986257299854768",
            "extra": "mean: 11.860226062495371 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07688921888447875,
            "unit": "iter/sec",
            "range": "stddev: 0.10184372348333486",
            "extra": "mean: 13.005724528199949 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09056475840207781,
            "unit": "iter/sec",
            "range": "stddev: 0.029459167341256132",
            "extra": "mean: 11.041822643199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.56455417107585,
            "unit": "iter/sec",
            "range": "stddev: 0.0002748374303421874",
            "extra": "mean: 23.493726634156456 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}