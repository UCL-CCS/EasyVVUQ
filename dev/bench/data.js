window.BENCHMARK_DATA = {
  "lastUpdate": 1621001400137,
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
          "id": "cb8689b23ba2e49486bb3f084fcbd12f1ee4e253",
          "message": "added a kubrnetes action test",
          "timestamp": "2021-05-14T16:02:31+02:00",
          "tree_id": "fd095e93742e36e640c0f39dfcf1b56d49e397cd",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/cb8689b23ba2e49486bb3f084fcbd12f1ee4e253"
        },
        "date": 1621001397328,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06620671579968257,
            "unit": "iter/sec",
            "range": "stddev: 0.15709076560971033",
            "extra": "mean: 15.104207902800013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08708785561424173,
            "unit": "iter/sec",
            "range": "stddev: 0.1528360115378044",
            "extra": "mean: 11.482657288400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.37668952796409,
            "unit": "iter/sec",
            "range": "stddev: 0.0005477552584223278",
            "extra": "mean: 10.062721999997848 msec\nrounds: 70"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06599299819024858,
            "unit": "iter/sec",
            "range": "stddev: 0.10780386277716197",
            "extra": "mean: 15.153122716400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08594600925143486,
            "unit": "iter/sec",
            "range": "stddev: 0.17449495745280444",
            "extra": "mean: 11.635211555600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.82003731961518,
            "unit": "iter/sec",
            "range": "stddev: 0.0014225133992597973",
            "extra": "mean: 19.297554608697183 msec\nrounds: 46"
          }
        ]
      }
    ]
  }
}