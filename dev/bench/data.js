window.BENCHMARK_DATA = {
  "lastUpdate": 1621347899893,
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
          "id": "191a5c73037d75075428c0ec08d8af540faf05d4",
          "message": "Update docker.yml",
          "timestamp": "2021-05-18T16:18:11+02:00",
          "tree_id": "2d2810885be4cde04016023f4c5ae26deb691f60",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/191a5c73037d75075428c0ec08d8af540faf05d4"
        },
        "date": 1621347898626,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07675298036166196,
            "unit": "iter/sec",
            "range": "stddev: 0.09977303667202299",
            "extra": "mean: 13.028810025199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08924927830131621,
            "unit": "iter/sec",
            "range": "stddev: 0.047087698489167995",
            "extra": "mean: 11.204572395800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.33641628537393,
            "unit": "iter/sec",
            "range": "stddev: 0.00030287961644872094",
            "extra": "mean: 11.320359621217422 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07684032305505707,
            "unit": "iter/sec",
            "range": "stddev: 0.1037536275470941",
            "extra": "mean: 13.014000465400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08883486265872442,
            "unit": "iter/sec",
            "range": "stddev: 0.05109042870984623",
            "extra": "mean: 11.256841853199967 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.35087065624691,
            "unit": "iter/sec",
            "range": "stddev: 0.0002498011915989844",
            "extra": "mean: 23.067587452384856 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}