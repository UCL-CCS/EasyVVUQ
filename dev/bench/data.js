window.BENCHMARK_DATA = {
  "lastUpdate": 1695819531443,
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
          "id": "a3864a662ad85c5bf3e2a4c7fc6dea49ca23a134",
          "message": "Merge pull request #400 from UCL-CCS/goghino-dev\n\nGoghino dev",
          "timestamp": "2023-08-12T09:33:20+02:00",
          "tree_id": "63a6ceedd09418141ee7d22fb62efb6ab982744c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/a3864a662ad85c5bf3e2a4c7fc6dea49ca23a134"
        },
        "date": 1691825937886,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09440782063344193,
            "unit": "iter/sec",
            "range": "stddev: 0.010029744277847107",
            "extra": "mean: 10.592342808999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.12898970283364736,
            "unit": "iter/sec",
            "range": "stddev: 0.06266291542393096",
            "extra": "mean: 7.7525568168000065 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.93703182242469,
            "unit": "iter/sec",
            "range": "stddev: 0.0003002499638489595",
            "extra": "mean: 12.355283823528312 msec\nrounds: 68"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09432309108537376,
            "unit": "iter/sec",
            "range": "stddev: 0.10862906083319758",
            "extra": "mean: 10.601857811200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.12888733604292194,
            "unit": "iter/sec",
            "range": "stddev: 0.05457446784336495",
            "extra": "mean: 7.758714166200013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.13277630432733,
            "unit": "iter/sec",
            "range": "stddev: 0.00044120282012384066",
            "extra": "mean: 23.734490999998332 msec\nrounds: 41"
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
          "id": "66f3efeb34e8ff1fee7e15418843be6ec4e6465a",
          "message": "Issue401: Inconsistent sampled values when mixing continuous and discrete distributions",
          "timestamp": "2023-09-07T03:59:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/402/commits/66f3efeb34e8ff1fee7e15418843be6ec4e6465a"
        },
        "date": 1695819033648,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09871238268380024,
            "unit": "iter/sec",
            "range": "stddev: 0.11154905928447001",
            "extra": "mean: 10.130441316599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1542111839891214,
            "unit": "iter/sec",
            "range": "stddev: 0.06593414971245735",
            "extra": "mean: 6.484613982799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.14387567597565,
            "unit": "iter/sec",
            "range": "stddev: 0.00011609558951358308",
            "extra": "mean: 11.34508770270194 msec\nrounds: 74"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09884860836327058,
            "unit": "iter/sec",
            "range": "stddev: 0.0711218321793032",
            "extra": "mean: 10.116480308199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.15391730221382047,
            "unit": "iter/sec",
            "range": "stddev: 0.05946973847793195",
            "extra": "mean: 6.496995371000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.66743352756686,
            "unit": "iter/sec",
            "range": "stddev: 0.00014567767982446388",
            "extra": "mean: 21.428219304352606 msec\nrounds: 46"
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
          "id": "ad7855cf43e7409fc9d0914ea8eb15674f540ce4",
          "message": "Issue401: Inconsistent sampled values when mixing continuous and discrete distributions",
          "timestamp": "2023-09-07T03:59:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/402/commits/ad7855cf43e7409fc9d0914ea8eb15674f540ce4"
        },
        "date": 1695819529406,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08012550652425851,
            "unit": "iter/sec",
            "range": "stddev: 0.08819298020780766",
            "extra": "mean: 12.4804203228 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11340061586921929,
            "unit": "iter/sec",
            "range": "stddev: 0.052768811206949096",
            "extra": "mean: 8.818294259999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.42169704841332,
            "unit": "iter/sec",
            "range": "stddev: 0.00021771183949600504",
            "extra": "mean: 14.001347508196961 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08007705503281855,
            "unit": "iter/sec",
            "range": "stddev: 0.0980858434012528",
            "extra": "mean: 12.487971736599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1130248951978343,
            "unit": "iter/sec",
            "range": "stddev: 0.04284750017336614",
            "extra": "mean: 8.847608292400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.30480563626055,
            "unit": "iter/sec",
            "range": "stddev: 0.0002532783255960283",
            "extra": "mean: 27.54456283333519 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}