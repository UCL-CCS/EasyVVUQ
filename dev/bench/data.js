window.BENCHMARK_DATA = {
  "lastUpdate": 1701772609513,
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
          "id": "09601789efbd768e34aaef5c817ad3de412108d2",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/09601789efbd768e34aaef5c817ad3de412108d2"
        },
        "date": 1701685418294,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11754912785960489,
            "unit": "iter/sec",
            "range": "stddev: 0.04720093090455282",
            "extra": "mean: 8.507081406799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1899542891274695,
            "unit": "iter/sec",
            "range": "stddev: 0.04359563461894944",
            "extra": "mean: 5.2644244286000115 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 118.22022539175151,
            "unit": "iter/sec",
            "range": "stddev: 0.00013414529173878147",
            "extra": "mean: 8.458789489584007 msec\nrounds: 96"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11765368764268365,
            "unit": "iter/sec",
            "range": "stddev: 0.0894390685782061",
            "extra": "mean: 8.499521094800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19004207566142833,
            "unit": "iter/sec",
            "range": "stddev: 0.019966442602751527",
            "extra": "mean: 5.261992621999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 60.81272811910511,
            "unit": "iter/sec",
            "range": "stddev: 0.0002370724915467558",
            "extra": "mean: 16.443925982755523 msec\nrounds: 58"
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
          "id": "63d76b2abb9aa86bcfcc2bd2edc87fcf4332467b",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/63d76b2abb9aa86bcfcc2bd2edc87fcf4332467b"
        },
        "date": 1701687289952,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11725938424861665,
            "unit": "iter/sec",
            "range": "stddev: 0.023291771900813347",
            "extra": "mean: 8.528102091 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1985909726225535,
            "unit": "iter/sec",
            "range": "stddev: 0.04674833230985998",
            "extra": "mean: 5.035475614999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 115.4724773720844,
            "unit": "iter/sec",
            "range": "stddev: 0.00035389323765110554",
            "extra": "mean: 8.660072276597324 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11711470956829774,
            "unit": "iter/sec",
            "range": "stddev: 0.08563709949652229",
            "extra": "mean: 8.538637065199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1980082015069927,
            "unit": "iter/sec",
            "range": "stddev: 0.022498384649719736",
            "extra": "mean: 5.050295858400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.64928463448744,
            "unit": "iter/sec",
            "range": "stddev: 0.00021112839114292682",
            "extra": "mean: 16.76466039999799 msec\nrounds: 55"
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
          "id": "46695a9aa57cfe6c674eb90aa186f20ded11eeaa",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/46695a9aa57cfe6c674eb90aa186f20ded11eeaa"
        },
        "date": 1701689285872,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1173377320616963,
            "unit": "iter/sec",
            "range": "stddev: 0.07755380735956177",
            "extra": "mean: 8.522407774800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1941558571098977,
            "unit": "iter/sec",
            "range": "stddev: 0.03838634776507938",
            "extra": "mean: 5.150501328600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.87950491667786,
            "unit": "iter/sec",
            "range": "stddev: 0.00024922259499640626",
            "extra": "mean: 9.100878282608797 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11753432802117048,
            "unit": "iter/sec",
            "range": "stddev: 0.10986280167402851",
            "extra": "mean: 8.5081526124 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1941100487707715,
            "unit": "iter/sec",
            "range": "stddev: 0.033461273011055864",
            "extra": "mean: 5.151716803600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.64523108434141,
            "unit": "iter/sec",
            "range": "stddev: 0.00019289784953890435",
            "extra": "mean: 17.051684877186975 msec\nrounds: 57"
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
          "id": "cab3168def7e93a8f01a2ec70022ea0e3405c9af",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/cab3168def7e93a8f01a2ec70022ea0e3405c9af"
        },
        "date": 1701689416633,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11652655089680602,
            "unit": "iter/sec",
            "range": "stddev: 0.08349163990522487",
            "extra": "mean: 8.581735169400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19235939768516502,
            "unit": "iter/sec",
            "range": "stddev: 0.05678927048813772",
            "extra": "mean: 5.198602262399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.51770471526848,
            "unit": "iter/sec",
            "range": "stddev: 0.000413569146021732",
            "extra": "mean: 9.048323999999305 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11742647023452088,
            "unit": "iter/sec",
            "range": "stddev: 0.12406382094180245",
            "extra": "mean: 8.5159674646 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19586470075406134,
            "unit": "iter/sec",
            "range": "stddev: 0.00910612123995972",
            "extra": "mean: 5.105565199599982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.52691299199331,
            "unit": "iter/sec",
            "range": "stddev: 0.00019209689337833677",
            "extra": "mean: 16.799124122806525 msec\nrounds: 57"
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
          "id": "4d1d5d511d2d8ab306f7c9d1820033310f7cfc97",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/4d1d5d511d2d8ab306f7c9d1820033310f7cfc97"
        },
        "date": 1701690452771,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11592852649365275,
            "unit": "iter/sec",
            "range": "stddev: 0.06744671005269219",
            "extra": "mean: 8.6260045758 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19926884377072204,
            "unit": "iter/sec",
            "range": "stddev: 0.04569464513333801",
            "extra": "mean: 5.018345974600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.363792680213,
            "unit": "iter/sec",
            "range": "stddev: 0.00013583193709607012",
            "extra": "mean: 8.520515374999427 msec\nrounds: 96"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11615392049835957,
            "unit": "iter/sec",
            "range": "stddev: 0.07099770449519024",
            "extra": "mean: 8.609266012799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19934461537782025,
            "unit": "iter/sec",
            "range": "stddev: 0.066555794764146",
            "extra": "mean: 5.0164384832 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.663131558925855,
            "unit": "iter/sec",
            "range": "stddev: 0.0005335307470848609",
            "extra": "mean: 17.046481724139145 msec\nrounds: 58"
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
          "id": "5c6c117371a4c3bdb19444a21f70f245141ff2dc",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/5c6c117371a4c3bdb19444a21f70f245141ff2dc"
        },
        "date": 1701690511440,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11792271621910601,
            "unit": "iter/sec",
            "range": "stddev: 0.08123004923968688",
            "extra": "mean: 8.480130309599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1998153455558692,
            "unit": "iter/sec",
            "range": "stddev: 0.06088631279027199",
            "extra": "mean: 5.004620627200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.15714883314367,
            "unit": "iter/sec",
            "range": "stddev: 0.00015257801014146804",
            "extra": "mean: 8.535544010414675 msec\nrounds: 96"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11791442660911239,
            "unit": "iter/sec",
            "range": "stddev: 0.09470843336118871",
            "extra": "mean: 8.480726478999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1995035977894077,
            "unit": "iter/sec",
            "range": "stddev: 0.09574234952221027",
            "extra": "mean: 5.012440933800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.27169871014969,
            "unit": "iter/sec",
            "range": "stddev: 0.0003228467891228151",
            "extra": "mean: 17.16098933333174 msec\nrounds: 57"
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
          "id": "b7e310a149d150a095db23fbbbf69f5b94ac09c7",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/b7e310a149d150a095db23fbbbf69f5b94ac09c7"
        },
        "date": 1701694188295,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1162346784813671,
            "unit": "iter/sec",
            "range": "stddev: 0.07946433535095025",
            "extra": "mean: 8.603284433400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1977074656521405,
            "unit": "iter/sec",
            "range": "stddev: 0.0620399000849054",
            "extra": "mean: 5.057977940799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.17463225242919,
            "unit": "iter/sec",
            "range": "stddev: 0.0002179523468596518",
            "extra": "mean: 9.076499549450064 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11629559446809658,
            "unit": "iter/sec",
            "range": "stddev: 0.05973074942564462",
            "extra": "mean: 8.598778006799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19863649957133747,
            "unit": "iter/sec",
            "range": "stddev: 0.061500335630810136",
            "extra": "mean: 5.034321497600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.606360010275765,
            "unit": "iter/sec",
            "range": "stddev: 0.00020290046876743969",
            "extra": "mean: 17.3591943636366 msec\nrounds: 55"
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
          "id": "80067d796003c4a1c3dbbcaedd876cb2c85e9fea",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/80067d796003c4a1c3dbbcaedd876cb2c85e9fea"
        },
        "date": 1701694290196,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11703542379818054,
            "unit": "iter/sec",
            "range": "stddev: 0.08053188992594926",
            "extra": "mean: 8.544421573800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19775967761735022,
            "unit": "iter/sec",
            "range": "stddev: 0.06212467465668233",
            "extra": "mean: 5.056642547399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 116.51833739224358,
            "unit": "iter/sec",
            "range": "stddev: 0.00041500593615861783",
            "extra": "mean: 8.58234010526285 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11706341176653914,
            "unit": "iter/sec",
            "range": "stddev: 0.08896023807192596",
            "extra": "mean: 8.542378740799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19684544670346776,
            "unit": "iter/sec",
            "range": "stddev: 0.06620532523978458",
            "extra": "mean: 5.080127667400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.42402469657657,
            "unit": "iter/sec",
            "range": "stddev: 0.0005367082978829637",
            "extra": "mean: 16.828210561402955 msec\nrounds: 57"
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
          "id": "134dd302a890ae21890f3bb4fbfa82be2e731958",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/134dd302a890ae21890f3bb4fbfa82be2e731958"
        },
        "date": 1701694623177,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11742390419251457,
            "unit": "iter/sec",
            "range": "stddev: 0.024537937908852784",
            "extra": "mean: 8.516153562400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19916539015108528,
            "unit": "iter/sec",
            "range": "stddev: 0.039736591743488155",
            "extra": "mean: 5.020952682799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.60684938995537,
            "unit": "iter/sec",
            "range": "stddev: 0.0004067638190281777",
            "extra": "mean: 8.88045447872375 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11740401323700851,
            "unit": "iter/sec",
            "range": "stddev: 0.10347848678156918",
            "extra": "mean: 8.517596395800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19755762875484045,
            "unit": "iter/sec",
            "range": "stddev: 0.04523611980719332",
            "extra": "mean: 5.061814146599988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.1657259463241,
            "unit": "iter/sec",
            "range": "stddev: 0.00018330576884405294",
            "extra": "mean: 17.19225512499938 msec\nrounds: 56"
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
          "id": "c09cc37cbb52b6aaeba1b9149d9b8c876ec9c496",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/c09cc37cbb52b6aaeba1b9149d9b8c876ec9c496"
        },
        "date": 1701696196036,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11711705734183721,
            "unit": "iter/sec",
            "range": "stddev: 0.051234729667956044",
            "extra": "mean: 8.538465896399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1965124216267718,
            "unit": "iter/sec",
            "range": "stddev: 0.04207347380238388",
            "extra": "mean: 5.088736842799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 115.72360989619088,
            "unit": "iter/sec",
            "range": "stddev: 0.00013872131099839803",
            "extra": "mean: 8.641278999998736 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11681831910264572,
            "unit": "iter/sec",
            "range": "stddev: 0.08274933788850096",
            "extra": "mean: 8.560301223999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19642734627683875,
            "unit": "iter/sec",
            "range": "stddev: 0.03408709744980911",
            "extra": "mean: 5.090940843799979 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.92365803725686,
            "unit": "iter/sec",
            "range": "stddev: 0.00016925378689560303",
            "extra": "mean: 16.971112000000232 msec\nrounds: 56"
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
          "id": "aa13ffc6b04b06f16404b88dca47495a8eb0609f",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/aa13ffc6b04b06f16404b88dca47495a8eb0609f"
        },
        "date": 1701697705874,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11671978089976227,
            "unit": "iter/sec",
            "range": "stddev: 0.0866574265396647",
            "extra": "mean: 8.567528076999986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20380589251414374,
            "unit": "iter/sec",
            "range": "stddev: 0.07308351757513051",
            "extra": "mean: 4.9066294780000135 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.7348178994372,
            "unit": "iter/sec",
            "range": "stddev: 0.0007191755578992781",
            "extra": "mean: 8.949761755552446 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11641626732124978,
            "unit": "iter/sec",
            "range": "stddev: 0.06925829574845131",
            "extra": "mean: 8.589864827400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2010894447946599,
            "unit": "iter/sec",
            "range": "stddev: 0.07159433382104669",
            "extra": "mean: 4.972911437600009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.46885018938238,
            "unit": "iter/sec",
            "range": "stddev: 0.0005356143586755233",
            "extra": "mean: 17.400730947367283 msec\nrounds: 57"
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
          "id": "7f8ea9bd15b0730a09f16637c597462ef3f55fcb",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/7f8ea9bd15b0730a09f16637c597462ef3f55fcb"
        },
        "date": 1701698110246,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11793751792342153,
            "unit": "iter/sec",
            "range": "stddev: 0.05524265544790144",
            "extra": "mean: 8.479066014000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1975608091557158,
            "unit": "iter/sec",
            "range": "stddev: 0.049997341790644634",
            "extra": "mean: 5.061732659799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.18757927867031,
            "unit": "iter/sec",
            "range": "stddev: 0.0001578945722572307",
            "extra": "mean: 8.533327560440641 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11820476087826909,
            "unit": "iter/sec",
            "range": "stddev: 0.025320774849727917",
            "extra": "mean: 8.459896137599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1964975117103516,
            "unit": "iter/sec",
            "range": "stddev: 0.05242780255660183",
            "extra": "mean: 5.089122968000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 60.397175114168,
            "unit": "iter/sec",
            "range": "stddev: 0.00022135944548821247",
            "extra": "mean: 16.557065758617235 msec\nrounds: 58"
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
          "id": "39911e1ac22580eccc9814d936286a18bfbd65bb",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/39911e1ac22580eccc9814d936286a18bfbd65bb"
        },
        "date": 1701700172257,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11878354202517864,
            "unit": "iter/sec",
            "range": "stddev: 0.08877912738415615",
            "extra": "mean: 8.418674699799988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19854152617096407,
            "unit": "iter/sec",
            "range": "stddev: 0.04554587224354786",
            "extra": "mean: 5.0367296922000095 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.53447433048935,
            "unit": "iter/sec",
            "range": "stddev: 0.0005938624964054701",
            "extra": "mean: 8.508142021277516 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11924718117289008,
            "unit": "iter/sec",
            "range": "stddev: 0.08921513897318901",
            "extra": "mean: 8.38594246140002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19698476059669665,
            "unit": "iter/sec",
            "range": "stddev: 0.05324694965857768",
            "extra": "mean: 5.076534839400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 60.41117201887269,
            "unit": "iter/sec",
            "range": "stddev: 0.00030158658038400855",
            "extra": "mean: 16.553229586202963 msec\nrounds: 58"
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
          "id": "2cc076c1f940234c01891dd4087b4a23cfab773b",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/2cc076c1f940234c01891dd4087b4a23cfab773b"
        },
        "date": 1701704341552,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11452897395991316,
            "unit": "iter/sec",
            "range": "stddev: 0.12337316805535856",
            "extra": "mean: 8.731414989800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1829349416900622,
            "unit": "iter/sec",
            "range": "stddev: 0.08537527606171418",
            "extra": "mean: 5.466424242200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 97.88959481073175,
            "unit": "iter/sec",
            "range": "stddev: 0.0005023964159891821",
            "extra": "mean: 10.215590348836228 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11493460007661174,
            "unit": "iter/sec",
            "range": "stddev: 0.05784795912278358",
            "extra": "mean: 8.700600161600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.18355839885493744,
            "unit": "iter/sec",
            "range": "stddev: 0.06642137261364703",
            "extra": "mean: 5.447857500600014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.46636420739331,
            "unit": "iter/sec",
            "range": "stddev: 0.0008091326931042009",
            "extra": "mean: 19.059830333337352 msec\nrounds: 54"
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
          "id": "f4c2a880dbea29c9fdea43280d7c19b3f5a846cf",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/f4c2a880dbea29c9fdea43280d7c19b3f5a846cf"
        },
        "date": 1701706562466,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11840480300880331,
            "unit": "iter/sec",
            "range": "stddev: 0.09631634569726108",
            "extra": "mean: 8.445603341999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20139539661973746,
            "unit": "iter/sec",
            "range": "stddev: 0.0944873346951789",
            "extra": "mean: 4.965356789600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.02563129817607,
            "unit": "iter/sec",
            "range": "stddev: 0.00018686796351289554",
            "extra": "mean: 8.769958022727437 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1189564793202678,
            "unit": "iter/sec",
            "range": "stddev: 0.028539023591923278",
            "extra": "mean: 8.406435746199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20282070466848165,
            "unit": "iter/sec",
            "range": "stddev: 0.06266453586997275",
            "extra": "mean: 4.930463098600012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.575264672439175,
            "unit": "iter/sec",
            "range": "stddev: 0.000246621742788444",
            "extra": "mean: 16.78548984210593 msec\nrounds: 57"
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
          "id": "5511dc091aadfb198b8fbe22ae8b4856db35afde",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/5511dc091aadfb198b8fbe22ae8b4856db35afde"
        },
        "date": 1701768829764,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1182439949327026,
            "unit": "iter/sec",
            "range": "stddev: 0.07266111837639935",
            "extra": "mean: 8.457089094200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20065238901811897,
            "unit": "iter/sec",
            "range": "stddev: 0.06089297767689147",
            "extra": "mean: 4.9837433029999945 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.51331126469083,
            "unit": "iter/sec",
            "range": "stddev: 0.00015683281433750867",
            "extra": "mean: 8.809539505619703 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11801122832351982,
            "unit": "iter/sec",
            "range": "stddev: 0.05070519871275659",
            "extra": "mean: 8.473769947200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20025714007658166,
            "unit": "iter/sec",
            "range": "stddev: 0.05750926892415005",
            "extra": "mean: 4.993579752599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.85923195156708,
            "unit": "iter/sec",
            "range": "stddev: 0.0002620029427507379",
            "extra": "mean: 17.587293490911097 msec\nrounds: 55"
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
          "id": "185c5a8aa87afe59baec7197fe1ea1c9f509b2ec",
          "message": "Code scanning alerts",
          "timestamp": "2023-11-27T15:48:56Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/406/commits/185c5a8aa87afe59baec7197fe1ea1c9f509b2ec"
        },
        "date": 1701772086778,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11615765923464529,
            "unit": "iter/sec",
            "range": "stddev: 0.10820667993436257",
            "extra": "mean: 8.608988908600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19467399803886978,
            "unit": "iter/sec",
            "range": "stddev: 0.0762264558229067",
            "extra": "mean: 5.136792843799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.99428280837316,
            "unit": "iter/sec",
            "range": "stddev: 0.0004228821969207528",
            "extra": "mean: 8.772369765955908 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11628709188115373,
            "unit": "iter/sec",
            "range": "stddev: 0.08496264033977623",
            "extra": "mean: 8.59940672539999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19298115553945197,
            "unit": "iter/sec",
            "range": "stddev: 0.06521794338984227",
            "extra": "mean: 5.181853104799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.00029527058356,
            "unit": "iter/sec",
            "range": "stddev: 0.0003458686784847833",
            "extra": "mean: 16.949067719303116 msec\nrounds: 57"
          }
        ]
      },
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
          "id": "7c82457364227bc4c854e2da2421f396cfec5f0a",
          "message": "Merge pull request #406 from UCL-CCS/code_scanning_alerts\n\nCode scanning alerts",
          "timestamp": "2023-12-05T10:32:15Z",
          "tree_id": "c2c7efdd84c1c35ce60a2158969e132fba7fd706",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7c82457364227bc4c854e2da2421f396cfec5f0a"
        },
        "date": 1701772608163,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11455771880831092,
            "unit": "iter/sec",
            "range": "stddev: 0.10264977494353764",
            "extra": "mean: 8.729224101199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19179848329807184,
            "unit": "iter/sec",
            "range": "stddev: 0.05843504467405437",
            "extra": "mean: 5.213805567199984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.30407199468985,
            "unit": "iter/sec",
            "range": "stddev: 0.00021427060856860417",
            "extra": "mean: 9.587353406978304 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11544526161605542,
            "unit": "iter/sec",
            "range": "stddev: 0.07391371878513604",
            "extra": "mean: 8.662113853800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.18962020388178624,
            "unit": "iter/sec",
            "range": "stddev: 0.061835562522047714",
            "extra": "mean: 5.273699634999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.61620299700299,
            "unit": "iter/sec",
            "range": "stddev: 0.00041364508203859437",
            "extra": "mean: 17.662788160713205 msec\nrounds: 56"
          }
        ]
      }
    ]
  }
}