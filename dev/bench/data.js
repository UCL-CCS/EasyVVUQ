window.BENCHMARK_DATA = {
  "lastUpdate": 1733406416069,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "71005d5cec9a61469927b01379d8d667e9858922",
          "message": "Merge pull request #435 from mzrghorbani/dev\n\nFix issue #391 with database dump.",
          "timestamp": "2024-12-04T14:20:17Z",
          "tree_id": "5cd1ef52b1bc41fdc276c7f50f0ebbb293b2320f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/71005d5cec9a61469927b01379d8d667e9858922"
        },
        "date": 1733322277154,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11872301855001743,
            "unit": "iter/sec",
            "range": "stddev: 0.1018809475498958",
            "extra": "mean: 8.422966432400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19798332376057998,
            "unit": "iter/sec",
            "range": "stddev: 0.0670745914185555",
            "extra": "mean: 5.050930457199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.74604213651365,
            "unit": "iter/sec",
            "range": "stddev: 0.00018863224744407127",
            "extra": "mean: 9.456618704547282 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11927917601874193,
            "unit": "iter/sec",
            "range": "stddev: 0.05144954760354987",
            "extra": "mean: 8.383693058400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1984479614105786,
            "unit": "iter/sec",
            "range": "stddev: 0.024122999600444953",
            "extra": "mean: 5.039104422599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.168326530886205,
            "unit": "iter/sec",
            "range": "stddev: 0.00015537045496653954",
            "extra": "mean: 18.460972750003837 msec\nrounds: 52"
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
          "id": "dbdf9e8e45f63df0068ed89583d7cec8257e2819",
          "message": "Hackathon2024",
          "timestamp": "2024-12-04T14:20:22Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/432/commits/dbdf9e8e45f63df0068ed89583d7cec8257e2819"
        },
        "date": 1733336727664,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1200090355590133,
            "unit": "iter/sec",
            "range": "stddev: 0.06348891268448274",
            "extra": "mean: 8.33270591119999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19695050219881868,
            "unit": "iter/sec",
            "range": "stddev: 0.0635063187410515",
            "extra": "mean: 5.077417873200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.5415993759928,
            "unit": "iter/sec",
            "range": "stddev: 0.0001282202066183518",
            "extra": "mean: 9.474936952940157 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12023125083722849,
            "unit": "iter/sec",
            "range": "stddev: 0.07277750699999255",
            "extra": "mean: 8.317305135200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19702265351555523,
            "unit": "iter/sec",
            "range": "stddev: 0.04824573380325992",
            "extra": "mean: 5.075558480999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.31201847062492,
            "unit": "iter/sec",
            "range": "stddev: 0.0013369384632465617",
            "extra": "mean: 18.412131019230262 msec\nrounds: 52"
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
          "id": "31b690697ce3e8321fc8189286589f8fb9626b5f",
          "message": "Hackathon2024",
          "timestamp": "2024-12-04T14:20:22Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/432/commits/31b690697ce3e8321fc8189286589f8fb9626b5f"
        },
        "date": 1733399292979,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12052532547970167,
            "unit": "iter/sec",
            "range": "stddev: 0.11613044238071586",
            "extra": "mean: 8.297011404199987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1956666285853097,
            "unit": "iter/sec",
            "range": "stddev: 0.055239602109586915",
            "extra": "mean: 5.1107335330000065 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.58579628480766,
            "unit": "iter/sec",
            "range": "stddev: 0.0003546583294611497",
            "extra": "mean: 9.294907269661687 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12000609719394247,
            "unit": "iter/sec",
            "range": "stddev: 0.06399329856941936",
            "extra": "mean: 8.332909938599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19640472684817586,
            "unit": "iter/sec",
            "range": "stddev: 0.024378001733823797",
            "extra": "mean: 5.091527154399989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.11610880942931,
            "unit": "iter/sec",
            "range": "stddev: 0.0006194195166921895",
            "extra": "mean: 18.143515962957803 msec\nrounds: 54"
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
          "id": "6f5fc21f0b397cce6cbd2dff550f4ed881bee503",
          "message": "Hackathon2024",
          "timestamp": "2024-12-04T14:20:22Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/432/commits/6f5fc21f0b397cce6cbd2dff550f4ed881bee503"
        },
        "date": 1733406414312,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12044213756980524,
            "unit": "iter/sec",
            "range": "stddev: 0.0688747979366586",
            "extra": "mean: 8.302742048400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19582927357936403,
            "unit": "iter/sec",
            "range": "stddev: 0.07993397565103444",
            "extra": "mean: 5.106488839600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 100.33145959295925,
            "unit": "iter/sec",
            "range": "stddev: 0.0001735934217322291",
            "extra": "mean: 9.966963543209282 msec\nrounds: 81"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11921511685164803,
            "unit": "iter/sec",
            "range": "stddev: 0.08293453739464038",
            "extra": "mean: 8.388197960200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19650483450288117,
            "unit": "iter/sec",
            "range": "stddev: 0.09014289010843253",
            "extra": "mean: 5.088933320799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 50.61518981972847,
            "unit": "iter/sec",
            "range": "stddev: 0.0006553298850670672",
            "extra": "mean: 19.75691494117891 msec\nrounds: 51"
          }
        ]
      }
    ]
  }
}