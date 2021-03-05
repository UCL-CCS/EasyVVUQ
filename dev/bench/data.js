window.BENCHMARK_DATA = {
  "lastUpdate": 1614947671327,
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
      }
    ]
  }
}