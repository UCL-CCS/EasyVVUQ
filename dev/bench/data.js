window.BENCHMARK_DATA = {
  "lastUpdate": 1614955766899,
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
          "id": "63e0ef3a17702e294e559223e02e254d14ef0beb",
          "message": "switch to random sampler in the benchmark",
          "timestamp": "2021-03-05T10:36:11+01:00",
          "tree_id": "12bbfb4786ec32dded71e2f06ee12567c31d266f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/63e0ef3a17702e294e559223e02e254d14ef0beb"
        },
        "date": 1614937979811,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.016968405793070566,
            "unit": "iter/sec",
            "range": "stddev: 1.6657898172267298",
            "extra": "mean: 58.933055479400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.12581519660829585,
            "unit": "iter/sec",
            "range": "stddev: 0.04407669845616022",
            "extra": "mean: 7.948165459799975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.8837793767907066,
            "unit": "iter/sec",
            "range": "stddev: 0.019093985161128556",
            "extra": "mean: 1.1315041131999806 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.017861498281560688,
            "unit": "iter/sec",
            "range": "stddev: 0.6876158411863663",
            "extra": "mean: 55.98634471960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.13678770683100816,
            "unit": "iter/sec",
            "range": "stddev: 0.08577785617245892",
            "extra": "mean: 7.31059846799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.8788672877017757,
            "unit": "iter/sec",
            "range": "stddev: 0.023556023549316057",
            "extra": "mean: 1.1378282182000248 sec\nrounds: 5"
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "5c50000306784e571e642b17fe8bc737d151ef90",
          "message": "another typo in the benchmark",
          "timestamp": "2021-03-05T10:46:12+01:00",
          "tree_id": "c78908feec592add4ae406bf7df8c04bce42e47b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5c50000306784e571e642b17fe8bc737d151ef90"
        },
        "date": 1614938577631,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.017482682938384297,
            "unit": "iter/sec",
            "range": "stddev: 0.18012740520735981",
            "extra": "mean: 57.19945866 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10844356823695446,
            "unit": "iter/sec",
            "range": "stddev: 0.08016638635136153",
            "extra": "mean: 9.22138598219999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7280318465556737,
            "unit": "iter/sec",
            "range": "stddev: 0.042578129239668874",
            "extra": "mean: 1.3735662865999756 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.018192478490293547,
            "unit": "iter/sec",
            "range": "stddev: 0.4976523526012892",
            "extra": "mean: 54.967771463000055 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.12147321030897262,
            "unit": "iter/sec",
            "range": "stddev: 0.30325163100790237",
            "extra": "mean: 8.232267818200034 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7852006277666463,
            "unit": "iter/sec",
            "range": "stddev: 0.051753611805625876",
            "extra": "mean: 1.2735598579999987 sec\nrounds: 5"
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "5684e7db3bb40325cda1ca798cba9a0cd8684fd4",
          "message": "update draw_runs",
          "timestamp": "2021-03-05T11:12:18+01:00",
          "tree_id": "6eb4be6ecdf84101e3b836534d9fb0d52d559a88",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5684e7db3bb40325cda1ca798cba9a0cd8684fd4"
        },
        "date": 1614939547038,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07678228087427019,
            "unit": "iter/sec",
            "range": "stddev: 0.13976582539602264",
            "extra": "mean: 13.023838164399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10993628376474687,
            "unit": "iter/sec",
            "range": "stddev: 0.1003318943658082",
            "extra": "mean: 9.096177947400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7568487427783457,
            "unit": "iter/sec",
            "range": "stddev: 0.032386084143275255",
            "extra": "mean: 1.3212679674000127 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07643009683108958,
            "unit": "iter/sec",
            "range": "stddev: 0.044486313577701615",
            "extra": "mean: 13.083851015000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.110530184047251,
            "unit": "iter/sec",
            "range": "stddev: 0.06947507769450233",
            "extra": "mean: 9.047302405400012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7489156009902067,
            "unit": "iter/sec",
            "range": "stddev: 0.039666039505285966",
            "extra": "mean: 1.3352639451999835 sec\nrounds: 5"
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
          "id": "e2afe737804279d492fada6e1ed0fdd385aceb16",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/e2afe737804279d492fada6e1ed0fdd385aceb16"
        },
        "date": 1614946668118,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055265531877230094,
            "unit": "iter/sec",
            "range": "stddev: 0.09092270906727676",
            "extra": "mean: 18.0944607974 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0922476323884889,
            "unit": "iter/sec",
            "range": "stddev: 0.1839751164435058",
            "extra": "mean: 10.840386621399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6329884571472183,
            "unit": "iter/sec",
            "range": "stddev: 0.03935230478262955",
            "extra": "mean: 1.5798076390000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0555402885910414,
            "unit": "iter/sec",
            "range": "stddev: 0.11304612223697509",
            "extra": "mean: 18.004947856199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09159195378462923,
            "unit": "iter/sec",
            "range": "stddev: 0.12298306422299944",
            "extra": "mean: 10.91798961239997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6244598026955269,
            "unit": "iter/sec",
            "range": "stddev: 0.035640884833310224",
            "extra": "mean: 1.6013841014000036 sec\nrounds: 5"
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
          "id": "9ad218bf385aa4def8f1945e0123d2cdb2df2aeb",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/9ad218bf385aa4def8f1945e0123d2cdb2df2aeb"
        },
        "date": 1614946741770,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0756077212414739,
            "unit": "iter/sec",
            "range": "stddev: 0.04176873355067803",
            "extra": "mean: 13.226162402199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10938733904225156,
            "unit": "iter/sec",
            "range": "stddev: 0.027876338711772173",
            "extra": "mean: 9.141825815999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7581730588328497,
            "unit": "iter/sec",
            "range": "stddev: 0.028908339619988586",
            "extra": "mean: 1.318960082199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07538925789886586,
            "unit": "iter/sec",
            "range": "stddev: 0.1598356526009098",
            "extra": "mean: 13.264489237199985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10910255453412464,
            "unit": "iter/sec",
            "range": "stddev: 0.03116949744269527",
            "extra": "mean: 9.165688230399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7530518495914815,
            "unit": "iter/sec",
            "range": "stddev: 0.03239639516963097",
            "extra": "mean: 1.3279298106000055 sec\nrounds: 5"
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
          "id": "f9aec014f8a995a3a737816afcd65fd59ea4ee46",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/f9aec014f8a995a3a737816afcd65fd59ea4ee46"
        },
        "date": 1614947121234,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0711781626562015,
            "unit": "iter/sec",
            "range": "stddev: 0.18669086186619271",
            "extra": "mean: 14.049252786 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09839679523720782,
            "unit": "iter/sec",
            "range": "stddev: 0.38822561099751207",
            "extra": "mean: 10.162932619799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7152947009182175,
            "unit": "iter/sec",
            "range": "stddev: 0.03580962238876645",
            "extra": "mean: 1.3980251758000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07133509489140209,
            "unit": "iter/sec",
            "range": "stddev: 0.09869597526707134",
            "extra": "mean: 14.018345409400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09920195943500758,
            "unit": "iter/sec",
            "range": "stddev: 0.4606392143578559",
            "extra": "mean: 10.080446048600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7014125790013253,
            "unit": "iter/sec",
            "range": "stddev: 0.03577052382783376",
            "extra": "mean: 1.4256944200000021 sec\nrounds: 5"
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
          "id": "238971c1f7f12b341febaf14e6b93012b83efb3d",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/238971c1f7f12b341febaf14e6b93012b83efb3d"
        },
        "date": 1614947434026,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05831000101957147,
            "unit": "iter/sec",
            "range": "stddev: 0.12279070764647589",
            "extra": "mean: 17.1497167298 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10001229837231368,
            "unit": "iter/sec",
            "range": "stddev: 0.03497026994557346",
            "extra": "mean: 9.998770313999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6742794362263158,
            "unit": "iter/sec",
            "range": "stddev: 0.04544915472505505",
            "extra": "mean: 1.4830646558000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05834125424559189,
            "unit": "iter/sec",
            "range": "stddev: 0.14575275260389017",
            "extra": "mean: 17.140529680600025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09928713734747449,
            "unit": "iter/sec",
            "range": "stddev: 0.2089972685909612",
            "extra": "mean: 10.071798087000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6446207032495066,
            "unit": "iter/sec",
            "range": "stddev: 0.055641789991376575",
            "extra": "mean: 1.551299849599991 sec\nrounds: 5"
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
          "id": "b2713821790e1437aa3c6e5b5328cec3f09c62b4",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/b2713821790e1437aa3c6e5b5328cec3f09c62b4"
        },
        "date": 1614947670823,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.056241474401435315,
            "unit": "iter/sec",
            "range": "stddev: 0.06775661728793413",
            "extra": "mean: 17.780472696399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09421896551605836,
            "unit": "iter/sec",
            "range": "stddev: 0.07179729132468804",
            "extra": "mean: 10.613574395799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6403820347494495,
            "unit": "iter/sec",
            "range": "stddev: 0.03319480374122224",
            "extra": "mean: 1.5615678543999933 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0558541391486172,
            "unit": "iter/sec",
            "range": "stddev: 0.23405103075552228",
            "extra": "mean: 17.903776071799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09482208255911184,
            "unit": "iter/sec",
            "range": "stddev: 0.2555055717563184",
            "extra": "mean: 10.546066623000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6608715448023504,
            "unit": "iter/sec",
            "range": "stddev: 0.037329328342748144",
            "extra": "mean: 1.5131533622000233 sec\nrounds: 5"
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
          "id": "d58e95617a7093b3d1faa963385b1669b7113ec2",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/d58e95617a7093b3d1faa963385b1669b7113ec2"
        },
        "date": 1614948236838,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05710803526120733,
            "unit": "iter/sec",
            "range": "stddev: 0.3844741111138171",
            "extra": "mean: 17.510670703799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09553438143796229,
            "unit": "iter/sec",
            "range": "stddev: 0.08730583671409864",
            "extra": "mean: 10.467435753999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6378356269988744,
            "unit": "iter/sec",
            "range": "stddev: 0.03696381367971343",
            "extra": "mean: 1.567802044400014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.055141050522488154,
            "unit": "iter/sec",
            "range": "stddev: 0.34035760297477624",
            "extra": "mean: 18.135309184799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09436969253802027,
            "unit": "iter/sec",
            "range": "stddev: 0.521070817431925",
            "extra": "mean: 10.596622422999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6365352466248927,
            "unit": "iter/sec",
            "range": "stddev: 0.034051850171614856",
            "extra": "mean: 1.5710049134000201 sec\nrounds: 5"
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
          "id": "fbed52d9da66103da4d6e393d0eeb79f06527233",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/fbed52d9da66103da4d6e393d0eeb79f06527233"
        },
        "date": 1614948435995,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07081671830473428,
            "unit": "iter/sec",
            "range": "stddev: 0.04058843487197305",
            "extra": "mean: 14.1209593432 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10098746821080352,
            "unit": "iter/sec",
            "range": "stddev: 0.02182202610511429",
            "extra": "mean: 9.902218737799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7047643204282038,
            "unit": "iter/sec",
            "range": "stddev: 0.0371427547808901",
            "extra": "mean: 1.418914055399989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07063817885968185,
            "unit": "iter/sec",
            "range": "stddev: 0.08894993778325706",
            "extra": "mean: 14.156650357399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10144231760635321,
            "unit": "iter/sec",
            "range": "stddev: 0.03142991951928608",
            "extra": "mean: 9.857818941799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7019682067614761,
            "unit": "iter/sec",
            "range": "stddev: 0.03758526979976274",
            "extra": "mean: 1.4245659423999997 sec\nrounds: 5"
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
          "id": "978a58a96032f3b59b22739d82d5f476274006cf",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/978a58a96032f3b59b22739d82d5f476274006cf"
        },
        "date": 1614948792734,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07523024991239813,
            "unit": "iter/sec",
            "range": "stddev: 0.3449015590304297",
            "extra": "mean: 13.292525296200001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10830947549484794,
            "unit": "iter/sec",
            "range": "stddev: 0.10431925521275226",
            "extra": "mean: 9.2328025358 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7393705984069544,
            "unit": "iter/sec",
            "range": "stddev: 0.03837707578203886",
            "extra": "mean: 1.3525017118000051 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07434582580575737,
            "unit": "iter/sec",
            "range": "stddev: 0.20351151536880852",
            "extra": "mean: 13.450654279000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10510571382595153,
            "unit": "iter/sec",
            "range": "stddev: 0.05573517701043746",
            "extra": "mean: 9.514230612199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7083482139761526,
            "unit": "iter/sec",
            "range": "stddev: 0.043353824134359835",
            "extra": "mean: 1.4117350481999893 sec\nrounds: 5"
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
          "id": "2ceae9b6c1b891ca17d9d4bbf0f19f0127a852eb",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/2ceae9b6c1b891ca17d9d4bbf0f19f0127a852eb"
        },
        "date": 1614950596812,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.052511350207492494,
            "unit": "iter/sec",
            "range": "stddev: 0.10357548409356857",
            "extra": "mean: 19.043501948599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09059100143852855,
            "unit": "iter/sec",
            "range": "stddev: 0.029058948092200707",
            "extra": "mean: 11.038623970599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6137446947722988,
            "unit": "iter/sec",
            "range": "stddev: 0.03913364688328385",
            "extra": "mean: 1.6293419861999836 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05238272164374448,
            "unit": "iter/sec",
            "range": "stddev: 0.10569519191465644",
            "extra": "mean: 19.090264282199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09102462381190952,
            "unit": "iter/sec",
            "range": "stddev: 0.036613357534949875",
            "extra": "mean: 10.986038262200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.5917642502879342,
            "unit": "iter/sec",
            "range": "stddev: 0.05990919350470751",
            "extra": "mean: 1.689862135999988 sec\nrounds: 5"
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
          "id": "9659dfb843d478c68219271cc3ffa69ecf3727ff",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/9659dfb843d478c68219271cc3ffa69ecf3727ff"
        },
        "date": 1614954566363,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07099977366614052,
            "unit": "iter/sec",
            "range": "stddev: 0.06787235377426552",
            "extra": "mean: 14.084551940999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10264630458627842,
            "unit": "iter/sec",
            "range": "stddev: 0.027361690431936037",
            "extra": "mean: 9.742191928199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7141955017011935,
            "unit": "iter/sec",
            "range": "stddev: 0.03181498504165594",
            "extra": "mean: 1.4001768390000051 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07056874993191603,
            "unit": "iter/sec",
            "range": "stddev: 0.04259541881101322",
            "extra": "mean: 14.170578350399989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10218283835588038,
            "unit": "iter/sec",
            "range": "stddev: 0.02948541076368828",
            "extra": "mean: 9.78637916199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7075109339380053,
            "unit": "iter/sec",
            "range": "stddev: 0.033753463332543025",
            "extra": "mean: 1.413405718599995 sec\nrounds: 5"
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
          "id": "35cea447834dc495fb830c4c6946a6a53a1def18",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/35cea447834dc495fb830c4c6946a6a53a1def18"
        },
        "date": 1614954673774,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05875587218669318,
            "unit": "iter/sec",
            "range": "stddev: 0.12180834432177022",
            "extra": "mean: 17.0195754532 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0996593070210593,
            "unit": "iter/sec",
            "range": "stddev: 0.0725768475688176",
            "extra": "mean: 10.034185766399991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6814934875915356,
            "unit": "iter/sec",
            "range": "stddev: 0.036103400881031145",
            "extra": "mean: 1.4673654527999929 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05879477343037526,
            "unit": "iter/sec",
            "range": "stddev: 0.10307357473919013",
            "extra": "mean: 17.008314543199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09934497496562093,
            "unit": "iter/sec",
            "range": "stddev: 0.03567920753069933",
            "extra": "mean: 10.065934390199981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6744330950375694,
            "unit": "iter/sec",
            "range": "stddev: 0.04849632409121526",
            "extra": "mean: 1.4827267631999803 sec\nrounds: 5"
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
          "id": "b3cbddde5ed8f35beb0f99d261156c10f16b994d",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/b3cbddde5ed8f35beb0f99d261156c10f16b994d"
        },
        "date": 1614954928554,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09224381221492055,
            "unit": "iter/sec",
            "range": "stddev: 0.5113254236710731",
            "extra": "mean: 10.840835563800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.13316085650668197,
            "unit": "iter/sec",
            "range": "stddev: 0.08283730247178765",
            "extra": "mean: 7.509714387799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.9071104208465302,
            "unit": "iter/sec",
            "range": "stddev: 0.02265929295940244",
            "extra": "mean: 1.1024016227999938 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09369191792008305,
            "unit": "iter/sec",
            "range": "stddev: 0.07331440159651562",
            "extra": "mean: 10.673279213399985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.13499954517856744,
            "unit": "iter/sec",
            "range": "stddev: 0.04714941769229169",
            "extra": "mean: 7.407432363399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.885401091096487,
            "unit": "iter/sec",
            "range": "stddev: 0.024559074729384914",
            "extra": "mean: 1.1294316327999923 sec\nrounds: 5"
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
          "id": "e36577f1821f92958b2fc9395468adcfbb3fa8cd",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/e36577f1821f92958b2fc9395468adcfbb3fa8cd"
        },
        "date": 1614955186091,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06246729171689625,
            "unit": "iter/sec",
            "range": "stddev: 1.000225939232609",
            "extra": "mean: 16.008377704800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10813330695855557,
            "unit": "iter/sec",
            "range": "stddev: 0.5238529540290635",
            "extra": "mean: 9.247844425800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6991906972418163,
            "unit": "iter/sec",
            "range": "stddev: 0.04485405927821726",
            "extra": "mean: 1.430224978600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06351707344418236,
            "unit": "iter/sec",
            "range": "stddev: 0.713970843280216",
            "extra": "mean: 15.743798411600016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10661776807579165,
            "unit": "iter/sec",
            "range": "stddev: 0.6244124797730493",
            "extra": "mean: 9.379299698799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7566383346120701,
            "unit": "iter/sec",
            "range": "stddev: 0.07484790185510751",
            "extra": "mean: 1.3216353894000121 sec\nrounds: 5"
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
          "id": "a9f05a9717ed935282df8b9ffdd0d2f071b1dae9",
          "message": "Cleanup",
          "timestamp": "2021-03-05T10:12:25Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/323/commits/a9f05a9717ed935282df8b9ffdd0d2f071b1dae9"
        },
        "date": 1614955216116,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05424884705005109,
            "unit": "iter/sec",
            "range": "stddev: 0.26821154443882655",
            "extra": "mean: 18.433571483600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0946774827524968,
            "unit": "iter/sec",
            "range": "stddev: 0.12730775577818065",
            "extra": "mean: 10.562173506599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6319832286363634,
            "unit": "iter/sec",
            "range": "stddev: 0.03553304171675484",
            "extra": "mean: 1.582320471000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.052874418118189194,
            "unit": "iter/sec",
            "range": "stddev: 0.1926605230723552",
            "extra": "mean: 18.912737682800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09278337418411518,
            "unit": "iter/sec",
            "range": "stddev: 0.019028034650598095",
            "extra": "mean: 10.777792991399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6276847932631764,
            "unit": "iter/sec",
            "range": "stddev: 0.04670700882377546",
            "extra": "mean: 1.5931563274000156 sec\nrounds: 5"
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
          "id": "41d9296692d07ad0649a0c3b10473d711511af28",
          "message": "Merge pull request #323 from UCL-CCS/cleanup\n\nCleanup",
          "timestamp": "2021-03-05T15:36:37+01:00",
          "tree_id": "963da216a70fde98313711d4356681bdbcca4553",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/41d9296692d07ad0649a0c3b10473d711511af28"
        },
        "date": 1614955514490,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055058152510481406,
            "unit": "iter/sec",
            "range": "stddev: 0.08701182088424836",
            "extra": "mean: 18.162614515800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09192588946690053,
            "unit": "iter/sec",
            "range": "stddev: 0.033047916043101665",
            "extra": "mean: 10.878328246800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.625198596600553,
            "unit": "iter/sec",
            "range": "stddev: 0.03592950514925965",
            "extra": "mean: 1.5994917542000053 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05459063782859201,
            "unit": "iter/sec",
            "range": "stddev: 0.12483986556968406",
            "extra": "mean: 18.318159299399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0914793362651133,
            "unit": "iter/sec",
            "range": "stddev: 0.059163773613396836",
            "extra": "mean: 10.931430428200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6279274347485236,
            "unit": "iter/sec",
            "range": "stddev: 0.023661696484267945",
            "extra": "mean: 1.5925407055999812 sec\nrounds: 5"
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
            "email": "unaudio@gmail.com",
            "name": "Vytautas Jancauskas",
            "username": "orbitfold"
          },
          "distinct": true,
          "id": "9e15f8183945c2986492223612a3b3b8752c7e4c",
          "message": "experiment with fixed string lengths in the database",
          "timestamp": "2021-03-05T15:42:06+01:00",
          "tree_id": "aade91182a22441e2c9bef65b1baa22e0a856af1",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9e15f8183945c2986492223612a3b3b8752c7e4c"
        },
        "date": 1614955766457,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07005240281242801,
            "unit": "iter/sec",
            "range": "stddev: 0.05085239219074827",
            "extra": "mean: 14.275027834199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10283739585467563,
            "unit": "iter/sec",
            "range": "stddev: 0.008469423256029056",
            "extra": "mean: 9.724089099000008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6964499396593747,
            "unit": "iter/sec",
            "range": "stddev: 0.03892653055400142",
            "extra": "mean: 1.435853380200001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07009761377398453,
            "unit": "iter/sec",
            "range": "stddev: 0.04478448264154397",
            "extra": "mean: 14.265820848400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10304331325817655,
            "unit": "iter/sec",
            "range": "stddev: 0.0046201564544703965",
            "extra": "mean: 9.704656890199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6912586436138628,
            "unit": "iter/sec",
            "range": "stddev: 0.038726915281497236",
            "extra": "mean: 1.4466365220000057 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}