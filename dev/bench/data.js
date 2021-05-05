window.BENCHMARK_DATA = {
  "lastUpdate": 1620224955360,
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
          "id": "56beaf5f903cbe74254f9ef9eea2747e762bff7e",
          "message": "typo",
          "timestamp": "2021-03-05T16:01:01+01:00",
          "tree_id": "c9a9f6aaa70d3389a16efa0aa513bcb96e98d9cc",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/56beaf5f903cbe74254f9ef9eea2747e762bff7e"
        },
        "date": 1614956903283,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07004979306696195,
            "unit": "iter/sec",
            "range": "stddev: 0.09261292872638854",
            "extra": "mean: 14.275559658599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10240916449146001,
            "unit": "iter/sec",
            "range": "stddev: 0.01566427394054151",
            "extra": "mean: 9.764751084199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6961262225534123,
            "unit": "iter/sec",
            "range": "stddev: 0.040641284539070205",
            "extra": "mean: 1.4365210899999852 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07046760458505018,
            "unit": "iter/sec",
            "range": "stddev: 0.060728635083427324",
            "extra": "mean: 14.190918023799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10237663103595848,
            "unit": "iter/sec",
            "range": "stddev: 0.02022326600114367",
            "extra": "mean: 9.767854146799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6970848012597378,
            "unit": "iter/sec",
            "range": "stddev: 0.03750560401409054",
            "extra": "mean: 1.4345456939999963 sec\nrounds: 5"
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
          "id": "7c5040a5cc74eab0f08e53c2d61854cdb9431e57",
          "message": "more risky pragmas",
          "timestamp": "2021-03-05T16:10:11+01:00",
          "tree_id": "8f57339d4f9e8239fbe11a1345970872b8937774",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7c5040a5cc74eab0f08e53c2d61854cdb9431e57"
        },
        "date": 1614957514138,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05528576638568422,
            "unit": "iter/sec",
            "range": "stddev: 0.19479772736852244",
            "extra": "mean: 18.08783825159999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09720572547338416,
            "unit": "iter/sec",
            "range": "stddev: 0.03893054317171724",
            "extra": "mean: 10.287459870600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6427337224558197,
            "unit": "iter/sec",
            "range": "stddev: 0.031841570203445364",
            "extra": "mean: 1.5558542598000031 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05546970461298859,
            "unit": "iter/sec",
            "range": "stddev: 0.18530046088657745",
            "extra": "mean: 18.027858756 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09650195432436318,
            "unit": "iter/sec",
            "range": "stddev: 0.05456320171648578",
            "extra": "mean: 10.362484438799981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6391546502553271,
            "unit": "iter/sec",
            "range": "stddev: 0.042132612586534314",
            "extra": "mean: 1.564566571799992 sec\nrounds: 5"
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
          "id": "634cde8fb3b1285a59d356064f50643b0f31d463",
          "message": "move pragmas to an event listener",
          "timestamp": "2021-03-05T16:19:55+01:00",
          "tree_id": "061db97fdd08c23e86cd9c1219323da4fb122d7b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/634cde8fb3b1285a59d356064f50643b0f31d463"
        },
        "date": 1614957998964,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0763930553563667,
            "unit": "iter/sec",
            "range": "stddev: 0.23564679509793163",
            "extra": "mean: 13.090195114399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11162518609424621,
            "unit": "iter/sec",
            "range": "stddev: 0.13434068270543525",
            "extra": "mean: 8.958551694200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.770820744382078,
            "unit": "iter/sec",
            "range": "stddev: 0.03858943995538993",
            "extra": "mean: 1.297318484599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07747059220503306,
            "unit": "iter/sec",
            "range": "stddev: 0.17811053805458926",
            "extra": "mean: 12.908123864000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10946822509107433,
            "unit": "iter/sec",
            "range": "stddev: 0.14538718314375154",
            "extra": "mean: 9.135070922800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7724327515906234,
            "unit": "iter/sec",
            "range": "stddev: 0.04400720987046884",
            "extra": "mean: 1.2946110815999987 sec\nrounds: 5"
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
          "id": "c0eb4e34a326e852fbe4421e7a905e77252048c7",
          "message": "cache increase",
          "timestamp": "2021-03-05T16:53:37+01:00",
          "tree_id": "59d17f6ed0c5907d4855b21e8df65d18ce5eed30",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c0eb4e34a326e852fbe4421e7a905e77252048c7"
        },
        "date": 1614960051619,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07052010012835516,
            "unit": "iter/sec",
            "range": "stddev: 0.049886292383725994",
            "extra": "mean: 14.180354227799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1027637358916464,
            "unit": "iter/sec",
            "range": "stddev: 0.00928165097023449",
            "extra": "mean: 9.731059223599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7101015010422368,
            "unit": "iter/sec",
            "range": "stddev: 0.036449310631203984",
            "extra": "mean: 1.4082493819999968 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0706937017739991,
            "unit": "iter/sec",
            "range": "stddev: 0.05175387932884715",
            "extra": "mean: 14.145531707999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10313708451082568,
            "unit": "iter/sec",
            "range": "stddev: 0.0075150829522477305",
            "extra": "mean: 9.69583350879999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7060545183049204,
            "unit": "iter/sec",
            "range": "stddev: 0.03752226822125744",
            "extra": "mean: 1.4163212246000172 sec\nrounds: 5"
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
          "id": "46cbcd5a1fd03e19f13394c3a541687290df2c33",
          "message": "changed permissions on mcmc script",
          "timestamp": "2021-03-05T17:05:06+01:00",
          "tree_id": "3854c7cd769e5307ee5f2ee056ed44d9165f79c4",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/46cbcd5a1fd03e19f13394c3a541687290df2c33"
        },
        "date": 1614960768916,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0605030247828301,
            "unit": "iter/sec",
            "range": "stddev: 0.6550189671956397",
            "extra": "mean: 16.52809927420002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10161905188312431,
            "unit": "iter/sec",
            "range": "stddev: 0.09465508299278627",
            "extra": "mean: 9.840674376200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7207196416410897,
            "unit": "iter/sec",
            "range": "stddev: 0.04603557345189175",
            "extra": "mean: 1.3875020774000064 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0612642620542276,
            "unit": "iter/sec",
            "range": "stddev: 0.14350918310640953",
            "extra": "mean: 16.322729866799953 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10375221079036652,
            "unit": "iter/sec",
            "range": "stddev: 0.03422734315693978",
            "extra": "mean: 9.638348834999965 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7087972791499754,
            "unit": "iter/sec",
            "range": "stddev: 0.04277537454697367",
            "extra": "mean: 1.410840630200005 sec\nrounds: 5"
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
          "id": "f8c601476317fce0a7c6f33aa7bf44a74af71d7d",
          "message": "set temp_store to memory",
          "timestamp": "2021-03-05T17:18:50+01:00",
          "tree_id": "ae408859a3411c2067eaa5fb99d3d05e45a1fb75",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f8c601476317fce0a7c6f33aa7bf44a74af71d7d"
        },
        "date": 1614961673544,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05142978301674843,
            "unit": "iter/sec",
            "range": "stddev: 0.06300923914301726",
            "extra": "mean: 19.4439863702 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0889650600505124,
            "unit": "iter/sec",
            "range": "stddev: 0.07582660052344005",
            "extra": "mean: 11.240367841400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6231869787151751,
            "unit": "iter/sec",
            "range": "stddev: 0.0420152734742625",
            "extra": "mean: 1.6046548374000054 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05129649798738376,
            "unit": "iter/sec",
            "range": "stddev: 0.08496787576731521",
            "extra": "mean: 19.494508187399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08913796713581147,
            "unit": "iter/sec",
            "range": "stddev: 0.0537279477092978",
            "extra": "mean: 11.218564121799977 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6168245898463907,
            "unit": "iter/sec",
            "range": "stddev: 0.04163212060185263",
            "extra": "mean: 1.6212064442000156 sec\nrounds: 5"
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
          "id": "4689374db6809e7c93a028d44ea763b648db029d",
          "message": "more frequent commits to the db",
          "timestamp": "2021-03-08T17:49:06+01:00",
          "tree_id": "7c0406d1c885e21e490af7ee8dc5e90865160e56",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4689374db6809e7c93a028d44ea763b648db029d"
        },
        "date": 1615222550017,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0775585472576343,
            "unit": "iter/sec",
            "range": "stddev: 0.07325772471320031",
            "extra": "mean: 12.893485442399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.11151620213359562,
            "unit": "iter/sec",
            "range": "stddev: 0.10749459391820855",
            "extra": "mean: 8.967306820599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7651457241310413,
            "unit": "iter/sec",
            "range": "stddev: 0.06267495855585355",
            "extra": "mean: 1.3069405845999824 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.077599498181949,
            "unit": "iter/sec",
            "range": "stddev: 0.11893094133979575",
            "extra": "mean: 12.8866812728 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.11183649331322107,
            "unit": "iter/sec",
            "range": "stddev: 0.08319531021205694",
            "extra": "mean: 8.94162513839999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7615318649608176,
            "unit": "iter/sec",
            "range": "stddev: 0.014684819964399253",
            "extra": "mean: 1.313142687800007 sec\nrounds: 5"
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
          "id": "0b390222e0e46401d6b1d788832b284d76a4b4aa",
          "message": "added db benchmarking utility",
          "timestamp": "2021-03-09T14:11:51+01:00",
          "tree_id": "16e07c55336fd4969a6df84e49f9f0996c71ef56",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0b390222e0e46401d6b1d788832b284d76a4b4aa"
        },
        "date": 1615295949924,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0703207188121331,
            "unit": "iter/sec",
            "range": "stddev: 0.037170791695053856",
            "extra": "mean: 14.220559984199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.102848276963064,
            "unit": "iter/sec",
            "range": "stddev: 0.0165815832285608",
            "extra": "mean: 9.723060313000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7168210236132977,
            "unit": "iter/sec",
            "range": "stddev: 0.032835248865907114",
            "extra": "mean: 1.395048369199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07062704496567057,
            "unit": "iter/sec",
            "range": "stddev: 0.06497870115333647",
            "extra": "mean: 14.158882061200018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10291958065004923,
            "unit": "iter/sec",
            "range": "stddev: 0.01713546609625999",
            "extra": "mean: 9.716324082200014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6989073432022759,
            "unit": "iter/sec",
            "range": "stddev: 0.03466776901925474",
            "extra": "mean: 1.4308048266000015 sec\nrounds: 5"
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
          "id": "a595d5b2b9b8dc4355cad7312cec9cd59188e449",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/a595d5b2b9b8dc4355cad7312cec9cd59188e449"
        },
        "date": 1615464772706,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07030213553334141,
            "unit": "iter/sec",
            "range": "stddev: 0.03691390088716751",
            "extra": "mean: 14.22431896860005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10353712832519597,
            "unit": "iter/sec",
            "range": "stddev: 0.022726939205746324",
            "extra": "mean: 9.65837102280002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7048307045006532,
            "unit": "iter/sec",
            "range": "stddev: 0.03968575565132572",
            "extra": "mean: 1.418780415799938 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07041090024734259,
            "unit": "iter/sec",
            "range": "stddev: 0.051902309729248676",
            "extra": "mean: 14.202346461800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10365355262726977,
            "unit": "iter/sec",
            "range": "stddev: 0.009344536146847174",
            "extra": "mean: 9.647522681599957 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.696511579273153,
            "unit": "iter/sec",
            "range": "stddev: 0.03569465487586648",
            "extra": "mean: 1.4357263105999665 sec\nrounds: 5"
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
          "id": "ca7f1547d3cfa12ebad0a610ed4ceaf5e2a55792",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/ca7f1547d3cfa12ebad0a610ed4ceaf5e2a55792"
        },
        "date": 1615472883119,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07090136818046872,
            "unit": "iter/sec",
            "range": "stddev: 0.1693200542573761",
            "extra": "mean: 14.104100183999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1007513036419884,
            "unit": "iter/sec",
            "range": "stddev: 0.19891679417278302",
            "extra": "mean: 9.925429883800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7116706912092639,
            "unit": "iter/sec",
            "range": "stddev: 0.03390753756229283",
            "extra": "mean: 1.405144278599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07137067050392853,
            "unit": "iter/sec",
            "range": "stddev: 0.22832365870229962",
            "extra": "mean: 14.011357787999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09847993821320623,
            "unit": "iter/sec",
            "range": "stddev: 0.09968357458900856",
            "extra": "mean: 10.154352430999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6840603547693184,
            "unit": "iter/sec",
            "range": "stddev: 0.0504130816566238",
            "extra": "mean: 1.461859312600018 sec\nrounds: 5"
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
          "id": "cc0e76ac48c24829853c8cd945932e144458b5c3",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/cc0e76ac48c24829853c8cd945932e144458b5c3"
        },
        "date": 1615553873876,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.057148618124584126,
            "unit": "iter/sec",
            "range": "stddev: 0.0860537549317031",
            "extra": "mean: 17.498235877199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09792085523875674,
            "unit": "iter/sec",
            "range": "stddev: 0.02722789648488765",
            "extra": "mean: 10.212329105600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.665492156684673,
            "unit": "iter/sec",
            "range": "stddev: 0.030630052788159678",
            "extra": "mean: 1.5026473113999828 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.056739728366390754,
            "unit": "iter/sec",
            "range": "stddev: 0.32222884450726463",
            "extra": "mean: 17.624335342999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0962212463039065,
            "unit": "iter/sec",
            "range": "stddev: 0.03306860803284024",
            "extra": "mean: 10.3927151062 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6460529780614123,
            "unit": "iter/sec",
            "range": "stddev: 0.03510216274919767",
            "extra": "mean: 1.5478606769999943 sec\nrounds: 5"
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
          "id": "65a687c9c428cfb2c5172d949c8b33dd0cd3e142",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/65a687c9c428cfb2c5172d949c8b33dd0cd3e142"
        },
        "date": 1615554586016,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.058010857953449804,
            "unit": "iter/sec",
            "range": "stddev: 0.3791326957665626",
            "extra": "mean: 17.238152223199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09530251156167842,
            "unit": "iter/sec",
            "range": "stddev: 0.06655229627789562",
            "extra": "mean: 10.492902900599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6697821064275342,
            "unit": "iter/sec",
            "range": "stddev: 0.034755693564235246",
            "extra": "mean: 1.4930228658000033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06016366994899697,
            "unit": "iter/sec",
            "range": "stddev: 0.26559476110073893",
            "extra": "mean: 16.621326472400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1000579917969934,
            "unit": "iter/sec",
            "range": "stddev: 0.08014240283689648",
            "extra": "mean: 9.994204181400017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7094837373985138,
            "unit": "iter/sec",
            "range": "stddev: 0.049955923254763265",
            "extra": "mean: 1.409475576800014 sec\nrounds: 5"
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
          "id": "a36445db5d564fb9c803b5959a1ba753aa4f337a",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/a36445db5d564fb9c803b5959a1ba753aa4f337a"
        },
        "date": 1615558502927,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05670433767285388,
            "unit": "iter/sec",
            "range": "stddev: 0.11877854044364863",
            "extra": "mean: 17.63533516199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09886049085940819,
            "unit": "iter/sec",
            "range": "stddev: 0.04476770710746864",
            "extra": "mean: 10.115264362000016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6341279215506419,
            "unit": "iter/sec",
            "range": "stddev: 0.03486253118509116",
            "extra": "mean: 1.576968882799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05682622308391211,
            "unit": "iter/sec",
            "range": "stddev: 0.161020846227891",
            "extra": "mean: 17.597509489999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09542450046362708,
            "unit": "iter/sec",
            "range": "stddev: 0.05492797429064992",
            "extra": "mean: 10.479488969199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6390937033666189,
            "unit": "iter/sec",
            "range": "stddev: 0.05226408247203395",
            "extra": "mean: 1.56471577599998 sec\nrounds: 5"
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
          "id": "5634a6e6199cb0dff4ab21aa18ee2986e50c76dd",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/5634a6e6199cb0dff4ab21aa18ee2986e50c76dd"
        },
        "date": 1615565863988,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.04810692264686154,
            "unit": "iter/sec",
            "range": "stddev: 0.8498232696352855",
            "extra": "mean: 20.7870290798 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08440905921941233,
            "unit": "iter/sec",
            "range": "stddev: 0.17506284424524143",
            "extra": "mean: 11.847069606600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.5916148831405075,
            "unit": "iter/sec",
            "range": "stddev: 0.08958097714572368",
            "extra": "mean: 1.690288781600009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.04726455249912468,
            "unit": "iter/sec",
            "range": "stddev: 0.9208273562934111",
            "extra": "mean: 21.157504876799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08260480405143214,
            "unit": "iter/sec",
            "range": "stddev: 0.17211140652786383",
            "extra": "mean: 12.105833449799979 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.5521718207473004,
            "unit": "iter/sec",
            "range": "stddev: 0.06335066661309284",
            "extra": "mean: 1.8110304843999756 sec\nrounds: 5"
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
          "id": "56eee420472efed692b9a1654c5c8db29d86a5c8",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/56eee420472efed692b9a1654c5c8db29d86a5c8"
        },
        "date": 1615804590593,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07088521008699246,
            "unit": "iter/sec",
            "range": "stddev: 0.046965475682601086",
            "extra": "mean: 14.1073151758 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10337296721963456,
            "unit": "iter/sec",
            "range": "stddev: 0.010851975234792468",
            "extra": "mean: 9.673708967600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7026257948023902,
            "unit": "iter/sec",
            "range": "stddev: 0.03929406332446619",
            "extra": "mean: 1.423232690000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07099137251020542,
            "unit": "iter/sec",
            "range": "stddev: 0.03729968658144",
            "extra": "mean: 14.086218714200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10332405167205258,
            "unit": "iter/sec",
            "range": "stddev: 0.009275829286777539",
            "extra": "mean: 9.678288683200014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6991505183469469,
            "unit": "iter/sec",
            "range": "stddev: 0.0381017657795709",
            "extra": "mean: 1.4303071709999926 sec\nrounds: 5"
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
          "id": "f41904daad69a007f3457b48e757f49b096c3bcb",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/f41904daad69a007f3457b48e757f49b096c3bcb"
        },
        "date": 1615804748626,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.056884964025797166,
            "unit": "iter/sec",
            "range": "stddev: 0.07439781811994436",
            "extra": "mean: 17.579337828999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0961239689683588,
            "unit": "iter/sec",
            "range": "stddev: 0.03578095215249993",
            "extra": "mean: 10.403232520799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6520932440342051,
            "unit": "iter/sec",
            "range": "stddev: 0.029372293388472373",
            "extra": "mean: 1.533523018599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.056797807388103444,
            "unit": "iter/sec",
            "range": "stddev: 0.06368524536786804",
            "extra": "mean: 17.606313447399987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09593582492750073,
            "unit": "iter/sec",
            "range": "stddev: 0.02148728208038062",
            "extra": "mean: 10.423634765800012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6538784977549207,
            "unit": "iter/sec",
            "range": "stddev: 0.03505381758529092",
            "extra": "mean: 1.5293361127999787 sec\nrounds: 5"
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
          "id": "7f5dfb87308bb679eff3cf175c1764fd05c3b5a0",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/7f5dfb87308bb679eff3cf175c1764fd05c3b5a0"
        },
        "date": 1615804758583,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07369699800444933,
            "unit": "iter/sec",
            "range": "stddev: 0.05093405461686795",
            "extra": "mean: 13.569073735400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10304179172570543,
            "unit": "iter/sec",
            "range": "stddev: 0.06636466498190692",
            "extra": "mean: 9.7048001908 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7099943883151142,
            "unit": "iter/sec",
            "range": "stddev: 0.03663303541200802",
            "extra": "mean: 1.4084618363999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07177947716632985,
            "unit": "iter/sec",
            "range": "stddev: 0.04345411337453566",
            "extra": "mean: 13.931558705600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10372554942464847,
            "unit": "iter/sec",
            "range": "stddev: 0.031068603641208108",
            "extra": "mean: 9.640826253 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7148897546647934,
            "unit": "iter/sec",
            "range": "stddev: 0.03833996676205738",
            "extra": "mean: 1.3988170812000136 sec\nrounds: 5"
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
          "id": "7fd26eebdd84dafa21268db75b076bd2417b554d",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/7fd26eebdd84dafa21268db75b076bd2417b554d"
        },
        "date": 1615824131136,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07068448002622103,
            "unit": "iter/sec",
            "range": "stddev: 0.06902846199314838",
            "extra": "mean: 14.1473771842 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10332702492260201,
            "unit": "iter/sec",
            "range": "stddev: 0.020559661233555872",
            "extra": "mean: 9.678010189000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7173508305905715,
            "unit": "iter/sec",
            "range": "stddev: 0.02824939132197561",
            "extra": "mean: 1.3940180415999976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07088524398271763,
            "unit": "iter/sec",
            "range": "stddev: 0.07027011408717261",
            "extra": "mean: 14.107308430000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10283058776017769,
            "unit": "iter/sec",
            "range": "stddev: 0.02286464942816628",
            "extra": "mean: 9.724732900799983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7122361407312309,
            "unit": "iter/sec",
            "range": "stddev: 0.036739096749979654",
            "extra": "mean: 1.4040287241999976 sec\nrounds: 5"
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
          "id": "e37a9c58a5764a565f4751ca2dd4d9e553697c24",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/e37a9c58a5764a565f4751ca2dd4d9e553697c24"
        },
        "date": 1615825495449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07146428177183048,
            "unit": "iter/sec",
            "range": "stddev: 0.06788778045122323",
            "extra": "mean: 13.9930042702 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10434655139093653,
            "unit": "iter/sec",
            "range": "stddev: 0.02335344184284738",
            "extra": "mean: 9.583450403199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.710296338754998,
            "unit": "iter/sec",
            "range": "stddev: 0.026779234557505686",
            "extra": "mean: 1.4078630923999866 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07155557912743266,
            "unit": "iter/sec",
            "range": "stddev: 0.05129134422523316",
            "extra": "mean: 13.97515067579999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1039749113350074,
            "unit": "iter/sec",
            "range": "stddev: 0.03969228093519269",
            "extra": "mean: 9.617704763200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7134211482425891,
            "unit": "iter/sec",
            "range": "stddev: 0.033815456119031986",
            "extra": "mean: 1.4016966030000049 sec\nrounds: 5"
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
          "id": "cd6a3ebae474bcf7a799cfff8e874ac09a665143",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/cd6a3ebae474bcf7a799cfff8e874ac09a665143"
        },
        "date": 1615825755682,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.056284744775434256,
            "unit": "iter/sec",
            "range": "stddev: 0.13633726838743748",
            "extra": "mean: 17.766803491599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09695102565465843,
            "unit": "iter/sec",
            "range": "stddev: 0.03570248685813795",
            "extra": "mean: 10.314486033000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6647724112421856,
            "unit": "iter/sec",
            "range": "stddev: 0.037008820122587396",
            "extra": "mean: 1.5042742194000085 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05667043220323906,
            "unit": "iter/sec",
            "range": "stddev: 0.07022528049289088",
            "extra": "mean: 17.645886242999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09712008118418641,
            "unit": "iter/sec",
            "range": "stddev: 0.022448900958963944",
            "extra": "mean: 10.296531755399986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6593946083989257,
            "unit": "iter/sec",
            "range": "stddev: 0.029752628212355296",
            "extra": "mean: 1.5165425789999971 sec\nrounds: 5"
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
          "id": "1d554de6476b492d4925b4b353441f52fe01cd97",
          "message": "Dpc/new/dask tutorial",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/325/commits/1d554de6476b492d4925b4b353441f52fe01cd97"
        },
        "date": 1615961208789,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0586799760252541,
            "unit": "iter/sec",
            "range": "stddev: 0.08215117578178577",
            "extra": "mean: 17.0415884214 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07664960688604598,
            "unit": "iter/sec",
            "range": "stddev: 0.132406038494498",
            "extra": "mean: 13.046381326999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6622081890729975,
            "unit": "iter/sec",
            "range": "stddev: 0.039858008622166395",
            "extra": "mean: 1.5100991145999956 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05869726114250465,
            "unit": "iter/sec",
            "range": "stddev: 0.09600352483399967",
            "extra": "mean: 17.03657002960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07621238637184935,
            "unit": "iter/sec",
            "range": "stddev: 0.05454195473058944",
            "extra": "mean: 13.121226714000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6716595156481909,
            "unit": "iter/sec",
            "range": "stddev: 0.04266669761910801",
            "extra": "mean: 1.4888495981999768 sec\nrounds: 5"
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
          "id": "7987afec5b642c75908ff504fdb2e436c1467e8b",
          "message": "Dpc/new/dask tutorial",
          "timestamp": "2021-03-09T13:11:57Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/325/commits/7987afec5b642c75908ff504fdb2e436c1467e8b"
        },
        "date": 1615966594244,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07403790634293832,
            "unit": "iter/sec",
            "range": "stddev: 0.2400717808758288",
            "extra": "mean: 13.50659478899999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0805240798445966,
            "unit": "iter/sec",
            "range": "stddev: 0.28803492911138895",
            "extra": "mean: 12.41864547759999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7365408321517866,
            "unit": "iter/sec",
            "range": "stddev: 0.02979674599643236",
            "extra": "mean: 1.3576979800000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07484794918903884,
            "unit": "iter/sec",
            "range": "stddev: 0.25062202334988254",
            "extra": "mean: 13.360419501599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08191594672853704,
            "unit": "iter/sec",
            "range": "stddev: 0.056098069296232435",
            "extra": "mean: 12.207635264399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7575334635642602,
            "unit": "iter/sec",
            "range": "stddev: 0.03429652189269368",
            "extra": "mean: 1.3200736972000073 sec\nrounds: 5"
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
          "id": "189c26992bcabe8a5e71ece637b04e40ec9a998c",
          "message": "Merge pull request #325 from UCL-CCS/dpc/new/dask-tutorial\n\nDpc/new/dask tutorial",
          "timestamp": "2021-03-17T09:46:50+01:00",
          "tree_id": "a332bad7721ade4c667dac80ccbe01fbcd52dbc0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/189c26992bcabe8a5e71ece637b04e40ec9a998c"
        },
        "date": 1615971304355,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06244323075458417,
            "unit": "iter/sec",
            "range": "stddev: 0.409982420176776",
            "extra": "mean: 16.01454613919999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08083670241205786,
            "unit": "iter/sec",
            "range": "stddev: 0.22401327446467548",
            "extra": "mean: 12.3706184216 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.7130826242026673,
            "unit": "iter/sec",
            "range": "stddev: 0.0410289952159203",
            "extra": "mean: 1.40236203500001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06168575932934558,
            "unit": "iter/sec",
            "range": "stddev: 0.47315269537148924",
            "extra": "mean: 16.2111970554 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0830935366429861,
            "unit": "iter/sec",
            "range": "stddev: 0.23272916537915775",
            "extra": "mean: 12.0346303744 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.7179253563630772,
            "unit": "iter/sec",
            "range": "stddev: 0.06701086307167453",
            "extra": "mean: 1.3929024670000216 sec\nrounds: 5"
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
          "id": "653e5f846a3ee401dd84bda7611868796439afd2",
          "message": "missed a '%matplotlib inline' needed for binder",
          "timestamp": "2021-03-17T08:46:54Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/326/commits/653e5f846a3ee401dd84bda7611868796439afd2"
        },
        "date": 1615974132180,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08658802195472703,
            "unit": "iter/sec",
            "range": "stddev: 0.06831477810290762",
            "extra": "mean: 11.548941498200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.10118211700904078,
            "unit": "iter/sec",
            "range": "stddev: 0.05614106024117175",
            "extra": "mean: 9.883169373800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.856634187126193,
            "unit": "iter/sec",
            "range": "stddev: 0.039114989202507874",
            "extra": "mean: 1.1673594341999887 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08674482031722212,
            "unit": "iter/sec",
            "range": "stddev: 0.07417144511682094",
            "extra": "mean: 11.528065841199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.101089247547836,
            "unit": "iter/sec",
            "range": "stddev: 0.0509670648937696",
            "extra": "mean: 9.892248921199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.8496648858390287,
            "unit": "iter/sec",
            "range": "stddev: 0.037560872244615594",
            "extra": "mean: 1.1769345969999905 sec\nrounds: 5"
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
          "id": "4d95f4e99cdbb7d2753c1926e1ab6b211995d4d9",
          "message": "Merge pull request #326 from UCL-CCS/dpc/fix/dask-tutorial\n\nmissed a '%matplotlib inline' needed for binder",
          "timestamp": "2021-03-17T10:45:11+01:00",
          "tree_id": "8b1835bf6265a8e4afbfdab3649ac98be84deed8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4d95f4e99cdbb7d2753c1926e1ab6b211995d4d9"
        },
        "date": 1615974807122,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0694130554269488,
            "unit": "iter/sec",
            "range": "stddev: 0.08103651280721588",
            "extra": "mean: 14.406511769999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07440692010294611,
            "unit": "iter/sec",
            "range": "stddev: 0.05380124380142817",
            "extra": "mean: 13.439610168200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6814333517489433,
            "unit": "iter/sec",
            "range": "stddev: 0.04087488854863495",
            "extra": "mean: 1.4674949464000178 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06946342528102312,
            "unit": "iter/sec",
            "range": "stddev: 0.04855515602899678",
            "extra": "mean: 14.396065209199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07444492582738714,
            "unit": "iter/sec",
            "range": "stddev: 0.05782988209878779",
            "extra": "mean: 13.43274896019999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6821401848211543,
            "unit": "iter/sec",
            "range": "stddev: 0.0395553719668982",
            "extra": "mean: 1.4659743294000236 sec\nrounds: 5"
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
          "id": "11b28094fcf247ae9111eb7248f0ec3901356b5c",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/11b28094fcf247ae9111eb7248f0ec3901356b5c"
        },
        "date": 1615978706824,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.067655500145203,
            "unit": "iter/sec",
            "range": "stddev: 0.06959361410927244",
            "extra": "mean: 14.7807642816 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07642778914587595,
            "unit": "iter/sec",
            "range": "stddev: 0.04255289876432442",
            "extra": "mean: 13.084246073000008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6854073802171545,
            "unit": "iter/sec",
            "range": "stddev: 0.03899906117194955",
            "extra": "mean: 1.4589863325999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06774263483405239,
            "unit": "iter/sec",
            "range": "stddev: 0.061352581691731085",
            "extra": "mean: 14.76175236539998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07624354731790542,
            "unit": "iter/sec",
            "range": "stddev: 0.10309705205126755",
            "extra": "mean: 13.115864032799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6830032690484397,
            "unit": "iter/sec",
            "range": "stddev: 0.039725391729538546",
            "extra": "mean: 1.4641218355999968 sec\nrounds: 5"
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
          "id": "30f2ef8357265d74cca9f11b7d1f469f71dbf7d4",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/30f2ef8357265d74cca9f11b7d1f469f71dbf7d4"
        },
        "date": 1615980617873,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05316983914225507,
            "unit": "iter/sec",
            "range": "stddev: 0.07174345754952562",
            "extra": "mean: 18.8076551694 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06817835334612488,
            "unit": "iter/sec",
            "range": "stddev: 0.25790875499216676",
            "extra": "mean: 14.6674120292 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6105707740286432,
            "unit": "iter/sec",
            "range": "stddev: 0.05431015427020895",
            "extra": "mean: 1.637811769799987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053972000530175514,
            "unit": "iter/sec",
            "range": "stddev: 0.12541624161857862",
            "extra": "mean: 18.5281255128 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06893680677004156,
            "unit": "iter/sec",
            "range": "stddev: 0.15011195099545047",
            "extra": "mean: 14.506038890599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.5962450174978892,
            "unit": "iter/sec",
            "range": "stddev: 0.04538094957040949",
            "extra": "mean: 1.677162862 sec\nrounds: 5"
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
          "id": "f958472164069d30246ba596041ae65fc5721d1b",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/f958472164069d30246ba596041ae65fc5721d1b"
        },
        "date": 1615981109311,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07221364801103136,
            "unit": "iter/sec",
            "range": "stddev: 0.1541221531577032",
            "extra": "mean: 13.847797854600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07871424126882913,
            "unit": "iter/sec",
            "range": "stddev: 0.2068385808014812",
            "extra": "mean: 12.704181402 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.625532891391991,
            "unit": "iter/sec",
            "range": "stddev: 0.06999034163593264",
            "extra": "mean: 1.5986369601999855 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07267169668519552,
            "unit": "iter/sec",
            "range": "stddev: 0.24204505585550473",
            "extra": "mean: 13.760515381000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07840100170057156,
            "unit": "iter/sec",
            "range": "stddev: 0.20192373647695366",
            "extra": "mean: 12.754939073599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.6226861121065052,
            "unit": "iter/sec",
            "range": "stddev: 0.05799526776597753",
            "extra": "mean: 1.6059455648000038 sec\nrounds: 5"
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
          "id": "388df98b3a3811045b1100e914115ac9619fd9aa",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/388df98b3a3811045b1100e914115ac9619fd9aa"
        },
        "date": 1615981280418,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055587526615254394,
            "unit": "iter/sec",
            "range": "stddev: 0.08993823985871813",
            "extra": "mean: 17.989647334399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0755359672541634,
            "unit": "iter/sec",
            "range": "stddev: 0.031804319774940464",
            "extra": "mean: 13.238726349199982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 0.6642742470066967,
            "unit": "iter/sec",
            "range": "stddev: 0.035600734121391885",
            "extra": "mean: 1.5054023311999913 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05574791518137926,
            "unit": "iter/sec",
            "range": "stddev: 0.04721649382368098",
            "extra": "mean: 17.937890533600022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07549262560798362,
            "unit": "iter/sec",
            "range": "stddev: 0.04270019997640571",
            "extra": "mean: 13.246326935199965 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 0.670553159519809,
            "unit": "iter/sec",
            "range": "stddev: 0.038352627562835015",
            "extra": "mean: 1.4913060743999949 sec\nrounds: 5"
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
          "id": "ccc12d4226ff7475abb031d9f1b0f06a31966f26",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/ccc12d4226ff7475abb031d9f1b0f06a31966f26"
        },
        "date": 1616679576301,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05331172262276957,
            "unit": "iter/sec",
            "range": "stddev: 0.10039975406902546",
            "extra": "mean: 18.757600595200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07239084026259104,
            "unit": "iter/sec",
            "range": "stddev: 0.1036986677560182",
            "extra": "mean: 13.81390237179998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.27694300535217,
            "unit": "iter/sec",
            "range": "stddev: 0.000821869987079031",
            "extra": "mean: 15.319344839999758 msec\nrounds: 50"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05323173476739994,
            "unit": "iter/sec",
            "range": "stddev: 0.03294438674725716",
            "extra": "mean: 18.785786417999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07261043990703718,
            "unit": "iter/sec",
            "range": "stddev: 0.05535628962876063",
            "extra": "mean: 13.772124246600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.32582452784367,
            "unit": "iter/sec",
            "range": "stddev: 0.0007923052132686848",
            "extra": "mean: 30.935019124992635 msec\nrounds: 32"
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
          "id": "353608e36b0e7eeb80e8ce3629f83e45971171ff",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/353608e36b0e7eeb80e8ce3629f83e45971171ff"
        },
        "date": 1616681049019,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06853192902447156,
            "unit": "iter/sec",
            "range": "stddev: 0.0464014261830099",
            "extra": "mean: 14.591738686399992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07532552233575678,
            "unit": "iter/sec",
            "range": "stddev: 0.04448945957245006",
            "extra": "mean: 13.2757127862 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.24353399331018,
            "unit": "iter/sec",
            "range": "stddev: 0.0003105623263663263",
            "extra": "mean: 15.56576884615551 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06880635233909177,
            "unit": "iter/sec",
            "range": "stddev: 0.06507843091418795",
            "extra": "mean: 14.533541831600019 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07533293394602086,
            "unit": "iter/sec",
            "range": "stddev: 0.14677128725981828",
            "extra": "mean: 13.2744066588 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.39510226378271,
            "unit": "iter/sec",
            "range": "stddev: 0.00027869970811568207",
            "extra": "mean: 29.944510787874098 msec\nrounds: 33"
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
          "id": "c3bff38960646dbce895735719caa6030696e110",
          "message": "The rework of the actions system",
          "timestamp": "2021-03-17T09:45:15Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/324/commits/c3bff38960646dbce895735719caa6030696e110"
        },
        "date": 1616681745381,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07720052724828247,
            "unit": "iter/sec",
            "range": "stddev: 0.0649019915650427",
            "extra": "mean: 12.953279409399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08552467430978564,
            "unit": "iter/sec",
            "range": "stddev: 0.16879304644801743",
            "extra": "mean: 11.692532103400026 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.07926077004807,
            "unit": "iter/sec",
            "range": "stddev: 0.0005424413609719867",
            "extra": "mean: 13.683772789473199 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07750826331182084,
            "unit": "iter/sec",
            "range": "stddev: 0.063755024916422",
            "extra": "mean: 12.901850167599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0852560056055249,
            "unit": "iter/sec",
            "range": "stddev: 0.11322704572237376",
            "extra": "mean: 11.729378979199987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.11522806805369,
            "unit": "iter/sec",
            "range": "stddev: 0.001101300210972915",
            "extra": "mean: 26.943118823530366 msec\nrounds: 34"
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
          "id": "5d503eb182602c20da81b281b15e65577f0d48c9",
          "message": "Merge pull request #324 from UCL-CCS/actions-rework\n\nThe rework of the actions system",
          "timestamp": "2021-03-26T13:21:34+01:00",
          "tree_id": "c113d26a1ca9db094c49393a5d582638a1b03047",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5d503eb182602c20da81b281b15e65577f0d48c9"
        },
        "date": 1616761714330,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07670923579020951,
            "unit": "iter/sec",
            "range": "stddev: 0.3561066538107395",
            "extra": "mean: 13.036239895999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0842368012701512,
            "unit": "iter/sec",
            "range": "stddev: 0.2143674565234333",
            "extra": "mean: 11.871295976600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.13368383710932,
            "unit": "iter/sec",
            "range": "stddev: 0.0007933685599161141",
            "extra": "mean: 13.67358989090855 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07767942296000492,
            "unit": "iter/sec",
            "range": "stddev: 0.18408049993266146",
            "extra": "mean: 12.873422096799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08495139489061485,
            "unit": "iter/sec",
            "range": "stddev: 0.21610459689437012",
            "extra": "mean: 11.77143708220001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.22741164922884,
            "unit": "iter/sec",
            "range": "stddev: 0.0012739256296989039",
            "extra": "mean: 26.15923906059627 msec\nrounds: 33"
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
          "id": "94f685b1d8f204c96978d28577f22822d96f8163",
          "message": "Merge pull request #327 from UCL-CCS/actions-rework\n\nadded execute_local helper function",
          "timestamp": "2021-03-29T11:31:29+02:00",
          "tree_id": "f38089571bdf36ef72fb44c016bc50e17db0fd58",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/94f685b1d8f204c96978d28577f22822d96f8163"
        },
        "date": 1617010760625,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06675200881712055,
            "unit": "iter/sec",
            "range": "stddev: 0.11797821095968264",
            "extra": "mean: 14.980822565799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07471017277745298,
            "unit": "iter/sec",
            "range": "stddev: 0.08382747108342292",
            "extra": "mean: 13.385058056000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 62.90841150682192,
            "unit": "iter/sec",
            "range": "stddev: 0.0007504257288226671",
            "extra": "mean: 15.896125431359174 msec\nrounds: 51"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06705854789012615,
            "unit": "iter/sec",
            "range": "stddev: 0.05353244159494118",
            "extra": "mean: 14.912341997600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07836959614930679,
            "unit": "iter/sec",
            "range": "stddev: 0.12316738982717818",
            "extra": "mean: 12.760050442200031 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.64325542150838,
            "unit": "iter/sec",
            "range": "stddev: 0.0013668166675925549",
            "extra": "mean: 30.634199533331717 msec\nrounds: 30"
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
          "id": "f1771c490aa98a980719179e512061fa04f4f6d2",
          "message": "added execute_local helper function",
          "timestamp": "2021-03-26T12:21:43Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/327/commits/f1771c490aa98a980719179e512061fa04f4f6d2"
        },
        "date": 1617010769693,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06845240696930734,
            "unit": "iter/sec",
            "range": "stddev: 0.02550024705725329",
            "extra": "mean: 14.608690099799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07578656135452924,
            "unit": "iter/sec",
            "range": "stddev: 0.09493402704748266",
            "extra": "mean: 13.194951481199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 61.46136727383862,
            "unit": "iter/sec",
            "range": "stddev: 0.00017646971350112497",
            "extra": "mean: 16.270383240004094 msec\nrounds: 50"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06817110876556888,
            "unit": "iter/sec",
            "range": "stddev: 0.06645578141683381",
            "extra": "mean: 14.668970742999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0758039341324376,
            "unit": "iter/sec",
            "range": "stddev: 0.0366028712005991",
            "extra": "mean: 13.191927456599979 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.98563668487766,
            "unit": "iter/sec",
            "range": "stddev: 0.00017073371784697352",
            "extra": "mean: 30.316225500005345 msec\nrounds: 32"
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
          "id": "f8628e566168f127dff7d41bac79e24fa0c2764e",
          "message": "Merge pull request #328 from UCL-CCS/actions-rework\n\nchanges",
          "timestamp": "2021-03-29T14:59:40+02:00",
          "tree_id": "901553a102d7c0049765b3c96b1fd22017f02069",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f8628e566168f127dff7d41bac79e24fa0c2764e"
        },
        "date": 1617023245919,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06821095217024518,
            "unit": "iter/sec",
            "range": "stddev: 0.2359717878974059",
            "extra": "mean: 14.660402298800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07733200978769587,
            "unit": "iter/sec",
            "range": "stddev: 0.04094118426895874",
            "extra": "mean: 12.931255798799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.46228649682428,
            "unit": "iter/sec",
            "range": "stddev: 0.00024194874408321697",
            "extra": "mean: 15.275971150939132 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06896186610436518,
            "unit": "iter/sec",
            "range": "stddev: 0.061598171884455",
            "extra": "mean: 14.500767692199986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0771093915330259,
            "unit": "iter/sec",
            "range": "stddev: 0.047251110127068625",
            "extra": "mean: 12.96858891139999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.68960980049931,
            "unit": "iter/sec",
            "range": "stddev: 0.00037498723298561715",
            "extra": "mean: 29.68274212499722 msec\nrounds: 32"
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
          "id": "43eb2b3a04b2b7f88c8a2db3bf4c37c0c1c40792",
          "message": "changes",
          "timestamp": "2021-03-29T09:31:32Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/328/commits/43eb2b3a04b2b7f88c8a2db3bf4c37c0c1c40792"
        },
        "date": 1617023302473,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05593658858941514,
            "unit": "iter/sec",
            "range": "stddev: 0.16666986847960483",
            "extra": "mean: 17.877386254999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07681913610314574,
            "unit": "iter/sec",
            "range": "stddev: 0.08299059764407123",
            "extra": "mean: 13.017589766400016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 67.058471687528,
            "unit": "iter/sec",
            "range": "stddev: 0.00043664424125165806",
            "extra": "mean: 14.912358943396363 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05274597617944588,
            "unit": "iter/sec",
            "range": "stddev: 0.15695094869421103",
            "extra": "mean: 18.95879216640001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07339687369672512,
            "unit": "iter/sec",
            "range": "stddev: 0.08762269778580303",
            "extra": "mean: 13.624558508200039 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.28325423955464,
            "unit": "iter/sec",
            "range": "stddev: 0.0014925155657285834",
            "extra": "mean: 30.045139000007264 msec\nrounds: 30"
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
          "id": "d849b676f06983e8a58ab78367fa88f4b5e270d4",
          "message": "added test_actions_action_statuses.py",
          "timestamp": "2021-03-29T15:02:14+02:00",
          "tree_id": "ecc55cdcb29c43c13270834bea371ff305c578b7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d849b676f06983e8a58ab78367fa88f4b5e270d4"
        },
        "date": 1617023419084,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06819509805814546,
            "unit": "iter/sec",
            "range": "stddev: 0.04564495646959287",
            "extra": "mean: 14.663810573999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07285194719235645,
            "unit": "iter/sec",
            "range": "stddev: 0.028467836451127163",
            "extra": "mean: 13.726469072400016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.47502738372173,
            "unit": "iter/sec",
            "range": "stddev: 0.00025643452881776594",
            "extra": "mean: 15.75422715384998 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06844899395575808,
            "unit": "iter/sec",
            "range": "stddev: 0.06055156429902301",
            "extra": "mean: 14.609418520400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07252915775673562,
            "unit": "iter/sec",
            "range": "stddev: 0.03604970731371063",
            "extra": "mean: 13.78755842380001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.88866748328362,
            "unit": "iter/sec",
            "range": "stddev: 0.0002886797726084754",
            "extra": "mean: 30.40561009375864 msec\nrounds: 32"
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
          "id": "0ab92a821f317297259410d410e7397c0a91ee4e",
          "message": "remove unused imports in sampling/base",
          "timestamp": "2021-03-29T15:52:19+02:00",
          "tree_id": "d5821df3a576e4daa8723f34dcb5382b1fdca16f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0ab92a821f317297259410d410e7397c0a91ee4e"
        },
        "date": 1617026494002,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053119485286262105,
            "unit": "iter/sec",
            "range": "stddev: 0.33582190733591005",
            "extra": "mean: 18.825483617000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06630930931251897,
            "unit": "iter/sec",
            "range": "stddev: 0.18126655205115288",
            "extra": "mean: 15.0808387294 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 61.382900001696086,
            "unit": "iter/sec",
            "range": "stddev: 0.001208717751717687",
            "extra": "mean: 16.29118207142981 msec\nrounds: 42"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05362229613355603,
            "unit": "iter/sec",
            "range": "stddev: 0.17249809714070943",
            "extra": "mean: 18.6489589612 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06957924439369154,
            "unit": "iter/sec",
            "range": "stddev: 0.36621800387565495",
            "extra": "mean: 14.372102035800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 31.365946733821556,
            "unit": "iter/sec",
            "range": "stddev: 0.00220052266186674",
            "extra": "mean: 31.881709437506345 msec\nrounds: 32"
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
          "id": "2977ce3f40a8366e26c0b14a75c3ded2d574e620",
          "message": "fix db_benchmark.py script",
          "timestamp": "2021-03-29T17:34:52+02:00",
          "tree_id": "de3d441bc09ea180901d4f074709f14568dd97a8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/2977ce3f40a8366e26c0b14a75c3ded2d574e620"
        },
        "date": 1617032605166,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05790646631319982,
            "unit": "iter/sec",
            "range": "stddev: 0.3354031275249731",
            "extra": "mean: 17.269228527800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07449667074111024,
            "unit": "iter/sec",
            "range": "stddev: 0.21281720569464377",
            "extra": "mean: 13.423418658199983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.04276114608732,
            "unit": "iter/sec",
            "range": "stddev: 0.0010762193755245722",
            "extra": "mean: 13.690610600001492 msec\nrounds: 50"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.057468890300874674,
            "unit": "iter/sec",
            "range": "stddev: 0.21042227034548802",
            "extra": "mean: 17.400718802200014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07432715963055418,
            "unit": "iter/sec",
            "range": "stddev: 0.1676172538036183",
            "extra": "mean: 13.454032213400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.25145550350215,
            "unit": "iter/sec",
            "range": "stddev: 0.0035634465236146972",
            "extra": "mean: 30.073871499991235 msec\nrounds: 34"
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
          "id": "bc90de85c6975efbca13e691ebc5c06cf60a9ef1",
          "message": "exclude db_benchmark from coveralls report",
          "timestamp": "2021-03-29T17:38:02+02:00",
          "tree_id": "3ff7ba750ba6c4047a0fe80d4b949e53a4444af6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bc90de85c6975efbca13e691ebc5c06cf60a9ef1"
        },
        "date": 1617032822797,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05577924911919902,
            "unit": "iter/sec",
            "range": "stddev: 0.13683843688128428",
            "extra": "mean: 17.9278139414 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0710897782629626,
            "unit": "iter/sec",
            "range": "stddev: 0.11528046914411332",
            "extra": "mean: 14.066719920000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 67.75991712724549,
            "unit": "iter/sec",
            "range": "stddev: 0.001154312957147611",
            "extra": "mean: 14.757987352937768 msec\nrounds: 51"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.055417497635118294,
            "unit": "iter/sec",
            "range": "stddev: 0.14533889766874444",
            "extra": "mean: 18.044842200999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0717280042182316,
            "unit": "iter/sec",
            "range": "stddev: 0.068905855032869",
            "extra": "mean: 13.941556173199967 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.35622842938644,
            "unit": "iter/sec",
            "range": "stddev: 0.0013685096447359102",
            "extra": "mean: 29.106803794116544 msec\nrounds: 34"
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
          "id": "aa55256c78ba65a51881b1bb005da4ae2bd7edd5",
          "message": "rework execute signature, get rid of unused import",
          "timestamp": "2021-03-30T15:12:22+02:00",
          "tree_id": "4cc1a738a7735438a4e933fb01f72003739193b5",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/aa55256c78ba65a51881b1bb005da4ae2bd7edd5"
        },
        "date": 1617110422644,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06856129729344462,
            "unit": "iter/sec",
            "range": "stddev: 0.03742931399330716",
            "extra": "mean: 14.585488307200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07579353835948875,
            "unit": "iter/sec",
            "range": "stddev: 0.05188550996247394",
            "extra": "mean: 13.193736849400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 61.145054662541824,
            "unit": "iter/sec",
            "range": "stddev: 0.00033356158719787313",
            "extra": "mean: 16.35455239215955 msec\nrounds: 51"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06855281965829489,
            "unit": "iter/sec",
            "range": "stddev: 0.07191905455479114",
            "extra": "mean: 14.587292032400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07582502971319954,
            "unit": "iter/sec",
            "range": "stddev: 0.05028217941684767",
            "extra": "mean: 13.188257278399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.399469715454366,
            "unit": "iter/sec",
            "range": "stddev: 0.0003776377508208026",
            "extra": "mean: 30.864702687495083 msec\nrounds: 32"
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
          "id": "abae9b926200ee1757994458d6a1e6b9c1a8ed96",
          "message": "remove unused import in sql.py",
          "timestamp": "2021-03-30T15:15:19+02:00",
          "tree_id": "fe55341b58c66f760174cec77776a1a4ddb5f383",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/abae9b926200ee1757994458d6a1e6b9c1a8ed96"
        },
        "date": 1617110611225,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06590406845020307,
            "unit": "iter/sec",
            "range": "stddev: 0.07442547192209273",
            "extra": "mean: 15.173570062 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07228640527319304,
            "unit": "iter/sec",
            "range": "stddev: 0.04672000811435757",
            "extra": "mean: 13.833859855399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 62.75772644918261,
            "unit": "iter/sec",
            "range": "stddev: 0.00023558971039755737",
            "extra": "mean: 15.934292980000466 msec\nrounds: 50"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0661002872499229,
            "unit": "iter/sec",
            "range": "stddev: 0.04540948628996172",
            "extra": "mean: 15.128527297000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07211403114527136,
            "unit": "iter/sec",
            "range": "stddev: 0.036262336091573144",
            "extra": "mean: 13.866926922799985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.37954975655371,
            "unit": "iter/sec",
            "range": "stddev: 0.0002775430526990806",
            "extra": "mean: 30.883690709676937 msec\nrounds: 31"
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
          "id": "1f4c564036a2903ed319a36cc9b25b28a4a89dff",
          "message": "remove unused import in encoders/base.py",
          "timestamp": "2021-03-30T15:15:56+02:00",
          "tree_id": "3b19f9259e950ccfba1ff122e0b760140a7a7992",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1f4c564036a2903ed319a36cc9b25b28a4a89dff"
        },
        "date": 1617110619974,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07042141506344331,
            "unit": "iter/sec",
            "range": "stddev: 0.30872080096373977",
            "extra": "mean: 14.200225870200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07710382019787139,
            "unit": "iter/sec",
            "range": "stddev: 0.15727542026186697",
            "extra": "mean: 12.969525990199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.81403820607636,
            "unit": "iter/sec",
            "range": "stddev: 0.0005217027586967048",
            "extra": "mean: 15.670533132077828 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0686791259011681,
            "unit": "iter/sec",
            "range": "stddev: 0.14420587931758425",
            "extra": "mean: 14.560464870199985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07642029607935155,
            "unit": "iter/sec",
            "range": "stddev: 0.044961701082209767",
            "extra": "mean: 13.085528993000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.44537510082251,
            "unit": "iter/sec",
            "range": "stddev: 0.0001936497740657954",
            "extra": "mean: 30.821033718751778 msec\nrounds: 32"
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
          "id": "19a8582098d415b94ae843a1341154dc81949238",
          "message": "remove unused import in pce_analysis",
          "timestamp": "2021-03-30T15:17:02+02:00",
          "tree_id": "2ae6b7c16478605578b2f8a4987a6d6454b21200",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/19a8582098d415b94ae843a1341154dc81949238"
        },
        "date": 1617110686220,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06996720462956646,
            "unit": "iter/sec",
            "range": "stddev: 0.07729083896542621",
            "extra": "mean: 14.292410355600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07663748317412844,
            "unit": "iter/sec",
            "range": "stddev: 0.119445184776352",
            "extra": "mean: 13.04844520700001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.48886345559144,
            "unit": "iter/sec",
            "range": "stddev: 0.0002695841731349491",
            "extra": "mean: 15.750793849057795 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0689900967171107,
            "unit": "iter/sec",
            "range": "stddev: 0.09848162180280308",
            "extra": "mean: 14.49483400639998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07617005229215532,
            "unit": "iter/sec",
            "range": "stddev: 0.22918428676224556",
            "extra": "mean: 13.128519279000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.48264747488181,
            "unit": "iter/sec",
            "range": "stddev: 0.0005122707153257805",
            "extra": "mean: 29.86621654545643 msec\nrounds: 33"
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
          "id": "6682c01593aca6f878c4b6ee8e920994b9714929",
          "message": "fix executor",
          "timestamp": "2021-03-30T15:59:49+02:00",
          "tree_id": "16e3f1f5f4b12b7f2fc1bef184a3d641e4a7c24d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/6682c01593aca6f878c4b6ee8e920994b9714929"
        },
        "date": 1617113232549,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07346844242843684,
            "unit": "iter/sec",
            "range": "stddev: 0.21460929318660668",
            "extra": "mean: 13.6112862468 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08089200620765169,
            "unit": "iter/sec",
            "range": "stddev: 0.06232134803397554",
            "extra": "mean: 12.362160946200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.30414120812932,
            "unit": "iter/sec",
            "range": "stddev: 0.000586916096161487",
            "extra": "mean: 14.22391316949007 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07406154288076838,
            "unit": "iter/sec",
            "range": "stddev: 0.12560250917570412",
            "extra": "mean: 13.502284196400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08013943315210266,
            "unit": "iter/sec",
            "range": "stddev: 0.0884959562701723",
            "extra": "mean: 12.478251475799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.38696851219074,
            "unit": "iter/sec",
            "range": "stddev: 0.0009326025001089058",
            "extra": "mean: 29.080783891882874 msec\nrounds: 37"
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
          "id": "e868ffb8d1b59de1dc177cdd10b1b40ffad167fc",
          "message": "added encoder_decoder_tutorial",
          "timestamp": "2021-03-30T13:59:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/316/commits/e868ffb8d1b59de1dc177cdd10b1b40ffad167fc"
        },
        "date": 1617279197306,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07257358921526563,
            "unit": "iter/sec",
            "range": "stddev: 0.1902528750220166",
            "extra": "mean: 13.779117318200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09090608140872243,
            "unit": "iter/sec",
            "range": "stddev: 0.125596392757675",
            "extra": "mean: 11.000364161599975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 66.16756728674979,
            "unit": "iter/sec",
            "range": "stddev: 0.0005502976626647638",
            "extra": "mean: 15.113144415092505 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08232137616086575,
            "unit": "iter/sec",
            "range": "stddev: 0.1313728930328539",
            "extra": "mean: 12.147513156800017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09159457825619098,
            "unit": "iter/sec",
            "range": "stddev: 0.4636292678736904",
            "extra": "mean: 10.917676777799988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.74869182387765,
            "unit": "iter/sec",
            "range": "stddev: 0.000834901092513317",
            "extra": "mean: 27.973051571416363 msec\nrounds: 35"
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
          "id": "d100205235719a1e5b457d200070a0be0e2d2491",
          "message": "Merge pull request #316 from UCL-CCS/encoder-decoder-tutorial\n\nadded encoder_decoder_tutorial",
          "timestamp": "2021-04-01T14:13:06+02:00",
          "tree_id": "5c4b6116a2d7caef96437df88e089c4f0cae3a0f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d100205235719a1e5b457d200070a0be0e2d2491"
        },
        "date": 1617279721268,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053984534871649725,
            "unit": "iter/sec",
            "range": "stddev: 0.052288933871241096",
            "extra": "mean: 18.523823579799988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07475068775148416,
            "unit": "iter/sec",
            "range": "stddev: 0.1101044387693359",
            "extra": "mean: 13.377803336400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.1050049433525,
            "unit": "iter/sec",
            "range": "stddev: 0.0008679953035881184",
            "extra": "mean: 15.599406019602798 msec\nrounds: 51"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.054899401921812245,
            "unit": "iter/sec",
            "range": "stddev: 0.10529570449056794",
            "extra": "mean: 18.215134682600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07404388231468015,
            "unit": "iter/sec",
            "range": "stddev: 0.02989722935930766",
            "extra": "mean: 13.505504691800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.26233169868986,
            "unit": "iter/sec",
            "range": "stddev: 0.0008671785768228042",
            "extra": "mean: 30.064037874993232 msec\nrounds: 32"
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
          "id": "a6598d5ed9f980ae33cc5a7b1b8623679ae3df2b",
          "message": "Actions tweak",
          "timestamp": "2021-04-01T12:13:09Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/329/commits/a6598d5ed9f980ae33cc5a7b1b8623679ae3df2b"
        },
        "date": 1617283998854,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06834379657084694,
            "unit": "iter/sec",
            "range": "stddev: 0.0750980228639547",
            "extra": "mean: 14.631905896000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07644064179280938,
            "unit": "iter/sec",
            "range": "stddev: 0.06037825053593152",
            "extra": "mean: 13.082046101999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 59.51277370695788,
            "unit": "iter/sec",
            "range": "stddev: 0.0003870364177241609",
            "extra": "mean: 16.803115326535114 msec\nrounds: 49"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06833099692250946,
            "unit": "iter/sec",
            "range": "stddev: 0.0490686997544281",
            "extra": "mean: 14.63464672020001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07646571957647753,
            "unit": "iter/sec",
            "range": "stddev: 0.04283859975875293",
            "extra": "mean: 13.077755699399983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.1582202121408,
            "unit": "iter/sec",
            "range": "stddev: 0.00027078393999341245",
            "extra": "mean: 31.0962482812549 msec\nrounds: 32"
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
          "id": "bdd866c5d5d1f61140b776ec9ac47791b928a7cf",
          "message": "Merge pull request #329 from UCL-CCS/actions-tweak\n\nActions tweak",
          "timestamp": "2021-04-01T15:25:33+02:00",
          "tree_id": "f6f17602465463b3451a2ef9398c91c2b934c9c6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bdd866c5d5d1f61140b776ec9ac47791b928a7cf"
        },
        "date": 1617284009040,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06182656309236346,
            "unit": "iter/sec",
            "range": "stddev: 0.8356442572662944",
            "extra": "mean: 16.174277688800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0818413550974361,
            "unit": "iter/sec",
            "range": "stddev: 0.7756316749796424",
            "extra": "mean: 12.218761514999983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.51482957932147,
            "unit": "iter/sec",
            "range": "stddev: 0.0011776221564100057",
            "extra": "mean: 12.267706442628423 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0611874285275032,
            "unit": "iter/sec",
            "range": "stddev: 0.7781592133052961",
            "extra": "mean: 16.343226444799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07885862726921332,
            "unit": "iter/sec",
            "range": "stddev: 0.9090120219616384",
            "extra": "mean: 12.680920713799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 30.486232894201496,
            "unit": "iter/sec",
            "range": "stddev: 0.003906173722327369",
            "extra": "mean: 32.801691290307005 msec\nrounds: 31"
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
          "id": "dc53dc7c756e190ebb8d582e36a88a09b152c87b",
          "message": "Update README.md",
          "timestamp": "2021-04-01T17:50:08+02:00",
          "tree_id": "2485739b63c08ad4f1a0b3f75612e68ec8e0397e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/dc53dc7c756e190ebb8d582e36a88a09b152c87b"
        },
        "date": 1617292750786,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.052725264991093666,
            "unit": "iter/sec",
            "range": "stddev: 0.13234586539195126",
            "extra": "mean: 18.966239433199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07254604608478787,
            "unit": "iter/sec",
            "range": "stddev: 0.08291723601575479",
            "extra": "mean: 13.7843487546 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.57886818953824,
            "unit": "iter/sec",
            "range": "stddev: 0.0013924648115793837",
            "extra": "mean: 15.248814558826579 msec\nrounds: 34"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05271638513235251,
            "unit": "iter/sec",
            "range": "stddev: 0.1372825054008541",
            "extra": "mean: 18.96943421839999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07265455358669395,
            "unit": "iter/sec",
            "range": "stddev: 0.12363000133020251",
            "extra": "mean: 13.763762223200024 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 31.892436634090124,
            "unit": "iter/sec",
            "range": "stddev: 0.002171674239875388",
            "extra": "mean: 31.3553966250133 msec\nrounds: 32"
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
          "id": "5e3360c669247008758f9630d51d218fdd9cdc4c",
          "message": "fix a bug with pool passing",
          "timestamp": "2021-04-08T12:33:59+02:00",
          "tree_id": "fa798e6c676da182f44bbe8bb8297a83dce0546b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5e3360c669247008758f9630d51d218fdd9cdc4c"
        },
        "date": 1617878516851,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06846713796051664,
            "unit": "iter/sec",
            "range": "stddev: 0.12744917166727726",
            "extra": "mean: 14.605546979000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07271235201620417,
            "unit": "iter/sec",
            "range": "stddev: 0.024843678987030642",
            "extra": "mean: 13.752821525800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.0160802645763,
            "unit": "iter/sec",
            "range": "stddev: 0.0003992079094584567",
            "extra": "mean: 15.380810346157476 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06840260894286246,
            "unit": "iter/sec",
            "range": "stddev: 0.1462334674972688",
            "extra": "mean: 14.619325424200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07318925399637154,
            "unit": "iter/sec",
            "range": "stddev: 0.20177714093721735",
            "extra": "mean: 13.663207990199988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.49954185163327,
            "unit": "iter/sec",
            "range": "stddev: 0.0006673594223142368",
            "extra": "mean: 29.85115451515481 msec\nrounds: 33"
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
          "id": "af500d96821f7fd9c10d5dac438fc8f99e49adb9",
          "message": "patch up some things wrt dask support",
          "timestamp": "2021-04-08T12:53:41+02:00",
          "tree_id": "a1fee9d4bfb02bd1b566c4f416d9d9b4e8460e85",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/af500d96821f7fd9c10d5dac438fc8f99e49adb9"
        },
        "date": 1617879769148,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05173347812151542,
            "unit": "iter/sec",
            "range": "stddev: 0.19934200005949698",
            "extra": "mean: 19.329842807999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06954797119940034,
            "unit": "iter/sec",
            "range": "stddev: 0.07638588492845876",
            "extra": "mean: 14.37856464759999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 62.021233291727015,
            "unit": "iter/sec",
            "range": "stddev: 0.001760615035371246",
            "extra": "mean: 16.123510400000214 msec\nrounds: 50"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05093358734613644,
            "unit": "iter/sec",
            "range": "stddev: 0.5183500556277003",
            "extra": "mean: 19.633409938400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07377868158030731,
            "unit": "iter/sec",
            "range": "stddev: 0.8349111734438777",
            "extra": "mean: 13.554050825800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 31.645063023858217,
            "unit": "iter/sec",
            "range": "stddev: 0.0026710840293377265",
            "extra": "mean: 31.60050587499441 msec\nrounds: 32"
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
          "id": "bfae1d6722d296650adb9b694b3a08d6cb2f7e88",
          "message": "removed dask campaign",
          "timestamp": "2021-04-09T11:24:24+02:00",
          "tree_id": "3f206760c5bc087b58004a4539b9a31476394ef2",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bfae1d6722d296650adb9b694b3a08d6cb2f7e88"
        },
        "date": 1617960675842,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07660907951985474,
            "unit": "iter/sec",
            "range": "stddev: 0.11461523763110487",
            "extra": "mean: 13.053283060799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08648791863217054,
            "unit": "iter/sec",
            "range": "stddev: 0.03927473384630309",
            "extra": "mean: 11.562308537600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 68.94625715845517,
            "unit": "iter/sec",
            "range": "stddev: 0.0006016346688627022",
            "extra": "mean: 14.504050563640579 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07686426451016336,
            "unit": "iter/sec",
            "range": "stddev: 0.1249415499086057",
            "extra": "mean: 13.009946902800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08666897072115441,
            "unit": "iter/sec",
            "range": "stddev: 0.05944052951342174",
            "extra": "mean: 11.538154793800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.50340180525069,
            "unit": "iter/sec",
            "range": "stddev: 0.0010450422032843455",
            "extra": "mean: 27.394707083331582 msec\nrounds: 36"
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
          "id": "fdc31fe1f8e1726899bb27f9aa1990eebf36fa98",
          "message": "remove some obsolete stuff from base_element",
          "timestamp": "2021-04-09T13:38:39+02:00",
          "tree_id": "6f5abe7ed40495e79b36a98e7927fd8eaff725de",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/fdc31fe1f8e1726899bb27f9aa1990eebf36fa98"
        },
        "date": 1617968781629,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06903403840734758,
            "unit": "iter/sec",
            "range": "stddev: 0.06661540627919145",
            "extra": "mean: 14.485607724399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07648040940417385,
            "unit": "iter/sec",
            "range": "stddev: 0.04321080697994364",
            "extra": "mean: 13.075243814600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.26692704654303,
            "unit": "iter/sec",
            "range": "stddev: 0.0003008745710949462",
            "extra": "mean: 15.321695769235188 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0686460801345058,
            "unit": "iter/sec",
            "range": "stddev: 0.1278704431803201",
            "extra": "mean: 14.567474181200009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0756707893866925,
            "unit": "iter/sec",
            "range": "stddev: 0.04072267900041835",
            "extra": "mean: 13.215139000199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.31408348423375,
            "unit": "iter/sec",
            "range": "stddev: 0.00028855350116291356",
            "extra": "mean: 30.017334875001467 msec\nrounds: 32"
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
          "id": "02cde69dd62cbfc3ef4ec38fa7d64af28b322de8",
          "message": "removed unused method in analysis results",
          "timestamp": "2021-04-13T12:10:00+02:00",
          "tree_id": "d8738355561d098e1ad0d69af6560531a1d13367",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/02cde69dd62cbfc3ef4ec38fa7d64af28b322de8"
        },
        "date": 1618308962861,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08753494475461095,
            "unit": "iter/sec",
            "range": "stddev: 0.32861182711392084",
            "extra": "mean: 11.42400903780001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09849740842605859,
            "unit": "iter/sec",
            "range": "stddev: 0.11302229421205803",
            "extra": "mean: 10.152551381599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.8469277072411,
            "unit": "iter/sec",
            "range": "stddev: 0.0006467720529785308",
            "extra": "mean: 11.926495428569401 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0874550011999363,
            "unit": "iter/sec",
            "range": "stddev: 0.2929562772525075",
            "extra": "mean: 11.434451847000014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10338566836117052,
            "unit": "iter/sec",
            "range": "stddev: 0.15211561251940175",
            "extra": "mean: 9.672520532600037 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.66370899472803,
            "unit": "iter/sec",
            "range": "stddev: 0.00068954580789001",
            "extra": "mean: 22.902314599997453 msec\nrounds: 40"
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
          "id": "d9d39b2a8793632b37f5374ce88695a891010ad5",
          "message": "cleanup vector qoi tutorial",
          "timestamp": "2021-04-13T12:11:25+02:00",
          "tree_id": "f4180d5def22ae1d63e3290caf2904e632f4fec7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d9d39b2a8793632b37f5374ce88695a891010ad5"
        },
        "date": 1618309120775,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.072604408142008,
            "unit": "iter/sec",
            "range": "stddev: 0.16053552581534916",
            "extra": "mean: 13.773268395000008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08243257498845362,
            "unit": "iter/sec",
            "range": "stddev: 0.06150610404169688",
            "extra": "mean: 12.131126561799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 68.92059639542963,
            "unit": "iter/sec",
            "range": "stddev: 0.0004929306608648251",
            "extra": "mean: 14.509450763637233 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07273776471446422,
            "unit": "iter/sec",
            "range": "stddev: 0.11233792716082909",
            "extra": "mean: 13.748016644799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08242266763849172,
            "unit": "iter/sec",
            "range": "stddev: 0.068932700058189",
            "extra": "mean: 12.13258474459999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.57850987482623,
            "unit": "iter/sec",
            "range": "stddev: 0.0005609883331915758",
            "extra": "mean: 28.91969618181892 msec\nrounds: 33"
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
          "id": "b8f5d104aff8e89b8d6b85879cfa62e075e20bef",
          "message": "added supported_stats method",
          "timestamp": "2021-04-13T12:14:41+02:00",
          "tree_id": "8440724a02f7d31245568e011178956dc17a7832",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/b8f5d104aff8e89b8d6b85879cfa62e075e20bef"
        },
        "date": 1618309333045,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0690672426238767,
            "unit": "iter/sec",
            "range": "stddev: 0.110960270266437",
            "extra": "mean: 14.478643739200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07807055903998679,
            "unit": "iter/sec",
            "range": "stddev: 0.04138513165230347",
            "extra": "mean: 12.808925826799987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.64811907576156,
            "unit": "iter/sec",
            "range": "stddev: 0.0002742157969523452",
            "extra": "mean: 15.468354134605114 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06918681366878267,
            "unit": "iter/sec",
            "range": "stddev: 0.11780538229937546",
            "extra": "mean: 14.453621246200033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08226767573380227,
            "unit": "iter/sec",
            "range": "stddev: 0.0389269309735942",
            "extra": "mean: 12.155442475799987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.49114305815223,
            "unit": "iter/sec",
            "range": "stddev: 0.00040871462994551455",
            "extra": "mean: 29.858640484848586 msec\nrounds: 33"
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
          "id": "0a78fcc4e58c95ed14ba86c7aae1e5b49f5e0540",
          "message": "implemented supported_stats for all analysis methods",
          "timestamp": "2021-04-13T14:34:49+02:00",
          "tree_id": "b94bf8f77698094b69d5f7f9e1d5014c31e225ba",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0a78fcc4e58c95ed14ba86c7aae1e5b49f5e0540"
        },
        "date": 1618317816106,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05445232707072753,
            "unit": "iter/sec",
            "range": "stddev: 0.24373313195564458",
            "extra": "mean: 18.364688045399987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07191621490696466,
            "unit": "iter/sec",
            "range": "stddev: 0.0939648642903691",
            "extra": "mean: 13.905069966399969 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.40537036092495,
            "unit": "iter/sec",
            "range": "stddev: 0.0018925267767969873",
            "extra": "mean: 15.526655531922923 msec\nrounds: 47"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.054714965340314975,
            "unit": "iter/sec",
            "range": "stddev: 0.16824523844783565",
            "extra": "mean: 18.276535382600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07570995680673798,
            "unit": "iter/sec",
            "range": "stddev: 0.09645113496212585",
            "extra": "mean: 13.208302344599975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.78740215138139,
            "unit": "iter/sec",
            "range": "stddev: 0.0018595596601174594",
            "extra": "mean: 30.49951915625826 msec\nrounds: 32"
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
          "id": "0ef4191991bc1619b1825d98d0ca7cfe635559b0",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/0ef4191991bc1619b1825d98d0ca7cfe635559b0"
        },
        "date": 1618393441430,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06792953942935347,
            "unit": "iter/sec",
            "range": "stddev: 0.32080297277006264",
            "extra": "mean: 14.72113617140003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07784036915547855,
            "unit": "iter/sec",
            "range": "stddev: 0.14730850213513746",
            "extra": "mean: 12.846804438999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.896788544606906,
            "unit": "iter/sec",
            "range": "stddev: 0.00047764032210963144",
            "extra": "mean: 15.650238811327602 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07083869993215301,
            "unit": "iter/sec",
            "range": "stddev: 0.08233651428370325",
            "extra": "mean: 14.11657753400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08283593188397521,
            "unit": "iter/sec",
            "range": "stddev: 0.036210259708882496",
            "extra": "mean: 12.072055897199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.113946038005835,
            "unit": "iter/sec",
            "range": "stddev: 0.0007287285515548655",
            "extra": "mean: 29.31352470587586 msec\nrounds: 34"
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
          "id": "f54fb8baa4d57f17ce4a0d00c8852d9d2b830529",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/f54fb8baa4d57f17ce4a0d00c8852d9d2b830529"
        },
        "date": 1618397138856,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07057160153276575,
            "unit": "iter/sec",
            "range": "stddev: 0.1362736703392777",
            "extra": "mean: 14.17000575699999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07473078849897498,
            "unit": "iter/sec",
            "range": "stddev: 0.021575367277521813",
            "extra": "mean: 13.381365566800037 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.301224151470606,
            "unit": "iter/sec",
            "range": "stddev: 0.00033653127437017436",
            "extra": "mean: 15.797482803920914 msec\nrounds: 51"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07027583476648008,
            "unit": "iter/sec",
            "range": "stddev: 0.16527231367374096",
            "extra": "mean: 14.229642427199973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08026045503771796,
            "unit": "iter/sec",
            "range": "stddev: 0.1535768411412371",
            "extra": "mean: 12.459435964199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.04599728543657,
            "unit": "iter/sec",
            "range": "stddev: 0.00042540197314176466",
            "extra": "mean: 29.372028424256424 msec\nrounds: 33"
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
          "id": "bde78bb5971f1c2ec56adab08c5d136788094fbd",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/bde78bb5971f1c2ec56adab08c5d136788094fbd"
        },
        "date": 1618397146802,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05440855023385223,
            "unit": "iter/sec",
            "range": "stddev: 0.1217672613241109",
            "extra": "mean: 18.37946417799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07561466849995907,
            "unit": "iter/sec",
            "range": "stddev: 0.0719100033915418",
            "extra": "mean: 13.224947220399986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.42959331618839,
            "unit": "iter/sec",
            "range": "stddev: 0.0004991089622762553",
            "extra": "mean: 14.403080188672766 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05576209013854278,
            "unit": "iter/sec",
            "range": "stddev: 0.08045090721641088",
            "extra": "mean: 17.933330646599984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08086393570117759,
            "unit": "iter/sec",
            "range": "stddev: 0.027842444919649174",
            "extra": "mean: 12.366452254999967 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.751875807617004,
            "unit": "iter/sec",
            "range": "stddev: 0.0011621494392102868",
            "extra": "mean: 28.77542511765127 msec\nrounds: 34"
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
          "id": "68e0c4751266ac3b3ba028174946a473eacc1c2d",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/68e0c4751266ac3b3ba028174946a473eacc1c2d"
        },
        "date": 1618397426306,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06844069801148842,
            "unit": "iter/sec",
            "range": "stddev: 0.2642215996509627",
            "extra": "mean: 14.61118938080001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07550455042460098,
            "unit": "iter/sec",
            "range": "stddev: 0.05424662708785296",
            "extra": "mean: 13.24423487560001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.35886858377748,
            "unit": "iter/sec",
            "range": "stddev: 0.0009121637202039221",
            "extra": "mean: 15.300142454549876 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06922832509769947,
            "unit": "iter/sec",
            "range": "stddev: 0.31607935399859377",
            "extra": "mean: 14.444954411199978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08386738101595212,
            "unit": "iter/sec",
            "range": "stddev: 0.026711026763128542",
            "extra": "mean: 11.923586832999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.39138632286137,
            "unit": "iter/sec",
            "range": "stddev: 0.00041581082956215326",
            "extra": "mean: 29.07704826470629 msec\nrounds: 34"
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
          "id": "324f59989281df11f15c750a7513bc8efbe270a7",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/324f59989281df11f15c750a7513bc8efbe270a7"
        },
        "date": 1618397476205,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06176267774751596,
            "unit": "iter/sec",
            "range": "stddev: 0.07063975632721084",
            "extra": "mean: 16.19100784599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08175987091846805,
            "unit": "iter/sec",
            "range": "stddev: 0.40566613127874007",
            "extra": "mean: 12.230939075200013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.05434678558062,
            "unit": "iter/sec",
            "range": "stddev: 0.0009042434062072691",
            "extra": "mean: 13.323678678556153 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06062137984624981,
            "unit": "iter/sec",
            "range": "stddev: 0.6275084642626049",
            "extra": "mean: 16.49583039080003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08957784140713429,
            "unit": "iter/sec",
            "range": "stddev: 0.052617382394252656",
            "extra": "mean: 11.163475076999976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.435214168196346,
            "unit": "iter/sec",
            "range": "stddev: 0.0017351234272569276",
            "extra": "mean: 26.017807410254044 msec\nrounds: 39"
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
          "id": "d23f771031949443cdbc9d353f7c24e7782780ca",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/d23f771031949443cdbc9d353f7c24e7782780ca"
        },
        "date": 1618405093391,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.051354302718715786,
            "unit": "iter/sec",
            "range": "stddev: 0.23376214237630435",
            "extra": "mean: 19.472565044399982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06967905132406522,
            "unit": "iter/sec",
            "range": "stddev: 0.4608409592197451",
            "extra": "mean: 14.351515713800017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 54.32215832490132,
            "unit": "iter/sec",
            "range": "stddev: 0.00428899478945769",
            "extra": "mean: 18.408694183669784 msec\nrounds: 49"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.051494912569314794,
            "unit": "iter/sec",
            "range": "stddev: 0.20783741217712878",
            "extra": "mean: 19.41939407420002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07034961210433267,
            "unit": "iter/sec",
            "range": "stddev: 0.22044119093692566",
            "extra": "mean: 14.214719457399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.78144251677192,
            "unit": "iter/sec",
            "range": "stddev: 0.0017832802203978898",
            "extra": "mean: 30.505063939403264 msec\nrounds: 33"
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
          "id": "47a2af883deab5e497d396d8999e378d4b3532b3",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/47a2af883deab5e497d396d8999e378d4b3532b3"
        },
        "date": 1618493758521,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07646898572154139,
            "unit": "iter/sec",
            "range": "stddev: 0.07786756789125114",
            "extra": "mean: 13.077197121999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09071889342135983,
            "unit": "iter/sec",
            "range": "stddev: 0.042754229534622615",
            "extra": "mean: 11.023062146000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.68366332591869,
            "unit": "iter/sec",
            "range": "stddev: 0.0012271672670681657",
            "extra": "mean: 11.276033967213666 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07653696065464488,
            "unit": "iter/sec",
            "range": "stddev: 0.10669986629313412",
            "extra": "mean: 13.06558284319998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09021503572665382,
            "unit": "iter/sec",
            "range": "stddev: 0.12211949132444168",
            "extra": "mean: 11.084626769199986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.08463192142848,
            "unit": "iter/sec",
            "range": "stddev: 0.00039516586051317656",
            "extra": "mean: 27.712628527773912 msec\nrounds: 36"
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
          "id": "c792757b36df8945257e7fd54c17aa52cd58388e",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/c792757b36df8945257e7fd54c17aa52cd58388e"
        },
        "date": 1618494748900,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06823476750319335,
            "unit": "iter/sec",
            "range": "stddev: 0.09474212355348617",
            "extra": "mean: 14.655285517800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07778414844075651,
            "unit": "iter/sec",
            "range": "stddev: 0.045965382780545384",
            "extra": "mean: 12.856089833800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 63.61301310912147,
            "unit": "iter/sec",
            "range": "stddev: 0.0006508718609886141",
            "extra": "mean: 15.720053981480245 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0684114126091918,
            "unit": "iter/sec",
            "range": "stddev: 0.09534017530168255",
            "extra": "mean: 14.617444105599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07762633722269645,
            "unit": "iter/sec",
            "range": "stddev: 0.052169989883973214",
            "extra": "mean: 12.882225746800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.90074073298267,
            "unit": "iter/sec",
            "range": "stddev: 0.00028620335369713783",
            "extra": "mean: 29.497880529409233 msec\nrounds: 34"
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
          "id": "e655568fedefc1d4f3563ed46202a6b75f36a688",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/e655568fedefc1d4f3563ed46202a6b75f36a688"
        },
        "date": 1618561886482,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05030294305691076,
            "unit": "iter/sec",
            "range": "stddev: 0.206293554060653",
            "extra": "mean: 19.879552551600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06505313957014378,
            "unit": "iter/sec",
            "range": "stddev: 0.46218808859725236",
            "extra": "mean: 15.37204824559999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.63014002445257,
            "unit": "iter/sec",
            "range": "stddev: 0.0024576951842787383",
            "extra": "mean: 14.158261609757451 msec\nrounds: 41"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.04915491578079875,
            "unit": "iter/sec",
            "range": "stddev: 0.268020698394457",
            "extra": "mean: 20.343845251599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06556479740369342,
            "unit": "iter/sec",
            "range": "stddev: 0.24038645462680253",
            "extra": "mean: 15.252087089400016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 28.87775248484507,
            "unit": "iter/sec",
            "range": "stddev: 0.003168823031825329",
            "extra": "mean: 34.62873367741468 msec\nrounds: 31"
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
          "id": "9db113acb55959dacae5cdecb05ae8bf4cb4ae21",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/9db113acb55959dacae5cdecb05ae8bf4cb4ae21"
        },
        "date": 1618564276056,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07130864620480094,
            "unit": "iter/sec",
            "range": "stddev: 0.573720487954636",
            "extra": "mean: 14.023544874599986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08230730180299044,
            "unit": "iter/sec",
            "range": "stddev: 0.07945525718744195",
            "extra": "mean: 12.149590353400061 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 79.98054332628192,
            "unit": "iter/sec",
            "range": "stddev: 0.0015421247535022976",
            "extra": "mean: 12.50304084482752 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0760982772386096,
            "unit": "iter/sec",
            "range": "stddev: 0.1726938913478432",
            "extra": "mean: 13.1409019532 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08327626741056862,
            "unit": "iter/sec",
            "range": "stddev: 0.17067656191455255",
            "extra": "mean: 12.008223124000029 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.989089777192035,
            "unit": "iter/sec",
            "range": "stddev: 0.0020265593628202507",
            "extra": "mean: 27.03499886111318 msec\nrounds: 36"
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
          "id": "0777616f1af49bc0fbda7fe7c7b3cb9281c50792",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/0777616f1af49bc0fbda7fe7c7b3cb9281c50792"
        },
        "date": 1618565982709,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0540579285652082,
            "unit": "iter/sec",
            "range": "stddev: 0.08283754533801553",
            "extra": "mean: 18.4986740436 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07302685638318306,
            "unit": "iter/sec",
            "range": "stddev: 0.06357293075214944",
            "extra": "mean: 13.693592323799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.00867185606856,
            "unit": "iter/sec",
            "range": "stddev: 0.0012158730628097378",
            "extra": "mean: 13.697003035083686 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.054186427871833615,
            "unit": "iter/sec",
            "range": "stddev: 0.07514749846038367",
            "extra": "mean: 18.454805737799983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07276639915447596,
            "unit": "iter/sec",
            "range": "stddev: 0.026511831102020524",
            "extra": "mean: 13.742606637400012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.816403249762246,
            "unit": "iter/sec",
            "range": "stddev: 0.0021092145197419373",
            "extra": "mean: 29.571447696970278 msec\nrounds: 33"
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
          "id": "9be65997b9c0efa56b296001c5ff9e9c04aaa531",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/9be65997b9c0efa56b296001c5ff9e9c04aaa531"
        },
        "date": 1618582080641,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053668067709302866,
            "unit": "iter/sec",
            "range": "stddev: 0.07119709502714416",
            "extra": "mean: 18.633053931 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07211073830938353,
            "unit": "iter/sec",
            "range": "stddev: 0.09255926016178567",
            "extra": "mean: 13.86756013659998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 76.72793199744953,
            "unit": "iter/sec",
            "range": "stddev: 0.0014392676456967334",
            "extra": "mean: 13.033063370367396 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053808857213034876,
            "unit": "iter/sec",
            "range": "stddev: 0.15995037632764073",
            "extra": "mean: 18.584301020199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07150285279949187,
            "unit": "iter/sec",
            "range": "stddev: 0.12735133158051573",
            "extra": "mean: 13.985455976199967 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.074704430833265,
            "unit": "iter/sec",
            "range": "stddev: 0.001409420070648327",
            "extra": "mean: 26.97256836843041 msec\nrounds: 38"
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
          "id": "5d05dc93ada3d7c578794c8824dd6492be550441",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/5d05dc93ada3d7c578794c8824dd6492be550441"
        },
        "date": 1618583651543,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07670451107227126,
            "unit": "iter/sec",
            "range": "stddev: 0.9265661340001915",
            "extra": "mean: 13.037042880800016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08072293680094791,
            "unit": "iter/sec",
            "range": "stddev: 0.0813166066829256",
            "extra": "mean: 12.38805275960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.29358106323211,
            "unit": "iter/sec",
            "range": "stddev: 0.0004968194498671645",
            "extra": "mean: 13.46011304999403 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07581327355269102,
            "unit": "iter/sec",
            "range": "stddev: 0.5099565858850127",
            "extra": "mean: 13.190302346 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0849605688435135,
            "unit": "iter/sec",
            "range": "stddev: 0.3478947644643767",
            "extra": "mean: 11.77016601480002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.406764047985945,
            "unit": "iter/sec",
            "range": "stddev: 0.0011273148850383318",
            "extra": "mean: 23.037884116275183 msec\nrounds: 43"
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
          "id": "0d7b444d0cfe1e4814d7b6b6ed48952a3433ab0b",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/0d7b444d0cfe1e4814d7b6b6ed48952a3433ab0b"
        },
        "date": 1618584988911,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053664177501143016,
            "unit": "iter/sec",
            "range": "stddev: 0.13668043036708588",
            "extra": "mean: 18.634404672999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07049576690299775,
            "unit": "iter/sec",
            "range": "stddev: 0.0655648332721026",
            "extra": "mean: 14.185248901199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 66.29370320309245,
            "unit": "iter/sec",
            "range": "stddev: 0.0007490447645541018",
            "extra": "mean: 15.084388888888506 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053547148307977806,
            "unit": "iter/sec",
            "range": "stddev: 0.20707305771046405",
            "extra": "mean: 18.67513082579999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07337128854223877,
            "unit": "iter/sec",
            "range": "stddev: 0.15226629242295966",
            "extra": "mean: 13.629309500600016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.233369193234374,
            "unit": "iter/sec",
            "range": "stddev: 0.0017834210016353788",
            "extra": "mean: 27.598868729732253 msec\nrounds: 37"
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
          "id": "8b6c38977e65f1e1fd8f1caf11684ce661bc646b",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/8b6c38977e65f1e1fd8f1caf11684ce661bc646b"
        },
        "date": 1618585245054,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06103738932807246,
            "unit": "iter/sec",
            "range": "stddev: 0.22184273467590812",
            "extra": "mean: 16.383400584599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08171173532891939,
            "unit": "iter/sec",
            "range": "stddev: 0.06782243615276705",
            "extra": "mean: 12.238144202599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.30110054092304,
            "unit": "iter/sec",
            "range": "stddev: 0.001064682431146458",
            "extra": "mean: 12.150505806453515 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06077887901870638,
            "unit": "iter/sec",
            "range": "stddev: 0.12332943564145368",
            "extra": "mean: 16.453083968399984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08078224107259485,
            "unit": "iter/sec",
            "range": "stddev: 0.20976516042821652",
            "extra": "mean: 12.37895837900005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.904807758619256,
            "unit": "iter/sec",
            "range": "stddev: 0.0017347532915824454",
            "extra": "mean: 24.447004027033596 msec\nrounds: 37"
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
          "id": "58cc1f1e5143371c7c2632b4752f69a877ca7f86",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/58cc1f1e5143371c7c2632b4752f69a877ca7f86"
        },
        "date": 1618585530977,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05954064418660144,
            "unit": "iter/sec",
            "range": "stddev: 0.12940064270953697",
            "extra": "mean: 16.795249928200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07731542664969887,
            "unit": "iter/sec",
            "range": "stddev: 0.08506915219089332",
            "extra": "mean: 12.934029382400036 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.1814593024003,
            "unit": "iter/sec",
            "range": "stddev: 0.0008676469528536674",
            "extra": "mean: 12.168194730156035 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06036183156442548,
            "unit": "iter/sec",
            "range": "stddev: 0.12619978180703062",
            "extra": "mean: 16.566760386199984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08202117112001057,
            "unit": "iter/sec",
            "range": "stddev: 0.1496188026197497",
            "extra": "mean: 12.19197417380001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.38568502474003,
            "unit": "iter/sec",
            "range": "stddev: 0.0015409505142807483",
            "extra": "mean: 25.389935439026953 msec\nrounds: 41"
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
          "id": "842a9de07122c68cd17698385ac4efcf694517e0",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/842a9de07122c68cd17698385ac4efcf694517e0"
        },
        "date": 1618586000288,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07711303996297748,
            "unit": "iter/sec",
            "range": "stddev: 0.08454980200758677",
            "extra": "mean: 12.967975331800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09014000935928965,
            "unit": "iter/sec",
            "range": "stddev: 0.05871116142140542",
            "extra": "mean: 11.093852852999976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.12683277195559,
            "unit": "iter/sec",
            "range": "stddev: 0.00019915383801691558",
            "extra": "mean: 13.674870934428103 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07798243511357084,
            "unit": "iter/sec",
            "range": "stddev: 0.09763861107442606",
            "extra": "mean: 12.823400532999973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09436974363147917,
            "unit": "iter/sec",
            "range": "stddev: 0.10313889403862775",
            "extra": "mean: 10.596616685799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.51567321291667,
            "unit": "iter/sec",
            "range": "stddev: 0.0002981521634839326",
            "extra": "mean: 25.306414358977072 msec\nrounds: 39"
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
          "id": "1c0be338082aedb02dcddc2c4918fa6638c8f06e",
          "message": "Get rid of save_state method",
          "timestamp": "2021-04-13T12:34:55Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/330/commits/1c0be338082aedb02dcddc2c4918fa6638c8f06e"
        },
        "date": 1618586376555,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06842363314254506,
            "unit": "iter/sec",
            "range": "stddev: 0.07884671832896589",
            "extra": "mean: 14.614833414600009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07393205092625993,
            "unit": "iter/sec",
            "range": "stddev: 0.05396302367258766",
            "extra": "mean: 13.525933441199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 66.92530824093917,
            "unit": "iter/sec",
            "range": "stddev: 0.0002568506379337044",
            "extra": "mean: 14.942030545453441 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06832757000042114,
            "unit": "iter/sec",
            "range": "stddev: 0.09349266661439366",
            "extra": "mean: 14.635380710799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07409437457485954,
            "unit": "iter/sec",
            "range": "stddev: 0.03772761287620853",
            "extra": "mean: 13.496301247400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.60237545966084,
            "unit": "iter/sec",
            "range": "stddev: 0.0002806324465199678",
            "extra": "mean: 28.088013428571553 msec\nrounds: 35"
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
          "id": "e7913057addcc24737feb6a998d9d792007c9a23",
          "message": "Merge pull request #330 from UCL-CCS/remove-save-state\n\nGet rid of save_state method",
          "timestamp": "2021-04-16T17:17:25+02:00",
          "tree_id": "2dd70de1c3de7016269a7d402782c1a0abf3b885",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e7913057addcc24737feb6a998d9d792007c9a23"
        },
        "date": 1618586701032,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06024805906246163,
            "unit": "iter/sec",
            "range": "stddev: 0.8782008239747694",
            "extra": "mean: 16.598045074999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08503569198873571,
            "unit": "iter/sec",
            "range": "stddev: 0.14332928608335138",
            "extra": "mean: 11.759767888199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.52914484118627,
            "unit": "iter/sec",
            "range": "stddev: 0.0010272389874702327",
            "extra": "mean: 11.169547098588705 msec\nrounds: 71"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06461111669864814,
            "unit": "iter/sec",
            "range": "stddev: 0.1414449344919502",
            "extra": "mean: 15.477212763000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0848587422547968,
            "unit": "iter/sec",
            "range": "stddev: 0.1586130196220136",
            "extra": "mean: 11.784289672800014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.235436777707314,
            "unit": "iter/sec",
            "range": "stddev: 0.0026033167202353207",
            "extra": "mean: 24.25098599999842 msec\nrounds: 40"
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
          "id": "0940a22b52603ee09d091245404957fdeeb18282",
          "message": "remove worker.py",
          "timestamp": "2021-04-16T15:17:29Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/331/commits/0940a22b52603ee09d091245404957fdeeb18282"
        },
        "date": 1618824757728,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.057551529009286555,
            "unit": "iter/sec",
            "range": "stddev: 0.1370276642656318",
            "extra": "mean: 17.375732968600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07818983450864919,
            "unit": "iter/sec",
            "range": "stddev: 0.14438694934343677",
            "extra": "mean: 12.789386322200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.02481073177802,
            "unit": "iter/sec",
            "range": "stddev: 0.0014006886766316545",
            "extra": "mean: 12.81643608771638 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05559575778201647,
            "unit": "iter/sec",
            "range": "stddev: 0.26815355475826874",
            "extra": "mean: 17.9869838976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08257925257000721,
            "unit": "iter/sec",
            "range": "stddev: 0.13032847715735257",
            "extra": "mean: 12.10957920879996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.73135294832565,
            "unit": "iter/sec",
            "range": "stddev: 0.0016386134442795952",
            "extra": "mean: 24.551111800009753 msec\nrounds: 35"
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
          "id": "3dacd8e6fe94e0ab69b9f194b59ce99af5ce7e96",
          "message": "Merge pull request #331 from UCL-CCS/remove-worker\n\nremove worker.py",
          "timestamp": "2021-04-19T11:59:45+02:00",
          "tree_id": "343ef20da55ce9b7e77bbe49d09b531949028ba0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3dacd8e6fe94e0ab69b9f194b59ce99af5ce7e96"
        },
        "date": 1618826907088,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05478395628478564,
            "unit": "iter/sec",
            "range": "stddev: 0.1277151360452581",
            "extra": "mean: 18.253519238400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07291678945337512,
            "unit": "iter/sec",
            "range": "stddev: 0.148559399090894",
            "extra": "mean: 13.714262620400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.80144137015995,
            "unit": "iter/sec",
            "range": "stddev: 0.000673977603800243",
            "extra": "mean: 13.549870862065964 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05451477707920423,
            "unit": "iter/sec",
            "range": "stddev: 0.13308569091395062",
            "extra": "mean: 18.34365017299998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0750667448913433,
            "unit": "iter/sec",
            "range": "stddev: 0.2606617228020345",
            "extra": "mean: 13.32147812520002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.63956334109473,
            "unit": "iter/sec",
            "range": "stddev: 0.0014416599402287257",
            "extra": "mean: 25.880209648654592 msec\nrounds: 37"
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
          "id": "9318a090680c914a69d24fdac402f06f510c77df",
          "message": "bug in resurrect sampler",
          "timestamp": "2021-04-19T09:59:48Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/332/commits/9318a090680c914a69d24fdac402f06f510c77df"
        },
        "date": 1618838202958,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05570245318127298,
            "unit": "iter/sec",
            "range": "stddev: 0.11337985718250287",
            "extra": "mean: 17.95253068559999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07194841770075608,
            "unit": "iter/sec",
            "range": "stddev: 0.07411389900951233",
            "extra": "mean: 13.898846311800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.74021301391622,
            "unit": "iter/sec",
            "range": "stddev: 0.0006654851145471615",
            "extra": "mean: 13.74755391228626 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.055667670720035096,
            "unit": "iter/sec",
            "range": "stddev: 0.07637193680703688",
            "extra": "mean: 17.963747846199976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07117777283254975,
            "unit": "iter/sec",
            "range": "stddev: 0.1644740122881967",
            "extra": "mean: 14.049329730400018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.012656445467414,
            "unit": "iter/sec",
            "range": "stddev: 0.0009487095885263402",
            "extra": "mean: 26.30702754054009 msec\nrounds: 37"
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
          "id": "4664961384035de8468c2e7cce22c86fd70fbf72",
          "message": "Merge pull request #332 from UCL-CCS/remove-worker\n\nbug in resurrect sampler",
          "timestamp": "2021-04-19T15:14:03+02:00",
          "tree_id": "980f876f7dc4706a5c542033252986f730cb3b30",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4664961384035de8468c2e7cce22c86fd70fbf72"
        },
        "date": 1618838452248,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0767951212028536,
            "unit": "iter/sec",
            "range": "stddev: 0.07389933943711705",
            "extra": "mean: 13.0216605474 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0861226254513545,
            "unit": "iter/sec",
            "range": "stddev: 0.0696683850416549",
            "extra": "mean: 11.611350615000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.94508946353344,
            "unit": "iter/sec",
            "range": "stddev: 0.0001287321938599311",
            "extra": "mean: 13.523548450004341 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07658344452427224,
            "unit": "iter/sec",
            "range": "stddev: 0.10340886628932772",
            "extra": "mean: 13.057652423600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08596035647962222,
            "unit": "iter/sec",
            "range": "stddev: 0.0519934356369294",
            "extra": "mean: 11.633269578599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.119006818240315,
            "unit": "iter/sec",
            "range": "stddev: 0.0001209370256806401",
            "extra": "mean: 25.56302118421172 msec\nrounds: 38"
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
          "id": "c4a04fc2ab844513b4d3145990db12919cd150b2",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-04-20T12:12:40+02:00",
          "tree_id": "637704ee42478ce0c8a55155d9a10710aba5ce09",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c4a04fc2ab844513b4d3145990db12919cd150b2"
        },
        "date": 1618913981228,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07678835674005693,
            "unit": "iter/sec",
            "range": "stddev: 0.5228381958760616",
            "extra": "mean: 13.022807655400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.086721262282353,
            "unit": "iter/sec",
            "range": "stddev: 0.06726923514182029",
            "extra": "mean: 11.5311974674 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.15597730081849,
            "unit": "iter/sec",
            "range": "stddev: 0.0010985797342537885",
            "extra": "mean: 12.02559373913049 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07747786538605948,
            "unit": "iter/sec",
            "range": "stddev: 0.21222519132857515",
            "extra": "mean: 12.906912122800032 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08650639345072003,
            "unit": "iter/sec",
            "range": "stddev: 0.16442851324069976",
            "extra": "mean: 11.5598392224 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.12184144061732,
            "unit": "iter/sec",
            "range": "stddev: 0.0018844145653963869",
            "extra": "mean: 23.19010428571541 msec\nrounds: 42"
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
          "id": "ec6febd76a565c9fb907089880807c249ac42e8b",
          "message": "added an assertion to jinja test",
          "timestamp": "2021-04-20T12:17:29+02:00",
          "tree_id": "09f8fac8c2b44f64f29c69a1f55a84733480d22c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ec6febd76a565c9fb907089880807c249ac42e8b"
        },
        "date": 1618914216667,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08852754177858439,
            "unit": "iter/sec",
            "range": "stddev: 0.1325526996630105",
            "extra": "mean: 11.295919664200017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09841564670840161,
            "unit": "iter/sec",
            "range": "stddev: 0.08911157696600677",
            "extra": "mean: 10.160985914799983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 94.20984172829873,
            "unit": "iter/sec",
            "range": "stddev: 0.0004617440804805302",
            "extra": "mean: 10.614602271427234 msec\nrounds: 70"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08722940217427036,
            "unit": "iter/sec",
            "range": "stddev: 0.2628007077014414",
            "extra": "mean: 11.464024458200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09733531796103921,
            "unit": "iter/sec",
            "range": "stddev: 0.1660016755026137",
            "extra": "mean: 10.273763120600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.90740770074851,
            "unit": "iter/sec",
            "range": "stddev: 0.0008861493533842694",
            "extra": "mean: 21.318594418596337 msec\nrounds: 43"
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
          "id": "69ba2c250c20644dfd9fc41438c3272c2b65d4a0",
          "message": "call plotting routines in mcmc test",
          "timestamp": "2021-04-20T12:40:07+02:00",
          "tree_id": "9278987171e8e52775f7013861ec02decbc229d9",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/69ba2c250c20644dfd9fc41438c3272c2b65d4a0"
        },
        "date": 1618915700570,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.057438806425863055,
            "unit": "iter/sec",
            "range": "stddev: 1.0763963668735075",
            "extra": "mean: 17.4098325196 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07988281046892658,
            "unit": "iter/sec",
            "range": "stddev: 0.18035854456576228",
            "extra": "mean: 12.518337726599986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.54821659651324,
            "unit": "iter/sec",
            "range": "stddev: 0.0014442655366762413",
            "extra": "mean: 12.895203060607358 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.058497581465245904,
            "unit": "iter/sec",
            "range": "stddev: 0.5894555041004436",
            "extra": "mean: 17.094723832199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07569495614744685,
            "unit": "iter/sec",
            "range": "stddev: 0.07264348775020738",
            "extra": "mean: 13.210919867000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.85001829059946,
            "unit": "iter/sec",
            "range": "stddev: 0.0005646857541906922",
            "extra": "mean: 25.740013621614438 msec\nrounds: 37"
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
          "id": "8121287935cd136ec40c3d8604cb114821d5fcc3",
          "message": "update to mcmc and gp",
          "timestamp": "2021-04-20T12:41:28+02:00",
          "tree_id": "86c516237de54e4bcd7b5ea1685886f44ccb9a09",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/8121287935cd136ec40c3d8604cb114821d5fcc3"
        },
        "date": 1618915815985,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05445639484126158,
            "unit": "iter/sec",
            "range": "stddev: 0.09292032275154471",
            "extra": "mean: 18.363316244400018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0711859810670548,
            "unit": "iter/sec",
            "range": "stddev: 0.10566755972813525",
            "extra": "mean: 14.0477097458 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.98904224887255,
            "unit": "iter/sec",
            "range": "stddev: 0.0004890036022843777",
            "extra": "mean: 14.086681103461176 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05467066839892005,
            "unit": "iter/sec",
            "range": "stddev: 0.048211171950278096",
            "extra": "mean: 18.291343956199988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07322546314031209,
            "unit": "iter/sec",
            "range": "stddev: 0.06216305043597248",
            "extra": "mean: 13.656451692000019 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.67640386343268,
            "unit": "iter/sec",
            "range": "stddev: 0.0019238578759792708",
            "extra": "mean: 28.83805379411128 msec\nrounds: 34"
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
          "id": "9302038ac3ed2b63478b335087232763c85b49f2",
          "message": "update add_app docstring",
          "timestamp": "2021-04-21T11:38:16+02:00",
          "tree_id": "3bd8151df7a13886f6a25ff6b38c07e5a430ee57",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9302038ac3ed2b63478b335087232763c85b49f2"
        },
        "date": 1618998355399,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06896080634797279,
            "unit": "iter/sec",
            "range": "stddev: 0.05129683140593913",
            "extra": "mean: 14.500990533000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07629833269132426,
            "unit": "iter/sec",
            "range": "stddev: 0.059913565598394655",
            "extra": "mean: 13.106446297399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.58998174274053,
            "unit": "iter/sec",
            "range": "stddev: 0.00021776988054528605",
            "extra": "mean: 14.36988449999583 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06914013941709563,
            "unit": "iter/sec",
            "range": "stddev: 0.06208346700554184",
            "extra": "mean: 14.463378414200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07726560383338853,
            "unit": "iter/sec",
            "range": "stddev: 0.1594320597594061",
            "extra": "mean: 12.942369571799986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.614183746524844,
            "unit": "iter/sec",
            "range": "stddev: 0.0002805263285873149",
            "extra": "mean: 27.31182011110415 msec\nrounds: 36"
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
          "id": "df7a179b549869f8e4ed78da3abcc2923fff5229",
          "message": "don't show outdated tutorials",
          "timestamp": "2021-04-21T11:39:58+02:00",
          "tree_id": "f8f7dfca12720a0df774b42debf92aa9ba7c911a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/df7a179b549869f8e4ed78da3abcc2923fff5229"
        },
        "date": 1618998404712,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07636993959953492,
            "unit": "iter/sec",
            "range": "stddev: 0.08729809508954231",
            "extra": "mean: 13.094157272400015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09042602548101565,
            "unit": "iter/sec",
            "range": "stddev: 0.06881829826897042",
            "extra": "mean: 11.058763167799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 76.49735671030768,
            "unit": "iter/sec",
            "range": "stddev: 0.00020981806372068817",
            "extra": "mean: 13.072347111115988 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07655118598072838,
            "unit": "iter/sec",
            "range": "stddev: 0.11456393804651838",
            "extra": "mean: 13.063154896800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09056892231159488,
            "unit": "iter/sec",
            "range": "stddev: 0.05397518498986546",
            "extra": "mean: 11.04131499499997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.08158674313064,
            "unit": "iter/sec",
            "range": "stddev: 0.0001636179869333409",
            "extra": "mean: 25.587497421039835 msec\nrounds: 38"
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
          "id": "04270e00bf663561ee539e2e2c95910854246502",
          "message": "Dpc/update fusion tutorial",
          "timestamp": "2021-04-21T09:40:05Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/333/commits/04270e00bf663561ee539e2e2c95910854246502"
        },
        "date": 1619003418571,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06958895183151467,
            "unit": "iter/sec",
            "range": "stddev: 0.05828954600648673",
            "extra": "mean: 14.3700971732 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07870088589565485,
            "unit": "iter/sec",
            "range": "stddev: 0.03890137249894859",
            "extra": "mean: 12.706337274599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.6397388325925,
            "unit": "iter/sec",
            "range": "stddev: 0.0002955900541878474",
            "extra": "mean: 14.359617321424878 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06969520725322777,
            "unit": "iter/sec",
            "range": "stddev: 0.11847696020732477",
            "extra": "mean: 14.348188913000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07852318481410307,
            "unit": "iter/sec",
            "range": "stddev: 0.032857185947547454",
            "extra": "mean: 12.73509221979998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.9692134018099,
            "unit": "iter/sec",
            "range": "stddev: 0.0006488661875389601",
            "extra": "mean: 27.049534138885495 msec\nrounds: 36"
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
          "id": "1f3eadf1c11d55b51f6143dccdd4d7e0de4171e7",
          "message": "Merge pull request #333 from UCL-CCS/dpc/update-fusion-tutorial\n\nDpc/update fusion tutorial",
          "timestamp": "2021-04-21T13:20:27+02:00",
          "tree_id": "6121a7d6a4223f23944f27a0ff9e68e6da678c98",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1f3eadf1c11d55b51f6143dccdd4d7e0de4171e7"
        },
        "date": 1619004552454,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05332965464237913,
            "unit": "iter/sec",
            "range": "stddev: 0.11942020181491166",
            "extra": "mean: 18.751293378999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07203227350532268,
            "unit": "iter/sec",
            "range": "stddev: 0.34601850560218006",
            "extra": "mean: 13.882666079199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.03882996119935,
            "unit": "iter/sec",
            "range": "stddev: 0.0015788653336367396",
            "extra": "mean: 13.691347472724209 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05385570438154376,
            "unit": "iter/sec",
            "range": "stddev: 0.2613143451763997",
            "extra": "mean: 18.568135195399986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0770056238740142,
            "unit": "iter/sec",
            "range": "stddev: 0.0575930159777506",
            "extra": "mean: 12.986064519600017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.41689560850328,
            "unit": "iter/sec",
            "range": "stddev: 0.0012046498702354932",
            "extra": "mean: 26.72589437838724 msec\nrounds: 37"
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
          "id": "9151a0325412058144606c581d75a06a70107143",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-04-21T14:45:19+02:00",
          "tree_id": "38236157a3637fae4a45edfd2911d88072cb7d40",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9151a0325412058144606c581d75a06a70107143"
        },
        "date": 1619009581205,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06991174972325645,
            "unit": "iter/sec",
            "range": "stddev: 0.17602910857352377",
            "extra": "mean: 14.303747280800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07855415498642862,
            "unit": "iter/sec",
            "range": "stddev: 0.07134249832086037",
            "extra": "mean: 12.730071377799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.9872609187668,
            "unit": "iter/sec",
            "range": "stddev: 0.00024900720428400734",
            "extra": "mean: 14.28831457142873 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07042474246453785,
            "unit": "iter/sec",
            "range": "stddev: 0.15304460282331792",
            "extra": "mean: 14.199554943399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07872902299453059,
            "unit": "iter/sec",
            "range": "stddev: 0.18583830883733998",
            "extra": "mean: 12.701796135199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.94963582391453,
            "unit": "iter/sec",
            "range": "stddev: 0.0008897436961339267",
            "extra": "mean: 26.35071399999668 msec\nrounds: 36"
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
          "id": "025f233429385ffd78a48f53e3811a4a0b11e42a",
          "message": "fix a mistake",
          "timestamp": "2021-04-21T15:03:45+02:00",
          "tree_id": "0839d612966da6cac5a0ad4762aec6471235912e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/025f233429385ffd78a48f53e3811a4a0b11e42a"
        },
        "date": 1619010716159,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.059651465661489766,
            "unit": "iter/sec",
            "range": "stddev: 0.156418195155259",
            "extra": "mean: 16.7640474364 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07625766247266336,
            "unit": "iter/sec",
            "range": "stddev: 0.19743832014144244",
            "extra": "mean: 13.113436310200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.9072342332334,
            "unit": "iter/sec",
            "range": "stddev: 0.0006149498709970888",
            "extra": "mean: 11.917923515633255 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05858699421972653,
            "unit": "iter/sec",
            "range": "stddev: 0.4049372801058748",
            "extra": "mean: 17.068634657199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07993538432927882,
            "unit": "iter/sec",
            "range": "stddev: 0.08845474367762657",
            "extra": "mean: 12.510104359800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.363920966336615,
            "unit": "iter/sec",
            "range": "stddev: 0.001088201939618303",
            "extra": "mean: 23.604991634146046 msec\nrounds: 41"
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
          "id": "e72b5b279f9f19f5cb101cbf783d5d8533e4d1aa",
          "message": "added get_pdf to pce",
          "timestamp": "2021-04-21T15:34:49+02:00",
          "tree_id": "142576ca480fc6590cca9e1f1f4cba962ec336c5",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e72b5b279f9f19f5cb101cbf783d5d8533e4d1aa"
        },
        "date": 1619012624190,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05529018568953647,
            "unit": "iter/sec",
            "range": "stddev: 0.11611744555805568",
            "extra": "mean: 18.086392503999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07114024624041208,
            "unit": "iter/sec",
            "range": "stddev: 0.3797039647129391",
            "extra": "mean: 14.05674077399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.55729748818624,
            "unit": "iter/sec",
            "range": "stddev: 0.0009375351626598565",
            "extra": "mean: 13.782211226414818 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05539746525083743,
            "unit": "iter/sec",
            "range": "stddev: 0.18019874912446063",
            "extra": "mean: 18.051367431199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07058004221501442,
            "unit": "iter/sec",
            "range": "stddev: 0.23666632493463738",
            "extra": "mean: 14.168311162999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.05379202383495,
            "unit": "iter/sec",
            "range": "stddev: 0.0018975600133685547",
            "extra": "mean: 27.73633351351519 msec\nrounds: 37"
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
          "id": "62e65135090038dfe08da41ef0aca025b81da54d",
          "message": "rename get_pdf to get_distribution",
          "timestamp": "2021-04-21T16:18:44+02:00",
          "tree_id": "29cd7a80783f86af913dac91476dcc453f32a99c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/62e65135090038dfe08da41ef0aca025b81da54d"
        },
        "date": 1619015252714,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053754702136893005,
            "unit": "iter/sec",
            "range": "stddev: 0.23642684818751353",
            "extra": "mean: 18.603023740199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07425800162367009,
            "unit": "iter/sec",
            "range": "stddev: 0.04822451217643932",
            "extra": "mean: 13.46656223079999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.77767377172668,
            "unit": "iter/sec",
            "range": "stddev: 0.00039031221938009224",
            "extra": "mean: 12.857160050002866 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05386597841126983,
            "unit": "iter/sec",
            "range": "stddev: 0.15933306468098626",
            "extra": "mean: 18.564593635799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07418392800635354,
            "unit": "iter/sec",
            "range": "stddev: 0.024537829414490966",
            "extra": "mean: 13.480008768400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.74291768075137,
            "unit": "iter/sec",
            "range": "stddev: 0.0008167439038690837",
            "extra": "mean: 25.811169108123977 msec\nrounds: 37"
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
          "id": "0953b8b0cc307990fa26254e13d9365eb3f7faae",
          "message": "added an option to executelocal to redirect standard output/error",
          "timestamp": "2021-04-21T18:02:15+02:00",
          "tree_id": "bac482f632133905404ea3492427a944c226cfe8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0953b8b0cc307990fa26254e13d9365eb3f7faae"
        },
        "date": 1619021391659,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06880695755546104,
            "unit": "iter/sec",
            "range": "stddev: 0.22474735328143625",
            "extra": "mean: 14.533413996600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07724361617722181,
            "unit": "iter/sec",
            "range": "stddev: 0.19157518505358384",
            "extra": "mean: 12.946053660999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.2319452281958,
            "unit": "iter/sec",
            "range": "stddev: 0.0005736302794980988",
            "extra": "mean: 13.471289172416382 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07036326871860481,
            "unit": "iter/sec",
            "range": "stddev: 0.13232590503655212",
            "extra": "mean: 14.211960561399973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08146962716577333,
            "unit": "iter/sec",
            "range": "stddev: 0.2686422048644663",
            "extra": "mean: 12.274513027600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.81147664739842,
            "unit": "iter/sec",
            "range": "stddev: 0.0008980559563672643",
            "extra": "mean: 25.11838505405821 msec\nrounds: 37"
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
          "id": "9dedf1a99cf84ee7d2ea48e99f10d84dba3fd2ca",
          "message": "add a surrogate command to the PCE analysis",
          "timestamp": "2021-04-21T16:02:22Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/334/commits/9dedf1a99cf84ee7d2ea48e99f10d84dba3fd2ca"
        },
        "date": 1619025502037,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07669440521368776,
            "unit": "iter/sec",
            "range": "stddev: 0.09128050738855922",
            "extra": "mean: 13.038760744200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0919327517025403,
            "unit": "iter/sec",
            "range": "stddev: 0.1110028110533055",
            "extra": "mean: 10.877516243999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.91662891040859,
            "unit": "iter/sec",
            "range": "stddev: 0.00023564231758673585",
            "extra": "mean: 11.916589274190505 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07644750797499679,
            "unit": "iter/sec",
            "range": "stddev: 0.09037603083820095",
            "extra": "mean: 13.080871129599984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09238881592104696,
            "unit": "iter/sec",
            "range": "stddev: 0.10269844845532575",
            "extra": "mean: 10.823820935799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.870395846571135,
            "unit": "iter/sec",
            "range": "stddev: 0.00040602717987367297",
            "extra": "mean: 23.883222973682308 msec\nrounds: 38"
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
          "id": "985d926258a775a2a593647d616958afdaca70c9",
          "message": "Merge pull request #334 from UCL-CCS/dpc/add-pce-surrogate\n\nadd a surrogate command to the PCE analysis",
          "timestamp": "2021-04-22T10:54:23+02:00",
          "tree_id": "641aac0ebdeca2f31f934e288b2c83c958bbfa64",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/985d926258a775a2a593647d616958afdaca70c9"
        },
        "date": 1619082223518,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05279494731278477,
            "unit": "iter/sec",
            "range": "stddev: 0.3316996926364598",
            "extra": "mean: 18.941206514999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07024952014267224,
            "unit": "iter/sec",
            "range": "stddev: 0.3496580113974572",
            "extra": "mean: 14.234972679800013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.65857840088378,
            "unit": "iter/sec",
            "range": "stddev: 0.000732273483550128",
            "extra": "mean: 13.762999800004847 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05369317651624607,
            "unit": "iter/sec",
            "range": "stddev: 0.1886720924355224",
            "extra": "mean: 18.624340463399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07181970068023748,
            "unit": "iter/sec",
            "range": "stddev: 0.13214168073836416",
            "extra": "mean: 13.923756163400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 32.81680269304831,
            "unit": "iter/sec",
            "range": "stddev: 0.0015726646740973976",
            "extra": "mean: 30.47219466666182 msec\nrounds: 33"
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
          "id": "118de905743699b43e3cc2d5050ff6d526f3ff7b",
          "message": "Update README.md",
          "timestamp": "2021-04-22T13:32:42+02:00",
          "tree_id": "fb69c1bb0d4853c27dbd1de0323427be479687c6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/118de905743699b43e3cc2d5050ff6d526f3ff7b"
        },
        "date": 1619091579137,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07524713146680138,
            "unit": "iter/sec",
            "range": "stddev: 0.1726781639831103",
            "extra": "mean: 13.289543142799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08713517295209047,
            "unit": "iter/sec",
            "range": "stddev: 0.2981310687570774",
            "extra": "mean: 11.47642181819998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.08340745485154,
            "unit": "iter/sec",
            "range": "stddev: 0.00026517336098572737",
            "extra": "mean: 12.332979476187097 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07486153068276816,
            "unit": "iter/sec",
            "range": "stddev: 0.20486768216405374",
            "extra": "mean: 13.357995633799977 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08742951021814531,
            "unit": "iter/sec",
            "range": "stddev: 0.4546396164848832",
            "extra": "mean: 11.437785680199976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.16587760827018,
            "unit": "iter/sec",
            "range": "stddev: 0.0002737994696296864",
            "extra": "mean: 24.291963589745045 msec\nrounds: 39"
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
          "id": "50701ad476746f3c19656fb68a380322e079de32",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-04-22T14:12:34+02:00",
          "tree_id": "458832ef68727baee101323cfa0a793cae3ac15e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/50701ad476746f3c19656fb68a380322e079de32"
        },
        "date": 1619094040327,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06550728079767118,
            "unit": "iter/sec",
            "range": "stddev: 0.08657723032538857",
            "extra": "mean: 15.265478704399992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07461744578932185,
            "unit": "iter/sec",
            "range": "stddev: 0.06977362333835352",
            "extra": "mean: 13.401691647599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 68.59578368953638,
            "unit": "iter/sec",
            "range": "stddev: 0.00022913059725181904",
            "extra": "mean: 14.578155481479548 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06571043136458585,
            "unit": "iter/sec",
            "range": "stddev: 0.09683136636992473",
            "extra": "mean: 15.218283904600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07481385375954071,
            "unit": "iter/sec",
            "range": "stddev: 0.05608018442231878",
            "extra": "mean: 13.366508337000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.59579099034985,
            "unit": "iter/sec",
            "range": "stddev: 0.00026032830396903586",
            "extra": "mean: 28.09320911764831 msec\nrounds: 34"
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
          "id": "bfdd7a8fddc31d6d327e4efc089cccdf6b9895d0",
          "message": "added progress bar",
          "timestamp": "2021-04-22T14:26:57+02:00",
          "tree_id": "bbdbbf535173aab215e3569377802239839f0bad",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bfdd7a8fddc31d6d327e4efc089cccdf6b9895d0"
        },
        "date": 1619094988038,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05017413266197627,
            "unit": "iter/sec",
            "range": "stddev: 0.5300344604389373",
            "extra": "mean: 19.93058867079999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06779183630974309,
            "unit": "iter/sec",
            "range": "stddev: 0.21466597378607608",
            "extra": "mean: 14.751038686000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.51857235379467,
            "unit": "iter/sec",
            "range": "stddev: 0.00140108518953381",
            "extra": "mean: 13.98238201754235 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05123103935443673,
            "unit": "iter/sec",
            "range": "stddev: 0.06526971852896579",
            "extra": "mean: 19.519416599800014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06634861210771947,
            "unit": "iter/sec",
            "range": "stddev: 0.2559237407034512",
            "extra": "mean: 15.07190532300001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.91159742614147,
            "unit": "iter/sec",
            "range": "stddev: 0.0013184260042200893",
            "extra": "mean: 27.846157555555035 msec\nrounds: 36"
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
          "id": "4572388f0e0f1914f365cfdb2e1816c2d54ca90a",
          "message": "updated docstrings in action_statuses.py",
          "timestamp": "2021-04-22T15:38:49+02:00",
          "tree_id": "dd23e0318ad4fcad76b13008bfb07912f0eb19bf",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4572388f0e0f1914f365cfdb2e1816c2d54ca90a"
        },
        "date": 1619099144489,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07699081688585484,
            "unit": "iter/sec",
            "range": "stddev: 0.11080971730122563",
            "extra": "mean: 12.988562018800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09082715614273389,
            "unit": "iter/sec",
            "range": "stddev: 0.032565519522718994",
            "extra": "mean: 11.009923050199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.35622225071369,
            "unit": "iter/sec",
            "range": "stddev: 0.0002057651528825993",
            "extra": "mean: 14.213383948281223 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07730403084814806,
            "unit": "iter/sec",
            "range": "stddev: 0.08769241626808902",
            "extra": "mean: 12.935936057000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09125794638738864,
            "unit": "iter/sec",
            "range": "stddev: 0.040886756355359176",
            "extra": "mean: 10.957949850800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.59342541547906,
            "unit": "iter/sec",
            "range": "stddev: 0.0002065795329192068",
            "extra": "mean: 26.600395918916472 msec\nrounds: 37"
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
          "id": "2af4d5c150c8f0c44ed81e38aa82db14b042a358",
          "message": "fix a bug when not using progress bar",
          "timestamp": "2021-04-22T16:07:26+02:00",
          "tree_id": "fd6a9c0c624099bba9ee00582945aab3b7491cb4",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/2af4d5c150c8f0c44ed81e38aa82db14b042a358"
        },
        "date": 1619100915214,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06856984591293087,
            "unit": "iter/sec",
            "range": "stddev: 0.09333854879685877",
            "extra": "mean: 14.58366993080001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07430444697824337,
            "unit": "iter/sec",
            "range": "stddev: 0.032659994546324365",
            "extra": "mean: 13.458144709600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.8464404600628,
            "unit": "iter/sec",
            "range": "stddev: 0.00026853690417375246",
            "extra": "mean: 15.421046905664367 msec\nrounds: 53"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06933026278037441,
            "unit": "iter/sec",
            "range": "stddev: 0.1325612229071986",
            "extra": "mean: 14.423715703599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07840125352377335,
            "unit": "iter/sec",
            "range": "stddev: 0.05142640735674936",
            "extra": "mean: 12.754898104999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.79713186155124,
            "unit": "iter/sec",
            "range": "stddev: 0.0001927734365823058",
            "extra": "mean: 28.73800070588405 msec\nrounds: 34"
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
          "id": "f002fe9cb37a36b1aec4bd220098805606943a78",
          "message": "added pdocs workflow",
          "timestamp": "2021-04-22T17:18:34+02:00",
          "tree_id": "13775f348325576029593c056297d4203f9c3aa3",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f002fe9cb37a36b1aec4bd220098805606943a78"
        },
        "date": 1619105126000,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0760237393209346,
            "unit": "iter/sec",
            "range": "stddev: 0.11848586120944953",
            "extra": "mean: 13.153786026999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08976167517401427,
            "unit": "iter/sec",
            "range": "stddev: 0.040235202184996335",
            "extra": "mean: 11.140612049200001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.89355631700546,
            "unit": "iter/sec",
            "range": "stddev: 0.00028893204479106267",
            "extra": "mean: 12.838032403223107 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07609689149351084,
            "unit": "iter/sec",
            "range": "stddev: 0.08663773391870375",
            "extra": "mean: 13.141141252599983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08984790050902332,
            "unit": "iter/sec",
            "range": "stddev: 0.07116084020108389",
            "extra": "mean: 11.129920614000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.119650376391206,
            "unit": "iter/sec",
            "range": "stddev: 0.00015941142310802746",
            "extra": "mean: 24.92544153845517 msec\nrounds: 39"
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
          "id": "6d0a19e28584658457e7e3a731ff9ab0ef2efa73",
          "message": "fix yaml",
          "timestamp": "2021-04-22T17:25:15+02:00",
          "tree_id": "f1036fe70edb287959ba930185d1e888a9972ab7",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/6d0a19e28584658457e7e3a731ff9ab0ef2efa73"
        },
        "date": 1619105522676,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07550631963559656,
            "unit": "iter/sec",
            "range": "stddev: 0.09857590279730719",
            "extra": "mean: 13.243924546000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08869704075338936,
            "unit": "iter/sec",
            "range": "stddev: 0.03623779982428517",
            "extra": "mean: 11.274333297999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.2167549558931,
            "unit": "iter/sec",
            "range": "stddev: 0.00021996095981550868",
            "extra": "mean: 13.658075949998269 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07564470222289031,
            "unit": "iter/sec",
            "range": "stddev: 0.10533708739183976",
            "extra": "mean: 13.219696430999988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09885386080309465,
            "unit": "iter/sec",
            "range": "stddev: 0.25317699103561486",
            "extra": "mean: 10.115942785399989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.717558828724975,
            "unit": "iter/sec",
            "range": "stddev: 0.00017849816069019834",
            "extra": "mean: 25.82807465790145 msec\nrounds: 38"
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
          "id": "5797f3b06d9155124dd290a1d8c921bba2bb7ee4",
          "message": "simple pdoc",
          "timestamp": "2021-04-22T17:26:08+02:00",
          "tree_id": "13c4f926a6b212ba416a40b389e98f6a47a45847",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/5797f3b06d9155124dd290a1d8c921bba2bb7ee4"
        },
        "date": 1619105583851,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07741529228395201,
            "unit": "iter/sec",
            "range": "stddev: 0.19666095157055832",
            "extra": "mean: 12.917344500000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0869578597408143,
            "unit": "iter/sec",
            "range": "stddev: 0.30747844340664854",
            "extra": "mean: 11.49982305200001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.1983875531554,
            "unit": "iter/sec",
            "range": "stddev: 0.001107435119377639",
            "extra": "mean: 12.95363843333443 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07723888681790199,
            "unit": "iter/sec",
            "range": "stddev: 0.13826167097553885",
            "extra": "mean: 12.946846351600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08909519598716262,
            "unit": "iter/sec",
            "range": "stddev: 0.11616047730830134",
            "extra": "mean: 11.223949719399979 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.26364739211695,
            "unit": "iter/sec",
            "range": "stddev: 0.0014181791286053873",
            "extra": "mean: 24.836299361090315 msec\nrounds: 36"
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
          "id": "7c88d085f927e741fd741868b7e4b2f415994e64",
          "message": "further improvements",
          "timestamp": "2021-04-22T17:28:36+02:00",
          "tree_id": "4fd33b5eeec0b5598291c513943544f762c000b6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7c88d085f927e741fd741868b7e4b2f415994e64"
        },
        "date": 1619105836132,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055467985387341774,
            "unit": "iter/sec",
            "range": "stddev: 0.14349436583828443",
            "extra": "mean: 18.028417527999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07560961479030928,
            "unit": "iter/sec",
            "range": "stddev: 0.08266836772395096",
            "extra": "mean: 13.225831169400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.73049284740159,
            "unit": "iter/sec",
            "range": "stddev: 0.001082514928382378",
            "extra": "mean: 12.701558999995564 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05578851320851951,
            "unit": "iter/sec",
            "range": "stddev: 0.07134265792097146",
            "extra": "mean: 17.9248368972 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07516673628258995,
            "unit": "iter/sec",
            "range": "stddev: 0.04123705608802503",
            "extra": "mean: 13.303757080000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.33644071875636,
            "unit": "iter/sec",
            "range": "stddev: 0.0014135833333412465",
            "extra": "mean: 26.084842026316316 msec\nrounds: 38"
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
          "id": "66431711c335af14796826e7a043b4f5e6fb7d14",
          "message": "Update pdocs.yml",
          "timestamp": "2021-04-22T17:36:43+02:00",
          "tree_id": "bdeb9bf5cfa1ecf7a11c50b60c95405dca991a36",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/66431711c335af14796826e7a043b4f5e6fb7d14"
        },
        "date": 1619106265615,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06819028734979633,
            "unit": "iter/sec",
            "range": "stddev: 0.08156047430553758",
            "extra": "mean: 14.664845080800012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07610290652011921,
            "unit": "iter/sec",
            "range": "stddev: 0.024443195281446065",
            "extra": "mean: 13.140102602199978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.77454379632827,
            "unit": "iter/sec",
            "range": "stddev: 0.0002484453186082206",
            "extra": "mean: 14.331874428573801 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06852885049482882,
            "unit": "iter/sec",
            "range": "stddev: 0.07636662029157713",
            "extra": "mean: 14.59239419280001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07710377811800144,
            "unit": "iter/sec",
            "range": "stddev: 0.3184109875700369",
            "extra": "mean: 12.96953306840005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.63355233918774,
            "unit": "iter/sec",
            "range": "stddev: 0.0002516439174573339",
            "extra": "mean: 27.29738002858864 msec\nrounds: 35"
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
          "id": "d33da5571bb2ed096f1791fd6b293bc3a0710b2c",
          "message": "Merge pull request #335 from ZedThree/auto-docs\n\nAlways auto-generate the API docs",
          "timestamp": "2021-04-22T20:02:06+02:00",
          "tree_id": "1869ce7eb4f5c3b95006a303cc051ea68d53fe1a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d33da5571bb2ed096f1791fd6b293bc3a0710b2c"
        },
        "date": 1619114988897,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06997961618148411,
            "unit": "iter/sec",
            "range": "stddev: 0.3250989201088424",
            "extra": "mean: 14.289875460399992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07651292738999808,
            "unit": "iter/sec",
            "range": "stddev: 0.13350064995987726",
            "extra": "mean: 13.069686837400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 68.36643466027367,
            "unit": "iter/sec",
            "range": "stddev: 0.00024495558491826225",
            "extra": "mean: 14.627060851852194 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06803534890160336,
            "unit": "iter/sec",
            "range": "stddev: 0.19505642110237564",
            "extra": "mean: 14.698241666199987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07352678411207143,
            "unit": "iter/sec",
            "range": "stddev: 0.41816978814488615",
            "extra": "mean: 13.600486028 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.28272276850664,
            "unit": "iter/sec",
            "range": "stddev: 0.0005335052718730099",
            "extra": "mean: 26.12144402703384 msec\nrounds: 37"
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
          "id": "c54d8d91da7de544aaf7d88368ffd5cefc879448",
          "message": "Merge pull request #336 from ZedThree/fix-SC-logging\n\nFix for logging in SC sampling missing format string",
          "timestamp": "2021-04-23T17:28:23+02:00",
          "tree_id": "d8b3632e6e60617f2250faea42e7ccf60540d893",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c54d8d91da7de544aaf7d88368ffd5cefc879448"
        },
        "date": 1619192104820,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07689243259390426,
            "unit": "iter/sec",
            "range": "stddev: 0.08698923888487983",
            "extra": "mean: 13.005180955599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08835335466367386,
            "unit": "iter/sec",
            "range": "stddev: 0.032429178218402896",
            "extra": "mean: 11.318189374999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.25407826803935,
            "unit": "iter/sec",
            "range": "stddev: 0.00031131448192913503",
            "extra": "mean: 12.778886699997352 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07697304490477443,
            "unit": "iter/sec",
            "range": "stddev: 0.07869356803719285",
            "extra": "mean: 12.991560892999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09085841918027787,
            "unit": "iter/sec",
            "range": "stddev: 0.1617942236273571",
            "extra": "mean: 11.006134698599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.697396773214535,
            "unit": "iter/sec",
            "range": "stddev: 0.0002850995938895053",
            "extra": "mean: 25.190568684210074 msec\nrounds: 38"
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
          "id": "1a7eae14d2cd26d4aa375cdece395c732a206d80",
          "message": "Merge branch 'dev' of https://github.com/UCL-CCS/EasyVVUQ into dev",
          "timestamp": "2021-04-26T12:49:32+02:00",
          "tree_id": "7acbc1a643cd2ddff0abc9e57f01cf41efc1410b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1a7eae14d2cd26d4aa375cdece395c732a206d80"
        },
        "date": 1619434578584,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08160776293468866,
            "unit": "iter/sec",
            "range": "stddev: 0.1533544179472063",
            "extra": "mean: 12.253736213800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09109495810018427,
            "unit": "iter/sec",
            "range": "stddev: 0.15454377486154566",
            "extra": "mean: 10.977555957599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.51289831044097,
            "unit": "iter/sec",
            "range": "stddev: 0.0006113464375038447",
            "extra": "mean: 11.558970044115528 msec\nrounds: 68"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08054876651185423,
            "unit": "iter/sec",
            "range": "stddev: 0.3276794297976144",
            "extra": "mean: 12.414839398599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08354727367110325,
            "unit": "iter/sec",
            "range": "stddev: 0.26043891984396916",
            "extra": "mean: 11.969271480199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.05331980544924,
            "unit": "iter/sec",
            "range": "stddev: 0.000783529600315632",
            "extra": "mean: 24.35856599999653 msec\nrounds: 40"
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
          "id": "92f6d7dda5e59c85208dd2bbb6113075b3054681",
          "message": "enable numpy style for pdoc",
          "timestamp": "2021-04-26T13:54:16+02:00",
          "tree_id": "33f8cf7d3bcde2c9b2060df9f5af8402678ab54c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/92f6d7dda5e59c85208dd2bbb6113075b3054681"
        },
        "date": 1619438552647,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.057321607040059536,
            "unit": "iter/sec",
            "range": "stddev: 0.6894486429643075",
            "extra": "mean: 17.4454285502 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07746965445910863,
            "unit": "iter/sec",
            "range": "stddev: 0.2785995364210629",
            "extra": "mean: 12.908280112800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.21177657078984,
            "unit": "iter/sec",
            "range": "stddev: 0.0013130392858304006",
            "extra": "mean: 12.466997275860901 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05999397587985447,
            "unit": "iter/sec",
            "range": "stddev: 0.08215607475742845",
            "extra": "mean: 16.668340201399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07837642800143022,
            "unit": "iter/sec",
            "range": "stddev: 0.30580010518465767",
            "extra": "mean: 12.758938184599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.3758165101841,
            "unit": "iter/sec",
            "range": "stddev: 0.001148003346304874",
            "extra": "mean: 27.490791848480733 msec\nrounds: 33"
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
          "id": "42c44448fe0557451b28f34626303f05b503dc57",
          "message": "updated sc_analysis docstrings to not crash pdoc",
          "timestamp": "2021-04-26T14:40:17+02:00",
          "tree_id": "5472516559d24e40304757c7d050e5757bd898e8",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/42c44448fe0557451b28f34626303f05b503dc57"
        },
        "date": 1619441322456,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05738397967271257,
            "unit": "iter/sec",
            "range": "stddev: 0.2246270053910005",
            "extra": "mean: 17.4264665104 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07483914417189819,
            "unit": "iter/sec",
            "range": "stddev: 0.1722297683698196",
            "extra": "mean: 13.36199138919999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.5785217223589,
            "unit": "iter/sec",
            "range": "stddev: 0.0007700766306379169",
            "extra": "mean: 11.964796450000867 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.059372371021653915,
            "unit": "iter/sec",
            "range": "stddev: 0.51575163415076",
            "extra": "mean: 16.842851023000016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07406347646289538,
            "unit": "iter/sec",
            "range": "stddev: 0.24547613205121724",
            "extra": "mean: 13.501931691000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.083898669191946,
            "unit": "iter/sec",
            "range": "stddev: 0.0011854556355321282",
            "extra": "mean: 24.947673085716815 msec\nrounds: 35"
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
          "id": "0ea2377e7ce280cb6bd8340e672c24ba647893b3",
          "message": "campaign.py docstring fixes",
          "timestamp": "2021-04-26T15:43:33+02:00",
          "tree_id": "489683fa2370b5614fc02551efd8a723cd9812be",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0ea2377e7ce280cb6bd8340e672c24ba647893b3"
        },
        "date": 1619445149305,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05244050375203695,
            "unit": "iter/sec",
            "range": "stddev: 0.34664489761162415",
            "extra": "mean: 19.069229478199986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07168001321470238,
            "unit": "iter/sec",
            "range": "stddev: 0.22930829982751652",
            "extra": "mean: 13.950890285200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.53474914953264,
            "unit": "iter/sec",
            "range": "stddev: 0.0011175166142407451",
            "extra": "mean: 14.17740917855984 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053907830932232295,
            "unit": "iter/sec",
            "range": "stddev: 0.5857884726805287",
            "extra": "mean: 18.550180608399977 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07233343472774299,
            "unit": "iter/sec",
            "range": "stddev: 0.5070015942180072",
            "extra": "mean: 13.824865413399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.952713757507176,
            "unit": "iter/sec",
            "range": "stddev: 0.001804889829552174",
            "extra": "mean: 27.061611944450053 msec\nrounds: 36"
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
          "id": "585bacc1f12599492be366c20f202a76617882ae",
          "message": "fix docstrings in directory_builder.py",
          "timestamp": "2021-04-26T15:51:57+02:00",
          "tree_id": "5aa8fe5a7e4a6900a720fe1b7602d5bf000f86f1",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/585bacc1f12599492be366c20f202a76617882ae"
        },
        "date": 1619445573315,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06920746106694851,
            "unit": "iter/sec",
            "range": "stddev: 0.14688534442243165",
            "extra": "mean: 14.449309143599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07837616386037682,
            "unit": "iter/sec",
            "range": "stddev: 0.045810583861540764",
            "extra": "mean: 12.75898118440001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.84785792437557,
            "unit": "iter/sec",
            "range": "stddev: 0.00032959415325354565",
            "extra": "mean: 14.114752785714709 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06928498786630884,
            "unit": "iter/sec",
            "range": "stddev: 0.14530135238785957",
            "extra": "mean: 14.433141013599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08040958501007422,
            "unit": "iter/sec",
            "range": "stddev: 0.2817624262190924",
            "extra": "mean: 12.436328329199977 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.56076833293747,
            "unit": "iter/sec",
            "range": "stddev: 0.0006330812039500498",
            "extra": "mean: 26.62352354286343 msec\nrounds: 35"
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
          "id": "bff5feb36447a48fb308c753728363ad66e08c01",
          "message": "added replace_app argument to add_app",
          "timestamp": "2021-04-26T18:27:58+02:00",
          "tree_id": "aa6f49a604ddf3fa5c13edd7116b8d47778b4609",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bff5feb36447a48fb308c753728363ad66e08c01"
        },
        "date": 1619454972099,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05985079606232334,
            "unit": "iter/sec",
            "range": "stddev: 0.24822923444404432",
            "extra": "mean: 16.708215525799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07807540747345568,
            "unit": "iter/sec",
            "range": "stddev: 0.16459341285265572",
            "extra": "mean: 12.808130400599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.94573858422993,
            "unit": "iter/sec",
            "range": "stddev: 0.0012190534746735556",
            "extra": "mean: 14.095279293100257 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0599197242073521,
            "unit": "iter/sec",
            "range": "stddev: 0.1371703568748608",
            "extra": "mean: 16.688995372200008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07767661239939763,
            "unit": "iter/sec",
            "range": "stddev: 0.3353961596466881",
            "extra": "mean: 12.873887893799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.39810518441245,
            "unit": "iter/sec",
            "range": "stddev: 0.0008214443929700067",
            "extra": "mean: 23.58595969443576 msec\nrounds: 36"
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
          "id": "bdbe4ad9e191308004952a3f530cff3235af58f0",
          "message": "malformed constant name in campaign db",
          "timestamp": "2021-04-27T10:15:40+02:00",
          "tree_id": "2aee0c3a64a5d214a9a7a3bd79c49440dc25134d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/bdbe4ad9e191308004952a3f530cff3235af58f0"
        },
        "date": 1619512340908,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07006671481244085,
            "unit": "iter/sec",
            "range": "stddev: 0.12534897041347862",
            "extra": "mean: 14.272111981799991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07810713215386808,
            "unit": "iter/sec",
            "range": "stddev: 0.0714937919369333",
            "extra": "mean: 12.80292813760001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.62973126710033,
            "unit": "iter/sec",
            "range": "stddev: 0.0003944255112434976",
            "extra": "mean: 13.960683396550754 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07005036204890135,
            "unit": "iter/sec",
            "range": "stddev: 0.14525687136396653",
            "extra": "mean: 14.2754437058 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07905765081353298,
            "unit": "iter/sec",
            "range": "stddev: 0.3493324403179966",
            "extra": "mean: 12.64899715219999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.993952028244664,
            "unit": "iter/sec",
            "range": "stddev: 0.000657099240231774",
            "extra": "mean: 26.31997848648651 msec\nrounds: 37"
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
          "id": "97e0882f4cffb33464fefc714eba4e909bd0768d",
          "message": "forgot to remove old arguments",
          "timestamp": "2021-04-27T12:09:48+02:00",
          "tree_id": "08ca162cd151205d9f60d3535c76db5367339207",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/97e0882f4cffb33464fefc714eba4e909bd0768d"
        },
        "date": 1619518680857,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05789467873577579,
            "unit": "iter/sec",
            "range": "stddev: 0.1432822866797716",
            "extra": "mean: 17.272744608599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08024062625762331,
            "unit": "iter/sec",
            "range": "stddev: 0.06335941444381515",
            "extra": "mean: 12.46251489600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.23111331711645,
            "unit": "iter/sec",
            "range": "stddev: 0.0009555017525757962",
            "extra": "mean: 12.463992566667532 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05790437462791618,
            "unit": "iter/sec",
            "range": "stddev: 0.13378850494278735",
            "extra": "mean: 17.269852345799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08004547731155554,
            "unit": "iter/sec",
            "range": "stddev: 0.06195011627477509",
            "extra": "mean: 12.492898207199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.258683143249634,
            "unit": "iter/sec",
            "range": "stddev: 0.0022629984001629145",
            "extra": "mean: 24.839361894718973 msec\nrounds: 38"
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
          "id": "2adb068258ccaa7dc189a68037693e8bd2eb5f9a",
          "message": "add get_distribution to SCAnalysisResults",
          "timestamp": "2021-04-27T10:09:54Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/337/commits/2adb068258ccaa7dc189a68037693e8bd2eb5f9a"
        },
        "date": 1619523025945,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05193586870246923,
            "unit": "iter/sec",
            "range": "stddev: 0.2537006601802222",
            "extra": "mean: 19.254515713000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07356111455943296,
            "unit": "iter/sec",
            "range": "stddev: 0.30353755563749085",
            "extra": "mean: 13.5941387782 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.2227409815852,
            "unit": "iter/sec",
            "range": "stddev: 0.0010055560885686601",
            "extra": "mean: 14.240401129631698 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053744829073872666,
            "unit": "iter/sec",
            "range": "stddev: 0.2461057876944568",
            "extra": "mean: 18.60644116339997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07619844113892667,
            "unit": "iter/sec",
            "range": "stddev: 0.05650104869772995",
            "extra": "mean: 13.123628056599978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.07557754334621,
            "unit": "iter/sec",
            "range": "stddev: 0.000863057621263222",
            "extra": "mean: 27.719583942861654 msec\nrounds: 35"
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
          "id": "24804c22f0a39b103feb968fff1dba50e0354652",
          "message": "Merge pull request #296 from UCL-CCS/gp_improvements\n\nGP improvements",
          "timestamp": "2021-04-27T13:24:35+02:00",
          "tree_id": "fe93c64688045a752d0c3d71be45cd617d1f691c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/24804c22f0a39b103feb968fff1dba50e0354652"
        },
        "date": 1619523126099,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06923658757320864,
            "unit": "iter/sec",
            "range": "stddev: 0.11535314354485843",
            "extra": "mean: 14.443230595999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07802329200988947,
            "unit": "iter/sec",
            "range": "stddev: 0.05303738671805075",
            "extra": "mean: 12.816685559400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.72798094666095,
            "unit": "iter/sec",
            "range": "stddev: 0.00040798108780267916",
            "extra": "mean: 13.941560696426539 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07021071569812683,
            "unit": "iter/sec",
            "range": "stddev: 0.11444057930404739",
            "extra": "mean: 14.242840142800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07917208704142613,
            "unit": "iter/sec",
            "range": "stddev: 0.09214170177630411",
            "extra": "mean: 12.630714148999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 37.17803830446178,
            "unit": "iter/sec",
            "range": "stddev: 0.0005153421099759675",
            "extra": "mean: 26.897599916668785 msec\nrounds: 36"
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
          "id": "2efd1ea67871f57d1e38bf9dd890adb355a6583f",
          "message": "GP improvements",
          "timestamp": "2021-04-27T10:09:54Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/296/commits/2efd1ea67871f57d1e38bf9dd890adb355a6583f"
        },
        "date": 1619523211746,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.050379391163627225,
            "unit": "iter/sec",
            "range": "stddev: 0.09724682312115088",
            "extra": "mean: 19.849386364199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06807564226455216,
            "unit": "iter/sec",
            "range": "stddev: 0.060337910418213375",
            "extra": "mean: 14.689541908599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 69.04638577993347,
            "unit": "iter/sec",
            "range": "stddev: 0.0011315018351341342",
            "extra": "mean: 14.483017303573677 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05113199062945888,
            "unit": "iter/sec",
            "range": "stddev: 0.09798959871362357",
            "extra": "mean: 19.557228022799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06802678775588285,
            "unit": "iter/sec",
            "range": "stddev: 0.06462122887496388",
            "extra": "mean: 14.700091434399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 34.7995792629631,
            "unit": "iter/sec",
            "range": "stddev: 0.001586242701444731",
            "extra": "mean: 28.73597960606069 msec\nrounds: 33"
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
          "id": "920bc24f1106f6eba76ab0e4ce969a5c86584f4c",
          "message": "missing argument",
          "timestamp": "2021-04-27T13:43:08+02:00",
          "tree_id": "055b999058500cb2a6c3ee0d2318696cac59bb7a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/920bc24f1106f6eba76ab0e4ce969a5c86584f4c"
        },
        "date": 1619524232122,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07175661116906046,
            "unit": "iter/sec",
            "range": "stddev: 0.20741274969775358",
            "extra": "mean: 13.935998143000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07837616275344013,
            "unit": "iter/sec",
            "range": "stddev: 0.10294974423349205",
            "extra": "mean: 12.75898136460001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.69666565476388,
            "unit": "iter/sec",
            "range": "stddev: 0.000578495774105012",
            "extra": "mean: 13.94765001785763 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07139871456180429,
            "unit": "iter/sec",
            "range": "stddev: 0.19066841852055977",
            "extra": "mean: 14.005854393000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07910596904173518,
            "unit": "iter/sec",
            "range": "stddev: 0.15989357392703032",
            "extra": "mean: 12.641271096399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.09008757027686,
            "unit": "iter/sec",
            "range": "stddev: 0.0009317785664795769",
            "extra": "mean: 26.253549513504872 msec\nrounds: 37"
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
          "id": "7695cd5f81d6754de027be8fb83d09549155831c",
          "message": "fix gp test",
          "timestamp": "2021-04-27T14:05:05+02:00",
          "tree_id": "2d6e3c1efa87cb42136b9ceeae6479a63cf75031",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7695cd5f81d6754de027be8fb83d09549155831c"
        },
        "date": 1619525645980,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.053287111185363,
            "unit": "iter/sec",
            "range": "stddev: 0.22635500960052532",
            "extra": "mean: 18.766264069399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07051369523701798,
            "unit": "iter/sec",
            "range": "stddev: 0.10599763212069864",
            "extra": "mean: 14.181642255999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 64.262937588049,
            "unit": "iter/sec",
            "range": "stddev: 0.0007858601992646677",
            "extra": "mean: 15.561068907406597 msec\nrounds: 54"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05346130979911886,
            "unit": "iter/sec",
            "range": "stddev: 0.16663174276968393",
            "extra": "mean: 18.705115975600016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07192078266417858,
            "unit": "iter/sec",
            "range": "stddev: 0.2743919269443411",
            "extra": "mean: 13.904186842200033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 33.69513888427705,
            "unit": "iter/sec",
            "range": "stddev: 0.002759278317052526",
            "extra": "mean: 29.6778714411717 msec\nrounds: 34"
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
          "id": "4b7437c12fe232e4d4385a7e756589ea82ee1d38",
          "message": "pass a rundir to all actions",
          "timestamp": "2021-04-27T14:22:57+02:00",
          "tree_id": "3ad27ce782ef8133b9dc5293233d287c6434694b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4b7437c12fe232e4d4385a7e756589ea82ee1d38"
        },
        "date": 1619526630362,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0689221999324729,
            "unit": "iter/sec",
            "range": "stddev: 0.23148918515861514",
            "extra": "mean: 14.509113188200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07864324364139309,
            "unit": "iter/sec",
            "range": "stddev: 0.06289854487174752",
            "extra": "mean: 12.715650495799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 72.7708599422404,
            "unit": "iter/sec",
            "range": "stddev: 0.0003833418788459211",
            "extra": "mean: 13.741764228067646 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07118782342551856,
            "unit": "iter/sec",
            "range": "stddev: 0.13673502263488438",
            "extra": "mean: 14.047346187599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07822961577577849,
            "unit": "iter/sec",
            "range": "stddev: 0.10794476901350555",
            "extra": "mean: 12.782882672799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 36.67808252967503,
            "unit": "iter/sec",
            "range": "stddev: 0.0002827358914567956",
            "extra": "mean: 27.264238777775063 msec\nrounds: 36"
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
          "id": "0580021d6cf0176be42528dca823c34bd4814cc7",
          "message": "remove run_dir updating in add_runs",
          "timestamp": "2021-04-27T14:39:22+02:00",
          "tree_id": "8aca005a11c8a5ca426729701eb35451b176a600",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0580021d6cf0176be42528dca823c34bd4814cc7"
        },
        "date": 1619527695395,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05311073444872723,
            "unit": "iter/sec",
            "range": "stddev: 0.29161482107523423",
            "extra": "mean: 18.828585414600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07381230184351577,
            "unit": "iter/sec",
            "range": "stddev: 0.050464054672836225",
            "extra": "mean: 13.547877183399986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.92895756128661,
            "unit": "iter/sec",
            "range": "stddev: 0.001138132485040444",
            "extra": "mean: 13.170205836065149 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.053405894641210525,
            "unit": "iter/sec",
            "range": "stddev: 0.09562326119649787",
            "extra": "mean: 18.724524824800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07366536962495046,
            "unit": "iter/sec",
            "range": "stddev: 0.13948301336695837",
            "extra": "mean: 13.5748996454 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.21477611882511,
            "unit": "iter/sec",
            "range": "stddev: 0.0005314375611716211",
            "extra": "mean: 24.26314283782422 msec\nrounds: 37"
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
          "id": "e5e259dd527395be956050afce4ef27beb387d46",
          "message": "fix a rundir issue",
          "timestamp": "2021-04-27T15:04:51+02:00",
          "tree_id": "0aa1ad984dc95cee11b169939aedee05006e32ef",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e5e259dd527395be956050afce4ef27beb387d46"
        },
        "date": 1619529147235,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06427126653653255,
            "unit": "iter/sec",
            "range": "stddev: 0.1454959262944748",
            "extra": "mean: 15.559052339999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08458613819903928,
            "unit": "iter/sec",
            "range": "stddev: 0.13790254009353448",
            "extra": "mean: 11.822268060600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 96.50572957160698,
            "unit": "iter/sec",
            "range": "stddev: 0.0007656419777058549",
            "extra": "mean: 10.362079064518161 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06469841372995846,
            "unit": "iter/sec",
            "range": "stddev: 0.1322462830021481",
            "extra": "mean: 15.4563294886 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08832303504986297,
            "unit": "iter/sec",
            "range": "stddev: 0.3410132248055775",
            "extra": "mean: 11.322074693600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 49.08106365168146,
            "unit": "iter/sec",
            "range": "stddev: 0.0016517356740056656",
            "extra": "mean: 20.37445657447037 msec\nrounds: 47"
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
          "id": "16973b3a8d2f64ec816773a9a9d9a34be8b881d5",
          "message": "Fix the issues remaining with replace_actions",
          "timestamp": "2021-04-27T13:04:59Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/338/commits/16973b3a8d2f64ec816773a9a9d9a34be8b881d5"
        },
        "date": 1619604162589,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06561792754819143,
            "unit": "iter/sec",
            "range": "stddev: 0.0808678563907075",
            "extra": "mean: 15.239737635200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07337329280485304,
            "unit": "iter/sec",
            "range": "stddev: 0.029756970723888276",
            "extra": "mean: 13.628937202800012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.91404451247021,
            "unit": "iter/sec",
            "range": "stddev: 0.0001940461631421085",
            "extra": "mean: 13.348631842104584 msec\nrounds: 57"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06587292026622005,
            "unit": "iter/sec",
            "range": "stddev: 0.08258728929952319",
            "extra": "mean: 15.180744924599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0732080962400695,
            "unit": "iter/sec",
            "range": "stddev: 0.06990517085517002",
            "extra": "mean: 13.6596913642 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.617883655749736,
            "unit": "iter/sec",
            "range": "stddev: 0.0004998359762994305",
            "extra": "mean: 25.241126171434708 msec\nrounds: 35"
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
          "id": "24211015d12338d791aa8b812572aba4688e00b7",
          "message": "Merge pull request #338 from UCL-CCS/replace-action-fix\n\nFix the issues remaining with replace_actions",
          "timestamp": "2021-04-28T12:18:29+02:00",
          "tree_id": "5639d1c9b17eb981b8616f27a35f507f34723f36",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/24211015d12338d791aa8b812572aba4688e00b7"
        },
        "date": 1619605557956,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06969142400878887,
            "unit": "iter/sec",
            "range": "stddev: 0.18020494253114214",
            "extra": "mean: 14.348967813799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07883607072520062,
            "unit": "iter/sec",
            "range": "stddev: 0.10653782823061847",
            "extra": "mean: 12.684548973599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.86889341970043,
            "unit": "iter/sec",
            "range": "stddev: 0.0003157779017403311",
            "extra": "mean: 12.842098507939053 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07112658892450265,
            "unit": "iter/sec",
            "range": "stddev: 0.11441568825865966",
            "extra": "mean: 14.059439868000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07944100339672462,
            "unit": "iter/sec",
            "range": "stddev: 0.06267495627433939",
            "extra": "mean: 12.58795782080001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.15886344384023,
            "unit": "iter/sec",
            "range": "stddev: 0.0004272246702283921",
            "extra": "mean: 24.296103349998077 msec\nrounds: 40"
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
          "id": "222c03e2eefe057f9394286ea039524826453165",
          "message": "Fix the issues remaining with replace_actions",
          "timestamp": "2021-04-27T13:04:59Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/338/commits/222c03e2eefe057f9394286ea039524826453165"
        },
        "date": 1619605620001,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0546830872407032,
            "unit": "iter/sec",
            "range": "stddev: 0.10923649288196158",
            "extra": "mean: 18.28718988740001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07188293322568408,
            "unit": "iter/sec",
            "range": "stddev: 0.08143590744441058",
            "extra": "mean: 13.9115079912 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.39184993365546,
            "unit": "iter/sec",
            "range": "stddev: 0.0011616940509425332",
            "extra": "mean: 12.439071881356933 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0547344645372399,
            "unit": "iter/sec",
            "range": "stddev: 0.10026760306365787",
            "extra": "mean: 18.270024352199993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07204840731755059,
            "unit": "iter/sec",
            "range": "stddev: 0.06439741990887525",
            "extra": "mean: 13.879557331399962 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.64164807228748,
            "unit": "iter/sec",
            "range": "stddev: 0.0013227804581029622",
            "extra": "mean: 24.014419368418324 msec\nrounds: 38"
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
          "id": "abdd4418e98a80c1e92514ae5bda89f0df3dfbf6",
          "message": "Update requirements.txt",
          "timestamp": "2021-04-28T12:34:20+02:00",
          "tree_id": "5639d1c9b17eb981b8616f27a35f507f34723f36",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/abdd4418e98a80c1e92514ae5bda89f0df3dfbf6"
        },
        "date": 1619606456602,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07717668776987033,
            "unit": "iter/sec",
            "range": "stddev: 0.09135246043047864",
            "extra": "mean: 12.957280610199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08813654442769078,
            "unit": "iter/sec",
            "range": "stddev: 0.03678826884001813",
            "extra": "mean: 11.346031393599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 89.90439176501185,
            "unit": "iter/sec",
            "range": "stddev: 0.00018890701723569737",
            "extra": "mean: 11.122927149251575 msec\nrounds: 67"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07707559197600693,
            "unit": "iter/sec",
            "range": "stddev: 0.10014970373453316",
            "extra": "mean: 12.974275959 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09397826932313613,
            "unit": "iter/sec",
            "range": "stddev: 0.8616723904903544",
            "extra": "mean: 10.640757775199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.898895212986815,
            "unit": "iter/sec",
            "range": "stddev: 0.0004681320421910858",
            "extra": "mean: 19.268232895827946 msec\nrounds: 48"
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
          "id": "508c1ff0ce71876001c4091a4e9a7455b959f67e",
          "message": "skip one test",
          "timestamp": "2021-04-28T12:35:54+02:00",
          "tree_id": "fa4c84430b9b37778d1eb37c4aa7766d9a56ddd1",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/508c1ff0ce71876001c4091a4e9a7455b959f67e"
        },
        "date": 1619606613340,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06932497673514512,
            "unit": "iter/sec",
            "range": "stddev: 0.1067474240277133",
            "extra": "mean: 14.424815515199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07771092087091581,
            "unit": "iter/sec",
            "range": "stddev: 0.046935032624519715",
            "extra": "mean: 12.868204221399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 73.10740286535264,
            "unit": "iter/sec",
            "range": "stddev: 0.0001260996623827738",
            "extra": "mean: 13.67850533333505 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06920973624009034,
            "unit": "iter/sec",
            "range": "stddev: 0.10329099638331081",
            "extra": "mean: 14.448834142800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07737177138180745,
            "unit": "iter/sec",
            "range": "stddev: 0.06381364673872575",
            "extra": "mean: 12.924610386199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.65924788103266,
            "unit": "iter/sec",
            "range": "stddev: 0.00014186655365037727",
            "extra": "mean: 25.867031947370833 msec\nrounds: 38"
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
          "id": "e4179bd165efa40cd4b2891bb96066b16e674eb7",
          "message": "missing import",
          "timestamp": "2021-04-28T12:37:55+02:00",
          "tree_id": "4c5d6deedba0bde5ab6345f820fe9a8c36b65992",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e4179bd165efa40cd4b2891bb96066b16e674eb7"
        },
        "date": 1619606780252,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055671449834398395,
            "unit": "iter/sec",
            "range": "stddev: 0.13046848629126728",
            "extra": "mean: 17.962528423000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07643080116027481,
            "unit": "iter/sec",
            "range": "stddev: 0.1933209980877488",
            "extra": "mean: 13.083730444000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.0314531559948,
            "unit": "iter/sec",
            "range": "stddev: 0.0009641373270561612",
            "extra": "mean: 12.19044600000385 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05608433241148082,
            "unit": "iter/sec",
            "range": "stddev: 0.1428100587710985",
            "extra": "mean: 17.830291580600033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07946999056937959,
            "unit": "iter/sec",
            "range": "stddev: 0.09344489899206886",
            "extra": "mean: 12.583366285000011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 44.27885751985003,
            "unit": "iter/sec",
            "range": "stddev: 0.0013339606881981215",
            "extra": "mean: 22.584141868423416 msec\nrounds: 38"
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
          "id": "a7d58e7bf8ef625545df2075ebe42fa52c0b04b3",
          "message": "unused import in campaign.py",
          "timestamp": "2021-04-28T12:44:00+02:00",
          "tree_id": "35aa5ccee33a0dc7eb5fedfc9bb7facf1e96021d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/a7d58e7bf8ef625545df2075ebe42fa52c0b04b3"
        },
        "date": 1619607040339,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07676827276683183,
            "unit": "iter/sec",
            "range": "stddev: 0.10437854217511175",
            "extra": "mean: 13.02621465819999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08929161738483526,
            "unit": "iter/sec",
            "range": "stddev: 0.04872859125726669",
            "extra": "mean: 11.199259564199963 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.59987771615215,
            "unit": "iter/sec",
            "range": "stddev: 0.00014391594716335038",
            "extra": "mean: 12.406966714288211 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0772256059532733,
            "unit": "iter/sec",
            "range": "stddev: 0.11346305619881608",
            "extra": "mean: 12.949072883999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09446003831112312,
            "unit": "iter/sec",
            "range": "stddev: 0.061927895875865405",
            "extra": "mean: 10.586487342999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.52930655181187,
            "unit": "iter/sec",
            "range": "stddev: 0.0001302618918251117",
            "extra": "mean: 22.973028499999753 msec\nrounds: 42"
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
          "id": "1080a9e623cb36362497c64beb0323471a316b07",
          "message": "unused import in sql.py",
          "timestamp": "2021-04-28T12:44:57+02:00",
          "tree_id": "e2415bf7d3cf3e7b7c2618f99c5a23cca56637fb",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1080a9e623cb36362497c64beb0323471a316b07"
        },
        "date": 1619607129466,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07203648481603521,
            "unit": "iter/sec",
            "range": "stddev: 0.27650297858237466",
            "extra": "mean: 13.881854487399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08290594601028602,
            "unit": "iter/sec",
            "range": "stddev: 0.06032009251780646",
            "extra": "mean: 12.061861037999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.97235619422788,
            "unit": "iter/sec",
            "range": "stddev: 0.0005919382044928495",
            "extra": "mean: 12.349893803279064 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07136013241094757,
            "unit": "iter/sec",
            "range": "stddev: 0.20425055094273753",
            "extra": "mean: 14.013426912399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08905555624048578,
            "unit": "iter/sec",
            "range": "stddev: 0.29842124612071796",
            "extra": "mean: 11.228945640400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.9809005290267,
            "unit": "iter/sec",
            "range": "stddev: 0.0006381238087236827",
            "extra": "mean: 23.820356099997753 msec\nrounds: 40"
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
          "id": "8be84414cff0b83de7c3e52f404c0bcb0bf0142a",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-28T10:45:03Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/8be84414cff0b83de7c3e52f404c0bcb0bf0142a"
        },
        "date": 1619623833459,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05131676692013295,
            "unit": "iter/sec",
            "range": "stddev: 0.17807657517394848",
            "extra": "mean: 19.486808308800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06797291567482897,
            "unit": "iter/sec",
            "range": "stddev: 0.06255360845786931",
            "extra": "mean: 14.711742023599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 65.52910558898544,
            "unit": "iter/sec",
            "range": "stddev: 0.0011893402924197248",
            "extra": "mean: 15.260394461542695 msec\nrounds: 52"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05042677824424863,
            "unit": "iter/sec",
            "range": "stddev: 0.1596644333542191",
            "extra": "mean: 19.830733487599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07074735221647278,
            "unit": "iter/sec",
            "range": "stddev: 0.24767037143481868",
            "extra": "mean: 14.134804606399962 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 35.46748923682287,
            "unit": "iter/sec",
            "range": "stddev: 0.0007519037102996442",
            "extra": "mean: 28.194834805554418 msec\nrounds: 36"
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
          "id": "d33d58d1558043444089db886613cc3db7c88d7a",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-28T10:45:03Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/d33d58d1558043444089db886613cc3db7c88d7a"
        },
        "date": 1619623941768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0770159623170901,
            "unit": "iter/sec",
            "range": "stddev: 0.10805674680229033",
            "extra": "mean: 12.984321300600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09001955081386563,
            "unit": "iter/sec",
            "range": "stddev: 0.043560741614028564",
            "extra": "mean: 11.1086979546 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.307448730787,
            "unit": "iter/sec",
            "range": "stddev: 0.00017427766488437038",
            "extra": "mean: 12.452145047619174 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07713031151741431,
            "unit": "iter/sec",
            "range": "stddev: 0.09237976751165569",
            "extra": "mean: 12.965071452800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09026491016856722,
            "unit": "iter/sec",
            "range": "stddev: 0.05932814143707927",
            "extra": "mean: 11.078502134799976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.941580200828284,
            "unit": "iter/sec",
            "range": "stddev: 0.00018703992263119685",
            "extra": "mean: 23.28745228571517 msec\nrounds: 42"
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
          "id": "e57f4eff0325caaff8ada4a83a297a5279ae4515",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-28T10:45:03Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/e57f4eff0325caaff8ada4a83a297a5279ae4515"
        },
        "date": 1619626753718,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05421751113370484,
            "unit": "iter/sec",
            "range": "stddev: 0.2313211728201684",
            "extra": "mean: 18.444225474199982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07265694234899148,
            "unit": "iter/sec",
            "range": "stddev: 0.3679890283320739",
            "extra": "mean: 13.763309708199973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.8195671686025,
            "unit": "iter/sec",
            "range": "stddev: 0.0009445207792938489",
            "extra": "mean: 12.687204915257976 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05560843789420234,
            "unit": "iter/sec",
            "range": "stddev: 0.1566719975222887",
            "extra": "mean: 17.98288241619998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07635147440557843,
            "unit": "iter/sec",
            "range": "stddev: 0.1334826600756058",
            "extra": "mean: 13.097324023999954 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.14426305033981,
            "unit": "iter/sec",
            "range": "stddev: 0.0014726992269278075",
            "extra": "mean: 24.910159609756125 msec\nrounds: 41"
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
          "id": "61a8e6f163210bf2fa00147aa4435922c0a0f262",
          "message": "added an error message",
          "timestamp": "2021-04-28T18:25:19+02:00",
          "tree_id": "d0abe08806a398d2e8bb13b85029cd17b81c7c11",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/61a8e6f163210bf2fa00147aa4435922c0a0f262"
        },
        "date": 1619627656236,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.054910983913525196,
            "unit": "iter/sec",
            "range": "stddev: 0.15778845298904232",
            "extra": "mean: 18.211292691 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0703244764055738,
            "unit": "iter/sec",
            "range": "stddev: 0.1606552560900217",
            "extra": "mean: 14.21980014799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 79.96780712771496,
            "unit": "iter/sec",
            "range": "stddev: 0.0012079177547140454",
            "extra": "mean: 12.50503216129111 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.055229185319164376,
            "unit": "iter/sec",
            "range": "stddev: 0.14222890354926906",
            "extra": "mean: 18.106368837800016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.06859488158884877,
            "unit": "iter/sec",
            "range": "stddev: 0.3464781962538191",
            "extra": "mean: 14.578347200799987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.236400945553996,
            "unit": "iter/sec",
            "range": "stddev: 0.001744743854565429",
            "extra": "mean: 24.250418976193835 msec\nrounds: 42"
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
          "id": "591508d8b9d4107a6e3daad2157b4b6fcb40f757",
          "message": "Update README.md",
          "timestamp": "2021-04-29T08:49:54+02:00",
          "tree_id": "3028ec7525d131ccb743de84783da7b5bebff85f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/591508d8b9d4107a6e3daad2157b4b6fcb40f757"
        },
        "date": 1619679454877,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06928173045194537,
            "unit": "iter/sec",
            "range": "stddev: 0.1315604303042246",
            "extra": "mean: 14.433819615599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07486570330320053,
            "unit": "iter/sec",
            "range": "stddev: 0.043942312329160446",
            "extra": "mean: 13.357251129399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.15786110633356,
            "unit": "iter/sec",
            "range": "stddev: 0.00023752149361671893",
            "extra": "mean: 12.794618300000593 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06951427538245365,
            "unit": "iter/sec",
            "range": "stddev: 0.09282294961352493",
            "extra": "mean: 14.3855344028 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07428496792817155,
            "unit": "iter/sec",
            "range": "stddev: 0.09406068394656701",
            "extra": "mean: 13.461673712599985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.98696027276087,
            "unit": "iter/sec",
            "range": "stddev: 0.00013181549804494093",
            "extra": "mean: 25.008152487179686 msec\nrounds: 39"
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
          "id": "51d89ac0e7115e66de8f167f48a0637c077b100d",
          "message": "AnalysisResults docstring updates",
          "timestamp": "2021-04-29T13:18:11+02:00",
          "tree_id": "cdc263cdc67da88dda1dcb3ab414b5618b96c123",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/51d89ac0e7115e66de8f167f48a0637c077b100d"
        },
        "date": 1619695550723,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06901781683436309,
            "unit": "iter/sec",
            "range": "stddev: 0.07656135999281419",
            "extra": "mean: 14.489012343000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07510840823288675,
            "unit": "iter/sec",
            "range": "stddev: 0.06721074483693765",
            "extra": "mean: 13.314088575799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.31756114585747,
            "unit": "iter/sec",
            "range": "stddev: 0.00018657027668064335",
            "extra": "mean: 13.277116050842825 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06992289470861524,
            "unit": "iter/sec",
            "range": "stddev: 0.08957671665979068",
            "extra": "mean: 14.301467411600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07912487263187351,
            "unit": "iter/sec",
            "range": "stddev: 0.04976444574487241",
            "extra": "mean: 12.638250991600012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.43560007047946,
            "unit": "iter/sec",
            "range": "stddev: 0.00022532120822180412",
            "extra": "mean: 24.73068282050952 msec\nrounds: 39"
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
          "id": "9f35e658d7008d0d68dc1c19fa6ae1c785728d91",
          "message": "removed some unused things in AnalysisResults",
          "timestamp": "2021-04-29T13:41:37+02:00",
          "tree_id": "a8f058b7c3be00a17f22a4f5d7c8e6604d0429c2",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9f35e658d7008d0d68dc1c19fa6ae1c785728d91"
        },
        "date": 1619696901795,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07671620974559269,
            "unit": "iter/sec",
            "range": "stddev: 0.08774121782693885",
            "extra": "mean: 13.035054825 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09002752256131784,
            "unit": "iter/sec",
            "range": "stddev: 0.038511567752127676",
            "extra": "mean: 11.107714302800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 84.68725287405097,
            "unit": "iter/sec",
            "range": "stddev: 0.0003123824004737854",
            "extra": "mean: 11.80815253846084 msec\nrounds: 65"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0768658645768549,
            "unit": "iter/sec",
            "range": "stddev: 0.08441546619023774",
            "extra": "mean: 13.00967608320001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09011990756540528,
            "unit": "iter/sec",
            "range": "stddev: 0.05963644547037029",
            "extra": "mean: 11.096327404399982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 44.30504953923185,
            "unit": "iter/sec",
            "range": "stddev: 0.00019765578250198295",
            "extra": "mean: 22.570790697672194 msec\nrounds: 43"
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
          "id": "265550d34df265f309c33397fae3fac1780156a0",
          "message": "added a docstring to supported_stats",
          "timestamp": "2021-04-29T13:46:22+02:00",
          "tree_id": "ace745b4b319e2f02d0168707439869083ceb578",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/265550d34df265f309c33397fae3fac1780156a0"
        },
        "date": 1619697177480,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08052619156630358,
            "unit": "iter/sec",
            "range": "stddev: 0.09031135966856522",
            "extra": "mean: 12.41831981060002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08970852813284125,
            "unit": "iter/sec",
            "range": "stddev: 0.06427956006017709",
            "extra": "mean: 11.147212208399969 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.47223827140367,
            "unit": "iter/sec",
            "range": "stddev: 0.0006229825319734732",
            "extra": "mean: 11.30298068115254 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08153740863245619,
            "unit": "iter/sec",
            "range": "stddev: 0.13246662870642653",
            "extra": "mean: 12.26430931240004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09548139618324114,
            "unit": "iter/sec",
            "range": "stddev: 0.1299996797701126",
            "extra": "mean: 10.473244422200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.25897769475244,
            "unit": "iter/sec",
            "range": "stddev: 0.001021287142180707",
            "extra": "mean: 21.6174254130445 msec\nrounds: 46"
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
          "id": "f7582b911a0ea2a9c9d897d0a99565930f18f3b2",
          "message": "more docstring editing in results.py",
          "timestamp": "2021-04-29T14:29:40+02:00",
          "tree_id": "dbf0d580595a6fadbc68bbc6defa9ca86c1651d0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f7582b911a0ea2a9c9d897d0a99565930f18f3b2"
        },
        "date": 1619699888707,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05790108902314751,
            "unit": "iter/sec",
            "range": "stddev: 0.5947111241433523",
            "extra": "mean: 17.270832325800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07438454909237055,
            "unit": "iter/sec",
            "range": "stddev: 0.1748549184507827",
            "extra": "mean: 13.443652105199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.65361451636623,
            "unit": "iter/sec",
            "range": "stddev: 0.0007176604069727478",
            "extra": "mean: 11.95405608928419 msec\nrounds: 56"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.057437463216255195,
            "unit": "iter/sec",
            "range": "stddev: 0.1210137510016508",
            "extra": "mean: 17.410239659000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07518470024734379,
            "unit": "iter/sec",
            "range": "stddev: 0.08392772876787022",
            "extra": "mean: 13.3005783984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.94259224893759,
            "unit": "iter/sec",
            "range": "stddev: 0.0008493603141721785",
            "extra": "mean: 23.286903459460813 msec\nrounds: 37"
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
          "id": "49a3d200384a06ae21b1f1572263b7a3499de7f9",
          "message": "sobols_second docstring",
          "timestamp": "2021-04-29T16:40:04+02:00",
          "tree_id": "2624117351b11370b98a5c1884b48293f3c8e585",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/49a3d200384a06ae21b1f1572263b7a3499de7f9"
        },
        "date": 1619707735057,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.056350703812523224,
            "unit": "iter/sec",
            "range": "stddev: 0.15788672231234685",
            "extra": "mean: 17.746007278400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07451274295100685,
            "unit": "iter/sec",
            "range": "stddev: 0.03825410739060538",
            "extra": "mean: 13.42052326080002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 82.19699723000836,
            "unit": "iter/sec",
            "range": "stddev: 0.0005424760592975356",
            "extra": "mean: 12.16589454237291 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.056434169105378275,
            "unit": "iter/sec",
            "range": "stddev: 0.12840936909680703",
            "extra": "mean: 17.719761198800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07448699225436872,
            "unit": "iter/sec",
            "range": "stddev: 0.1062295840672152",
            "extra": "mean: 13.425162833599973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.23984746695374,
            "unit": "iter/sec",
            "range": "stddev: 0.0010303324190096838",
            "extra": "mean: 24.248392305556383 msec\nrounds: 36"
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
          "id": "d9ca8dea8a641318670d3cfbeec93e12e4244b41",
          "message": "better docstrings in sobols_total etc",
          "timestamp": "2021-04-29T16:45:49+02:00",
          "tree_id": "cfd7fc9a1ae29ce5e590ecb235164d2ebe9261a4",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d9ca8dea8a641318670d3cfbeec93e12e4244b41"
        },
        "date": 1619708071903,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05389825932100908,
            "unit": "iter/sec",
            "range": "stddev: 0.11807552007632334",
            "extra": "mean: 18.553474872799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07262507224842957,
            "unit": "iter/sec",
            "range": "stddev: 0.08942872627742214",
            "extra": "mean: 13.769349468999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 81.41682328652043,
            "unit": "iter/sec",
            "range": "stddev: 0.0004920546881784057",
            "extra": "mean: 12.28247381356087 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05452293881767125,
            "unit": "iter/sec",
            "range": "stddev: 0.1895458432675513",
            "extra": "mean: 18.34090424480005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07778852315782783,
            "unit": "iter/sec",
            "range": "stddev: 0.0531236682233669",
            "extra": "mean: 12.855366825400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.852721280309595,
            "unit": "iter/sec",
            "range": "stddev: 0.0009418255585039558",
            "extra": "mean: 23.893308951226285 msec\nrounds: 41"
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
          "id": "c5ca7c3fe916baea8f01300feb5203374df5ce39",
          "message": "added surrogate docstring",
          "timestamp": "2021-04-29T16:49:36+02:00",
          "tree_id": "0b149d8bd6ab16f1f3dd7ffab497a299a955ec8a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c5ca7c3fe916baea8f01300feb5203374df5ce39"
        },
        "date": 1619708248768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0688582800400931,
            "unit": "iter/sec",
            "range": "stddev: 0.12117875217568252",
            "extra": "mean: 14.522581734800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07597005764689736,
            "unit": "iter/sec",
            "range": "stddev: 0.045087558416786445",
            "extra": "mean: 13.163080705399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.14482352234721,
            "unit": "iter/sec",
            "range": "stddev: 0.00022757488487347059",
            "extra": "mean: 13.487118216669575 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06899553839637548,
            "unit": "iter/sec",
            "range": "stddev: 0.08599821410876858",
            "extra": "mean: 14.493690798599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07597710862220428,
            "unit": "iter/sec",
            "range": "stddev: 0.09846327005862027",
            "extra": "mean: 13.161859119600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.8707319948988,
            "unit": "iter/sec",
            "range": "stddev: 0.00023328346343620928",
            "extra": "mean: 25.726297105267662 msec\nrounds: 38"
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
          "id": "4ce754a77616770d29a454869b34e43e86979dd3",
          "message": "removed unused code in results.py",
          "timestamp": "2021-04-29T17:11:19+02:00",
          "tree_id": "a78886b21b6179a11ae1ae2574901a0c42aabe66",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4ce754a77616770d29a454869b34e43e86979dd3"
        },
        "date": 1619709616186,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05390039743197706,
            "unit": "iter/sec",
            "range": "stddev: 0.26968830072976196",
            "extra": "mean: 18.552738897000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07333353411732313,
            "unit": "iter/sec",
            "range": "stddev: 0.15252858365283012",
            "extra": "mean: 13.63632630059999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 84.88356062202291,
            "unit": "iter/sec",
            "range": "stddev: 0.0009898397047767502",
            "extra": "mean: 11.780844166668375 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05450716746608266,
            "unit": "iter/sec",
            "range": "stddev: 0.33491843991174136",
            "extra": "mean: 18.3462110854 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07342177568233577,
            "unit": "iter/sec",
            "range": "stddev: 0.19660453121890692",
            "extra": "mean: 13.619937555400009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 42.91608423639402,
            "unit": "iter/sec",
            "range": "stddev: 0.0015858056287969154",
            "extra": "mean: 23.301287099999968 msec\nrounds: 40"
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
          "id": "b907b4bfa382e02839f1ee09ab5b3871d93486f1",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-29T15:11:28Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/b907b4bfa382e02839f1ee09ab5b3871d93486f1"
        },
        "date": 1619792533574,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06768268635153642,
            "unit": "iter/sec",
            "range": "stddev: 0.386407876878913",
            "extra": "mean: 14.774827269799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07217825075372229,
            "unit": "iter/sec",
            "range": "stddev: 0.29830326391246254",
            "extra": "mean: 13.85458901479999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 71.23770966070447,
            "unit": "iter/sec",
            "range": "stddev: 0.0011398623156854046",
            "extra": "mean: 14.037509133334918 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06619639285886396,
            "unit": "iter/sec",
            "range": "stddev: 0.29728750601630466",
            "extra": "mean: 15.106563315800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07541630893125295,
            "unit": "iter/sec",
            "range": "stddev: 0.33520819333999435",
            "extra": "mean: 13.2597314052 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.23525454290235,
            "unit": "iter/sec",
            "range": "stddev: 0.0003015544603601169",
            "extra": "mean: 24.853825615386935 msec\nrounds: 39"
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
          "id": "5111b2062073340c4e8c3c743a873905e766dd40",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-29T15:11:28Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/5111b2062073340c4e8c3c743a873905e766dd40"
        },
        "date": 1619795007449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0677666200274483,
            "unit": "iter/sec",
            "range": "stddev: 0.08985197546259097",
            "extra": "mean: 14.756527617800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07036041716715143,
            "unit": "iter/sec",
            "range": "stddev: 0.03776117362130551",
            "extra": "mean: 14.212536540600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.09497841316174,
            "unit": "iter/sec",
            "range": "stddev: 0.00018819384801063463",
            "extra": "mean: 13.316469637931638 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06881173172541988,
            "unit": "iter/sec",
            "range": "stddev: 0.09280002590945612",
            "extra": "mean: 14.53240566579998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07457460853315631,
            "unit": "iter/sec",
            "range": "stddev: 0.05314088340105436",
            "extra": "mean: 13.409389867000026 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.753162705052645,
            "unit": "iter/sec",
            "range": "stddev: 0.00023901308163687496",
            "extra": "mean: 25.15523123076946 msec\nrounds: 39"
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
          "id": "5a4832bdb019f8cf74bd0297a6dd32646c7ff9ca",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-04-29T15:11:28Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/5a4832bdb019f8cf74bd0297a6dd32646c7ff9ca"
        },
        "date": 1619795486249,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06166066324542779,
            "unit": "iter/sec",
            "range": "stddev: 0.16521073184809504",
            "extra": "mean: 16.217795063599986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08168541987534583,
            "unit": "iter/sec",
            "range": "stddev: 0.09646053249193641",
            "extra": "mean: 12.242086794999977 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 91.49556500416014,
            "unit": "iter/sec",
            "range": "stddev: 0.0006614157933213315",
            "extra": "mean: 10.929491499992723 msec\nrounds: 68"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06280813498300276,
            "unit": "iter/sec",
            "range": "stddev: 0.1169155328962506",
            "extra": "mean: 15.921504440000035 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08614980131750676,
            "unit": "iter/sec",
            "range": "stddev: 0.047803813006576656",
            "extra": "mean: 11.607687826399978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 46.47459423844246,
            "unit": "iter/sec",
            "range": "stddev: 0.0014588201442258418",
            "extra": "mean: 21.517132454549294 msec\nrounds: 44"
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
          "id": "d964883f3270cff97807d6ff8a2d568dc1de87cf",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/d964883f3270cff97807d6ff8a2d568dc1de87cf"
        },
        "date": 1620040855731,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06957982394419537,
            "unit": "iter/sec",
            "range": "stddev: 0.17529900766063627",
            "extra": "mean: 14.371982326400007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07809148335985487,
            "unit": "iter/sec",
            "range": "stddev: 0.19201274168949756",
            "extra": "mean: 12.805493723200016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 76.2231384727087,
            "unit": "iter/sec",
            "range": "stddev: 0.00043382872948038434",
            "extra": "mean: 13.119375822579713 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07055621282169744,
            "unit": "iter/sec",
            "range": "stddev: 0.07726204433910275",
            "extra": "mean: 14.17309631579999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08009137380847452,
            "unit": "iter/sec",
            "range": "stddev: 0.19732483142311383",
            "extra": "mean: 12.485739130799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.28038159439926,
            "unit": "iter/sec",
            "range": "stddev: 0.0007748475238250474",
            "extra": "mean: 24.224582268291712 msec\nrounds: 41"
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
          "id": "fe86176a48c8cf0e3b683f85be83da1305216a01",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/fe86176a48c8cf0e3b683f85be83da1305216a01"
        },
        "date": 1620042042899,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07763644533726041,
            "unit": "iter/sec",
            "range": "stddev: 0.11003718433913573",
            "extra": "mean: 12.880548505999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0867529647772056,
            "unit": "iter/sec",
            "range": "stddev: 0.15145530193586257",
            "extra": "mean: 11.526983574199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 87.4095755383691,
            "unit": "iter/sec",
            "range": "stddev: 0.0008540383736110869",
            "extra": "mean: 11.44039418840379 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0771028069491092,
            "unit": "iter/sec",
            "range": "stddev: 0.2742712806355217",
            "extra": "mean: 12.969696429600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08534678061542064,
            "unit": "iter/sec",
            "range": "stddev: 0.14929346028410015",
            "extra": "mean: 11.716903587799981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.84293256167867,
            "unit": "iter/sec",
            "range": "stddev: 0.0017159377149225414",
            "extra": "mean: 21.813613224995265 msec\nrounds: 40"
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
          "id": "90b76c96187f9da6bcbd49fc5c214ce49a1596c2",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/90b76c96187f9da6bcbd49fc5c214ce49a1596c2"
        },
        "date": 1620043180526,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07155259067597516,
            "unit": "iter/sec",
            "range": "stddev: 0.08716393808688033",
            "extra": "mean: 13.975734359200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08149858669656197,
            "unit": "iter/sec",
            "range": "stddev: 0.10361904475825268",
            "extra": "mean: 12.270151428799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.86273193622308,
            "unit": "iter/sec",
            "range": "stddev: 0.00041602141205291147",
            "extra": "mean: 12.366636348481348 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07134201445455078,
            "unit": "iter/sec",
            "range": "stddev: 0.14174725053061174",
            "extra": "mean: 14.01698575019999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08177051547358025,
            "unit": "iter/sec",
            "range": "stddev: 0.06877680959094479",
            "extra": "mean: 12.229346900999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.98731620526309,
            "unit": "iter/sec",
            "range": "stddev: 0.0007388413023884187",
            "extra": "mean: 23.816716341461483 msec\nrounds: 41"
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
          "id": "9581430314ad29e8d07c2633463f34b5e3ac3635",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/9581430314ad29e8d07c2633463f34b5e3ac3635"
        },
        "date": 1620044891922,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06629005345266796,
            "unit": "iter/sec",
            "range": "stddev: 0.10239326205543295",
            "extra": "mean: 15.08521939440001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07287145762107235,
            "unit": "iter/sec",
            "range": "stddev: 0.05666273361472566",
            "extra": "mean: 13.722793980600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.08742334091812,
            "unit": "iter/sec",
            "range": "stddev: 0.00017278487196737744",
            "extra": "mean: 13.497567534484697 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06658386087323463,
            "unit": "iter/sec",
            "range": "stddev: 0.09396858754650644",
            "extra": "mean: 15.018654474000016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0729140348496173,
            "unit": "iter/sec",
            "range": "stddev: 0.05280217454169242",
            "extra": "mean: 13.7147807286 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.65174700318365,
            "unit": "iter/sec",
            "range": "stddev: 0.00020983078644891013",
            "extra": "mean: 25.87205178378179 msec\nrounds: 37"
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
          "id": "7e9b5a4767f58f9eeda098385ddac4ead1153dac",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/7e9b5a4767f58f9eeda098385ddac4ead1153dac"
        },
        "date": 1620058478581,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0548387292225085,
            "unit": "iter/sec",
            "range": "stddev: 0.3515986506484777",
            "extra": "mean: 18.235287618400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07348568370768635,
            "unit": "iter/sec",
            "range": "stddev: 0.6832732522181927",
            "extra": "mean: 13.608092754200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.21362050274949,
            "unit": "iter/sec",
            "range": "stddev: 0.0012976518842688395",
            "extra": "mean: 13.295464216663314 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05530985822503,
            "unit": "iter/sec",
            "range": "stddev: 0.3165930960757249",
            "extra": "mean: 18.079959560400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07412835271647653,
            "unit": "iter/sec",
            "range": "stddev: 0.3246326874012714",
            "extra": "mean: 13.490114960800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.343199240480004,
            "unit": "iter/sec",
            "range": "stddev: 0.0020003176062704632",
            "extra": "mean: 24.18777497559692 msec\nrounds: 41"
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
          "id": "4bfe9ac350d07813114835125a8cce09eb76a3d7",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/4bfe9ac350d07813114835125a8cce09eb76a3d7"
        },
        "date": 1620124254343,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07715765647103297,
            "unit": "iter/sec",
            "range": "stddev: 0.08802338259987808",
            "extra": "mean: 12.960476584399975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09133292852774655,
            "unit": "iter/sec",
            "range": "stddev: 0.04967290358605058",
            "extra": "mean: 10.94895363720002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 86.79433817790624,
            "unit": "iter/sec",
            "range": "stddev: 0.0005024581407956622",
            "extra": "mean: 11.521488855070881 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0773648266685902,
            "unit": "iter/sec",
            "range": "stddev: 0.0755144609848097",
            "extra": "mean: 12.92577057379999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09524648818265453,
            "unit": "iter/sec",
            "range": "stddev: 0.14123413084449155",
            "extra": "mean: 10.499074759400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 44.63378034090313,
            "unit": "iter/sec",
            "range": "stddev: 0.0003937897393295044",
            "extra": "mean: 22.404555302334174 msec\nrounds: 43"
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
          "id": "dea541904badcca918e641f10e4333b1134fcdc1",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/dea541904badcca918e641f10e4333b1134fcdc1"
        },
        "date": 1620135997376,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07611878977608058,
            "unit": "iter/sec",
            "range": "stddev: 0.09467853988277675",
            "extra": "mean: 13.137360734999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08952126544167976,
            "unit": "iter/sec",
            "range": "stddev: 0.04177063802123281",
            "extra": "mean: 11.170530209399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.18316681641562,
            "unit": "iter/sec",
            "range": "stddev: 0.00023334754127286308",
            "extra": "mean: 12.021663015150525 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0762757848100101,
            "unit": "iter/sec",
            "range": "stddev: 0.0958118336078313",
            "extra": "mean: 13.11032069339999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08942745929030155,
            "unit": "iter/sec",
            "range": "stddev: 0.04865514768611036",
            "extra": "mean: 11.182247689199983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.489762526586254,
            "unit": "iter/sec",
            "range": "stddev: 0.0001499689838795585",
            "extra": "mean: 22.99391723255968 msec\nrounds: 43"
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
          "id": "99d6a93f47c75c3e422ae024e6ffd2620a13e81e",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/99d6a93f47c75c3e422ae024e6ffd2620a13e81e"
        },
        "date": 1620145756985,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07382336928966272,
            "unit": "iter/sec",
            "range": "stddev: 0.13422473254270387",
            "extra": "mean: 13.5458461138 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08187470445120955,
            "unit": "iter/sec",
            "range": "stddev: 0.09686528243842059",
            "extra": "mean: 12.213784546799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.74119630986434,
            "unit": "iter/sec",
            "range": "stddev: 0.00040062448983121994",
            "extra": "mean: 12.385251218749005 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07411737208347773,
            "unit": "iter/sec",
            "range": "stddev: 0.18680951111872118",
            "extra": "mean: 13.492113547600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08192929506581156,
            "unit": "iter/sec",
            "range": "stddev: 0.06831212529855808",
            "extra": "mean: 12.205646334400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 43.05623448032363,
            "unit": "iter/sec",
            "range": "stddev: 0.0006263696915944994",
            "extra": "mean: 23.22544021951089 msec\nrounds: 41"
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
          "id": "9de1f9427b8c356e70cd0b7f841bf8bbc96c55f2",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/9de1f9427b8c356e70cd0b7f841bf8bbc96c55f2"
        },
        "date": 1620205467532,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07681975803468681,
            "unit": "iter/sec",
            "range": "stddev: 0.09303160901328432",
            "extra": "mean: 13.017484376199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08871236470747035,
            "unit": "iter/sec",
            "range": "stddev: 0.06666310260450099",
            "extra": "mean: 11.272385797599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 83.27371364053815,
            "unit": "iter/sec",
            "range": "stddev: 0.0001522125011145464",
            "extra": "mean: 12.008591382349424 msec\nrounds: 68"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07704989441469492,
            "unit": "iter/sec",
            "range": "stddev: 0.08562452816988096",
            "extra": "mean: 12.978603119399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08920168071940714,
            "unit": "iter/sec",
            "range": "stddev: 0.05545226195110301",
            "extra": "mean: 11.210551100999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.15928411807353,
            "unit": "iter/sec",
            "range": "stddev: 0.00010633231181405069",
            "extra": "mean: 22.14384084090878 msec\nrounds: 44"
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
          "id": "c6b6c9257f225751fec8ccd438b917676e0abc7e",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/c6b6c9257f225751fec8ccd438b917676e0abc7e"
        },
        "date": 1620210898802,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07102372080882831,
            "unit": "iter/sec",
            "range": "stddev: 0.13597835777133493",
            "extra": "mean: 14.079803037800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07889255667211692,
            "unit": "iter/sec",
            "range": "stddev: 0.08376087120369897",
            "extra": "mean: 12.675467017200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.70319572884026,
            "unit": "iter/sec",
            "range": "stddev: 0.00033908188942088425",
            "extra": "mean: 12.705964360651198 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0699593472652511,
            "unit": "iter/sec",
            "range": "stddev: 0.08598566805717003",
            "extra": "mean: 14.294015583200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0820023616512544,
            "unit": "iter/sec",
            "range": "stddev: 0.18709668833812398",
            "extra": "mean: 12.194770734199983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.8300072239642,
            "unit": "iter/sec",
            "range": "stddev: 0.0005231635094567849",
            "extra": "mean: 23.906283225002767 msec\nrounds: 40"
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
          "id": "f4aa897f9593785a79a6a9a2b6d975c7b93ba009",
          "message": "added test_surrogate_workflow.py",
          "timestamp": "2021-05-02T22:20:44Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/339/commits/f4aa897f9593785a79a6a9a2b6d975c7b93ba009"
        },
        "date": 1620213342677,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07697067063599197,
            "unit": "iter/sec",
            "range": "stddev: 0.11325892602219713",
            "extra": "mean: 12.991961636000008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08769816940413958,
            "unit": "iter/sec",
            "range": "stddev: 0.06537157705818755",
            "extra": "mean: 11.40274656580001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.62221753810844,
            "unit": "iter/sec",
            "range": "stddev: 0.0003241561402626159",
            "extra": "mean: 13.223627031250018 msec\nrounds: 64"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07718554008705197,
            "unit": "iter/sec",
            "range": "stddev: 0.11636873004642116",
            "extra": "mean: 12.95579455520001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08981743735777566,
            "unit": "iter/sec",
            "range": "stddev: 0.2256028600273949",
            "extra": "mean: 11.133695520799984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.27362529694571,
            "unit": "iter/sec",
            "range": "stddev: 0.0007174908386774631",
            "extra": "mean: 24.22854771795394 msec\nrounds: 39"
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
          "id": "8b0af2799d66559ee98921d64769f3c3bb19079f",
          "message": "Merge pull request #339 from UCL-CCS/surrogate-tests\n\nadded test_surrogate_workflow.py",
          "timestamp": "2021-05-05T13:16:17+02:00",
          "tree_id": "07a6627f4f3497a26a1bfc763cedd8e75407b360",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/8b0af2799d66559ee98921d64769f3c3bb19079f"
        },
        "date": 1620213835756,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06867527879903255,
            "unit": "iter/sec",
            "range": "stddev: 0.16109173454481987",
            "extra": "mean: 14.56128052900001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0756347553856592,
            "unit": "iter/sec",
            "range": "stddev: 0.19859109234719427",
            "extra": "mean: 13.22143497259999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 80.48729882701059,
            "unit": "iter/sec",
            "range": "stddev: 0.00041568778868707066",
            "extra": "mean: 12.424320539682613 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06945674154830671,
            "unit": "iter/sec",
            "range": "stddev: 0.1726146519415568",
            "extra": "mean: 14.397450523999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.0789642441709853,
            "unit": "iter/sec",
            "range": "stddev: 0.07800732363446945",
            "extra": "mean: 12.663959625000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.70870268352764,
            "unit": "iter/sec",
            "range": "stddev: 0.0003270862680811695",
            "extra": "mean: 25.18339639473616 msec\nrounds: 38"
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
          "id": "96d89e3bff1b7c9f0738b15beb6344a5333c0ec6",
          "message": "Update installation.rst",
          "timestamp": "2021-05-05T13:16:49+02:00",
          "tree_id": "d66b1f6eabc863cddad4dc5f1ac40a36cc344613",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/96d89e3bff1b7c9f0738b15beb6344a5333c0ec6"
        },
        "date": 1620213912420,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.055949612739399364,
            "unit": "iter/sec",
            "range": "stddev: 0.5698229060616511",
            "extra": "mean: 17.8732246934 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07554382013695668,
            "unit": "iter/sec",
            "range": "stddev: 0.6881559956113503",
            "extra": "mean: 13.237350165599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 84.6136739831249,
            "unit": "iter/sec",
            "range": "stddev: 0.000681121002095383",
            "extra": "mean: 11.818420746030212 msec\nrounds: 63"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05806553128437014,
            "unit": "iter/sec",
            "range": "stddev: 0.5664516050611433",
            "extra": "mean: 17.2219211274 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07752596333053606,
            "unit": "iter/sec",
            "range": "stddev: 0.5196571091259717",
            "extra": "mean: 12.898904535199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.862181637940914,
            "unit": "iter/sec",
            "range": "stddev: 0.0020853277016923463",
            "extra": "mean: 25.086434282066435 msec\nrounds: 39"
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
          "id": "d2eb03fe9b4109511447475442553d07a3ac0a7c",
          "message": "some renaming in campaign.py",
          "timestamp": "2021-05-05T13:41:32+02:00",
          "tree_id": "7c47034cf056494b7c973a1ad26917db25f9f2da",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d2eb03fe9b4109511447475442553d07a3ac0a7c"
        },
        "date": 1620215340333,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06969582261727016,
            "unit": "iter/sec",
            "range": "stddev: 0.17532329439579522",
            "extra": "mean: 14.348062228800018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07820021237898639,
            "unit": "iter/sec",
            "range": "stddev: 0.09077182055993621",
            "extra": "mean: 12.787689055800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.97904211871385,
            "unit": "iter/sec",
            "range": "stddev: 0.0002696345448182386",
            "extra": "mean: 12.823958499998225 msec\nrounds: 62"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07032199146741835,
            "unit": "iter/sec",
            "range": "stddev: 0.0863744494874027",
            "extra": "mean: 14.22030262699999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08353409091985095,
            "unit": "iter/sec",
            "range": "stddev: 0.3830633506552609",
            "extra": "mean: 11.971160384799987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.48124153151501,
            "unit": "iter/sec",
            "range": "stddev: 0.0013586637240241347",
            "extra": "mean: 21.987086682914683 msec\nrounds: 41"
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
          "id": "2c058b3511530a782af41e564629e6d8095ed38d",
          "message": "unused import",
          "timestamp": "2021-05-05T13:42:40+02:00",
          "tree_id": "ac0b1b1699bd19bd1eef7707ece9c1876fa10e2a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/2c058b3511530a782af41e564629e6d8095ed38d"
        },
        "date": 1620215368063,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.0770088727866653,
            "unit": "iter/sec",
            "range": "stddev: 0.10474590572606748",
            "extra": "mean: 12.98551665299999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08875680791381466,
            "unit": "iter/sec",
            "range": "stddev: 0.06819812050498827",
            "extra": "mean: 11.266741374599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 88.27374949089482,
            "unit": "iter/sec",
            "range": "stddev: 0.00020433642939236618",
            "extra": "mean: 11.328396106060355 msec\nrounds: 66"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.0770321219369225,
            "unit": "iter/sec",
            "range": "stddev: 0.07415381430920492",
            "extra": "mean: 12.981597479800007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08879167273958712,
            "unit": "iter/sec",
            "range": "stddev: 0.098311372300654",
            "extra": "mean: 11.262317390200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.6589514096086,
            "unit": "iter/sec",
            "range": "stddev: 0.00032702856493246294",
            "extra": "mean: 21.901510418602324 msec\nrounds: 43"
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
          "id": "1e8893278f410e80ec166b7b9368adc1cd35d6fe",
          "message": "unused variable",
          "timestamp": "2021-05-05T13:43:09+02:00",
          "tree_id": "2dc732ddfa63e0481788ac488917bc49e476e76e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1e8893278f410e80ec166b7b9368adc1cd35d6fe"
        },
        "date": 1620215516996,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05250361812242778,
            "unit": "iter/sec",
            "range": "stddev: 0.10605186797872936",
            "extra": "mean: 19.046306440600016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.0727031412581939,
            "unit": "iter/sec",
            "range": "stddev: 0.1005088217012679",
            "extra": "mean: 13.754563870199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.26889477682208,
            "unit": "iter/sec",
            "range": "stddev: 0.0005222019444514354",
            "extra": "mean: 12.776467622948113 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05251863231700207,
            "unit": "iter/sec",
            "range": "stddev: 0.10398767528272662",
            "extra": "mean: 19.040861421600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07753978646902882,
            "unit": "iter/sec",
            "range": "stddev: 0.18793080613046068",
            "extra": "mean: 12.896605027400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.15994851276838,
            "unit": "iter/sec",
            "range": "stddev: 0.0011399905293706313",
            "extra": "mean: 24.29546285000299 msec\nrounds: 40"
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
          "id": "1fdb2adb968f7532a9cbf93160c974ffed35a0f7",
          "message": "docstring updates in sql.py down to add_runs",
          "timestamp": "2021-05-05T14:50:16+02:00",
          "tree_id": "78ec6bed5e441924694582571dead4611ef45792",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1fdb2adb968f7532a9cbf93160c974ffed35a0f7"
        },
        "date": 1620219420532,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07695864837302258,
            "unit": "iter/sec",
            "range": "stddev: 0.0855991542427055",
            "extra": "mean: 12.99399120359999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.09130103763654661,
            "unit": "iter/sec",
            "range": "stddev: 0.04513794914439623",
            "extra": "mean: 10.952778039399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 77.63234071812552,
            "unit": "iter/sec",
            "range": "stddev: 0.00019443722206662255",
            "extra": "mean: 12.881229533331862 msec\nrounds: 60"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07703238715207264,
            "unit": "iter/sec",
            "range": "stddev: 0.09014745795735501",
            "extra": "mean: 12.981552785400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.09086374756798639,
            "unit": "iter/sec",
            "range": "stddev: 0.06867916963622506",
            "extra": "mean: 11.005489282199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 41.324165611268114,
            "unit": "iter/sec",
            "range": "stddev: 0.00042222473898034514",
            "extra": "mean: 24.198915700002033 msec\nrounds: 40"
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
          "id": "1579702a7067fc5d5ff5af74ed423803d1aa06bd",
          "message": "_run_to_dict docstring update",
          "timestamp": "2021-05-05T14:53:06+02:00",
          "tree_id": "c01cc4cbf60f87122108c6b74baad6f8284b3b89",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1579702a7067fc5d5ff5af74ed423803d1aa06bd"
        },
        "date": 1620219725948,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05323272966742868,
            "unit": "iter/sec",
            "range": "stddev: 0.133214828383957",
            "extra": "mean: 18.785435318599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.06933785808868116,
            "unit": "iter/sec",
            "range": "stddev: 0.03941753386368124",
            "extra": "mean: 14.4221357216 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 75.62410553306201,
            "unit": "iter/sec",
            "range": "stddev: 0.0016337993669952831",
            "extra": "mean: 13.223296896553856 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05273442541235979,
            "unit": "iter/sec",
            "range": "stddev: 0.12566939844407232",
            "extra": "mean: 18.962944834999984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07312436439431373,
            "unit": "iter/sec",
            "range": "stddev: 0.21653541641238147",
            "extra": "mean: 13.675332541800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 39.04683152022738,
            "unit": "iter/sec",
            "range": "stddev: 0.00156305170449125",
            "extra": "mean: 25.610272615384204 msec\nrounds: 39"
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
          "id": "e1e184779c76f097fbc24babfd30dd60c7e5746f",
          "message": "get_run_status docstring update",
          "timestamp": "2021-05-05T15:03:50+02:00",
          "tree_id": "5c0f942ca5d36177aff163cd66b19105abe25d36",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e1e184779c76f097fbc24babfd30dd60c7e5746f"
        },
        "date": 1620220299501,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06784831278625991,
            "unit": "iter/sec",
            "range": "stddev: 0.08105536480215932",
            "extra": "mean: 14.738760021199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07495711958155374,
            "unit": "iter/sec",
            "range": "stddev: 0.04612627217737245",
            "extra": "mean: 13.340960879800013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 70.68884875427393,
            "unit": "iter/sec",
            "range": "stddev: 0.0001559052535210578",
            "extra": "mean: 14.146502844828673 msec\nrounds: 58"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06791660442500394,
            "unit": "iter/sec",
            "range": "stddev: 0.08985397725214476",
            "extra": "mean: 14.723939873999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07509027251189501,
            "unit": "iter/sec",
            "range": "stddev: 0.052061830531592204",
            "extra": "mean: 13.317304180000018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 38.41812139179245,
            "unit": "iter/sec",
            "range": "stddev: 0.0005729816651846848",
            "extra": "mean: 26.02938310808809 msec\nrounds: 37"
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
          "id": "7b5ffca61ff4d0290115cabdd35e59fc8be31e20",
          "message": "updated docstrings in sql.py down to runs",
          "timestamp": "2021-05-05T15:11:08+02:00",
          "tree_id": "72b0adb45559b1da6bf3e3079e1f968710aa6c68",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7b5ffca61ff4d0290115cabdd35e59fc8be31e20"
        },
        "date": 1620220767838,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05717570868977485,
            "unit": "iter/sec",
            "range": "stddev: 0.07596073962831999",
            "extra": "mean: 17.4899449944 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07427138914281134,
            "unit": "iter/sec",
            "range": "stddev: 0.09580128061445613",
            "extra": "mean: 13.464134864599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 84.1325755707187,
            "unit": "iter/sec",
            "range": "stddev: 0.0004643644340970518",
            "extra": "mean: 11.886002457626384 msec\nrounds: 59"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.05889783981152699,
            "unit": "iter/sec",
            "range": "stddev: 0.49899426995428353",
            "extra": "mean: 16.978551390000018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07955734093238638,
            "unit": "iter/sec",
            "range": "stddev: 0.15906402084992172",
            "extra": "mean: 12.569550317799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 48.78480710046155,
            "unit": "iter/sec",
            "range": "stddev: 0.0014646936151522817",
            "extra": "mean: 20.498184976743286 msec\nrounds: 43"
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
          "id": "752c4626df00506ff56d10b747e13214024c40e6",
          "message": "removed superfluous colons in sql.py docstrings",
          "timestamp": "2021-05-05T15:24:48+02:00",
          "tree_id": "273d1d62e64a38a580d87cf4a62eff79fa29645f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/752c4626df00506ff56d10b747e13214024c40e6"
        },
        "date": 1620221433882,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.09129186251424572,
            "unit": "iter/sec",
            "range": "stddev: 0.13872365477462684",
            "extra": "mean: 10.953878828400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1071841655650269,
            "unit": "iter/sec",
            "range": "stddev: 0.04107013906715709",
            "extra": "mean: 9.329736297600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.8648053777554,
            "unit": "iter/sec",
            "range": "stddev: 0.00028780935758146854",
            "extra": "mean: 9.357617753245414 msec\nrounds: 77"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.09182305836686534,
            "unit": "iter/sec",
            "range": "stddev: 0.09361818886352453",
            "extra": "mean: 10.89051070380001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.10647320980298308,
            "unit": "iter/sec",
            "range": "stddev: 0.08600140406904137",
            "extra": "mean: 9.392033938399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.37807666271155,
            "unit": "iter/sec",
            "range": "stddev: 0.0006454426391962009",
            "extra": "mean: 18.389764062503627 msec\nrounds: 48"
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
          "id": "3eddfa6189a860343e0cfccef6a25bb13aabf901",
          "message": "Update README.md",
          "timestamp": "2021-05-05T15:25:57+02:00",
          "tree_id": "21e66013c73693d695709a20665c3f9ef88275b4",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3eddfa6189a860343e0cfccef6a25bb13aabf901"
        },
        "date": 1620221672101,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.05466949357715196,
            "unit": "iter/sec",
            "range": "stddev: 0.12025523398359662",
            "extra": "mean: 18.291737028599993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07376410539712247,
            "unit": "iter/sec",
            "range": "stddev: 0.05334105727695394",
            "extra": "mean: 13.556729178999978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 74.30239306932452,
            "unit": "iter/sec",
            "range": "stddev: 0.000623554858548824",
            "extra": "mean: 13.45851672727411 msec\nrounds: 55"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.054603785351291095,
            "unit": "iter/sec",
            "range": "stddev: 0.09885235251745268",
            "extra": "mean: 18.313748645200018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07864189511599456,
            "unit": "iter/sec",
            "range": "stddev: 0.143272285075882",
            "extra": "mean: 12.715868539600024 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.97508858026779,
            "unit": "iter/sec",
            "range": "stddev: 0.0009699811657792877",
            "extra": "mean: 24.40507231707526 msec\nrounds: 41"
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
          "id": "8f2c5676f91cbfce81c4a147e8853da129ca997c",
          "message": "Updates tutorials according to last version of easyvvuq 0.9.3",
          "timestamp": "2021-05-05T13:25:59Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/340/commits/8f2c5676f91cbfce81c4a147e8853da129ca997c"
        },
        "date": 1620223854648,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.06313590171871132,
            "unit": "iter/sec",
            "range": "stddev: 0.16665588083079322",
            "extra": "mean: 15.838848781399985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08300283155057747,
            "unit": "iter/sec",
            "range": "stddev: 0.24542101159578475",
            "extra": "mean: 12.047781760199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 93.0286787557017,
            "unit": "iter/sec",
            "range": "stddev: 0.0015586176031408758",
            "extra": "mean: 10.749373347825927 msec\nrounds: 69"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.06398818246425271,
            "unit": "iter/sec",
            "range": "stddev: 0.21604929456622163",
            "extra": "mean: 15.627885673399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08343350194099923,
            "unit": "iter/sec",
            "range": "stddev: 0.1070976539321278",
            "extra": "mean: 11.985593038000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.9888159059978,
            "unit": "iter/sec",
            "range": "stddev: 0.0015725822448158454",
            "extra": "mean: 19.234906249992758 msec\nrounds: 44"
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
          "id": "b01e1cfc1ce3ac67cf073d3abbcb834dc99a7fc3",
          "message": "Updates tutorials according to last version of easyvvuq 0.9.3",
          "timestamp": "2021-05-05T13:25:59Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/340/commits/b01e1cfc1ce3ac67cf073d3abbcb834dc99a7fc3"
        },
        "date": 1620224575350,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.07334968662493943,
            "unit": "iter/sec",
            "range": "stddev: 0.39016172108255925",
            "extra": "mean: 13.633323413000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.07708953176634385,
            "unit": "iter/sec",
            "range": "stddev: 0.11072201669541973",
            "extra": "mean: 12.971929872799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 78.85344689010647,
            "unit": "iter/sec",
            "range": "stddev: 0.0003330777533774562",
            "extra": "mean: 12.681753803275623 msec\nrounds: 61"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.07027498966454164,
            "unit": "iter/sec",
            "range": "stddev: 0.09806645627335177",
            "extra": "mean: 14.229813547800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.07720288289923241,
            "unit": "iter/sec",
            "range": "stddev: 0.12906108414853604",
            "extra": "mean: 12.952884172800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 40.760098497294855,
            "unit": "iter/sec",
            "range": "stddev: 0.0005774181508372878",
            "extra": "mean: 24.533797435900887 msec\nrounds: 39"
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
          "id": "7ef6a270eb8ab779ddca8eb60887b996806213dd",
          "message": "sql.py docstrings",
          "timestamp": "2021-05-05T16:22:27+02:00",
          "tree_id": "4a9b90ebb2df8e16ac76b9fadac106eabaef0dbd",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/7ef6a270eb8ab779ddca8eb60887b996806213dd"
        },
        "date": 1620224954131,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.08034280358273573,
            "unit": "iter/sec",
            "range": "stddev: 0.10725202448396222",
            "extra": "mean: 12.446665481000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.08824151481223796,
            "unit": "iter/sec",
            "range": "stddev: 0.1656356639319111",
            "extra": "mean: 11.332534376000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 87.08688566426088,
            "unit": "iter/sec",
            "range": "stddev: 0.0005979490240165823",
            "extra": "mean: 11.482785179105155 msec\nrounds: 67"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.08016274977630089,
            "unit": "iter/sec",
            "range": "stddev: 0.14321903897739982",
            "extra": "mean: 12.474621975800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.08909343240397842,
            "unit": "iter/sec",
            "range": "stddev: 0.1592467932033919",
            "extra": "mean: 11.224171894800019 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 45.6109969494819,
            "unit": "iter/sec",
            "range": "stddev: 0.0008857385312115711",
            "extra": "mean: 21.92453721429474 msec\nrounds: 42"
          }
        ]
      }
    ]
  }
}