window.BENCHMARK_DATA = {
  "lastUpdate": 1701684409667,
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
          "id": "f9e561874b11483ad0890996265a1890bac1a5c3",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/f9e561874b11483ad0890996265a1890bac1a5c3"
        },
        "date": 1701441450311,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11673977646189945,
            "unit": "iter/sec",
            "range": "stddev: 0.07970103273051564",
            "extra": "mean: 8.566060603400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1974252683572071,
            "unit": "iter/sec",
            "range": "stddev: 0.07092656554810695",
            "extra": "mean: 5.065207753399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 116.79206939705996,
            "unit": "iter/sec",
            "range": "stddev: 0.0001927975770049591",
            "extra": "mean: 8.562225202126381 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11681278014742537,
            "unit": "iter/sec",
            "range": "stddev: 0.07179245268052324",
            "extra": "mean: 8.560707131000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19531505762016124,
            "unit": "iter/sec",
            "range": "stddev: 0.07047690163051835",
            "extra": "mean: 5.119932954400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.638873541487946,
            "unit": "iter/sec",
            "range": "stddev: 0.0002025968761379229",
            "extra": "mean: 17.05353359648841 msec\nrounds: 57"
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
          "id": "986f0b761f6502370ee7eb37df0eb195bdb1dc55",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/986f0b761f6502370ee7eb37df0eb195bdb1dc55"
        },
        "date": 1701442976114,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11957080291781724,
            "unit": "iter/sec",
            "range": "stddev: 0.044155103462068565",
            "extra": "mean: 8.363245672 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2021870439423306,
            "unit": "iter/sec",
            "range": "stddev: 0.036390260472989044",
            "extra": "mean: 4.945915329199965 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.31379818311726,
            "unit": "iter/sec",
            "range": "stddev: 0.00027857244902030107",
            "extra": "mean: 8.903625522214043 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11926666155733054,
            "unit": "iter/sec",
            "range": "stddev: 0.12767005045360358",
            "extra": "mean: 8.384572746000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19868660221189843,
            "unit": "iter/sec",
            "range": "stddev: 0.049336744128313514",
            "extra": "mean: 5.033051996799986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.37521752353659,
            "unit": "iter/sec",
            "range": "stddev: 0.0004566307104150552",
            "extra": "mean: 17.429127821428786 msec\nrounds: 56"
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
          "id": "885e882cd28b69301885a8d5f950a0ba942daa5f",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/885e882cd28b69301885a8d5f950a0ba942daa5f"
        },
        "date": 1701445408598,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11651722774556851,
            "unit": "iter/sec",
            "range": "stddev: 0.024151458939052843",
            "extra": "mean: 8.582421838799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1943794810648982,
            "unit": "iter/sec",
            "range": "stddev: 0.04249723518404596",
            "extra": "mean: 5.144575932199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.05812351200964,
            "unit": "iter/sec",
            "range": "stddev: 0.00018886365371698245",
            "extra": "mean: 8.767459688171233 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11791135910477625,
            "unit": "iter/sec",
            "range": "stddev: 0.08474931748555922",
            "extra": "mean: 8.480947107999986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19499888502231044,
            "unit": "iter/sec",
            "range": "stddev: 0.06734883130989876",
            "extra": "mean: 5.1282344505999955 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.555030057512475,
            "unit": "iter/sec",
            "range": "stddev: 0.0002177112287876755",
            "extra": "mean: 17.07795212499771 msec\nrounds: 56"
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
          "id": "52ebc5deb8ce3132aa7207233fc29af9c8a8bc58",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/52ebc5deb8ce3132aa7207233fc29af9c8a8bc58"
        },
        "date": 1701682857356,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11647301483246836,
            "unit": "iter/sec",
            "range": "stddev: 0.08898336134949054",
            "extra": "mean: 8.58567970819999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20010446288598893,
            "unit": "iter/sec",
            "range": "stddev: 0.08195599053294719",
            "extra": "mean: 4.997389791199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.92370023040917,
            "unit": "iter/sec",
            "range": "stddev: 0.00017996805019525062",
            "extra": "mean: 8.48005954736933 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1163970936512361,
            "unit": "iter/sec",
            "range": "stddev: 0.06299712321679009",
            "extra": "mean: 8.591279804600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1968940394815821,
            "unit": "iter/sec",
            "range": "stddev: 0.05273769492837287",
            "extra": "mean: 5.07887390919999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 60.440128013380736,
            "unit": "iter/sec",
            "range": "stddev: 0.00015161711250236086",
            "extra": "mean: 16.545299172407635 msec\nrounds: 58"
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
          "id": "da44ce8bb4cc9080d9c8c03690b4b505f5a4be1c",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/da44ce8bb4cc9080d9c8c03690b4b505f5a4be1c"
        },
        "date": 1701684408549,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11754901473616935,
            "unit": "iter/sec",
            "range": "stddev: 0.06179266840181878",
            "extra": "mean: 8.507089593600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19790429903536844,
            "unit": "iter/sec",
            "range": "stddev: 0.05601348083330352",
            "extra": "mean: 5.052947333000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.14410135430713,
            "unit": "iter/sec",
            "range": "stddev: 0.000284541245698",
            "extra": "mean: 8.760855691490937 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11743242712884121,
            "unit": "iter/sec",
            "range": "stddev: 0.052464749217893285",
            "extra": "mean: 8.515535482400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19718937841336165,
            "unit": "iter/sec",
            "range": "stddev: 0.06287172935635114",
            "extra": "mean: 5.0712670634000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.83958151794863,
            "unit": "iter/sec",
            "range": "stddev: 0.0002455012773851344",
            "extra": "mean: 16.99536220690075 msec\nrounds: 58"
          }
        ]
      }
    ]
  }
}