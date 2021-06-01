window.BENCHMARK_DATA = {
  "lastUpdate": 1622550083475,
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
          "id": "1c005a3762faae75aa5888373ffd087f27c6a9e0",
          "message": "added a dialcet option to csv decoder",
          "timestamp": "2021-06-01T14:13:31+02:00",
          "tree_id": "fd555575ba962ce5b9c2da8187911ea038643da6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1c005a3762faae75aa5888373ffd087f27c6a9e0"
        },
        "date": 1622550081873,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0671424819308707,
            "unit": "iter/sec",
            "range": "stddev: 0.05058554039860839",
            "extra": "mean: 14.893700251199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07719388268188285,
            "unit": "iter/sec",
            "range": "stddev: 0.03485062986888893",
            "extra": "mean: 12.954394380199982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 76.44989404166884,
            "unit": "iter/sec",
            "range": "stddev: 0.00021100653708857004",
            "extra": "mean: 13.080462864408318 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06746697967998881,
            "unit": "iter/sec",
            "range": "stddev: 0.10573046043237962",
            "extra": "mean: 14.82206561999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07715516069099762,
            "unit": "iter/sec",
            "range": "stddev: 0.03715113597293062",
            "extra": "mean: 12.960895824 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.417437083765435,
            "unit": "iter/sec",
            "range": "stddev: 0.00017669001094009387",
            "extra": "mean: 25.36948299999602 msec\nrounds: 38"
          }
        ]
      }
    ]
  }
}