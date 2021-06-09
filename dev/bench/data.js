window.BENCHMARK_DATA = {
  "lastUpdate": 1623242825112,
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
          "id": "de27d87be3408df4e7a45e5b98c92521315cafde",
          "message": "Merge pull request #351 from UCL-CCS/add_progress_bar\n\nAdd progress bar",
          "timestamp": "2021-06-09T14:39:13+02:00",
          "tree_id": "9696950714c6f5aa3db00b025b5e25a68b098c88",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/de27d87be3408df4e7a45e5b98c92521315cafde"
        },
        "date": 1623242823841,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06639101446582836,
            "unit": "iter/sec",
            "range": "stddev: 0.15766352794254987",
            "extra": "mean: 15.062279256400018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0765753538242931,
            "unit": "iter/sec",
            "range": "stddev: 0.16938049673285607",
            "extra": "mean: 13.059032052200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.46875547710101,
            "unit": "iter/sec",
            "range": "stddev: 0.0013227710534126239",
            "extra": "mean: 12.908429906242525 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06535097996936802,
            "unit": "iter/sec",
            "range": "stddev: 0.2918280070697758",
            "extra": "mean: 15.301989357599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07583009525448887,
            "unit": "iter/sec",
            "range": "stddev: 0.04504595940368625",
            "extra": "mean: 13.18737628700003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.05404637353683,
            "unit": "iter/sec",
            "range": "stddev: 0.0011292925568843824",
            "extra": "mean: 26.278414394728077 msec\nrounds: 38"
          }
        ]
      }
    ]
  }
}