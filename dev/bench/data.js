window.BENCHMARK_DATA = {
  "lastUpdate": 1621263714748,
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
          "id": "45e7f387dc0c0daca2788ed74f419ddd05ebf7ad",
          "message": "Jsonpickle test",
          "timestamp": "2021-05-17T09:42:30Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/342/commits/45e7f387dc0c0daca2788ed74f419ddd05ebf7ad"
        },
        "date": 1621263713735,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07496289038910778,
            "unit": "iter/sec",
            "range": "stddev: 0.1635796332891689",
            "extra": "mean: 13.339933863399983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0841022996578142,
            "unit": "iter/sec",
            "range": "stddev: 0.043039157628181494",
            "extra": "mean: 11.890281289200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.03243477539218,
            "unit": "iter/sec",
            "range": "stddev: 0.00045455509892105113",
            "extra": "mean: 11.623523181817815 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07769057820324655,
            "unit": "iter/sec",
            "range": "stddev: 0.10716846599388868",
            "extra": "mean: 12.87157365959997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08361231812795872,
            "unit": "iter/sec",
            "range": "stddev: 0.21148859896999736",
            "extra": "mean: 11.95996023539999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.43321137160156,
            "unit": "iter/sec",
            "range": "stddev: 0.0006207703755879989",
            "extra": "mean: 23.02385590244063 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}