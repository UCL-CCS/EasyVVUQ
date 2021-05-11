window.BENCHMARK_DATA = {
  "lastUpdate": 1620733513422,
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
          "id": "3e37184c229ee6e6f83751ef1ab6cfa25696f76f",
          "message": "added docstrings to simple_csv decoder",
          "timestamp": "2021-05-11T13:37:21+02:00",
          "tree_id": "8db82f938446e88d5988a7dceb529d853bcdc2f8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3e37184c229ee6e6f83751ef1ab6cfa25696f76f"
        },
        "date": 1620733512526,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06258285457157016,
            "unit": "iter/sec",
            "range": "stddev: 0.35566597799731364",
            "extra": "mean: 15.97881731099999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08026981750944504,
            "unit": "iter/sec",
            "range": "stddev: 0.08970312225342494",
            "extra": "mean: 12.457982726599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.90017213840825,
            "unit": "iter/sec",
            "range": "stddev: 0.0010540090905830466",
            "extra": "mean: 11.12344922388383 msec\nrounds: 67"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06288689577640834,
            "unit": "iter/sec",
            "range": "stddev: 0.17870639290976292",
            "extra": "mean: 15.901564032600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08102947148656987,
            "unit": "iter/sec",
            "range": "stddev: 0.1349659585141488",
            "extra": "mean: 12.341188726199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 48.80621306084664,
            "unit": "iter/sec",
            "range": "stddev: 0.0017230248988516575",
            "extra": "mean: 20.489194659567243 msec\nrounds: 47"
          }
        ]
      }
    ]
  }
}