window.BENCHMARK_DATA = {
  "lastUpdate": 1621350867858,
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
          "id": "c4902f195b9a0303de6d0643f2c6c04f01426fc3",
          "message": "Update docker.yml",
          "timestamp": "2021-05-18T17:07:37+02:00",
          "tree_id": "d291b37c0512c4cebdd07dec1c91049e23d5f93f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c4902f195b9a0303de6d0643f2c6c04f01426fc3"
        },
        "date": 1621350866806,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0771881389509049,
            "unit": "iter/sec",
            "range": "stddev: 0.06844193342806135",
            "extra": "mean: 12.955358343800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08824612743130862,
            "unit": "iter/sec",
            "range": "stddev: 0.03243101956304233",
            "extra": "mean: 11.331942025199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 79.51142238604686,
            "unit": "iter/sec",
            "range": "stddev: 0.00009751739073667397",
            "extra": "mean: 12.576809343753936 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0774504092456707,
            "unit": "iter/sec",
            "range": "stddev: 0.10896747791224179",
            "extra": "mean: 12.911487618199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08846245765935305,
            "unit": "iter/sec",
            "range": "stddev: 0.03298524681584852",
            "extra": "mean: 11.304230364599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.79402878247491,
            "unit": "iter/sec",
            "range": "stddev: 0.00004434945091145293",
            "extra": "mean: 23.36774611904551 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}