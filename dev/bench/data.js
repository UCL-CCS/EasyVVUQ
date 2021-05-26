window.BENCHMARK_DATA = {
  "lastUpdate": 1622046525783,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
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
          "id": "c971eab20c0e7f4a35dfe1e21a292b1a16b7fec7",
          "message": "change get_params",
          "timestamp": "2021-05-26T13:59:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/346/commits/c971eab20c0e7f4a35dfe1e21a292b1a16b7fec7"
        },
        "date": 1622046446134,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06482108014000995,
            "unit": "iter/sec",
            "range": "stddev: 1.1933735410333313",
            "extra": "mean: 15.4270801696 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0847974853088379,
            "unit": "iter/sec",
            "range": "stddev: 0.2793530969702726",
            "extra": "mean: 11.792802538399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.75284104613763,
            "unit": "iter/sec",
            "range": "stddev: 0.0019364820660447099",
            "extra": "mean: 11.267244949152174 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06279542563571132,
            "unit": "iter/sec",
            "range": "stddev: 0.5581833516458158",
            "extra": "mean: 15.924726839200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08325381330369933,
            "unit": "iter/sec",
            "range": "stddev: 1.076347109848095",
            "extra": "mean: 12.011461821600017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.97591715996058,
            "unit": "iter/sec",
            "range": "stddev: 0.0014722254705387787",
            "extra": "mean: 18.189782938779388 msec\nrounds: 49"
          }
        ]
      },
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
          "id": "7453a09d6528b1075aa2822becce689f31ca9a90",
          "message": "Merge pull request #346 from UCL-CCS/gp-improvements\n\nchange get_params",
          "timestamp": "2021-05-26T18:20:00+02:00",
          "tree_id": "617f48472f460d255408c73799ca4d1d3313c36b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7453a09d6528b1075aa2822becce689f31ca9a90"
        },
        "date": 1622046524277,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05743883256820653,
            "unit": "iter/sec",
            "range": "stddev: 0.21878770688580165",
            "extra": "mean: 17.409824595799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07157148869197394,
            "unit": "iter/sec",
            "range": "stddev: 0.1537217695006885",
            "extra": "mean: 13.972044151599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.05986353491612,
            "unit": "iter/sec",
            "range": "stddev: 0.0005088031645529118",
            "extra": "mean: 12.976924096769212 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05539166089552866,
            "unit": "iter/sec",
            "range": "stddev: 0.16410612879116046",
            "extra": "mean: 18.053258989400014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07224572728089138,
            "unit": "iter/sec",
            "range": "stddev: 0.29997635638163656",
            "extra": "mean: 13.841649016999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.792931928581496,
            "unit": "iter/sec",
            "range": "stddev: 0.002211959449005053",
            "extra": "mean: 23.368345073175455 msec\nrounds: 41"
          }
        ]
      }
    ]
  }
}