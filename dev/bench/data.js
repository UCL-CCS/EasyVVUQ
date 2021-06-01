window.BENCHMARK_DATA = {
  "lastUpdate": 1622551092253,
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
          "id": "8dc8f2d9cdf7db6db6aaa62f4777074eb886dbd0",
          "message": "Update requirements.txt",
          "timestamp": "2021-06-01T14:30:15+02:00",
          "tree_id": "f819020c5a8aad72d56b996064e680ebf9a7e0e0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/8dc8f2d9cdf7db6db6aaa62f4777074eb886dbd0"
        },
        "date": 1622551091126,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06591926981761877,
            "unit": "iter/sec",
            "range": "stddev: 0.07279828885098867",
            "extra": "mean: 15.170070948400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07352807086787892,
            "unit": "iter/sec",
            "range": "stddev: 0.05851842908819949",
            "extra": "mean: 13.600248016799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.65951777924207,
            "unit": "iter/sec",
            "range": "stddev: 0.00016349739250950122",
            "extra": "mean: 13.394139551729525 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06613719792484045,
            "unit": "iter/sec",
            "range": "stddev: 0.1074645499109628",
            "extra": "mean: 15.120084179200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07342567292143813,
            "unit": "iter/sec",
            "range": "stddev: 0.033563737810354696",
            "extra": "mean: 13.619214645399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.618774659536214,
            "unit": "iter/sec",
            "range": "stddev: 0.00020624640951679855",
            "extra": "mean: 25.240558512813585 msec\nrounds: 39"
          }
        ]
      }
    ]
  }
}