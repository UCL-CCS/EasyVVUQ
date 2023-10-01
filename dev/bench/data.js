window.BENCHMARK_DATA = {
  "lastUpdate": 1696157715486,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "wouteredeling@gmail.com",
            "name": "Wouter Edeling",
            "username": "wedeling"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "f1d1c0f7b3c12b1c794ea3531e0b5d6829cf6c64",
          "message": "Merge pull request #402 from UCL-CCS/issue401\n\nIssue401: Inconsistent sampled values when mixing continuous and discrete distributions",
          "timestamp": "2023-09-29T10:26:47+02:00",
          "tree_id": "6e2868a0a1bae4873ba5aa4e016a66184d74a8cc",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f1d1c0f7b3c12b1c794ea3531e0b5d6829cf6c64"
        },
        "date": 1695976343546,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09444178299997076,
            "unit": "iter/sec",
            "range": "stddev: 0.07259364232978918",
            "extra": "mean: 10.588533679 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.13284388720851395,
            "unit": "iter/sec",
            "range": "stddev: 0.049213969408641964",
            "extra": "mean: 7.527632780199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 85.98097541573064,
            "unit": "iter/sec",
            "range": "stddev: 0.00019232363827929982",
            "extra": "mean: 11.630479826087726 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09431986722252589,
            "unit": "iter/sec",
            "range": "stddev: 0.08648639666684792",
            "extra": "mean: 10.6022201838 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.13228644127501413,
            "unit": "iter/sec",
            "range": "stddev: 0.04641308269869199",
            "extra": "mean: 7.559353705199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 44.1727114103137,
            "unit": "iter/sec",
            "range": "stddev: 0.00027733797978961766",
            "extra": "mean: 22.638411093019617 msec\nrounds: 43"
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
          "id": "62434d7bc7db7d206aeeb4c93ba107445c99cff9",
          "message": "Feature/decrease needed memory (Issue 404)",
          "timestamp": "2023-09-07T03:59:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/405/commits/62434d7bc7db7d206aeeb4c93ba107445c99cff9"
        },
        "date": 1696157714161,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09465230221071806,
            "unit": "iter/sec",
            "range": "stddev: 0.05420033796538261",
            "extra": "mean: 10.5649833828 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1352891253640535,
            "unit": "iter/sec",
            "range": "stddev: 0.05143533679171752",
            "extra": "mean: 7.391577093199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 87.01873845559219,
            "unit": "iter/sec",
            "range": "stddev: 0.00021129703647053682",
            "extra": "mean: 11.491777722223873 msec\nrounds: 72"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09453296006197197,
            "unit": "iter/sec",
            "range": "stddev: 0.08854146667184078",
            "extra": "mean: 10.578321035800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.13447945608988046,
            "unit": "iter/sec",
            "range": "stddev: 0.04340866346888071",
            "extra": "mean: 7.43608004580002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.80990584355007,
            "unit": "iter/sec",
            "range": "stddev: 0.00041779687550666956",
            "extra": "mean: 22.82588790697493 msec\nrounds: 43"
          }
        ]
      }
    ]
  }
}