window.BENCHMARK_DATA = {
  "lastUpdate": 1701440301840,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "DavidPCoster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "0d27a6381b1019596a3118a000083c39ec8ae49b",
          "message": "Merge pull request #405 from UCL-CCS/feature/decrease_needed_memory\n\nFeature/decrease needed memory (Issue 404)",
          "timestamp": "2023-10-03T13:20:17+02:00",
          "tree_id": "3c4cd6d17200ddfe6ff3a4a5611930f322193562",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0d27a6381b1019596a3118a000083c39ec8ae49b"
        },
        "date": 1696332415328,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08094409373872408,
            "unit": "iter/sec",
            "range": "stddev: 0.14249084540885787",
            "extra": "mean: 12.3542058946 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11467444459059077,
            "unit": "iter/sec",
            "range": "stddev: 0.08056124292395488",
            "extra": "mean: 8.720338725599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 67.86138045529297,
            "unit": "iter/sec",
            "range": "stddev: 0.00017029841610480265",
            "extra": "mean: 14.735921864407095 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0806325109493175,
            "unit": "iter/sec",
            "range": "stddev: 0.10499664710661842",
            "extra": "mean: 12.401945421599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.11402539885852998,
            "unit": "iter/sec",
            "range": "stddev: 0.07213734277034899",
            "extra": "mean: 8.769975900199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.959268038103694,
            "unit": "iter/sec",
            "range": "stddev: 0.00019887361353020265",
            "extra": "mean: 27.80924236111717 msec\nrounds: 36"
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
          "id": "0adb5cc0d7116b42cc2c2395af03159d12955c42",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-12T06:40:30Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/0adb5cc0d7116b42cc2c2395af03159d12955c42"
        },
        "date": 1700462289523,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11566742933441297,
            "unit": "iter/sec",
            "range": "stddev: 0.09119968357151895",
            "extra": "mean: 8.6454761358 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1938938861371292,
            "unit": "iter/sec",
            "range": "stddev: 0.020502999968659567",
            "extra": "mean: 5.157460196 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.32761596866118,
            "unit": "iter/sec",
            "range": "stddev: 0.00019032001055490114",
            "extra": "mean: 9.146819777782866 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11521708818031179,
            "unit": "iter/sec",
            "range": "stddev: 0.08544869173787797",
            "extra": "mean: 8.67926811719999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19620713789201139,
            "unit": "iter/sec",
            "range": "stddev: 0.03833837107204184",
            "extra": "mean: 5.096654539399992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.28410298842105,
            "unit": "iter/sec",
            "range": "stddev: 0.0003037703098992686",
            "extra": "mean: 18.088382481478348 msec\nrounds: 54"
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
          "id": "73ab8ceeed9bccfd488881e428430cfd0b930a17",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/73ab8ceeed9bccfd488881e428430cfd0b930a17"
        },
        "date": 1701440300671,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11687238123327832,
            "unit": "iter/sec",
            "range": "stddev: 0.030348779553169548",
            "extra": "mean: 8.556341450800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19928522325927972,
            "unit": "iter/sec",
            "range": "stddev: 0.03443834021888824",
            "extra": "mean: 5.017933510800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.28107934565405,
            "unit": "iter/sec",
            "range": "stddev: 0.0004789871797987319",
            "extra": "mean: 8.827599505374632 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11659220500169871,
            "unit": "iter/sec",
            "range": "stddev: 0.11234190416240648",
            "extra": "mean: 8.576902718199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2006308273315086,
            "unit": "iter/sec",
            "range": "stddev: 0.040359867606519814",
            "extra": "mean: 4.984278903199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.449501300947595,
            "unit": "iter/sec",
            "range": "stddev: 0.00017825504692537566",
            "extra": "mean: 17.108785836360724 msec\nrounds: 55"
          }
        ]
      }
    ]
  }
}