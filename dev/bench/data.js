window.BENCHMARK_DATA = {
  "lastUpdate": 1621263697463,
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
          "id": "14b04726f625a630f3d9b40338a6e744aa04e6e5",
          "message": "Merge pull request #342 from UCL-CCS/jsonpickle-test\n\nJsonpickle test",
          "timestamp": "2021-05-17T16:54:51+02:00",
          "tree_id": "3917a54979c95b671c8979b84975ac7dcd18613f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/14b04726f625a630f3d9b40338a6e744aa04e6e5"
        },
        "date": 1621263696470,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07690320591434888,
            "unit": "iter/sec",
            "range": "stddev: 0.09515746194536297",
            "extra": "mean: 13.003359068199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09036461356746457,
            "unit": "iter/sec",
            "range": "stddev: 0.04301302475089446",
            "extra": "mean: 11.0662787182 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.1128627764845,
            "unit": "iter/sec",
            "range": "stddev: 0.00023710561286166126",
            "extra": "mean: 12.9680051290347 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07722579002383496,
            "unit": "iter/sec",
            "range": "stddev: 0.11317012230056667",
            "extra": "mean: 12.949042019399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09016552530114096,
            "unit": "iter/sec",
            "range": "stddev: 0.03608000156773816",
            "extra": "mean: 11.090713403600011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.316096190518365,
            "unit": "iter/sec",
            "range": "stddev: 0.00026012110016736695",
            "extra": "mean: 24.203641975000778 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}