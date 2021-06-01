window.BENCHMARK_DATA = {
  "lastUpdate": 1622550222606,
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
      },
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
          "id": "fae0f922a3c9b09f800db0f9943e0118faf31293",
          "message": "typo",
          "timestamp": "2021-06-01T14:15:54+02:00",
          "tree_id": "01250d4d7195446c88c11aabaf1ef5ca22c1af07",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/fae0f922a3c9b09f800db0f9943e0118faf31293"
        },
        "date": 1622550221592,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06802367179503223,
            "unit": "iter/sec",
            "range": "stddev: 0.5030018617074759",
            "extra": "mean: 14.700764801599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0758613554020984,
            "unit": "iter/sec",
            "range": "stddev: 0.2794435609312085",
            "extra": "mean: 13.181942171999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.00908844951284,
            "unit": "iter/sec",
            "range": "stddev: 0.00019552513260916754",
            "extra": "mean: 13.69692487931169 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06683688225874006,
            "unit": "iter/sec",
            "range": "stddev: 0.30448667787317096",
            "extra": "mean: 14.961799027799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07776895267990262,
            "unit": "iter/sec",
            "range": "stddev: 0.08155970023974045",
            "extra": "mean: 12.858601865399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.270227696747284,
            "unit": "iter/sec",
            "range": "stddev: 0.00036210991891147843",
            "extra": "mean: 24.230542349995687 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}