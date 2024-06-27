window.BENCHMARK_DATA = {
  "lastUpdate": 1719481334447,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "David Coster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "5d4a4cacd9b14713949646cebcc370509be99ff6",
          "message": "Merge pull request #417 from UCL-CCS/module-index-fix\n\nUpdate conf.py",
          "timestamp": "2024-06-26T08:31:45+02:00",
          "tree_id": "5e6950cd820254ad240073d63a4b517502df470c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5d4a4cacd9b14713949646cebcc370509be99ff6"
        },
        "date": 1719383761105,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11734007271203396,
            "unit": "iter/sec",
            "range": "stddev: 0.08692521383708937",
            "extra": "mean: 8.522237773400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19983194456390538,
            "unit": "iter/sec",
            "range": "stddev: 0.029586010681161692",
            "extra": "mean: 5.004204919200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.56612648674745,
            "unit": "iter/sec",
            "range": "stddev: 0.0001802620773612944",
            "extra": "mean: 9.749807604650156 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11722904327483696,
            "unit": "iter/sec",
            "range": "stddev: 0.08052922479788575",
            "extra": "mean: 8.530309316399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19989115285476186,
            "unit": "iter/sec",
            "range": "stddev: 0.04005421175062335",
            "extra": "mean: 5.002722660400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.83422195276727,
            "unit": "iter/sec",
            "range": "stddev: 0.0003255057244326405",
            "extra": "mean: 18.575544769224557 msec\nrounds: 52"
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
          "id": "0afba86f7bb4ef883a9c766ec5520ddd5415c110",
          "message": "improve the documentation, adding in a reference to Diana's paper",
          "timestamp": "2024-06-26T06:31:49Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/418/commits/0afba86f7bb4ef883a9c766ec5520ddd5415c110"
        },
        "date": 1719481333453,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11721739879850668,
            "unit": "iter/sec",
            "range": "stddev: 0.06748131290103562",
            "extra": "mean: 8.531156724599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.195129613245536,
            "unit": "iter/sec",
            "range": "stddev: 0.04837446427309187",
            "extra": "mean: 5.124798759999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.6225859957878,
            "unit": "iter/sec",
            "range": "stddev: 0.0001009618422619531",
            "extra": "mean: 9.467672000000832 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.117128960649328,
            "unit": "iter/sec",
            "range": "stddev: 0.07199143068765618",
            "extra": "mean: 8.537598169199986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19542662676827074,
            "unit": "iter/sec",
            "range": "stddev: 0.013676581074261871",
            "extra": "mean: 5.117009982399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.603242258258824,
            "unit": "iter/sec",
            "range": "stddev: 0.00013681939020147854",
            "extra": "mean: 18.65558794339398 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}