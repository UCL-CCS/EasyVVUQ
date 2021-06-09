window.BENCHMARK_DATA = {
  "lastUpdate": 1623241277169,
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
          "id": "108ac2e03cfef7a9a2f2592940de1a90caf260a9",
          "message": "Merge pull request #350 from UCL-CCS/dataframe-sampling\n\nadded dataframe_sampler",
          "timestamp": "2021-06-09T10:35:38+02:00",
          "tree_id": "7eeb0798077bc667571762c59abbda54e4036e5a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/108ac2e03cfef7a9a2f2592940de1a90caf260a9"
        },
        "date": 1623228145509,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07533434131457449,
            "unit": "iter/sec",
            "range": "stddev: 0.05759948189169888",
            "extra": "mean: 13.274158671200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09008746404862901,
            "unit": "iter/sec",
            "range": "stddev: 0.0889886076777143",
            "extra": "mean: 11.100323564000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.88105752037755,
            "unit": "iter/sec",
            "range": "stddev: 0.00023221173806533307",
            "extra": "mean: 11.125814800001471 msec\nrounds: 70"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07557316547074928,
            "unit": "iter/sec",
            "range": "stddev: 0.08765987165863696",
            "extra": "mean: 13.232210054600023 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09046030769435304,
            "unit": "iter/sec",
            "range": "stddev: 0.03519970027536819",
            "extra": "mean: 11.054572170799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 47.13261331374291,
            "unit": "iter/sec",
            "range": "stddev: 0.000250809832141325",
            "extra": "mean: 21.21673146666833 msec\nrounds: 45"
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
          "id": "b21b3d44eedb40a4815bea22ec238fe541384ec2",
          "message": "added dataframe_sampler",
          "timestamp": "2021-06-01T14:08:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/350/commits/b21b3d44eedb40a4815bea22ec238fe541384ec2"
        },
        "date": 1623228293524,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05013006862604087,
            "unit": "iter/sec",
            "range": "stddev: 0.18197485921739165",
            "extra": "mean: 19.94810754120001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06979257418590655,
            "unit": "iter/sec",
            "range": "stddev: 0.05801861402862658",
            "extra": "mean: 14.328171895999981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.6707278581968,
            "unit": "iter/sec",
            "range": "stddev: 0.0008123005532885981",
            "extra": "mean: 13.392128732145839 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05083455811847052,
            "unit": "iter/sec",
            "range": "stddev: 0.20158097131592284",
            "extra": "mean: 19.671657176000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07091466178655109,
            "unit": "iter/sec",
            "range": "stddev: 0.14338935716236756",
            "extra": "mean: 14.10145624060001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.58431960141366,
            "unit": "iter/sec",
            "range": "stddev: 0.0019518018795689949",
            "extra": "mean: 25.262528447357408 msec\nrounds: 38"
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
          "id": "f5a48b668b4f779f4def35c5d3db07ac1954aef2",
          "message": "Integration with QCG-PJ",
          "timestamp": "2021-06-09T08:35:42Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/343/commits/f5a48b668b4f779f4def35c5d3db07ac1954aef2"
        },
        "date": 1623235304399,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05182646693815455,
            "unit": "iter/sec",
            "range": "stddev: 0.26199370958215185",
            "extra": "mean: 19.295160543999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07271740011485296,
            "unit": "iter/sec",
            "range": "stddev: 0.15514444082463302",
            "extra": "mean: 13.751866794199975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.380805473511,
            "unit": "iter/sec",
            "range": "stddev: 0.0012074370190130954",
            "extra": "mean: 13.444328730160455 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0533365942439533,
            "unit": "iter/sec",
            "range": "stddev: 0.19799622385318782",
            "extra": "mean: 18.748853656200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07172352288740183,
            "unit": "iter/sec",
            "range": "stddev: 0.10894584206974517",
            "extra": "mean: 13.94242725040001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.49470599986789,
            "unit": "iter/sec",
            "range": "stddev: 0.0011042383595745706",
            "extra": "mean: 26.670431820522165 msec\nrounds: 39"
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
          "id": "0a522145bac691a26d6372ec3fd9786b577cf511",
          "message": "Integration with QCG-PJ",
          "timestamp": "2021-06-09T08:35:42Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/343/commits/0a522145bac691a26d6372ec3fd9786b577cf511"
        },
        "date": 1623241276091,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07327156809293998,
            "unit": "iter/sec",
            "range": "stddev: 0.15294919964614212",
            "extra": "mean: 13.647858589999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08319665597002207,
            "unit": "iter/sec",
            "range": "stddev: 0.06788035849895863",
            "extra": "mean: 12.019713873599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.52483912660587,
            "unit": "iter/sec",
            "range": "stddev: 0.0005330715667951546",
            "extra": "mean: 11.972486393948188 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07302018143389051,
            "unit": "iter/sec",
            "range": "stddev: 0.24369600692446178",
            "extra": "mean: 13.694844087800016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08207602552399731,
            "unit": "iter/sec",
            "range": "stddev: 0.11282961326420575",
            "extra": "mean: 12.183825832399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.71777234128852,
            "unit": "iter/sec",
            "range": "stddev: 0.0008100639279649213",
            "extra": "mean: 23.409460400009152 msec\nrounds: 40"
          }
        ]
      }
    ]
  }
}