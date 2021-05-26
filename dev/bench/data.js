window.BENCHMARK_DATA = {
  "lastUpdate": 1622036121341,
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
          "id": "0441d5494f9f9de9b100ae440ea3910c399e1508",
          "message": "Update requirements.txt",
          "timestamp": "2021-05-25T18:32:44+02:00",
          "tree_id": "197ee7c0402e5d94b3b4a47b50305b9184bdd8c7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0441d5494f9f9de9b100ae440ea3910c399e1508"
        },
        "date": 1621960833112,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06893441786384197,
            "unit": "iter/sec",
            "range": "stddev: 0.08336337328934211",
            "extra": "mean: 14.506541593999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0761008972925815,
            "unit": "iter/sec",
            "range": "stddev: 0.06580595244521042",
            "extra": "mean: 13.140449529199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.90209733511108,
            "unit": "iter/sec",
            "range": "stddev: 0.00021579961624478027",
            "extra": "mean: 14.103955137936307 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06928743135037722,
            "unit": "iter/sec",
            "range": "stddev: 0.022073423073399132",
            "extra": "mean: 14.432632015800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07588348903432324,
            "unit": "iter/sec",
            "range": "stddev: 0.05256939182944068",
            "extra": "mean: 13.17809727419999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.71147463079201,
            "unit": "iter/sec",
            "range": "stddev: 0.0003079191054790602",
            "extra": "mean: 25.832133999994323 msec\nrounds: 38"
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
          "id": "152bcfac5b6728a5f6993be153e3060f920d8326",
          "message": "bump up chaospy",
          "timestamp": "2021-05-25T16:32:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/344/commits/152bcfac5b6728a5f6993be153e3060f920d8326"
        },
        "date": 1622035833999,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.071900873113513,
            "unit": "iter/sec",
            "range": "stddev: 0.20330636522350773",
            "extra": "mean: 13.908036949999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.081447507402537,
            "unit": "iter/sec",
            "range": "stddev: 0.11957776523414504",
            "extra": "mean: 12.277846577399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.57913671547216,
            "unit": "iter/sec",
            "range": "stddev: 0.0005954087496360615",
            "extra": "mean: 11.289340098358956 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07495345483509465,
            "unit": "iter/sec",
            "range": "stddev: 0.21360947866633043",
            "extra": "mean: 13.341613167799983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0831442321592301,
            "unit": "iter/sec",
            "range": "stddev: 0.11200861568175936",
            "extra": "mean: 12.027292501600026 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.60427731717219,
            "unit": "iter/sec",
            "range": "stddev: 0.000926501434063585",
            "extra": "mean: 22.9335299545529 msec\nrounds: 44"
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
          "id": "bf28cc10622a7c5c846ea79337923ed6e8f30dad",
          "message": "bump up chaospy",
          "timestamp": "2021-05-25T16:32:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/344/commits/bf28cc10622a7c5c846ea79337923ed6e8f30dad"
        },
        "date": 1622036120091,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06459655755510334,
            "unit": "iter/sec",
            "range": "stddev: 0.13818300883237358",
            "extra": "mean: 15.480701106199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07438718619189517,
            "unit": "iter/sec",
            "range": "stddev: 0.1800316806527835",
            "extra": "mean: 13.443175514400014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.03918433812616,
            "unit": "iter/sec",
            "range": "stddev: 0.0007702510494303076",
            "extra": "mean: 13.88133429310301 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06462231797525679,
            "unit": "iter/sec",
            "range": "stddev: 0.1456924971631946",
            "extra": "mean: 15.474530028200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07317428792345429,
            "unit": "iter/sec",
            "range": "stddev: 0.12409221619552253",
            "extra": "mean: 13.666002476799964 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.1886663778622,
            "unit": "iter/sec",
            "range": "stddev: 0.0011460160564325415",
            "extra": "mean: 26.889912906241875 msec\nrounds: 32"
          }
        ]
      }
    ]
  }
}