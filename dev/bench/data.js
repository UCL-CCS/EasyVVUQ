window.BENCHMARK_DATA = {
  "lastUpdate": 1621959379317,
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
          "id": "763a61df568e02c68efcf14e23ee17d91a259aa1",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-25T18:09:18+02:00",
          "tree_id": "f947f9b6bc63036e10b7ea279cb2817dbd00abd2",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/763a61df568e02c68efcf14e23ee17d91a259aa1"
        },
        "date": 1621959377887,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0768438565744786,
            "unit": "iter/sec",
            "range": "stddev: 0.09451901349193902",
            "extra": "mean: 13.0134020412 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08484488995918471,
            "unit": "iter/sec",
            "range": "stddev: 0.13877270292360255",
            "extra": "mean: 11.78621364799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.01094862628688,
            "unit": "iter/sec",
            "range": "stddev: 0.0005668384715673504",
            "extra": "mean: 11.626426820903328 msec\nrounds: 67"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07780259800089635,
            "unit": "iter/sec",
            "range": "stddev: 0.0739720015095283",
            "extra": "mean: 12.853041231200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08509642449831036,
            "unit": "iter/sec",
            "range": "stddev: 0.047789721067469405",
            "extra": "mean: 11.751375053599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 44.60797218695678,
            "unit": "iter/sec",
            "range": "stddev: 0.0012634219056220232",
            "extra": "mean: 22.417517564100272 msec\nrounds: 39"
          }
        ]
      }
    ]
  }
}