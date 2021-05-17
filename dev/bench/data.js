window.BENCHMARK_DATA = {
  "lastUpdate": 1621244595633,
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
          "id": "841a5b955cdc6ed509ddb802ab81277fdd1142f0",
          "message": "monkey patch in test_actions_kubernetes.py",
          "timestamp": "2021-05-14T16:14:48+02:00",
          "tree_id": "518d0309de3a620160d8e8978078576c2b53e0a4",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/841a5b955cdc6ed509ddb802ab81277fdd1142f0"
        },
        "date": 1621002231199,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.052589620750794444,
            "unit": "iter/sec",
            "range": "stddev: 0.4872439131053974",
            "extra": "mean: 19.015158993799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07007319899033547,
            "unit": "iter/sec",
            "range": "stddev: 0.5068005715022643",
            "extra": "mean: 14.270791321199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.61881489302267,
            "unit": "iter/sec",
            "range": "stddev: 0.0008033378333957906",
            "extra": "mean: 13.770535934428773 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.054394537381151443,
            "unit": "iter/sec",
            "range": "stddev: 0.1995219908123897",
            "extra": "mean: 18.384199005000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0726303264341629,
            "unit": "iter/sec",
            "range": "stddev: 0.050458797303908176",
            "extra": "mean: 13.768353373799972 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.881717088546154,
            "unit": "iter/sec",
            "range": "stddev: 0.001003945779401987",
            "extra": "mean: 25.07414607499925 msec\nrounds: 40"
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
          "id": "292ec3724ec0bf741ceac64e1412e3302beb808e",
          "message": "removed jsonpickle",
          "timestamp": "2021-05-14T14:14:54Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/341/commits/292ec3724ec0bf741ceac64e1412e3302beb808e"
        },
        "date": 1621244594493,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06610089013212175,
            "unit": "iter/sec",
            "range": "stddev: 0.09201932251603971",
            "extra": "mean: 15.128389315200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07355957259900266,
            "unit": "iter/sec",
            "range": "stddev: 0.0544718263547976",
            "extra": "mean: 13.594423739400009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.89829700423599,
            "unit": "iter/sec",
            "range": "stddev: 0.00019225905095589352",
            "extra": "mean: 13.532111571430098 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0663140185050899,
            "unit": "iter/sec",
            "range": "stddev: 0.07607609319458071",
            "extra": "mean: 15.079767785800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07332358266222212,
            "unit": "iter/sec",
            "range": "stddev: 0.03493911993741979",
            "extra": "mean: 13.638177018800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.59625824738172,
            "unit": "iter/sec",
            "range": "stddev: 0.00018572457392610083",
            "extra": "mean: 25.909247305542575 msec\nrounds: 36"
          }
        ]
      }
    ]
  }
}