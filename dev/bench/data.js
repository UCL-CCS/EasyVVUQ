window.BENCHMARK_DATA = {
  "lastUpdate": 1752904667209,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "f63677e12ae6029f4577fec4aab38330b70c4182",
          "message": "Fix GitHub Actions workflows, no jobs run, and  Docker Hub failure",
          "timestamp": "2025-06-20T13:42:30+01:00",
          "tree_id": "2c07da9fba7954ffa2e0a4047f3aaf90c78b975a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f63677e12ae6029f4577fec4aab38330b70c4182"
        },
        "date": 1750423617625,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11403607944206584,
            "unit": "iter/sec",
            "range": "stddev: 0.09905930307445804",
            "extra": "mean: 8.769154506999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19454313292366465,
            "unit": "iter/sec",
            "range": "stddev: 0.029276374992779866",
            "extra": "mean: 5.14024825739998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.67118377215328,
            "unit": "iter/sec",
            "range": "stddev: 0.0001624037744285325",
            "extra": "mean: 8.954861641301626 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11431554506960502,
            "unit": "iter/sec",
            "range": "stddev: 0.12653335179005754",
            "extra": "mean: 8.747716676599975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19949376213155307,
            "unit": "iter/sec",
            "range": "stddev: 0.022308542939704506",
            "extra": "mean: 5.0126880626000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.39540256282185,
            "unit": "iter/sec",
            "range": "stddev: 0.00024977512375035164",
            "extra": "mean: 17.73194187036872 msec\nrounds: 54"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "3d7727de7ff106f2bdf27ef4166d5b5e7decc6a2",
          "message": "Add conditional logic for Docker Hub authentication (build for all, push only with secret)",
          "timestamp": "2025-06-20T14:26:10+01:00",
          "tree_id": "db8ce02e3983a105501bbede97b38bac53a89356",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3d7727de7ff106f2bdf27ef4166d5b5e7decc6a2"
        },
        "date": 1750426260821,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11416312098672363,
            "unit": "iter/sec",
            "range": "stddev: 0.09099308537735086",
            "extra": "mean: 8.759396128599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20170751945703008,
            "unit": "iter/sec",
            "range": "stddev: 0.0707002632168006",
            "extra": "mean: 4.957673381200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.72220971067127,
            "unit": "iter/sec",
            "range": "stddev: 0.00031508045633757496",
            "extra": "mean: 9.113925089887639 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1153866020445603,
            "unit": "iter/sec",
            "range": "stddev: 0.11815399604297513",
            "extra": "mean: 8.666517448999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20606748246555626,
            "unit": "iter/sec",
            "range": "stddev: 0.027070329633180495",
            "extra": "mean: 4.852779235399976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.409526706779424,
            "unit": "iter/sec",
            "range": "stddev: 0.00022818791544108223",
            "extra": "mean: 18.72325148077126 msec\nrounds: 52"
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
          "id": "26238b66446daea05350a475e306db4e7e09ce87",
          "message": "Bump urllib3 from 2.3.0 to 2.5.0",
          "timestamp": "2025-06-20T13:26:46Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/453/commits/26238b66446daea05350a475e306db4e7e09ce87"
        },
        "date": 1750429318178,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11377851844490476,
            "unit": "iter/sec",
            "range": "stddev: 0.13657537458409863",
            "extra": "mean: 8.789005285599956 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1932834610683154,
            "unit": "iter/sec",
            "range": "stddev: 0.020239566281131174",
            "extra": "mean: 5.173748413199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.19426570807794,
            "unit": "iter/sec",
            "range": "stddev: 0.0001726475438561635",
            "extra": "mean: 9.597457146074714 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11401131931891383,
            "unit": "iter/sec",
            "range": "stddev: 0.09365596612350635",
            "extra": "mean: 8.771058926200022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20105136856933925,
            "unit": "iter/sec",
            "range": "stddev: 0.03254953990442435",
            "extra": "mean: 4.973853235200022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.20713672198483,
            "unit": "iter/sec",
            "range": "stddev: 0.0001739324637540713",
            "extra": "mean: 18.44775541509886 msec\nrounds: 53"
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
          "id": "3ff9f297401e1659d4e07bdb95b595b7b265c1ce",
          "message": "Merge pull request #450 from UCL-CCS/dependabot/pip/tornado-6.5.1\n\nBump tornado from 6.4.2 to 6.5.1",
          "timestamp": "2025-06-20T16:18:20+02:00",
          "tree_id": "2c57ae07765c53e980b75114b4f63619a01bab3e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/3ff9f297401e1659d4e07bdb95b595b7b265c1ce"
        },
        "date": 1750429354042,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11518338044635067,
            "unit": "iter/sec",
            "range": "stddev: 0.12288448861611062",
            "extra": "mean: 8.6818080536 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19669768043277253,
            "unit": "iter/sec",
            "range": "stddev: 0.007769745015798207",
            "extra": "mean: 5.0839440394 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.65738515285285,
            "unit": "iter/sec",
            "range": "stddev: 0.0001288310086368843",
            "extra": "mean: 8.876470891306468 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11627711722045661,
            "unit": "iter/sec",
            "range": "stddev: 0.10824665793216136",
            "extra": "mean: 8.600144412799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2022594094430735,
            "unit": "iter/sec",
            "range": "stddev: 0.01570278363056656",
            "extra": "mean: 4.944145751999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.561631114378145,
            "unit": "iter/sec",
            "range": "stddev: 0.0003176193987310404",
            "extra": "mean: 17.67982959999534 msec\nrounds: 55"
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
          "id": "f7b2ed723d52c375c0d2b0819726d41944bd7589",
          "message": "Merge pull request #453 from UCL-CCS/dependabot/pip/urllib3-2.5.0\n\nBump urllib3 from 2.3.0 to 2.5.0",
          "timestamp": "2025-06-20T16:18:52+02:00",
          "tree_id": "92fdf34860874b7f6c93b6414388dbec4e48ad0f",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/f7b2ed723d52c375c0d2b0819726d41944bd7589"
        },
        "date": 1750429432961,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11370190549503907,
            "unit": "iter/sec",
            "range": "stddev: 0.09480909122392442",
            "extra": "mean: 8.794927364199987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19577943172685452,
            "unit": "iter/sec",
            "range": "stddev: 0.018942988067947038",
            "extra": "mean: 5.107788858000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.47277634359621,
            "unit": "iter/sec",
            "range": "stddev: 0.00015320521851976176",
            "extra": "mean: 9.05200387912553 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1144368854846792,
            "unit": "iter/sec",
            "range": "stddev: 0.10252544330640884",
            "extra": "mean: 8.738441244399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20173952064322279,
            "unit": "iter/sec",
            "range": "stddev: 0.032195895589458394",
            "extra": "mean: 4.956886964000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.50673008975036,
            "unit": "iter/sec",
            "range": "stddev: 0.00019874452123573062",
            "extra": "mean: 17.697007036359867 msec\nrounds: 55"
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
          "id": "a5f42b64ec59715513a179206b47b4a991b67226",
          "message": "Merge pull request #449 from UCL-CCS/qmc_analysis_non_vectorized_bootstrapping_fix\n\nFix for non-vectorized bootstraping in QMC Analysis",
          "timestamp": "2025-06-20T16:19:12+02:00",
          "tree_id": "36372e7af746151f179dc5c05a8f5a63ad7accfc",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/a5f42b64ec59715513a179206b47b4a991b67226"
        },
        "date": 1750429569559,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11547207471388432,
            "unit": "iter/sec",
            "range": "stddev: 0.09158899596012629",
            "extra": "mean: 8.660102474799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20115687660396372,
            "unit": "iter/sec",
            "range": "stddev: 0.007881811001466803",
            "extra": "mean: 4.971244418199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.73524882100338,
            "unit": "iter/sec",
            "range": "stddev: 0.00008230606528116961",
            "extra": "mean: 8.792348989131774 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11654636080968077,
            "unit": "iter/sec",
            "range": "stddev: 0.09551847487266038",
            "extra": "mean: 8.580276492999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20481619478361981,
            "unit": "iter/sec",
            "range": "stddev: 0.0050060406890559146",
            "extra": "mean: 4.882426416800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.251182620446556,
            "unit": "iter/sec",
            "range": "stddev: 0.00014065644415785754",
            "extra": "mean: 17.46688809259396 msec\nrounds: 54"
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
          "id": "bad28472d7e112e9be205b87cf9bcee7f31956fe",
          "message": "Update python-package.yml",
          "timestamp": "2025-06-23T13:43:29Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/436/commits/bad28472d7e112e9be205b87cf9bcee7f31956fe"
        },
        "date": 1752568465059,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1145764424048466,
            "unit": "iter/sec",
            "range": "stddev: 0.09466797041882963",
            "extra": "mean: 8.727797608399996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20157143747773038,
            "unit": "iter/sec",
            "range": "stddev: 0.01429346047947449",
            "extra": "mean: 4.9610203335999925 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.14192401058831,
            "unit": "iter/sec",
            "range": "stddev: 0.00016207042833573903",
            "extra": "mean: 9.162382000000163 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11565914875597152,
            "unit": "iter/sec",
            "range": "stddev: 0.09680496918051779",
            "extra": "mean: 8.646095105800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2066719966390844,
            "unit": "iter/sec",
            "range": "stddev: 0.00831246344885199",
            "extra": "mean: 4.838584889399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.05944239217318,
            "unit": "iter/sec",
            "range": "stddev: 0.0001982471885146193",
            "extra": "mean: 18.162189018865764 msec\nrounds: 53"
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
          "id": "55d69f312f5f7202bbc4fb387e7e8f0fe5373319",
          "message": "Update python-package.yml",
          "timestamp": "2025-06-23T13:43:29Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/436/commits/55d69f312f5f7202bbc4fb387e7e8f0fe5373319"
        },
        "date": 1752569552634,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11354696503985844,
            "unit": "iter/sec",
            "range": "stddev: 0.09750937754072282",
            "extra": "mean: 8.806928478000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19725983189267493,
            "unit": "iter/sec",
            "range": "stddev: 0.0459862610145445",
            "extra": "mean: 5.069455805599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.10454220716062,
            "unit": "iter/sec",
            "range": "stddev: 0.00031012048370869196",
            "extra": "mean: 9.605728806818737 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11468602733472873,
            "unit": "iter/sec",
            "range": "stddev: 0.10988893156665208",
            "extra": "mean: 8.719458012799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20467621989555468,
            "unit": "iter/sec",
            "range": "stddev: 0.07513656173509631",
            "extra": "mean: 4.88576543239999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.793168652450674,
            "unit": "iter/sec",
            "range": "stddev: 0.0002951411789089835",
            "extra": "mean: 18.589721056605626 msec\nrounds: 53"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "David Coster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "898a448dde4c6a86895e5f76847a9e445ae5262a",
          "message": "Merge pull request #436 from UCL-CCS/djgroen-pyupdates\n\nUpdate python-package.yml",
          "timestamp": "2025-07-16T21:50:25+02:00",
          "tree_id": "eed7279ddbcf39c3df68e52ae812f7dbfc1468de",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/898a448dde4c6a86895e5f76847a9e445ae5262a"
        },
        "date": 1752695680993,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11593419631528107,
            "unit": "iter/sec",
            "range": "stddev: 0.09059695762867732",
            "extra": "mean: 8.625582716600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20609669129246108,
            "unit": "iter/sec",
            "range": "stddev: 0.01603206401395123",
            "extra": "mean: 4.852091480600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.05881366493657,
            "unit": "iter/sec",
            "range": "stddev: 0.00012106466671703156",
            "extra": "mean: 9.004238087910707 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11684736797414964,
            "unit": "iter/sec",
            "range": "stddev: 0.08759264554620601",
            "extra": "mean: 8.558173087999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21095990216493168,
            "unit": "iter/sec",
            "range": "stddev: 0.012626121957834767",
            "extra": "mean: 4.740237314000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.55449813678428,
            "unit": "iter/sec",
            "range": "stddev: 0.00012761150200410234",
            "extra": "mean: 17.68205948148231 msec\nrounds: 54"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "6ecfad69ff438c4107a03c8c578519f3e41d5cd7",
          "message": "Add dataset import functionality to address GitHub issue #116",
          "timestamp": "2025-07-17T11:25:39+01:00",
          "tree_id": "21b06b7f3909c4813a14c5e106764920f5a8724d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/6ecfad69ff438c4107a03c8c578519f3e41d5cd7"
        },
        "date": 1752748213916,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11461337448493836,
            "unit": "iter/sec",
            "range": "stddev: 0.09985346771206938",
            "extra": "mean: 8.724985234000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20184765924840511,
            "unit": "iter/sec",
            "range": "stddev: 0.039533410974009545",
            "extra": "mean: 4.95423134319999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.57263040755747,
            "unit": "iter/sec",
            "range": "stddev: 0.00013687134842459015",
            "extra": "mean: 9.043829348312686 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11607462914277854,
            "unit": "iter/sec",
            "range": "stddev: 0.1021880528063726",
            "extra": "mean: 8.615147060000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20826352352173616,
            "unit": "iter/sec",
            "range": "stddev: 0.011971963945716889",
            "extra": "mean: 4.801608957199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.834418019273414,
            "unit": "iter/sec",
            "range": "stddev: 0.00025981017635669283",
            "extra": "mean: 17.594972111105015 msec\nrounds: 54"
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
          "id": "f5b6a23a3d549e7547f23c221c17d048325102a5",
          "message": "Hackathon 2025 07",
          "timestamp": "2025-07-17T10:26:03Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/454/commits/f5b6a23a3d549e7547f23c221c17d048325102a5"
        },
        "date": 1752755398768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11584448315722462,
            "unit": "iter/sec",
            "range": "stddev: 0.10363048551313246",
            "extra": "mean: 8.632262605399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19939417692364222,
            "unit": "iter/sec",
            "range": "stddev: 0.008206535362981321",
            "extra": "mean: 5.015191594000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.22115045323216,
            "unit": "iter/sec",
            "range": "stddev: 0.0001430180880939565",
            "extra": "mean: 9.072668865167664 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11699610073902587,
            "unit": "iter/sec",
            "range": "stddev: 0.096528601849159",
            "extra": "mean: 8.5472934028 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20707308290970985,
            "unit": "iter/sec",
            "range": "stddev: 0.00469451819675412",
            "extra": "mean: 4.829212884399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.582862821753544,
            "unit": "iter/sec",
            "range": "stddev: 0.000173138543613739",
            "extra": "mean: 17.991156792460654 msec\nrounds: 53"
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
          "id": "28f5cf494169fe5a75fd6ac679755c42a03d5264",
          "message": "Hackathon 2025 07",
          "timestamp": "2025-07-17T10:26:03Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/454/commits/28f5cf494169fe5a75fd6ac679755c42a03d5264"
        },
        "date": 1752755421316,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11556836416130846,
            "unit": "iter/sec",
            "range": "stddev: 0.08772707349640536",
            "extra": "mean: 8.652887035800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19693588317225008,
            "unit": "iter/sec",
            "range": "stddev: 0.030033720388344412",
            "extra": "mean: 5.077794782199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.14917621512656,
            "unit": "iter/sec",
            "range": "stddev: 0.0001490566878441255",
            "extra": "mean: 9.246487444442803 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11737117850639708,
            "unit": "iter/sec",
            "range": "stddev: 0.12432609559958277",
            "extra": "mean: 8.519979203799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2066643865599836,
            "unit": "iter/sec",
            "range": "stddev: 0.031120270468129322",
            "extra": "mean: 4.838763062399982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.65182668217216,
            "unit": "iter/sec",
            "range": "stddev: 0.0002392628491310445",
            "extra": "mean: 17.96886211320618 msec\nrounds: 53"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "d7caf698b4d4aea3467a889d0bc9425c123a0031",
          "message": "Fix #169: Add discrete distribution support for SC and PCE samplers",
          "timestamp": "2025-07-17T13:32:17+01:00",
          "tree_id": "6123b28245c13cd69437d9b48bdf94aa4df207d1",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d7caf698b4d4aea3467a889d0bc9425c123a0031"
        },
        "date": 1752756026600,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11594106742339164,
            "unit": "iter/sec",
            "range": "stddev: 0.08882652246183838",
            "extra": "mean: 8.625071531800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1995116403387069,
            "unit": "iter/sec",
            "range": "stddev: 0.030753817477949016",
            "extra": "mean: 5.012238876399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.81299733769424,
            "unit": "iter/sec",
            "range": "stddev: 0.00008133675576719254",
            "extra": "mean: 8.943504098900329 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11690731612850531,
            "unit": "iter/sec",
            "range": "stddev: 0.1022091490288287",
            "extra": "mean: 8.553784597200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20445073115467852,
            "unit": "iter/sec",
            "range": "stddev: 0.011438818562289966",
            "extra": "mean: 4.891153943800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.28851144301963,
            "unit": "iter/sec",
            "range": "stddev: 0.00028137379257310027",
            "extra": "mean: 18.086940196076732 msec\nrounds: 51"
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
          "id": "a3996b70844bac0986a00daabb0b426e0a498190",
          "message": "Hackathon 2025 07",
          "timestamp": "2025-07-17T12:36:06Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/454/commits/a3996b70844bac0986a00daabb0b426e0a498190"
        },
        "date": 1752756627836,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11579914441986504,
            "unit": "iter/sec",
            "range": "stddev: 0.09187458595267073",
            "extra": "mean: 8.635642387599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20635409248329475,
            "unit": "iter/sec",
            "range": "stddev: 0.010220663475487727",
            "extra": "mean: 4.846039096999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.28372312008625,
            "unit": "iter/sec",
            "range": "stddev: 0.00009400537769217588",
            "extra": "mean: 8.906010347826733 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11690879041363156,
            "unit": "iter/sec",
            "range": "stddev: 0.09256872532487143",
            "extra": "mean: 8.553676729199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2102438230531717,
            "unit": "iter/sec",
            "range": "stddev: 0.01340912472043903",
            "extra": "mean: 4.756382306400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.0721902679216,
            "unit": "iter/sec",
            "range": "stddev: 0.00016849140085962628",
            "extra": "mean: 17.52166852727338 msec\nrounds: 55"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "0bb9da666ef797f3bd49aa941bfa2d41cf454800",
          "message": "Fix GitHub Actions syntax error in docker.yml\n\n- Remove secrets access from 'if' conditions (not supported in newer GitHub Actions)\n- Simplify conditions to check only github.event_name\n- Maintain proper secret usage in 'with:' contexts\n- Resolves: 'Unrecognized named-value: secrets' error\n\nThe workflow will still:\n- Skip Docker login/push for pull requests\n- Use secrets properly for authentication\n- Push images for branch pushes and tags",
          "timestamp": "2025-07-17T15:01:22+01:00",
          "tree_id": "7f5e65c2e051c6fa8e558afbf7d259b22ecd4913",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/0bb9da666ef797f3bd49aa941bfa2d41cf454800"
        },
        "date": 1752765557966,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1127711500162454,
            "unit": "iter/sec",
            "range": "stddev: 0.0705144709779411",
            "extra": "mean: 8.867516203000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20249082797089987,
            "unit": "iter/sec",
            "range": "stddev: 0.009498183862151633",
            "extra": "mean: 4.938495289000008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.30898891997911,
            "unit": "iter/sec",
            "range": "stddev: 0.00010128006560920238",
            "extra": "mean: 8.904006790698709 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11383060822982055,
            "unit": "iter/sec",
            "range": "stddev: 0.07077869443315227",
            "extra": "mean: 8.784983367400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2080078838256191,
            "unit": "iter/sec",
            "range": "stddev: 0.010605844565297175",
            "extra": "mean: 4.807510088599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.296108943050804,
            "unit": "iter/sec",
            "range": "stddev: 0.00027449906169466217",
            "extra": "mean: 18.08445511111632 msec\nrounds: 54"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "217d247ac08dca9acd422a2f9c8ec62533162734",
          "message": "Fix Docker login unauthorized error in GitHub Actions",
          "timestamp": "2025-07-17T16:22:03+01:00",
          "tree_id": "686f816f192b206ac552657ad569fe20c23d2828",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/217d247ac08dca9acd422a2f9c8ec62533162734"
        },
        "date": 1752766433340,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11486490161713186,
            "unit": "iter/sec",
            "range": "stddev: 0.11796185520338538",
            "extra": "mean: 8.705879567400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2044920174582975,
            "unit": "iter/sec",
            "range": "stddev: 0.022937291490612636",
            "extra": "mean: 4.890166434999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.76882645080039,
            "unit": "iter/sec",
            "range": "stddev: 0.0002126888435402305",
            "extra": "mean: 9.730577204545005 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11581905283085799,
            "unit": "iter/sec",
            "range": "stddev: 0.10924403401080256",
            "extra": "mean: 8.634157986600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20743508544565933,
            "unit": "iter/sec",
            "range": "stddev: 0.007229409215523837",
            "extra": "mean: 4.82078524879999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.08677287005498,
            "unit": "iter/sec",
            "range": "stddev: 0.00019845453879412694",
            "extra": "mean: 18.488808759260397 msec\nrounds: 54"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "4a5ac9e4a7e59a671dc1476c1c067e15aeda59ef",
          "message": "Attempt to fix Docker authentication issues in GitHub Actions",
          "timestamp": "2025-07-17T17:12:38+01:00",
          "tree_id": "5d714f53547573ebaac084ffde281ad07381fd26",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4a5ac9e4a7e59a671dc1476c1c067e15aeda59ef"
        },
        "date": 1752769044808,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11484497963961623,
            "unit": "iter/sec",
            "range": "stddev: 0.09710140330866296",
            "extra": "mean: 8.707389762600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19454649726494685,
            "unit": "iter/sec",
            "range": "stddev: 0.03638259784114078",
            "extra": "mean: 5.140159365799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.59844635183393,
            "unit": "iter/sec",
            "range": "stddev: 0.0001663767732572746",
            "extra": "mean: 9.208234865167688 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1155597475892491,
            "unit": "iter/sec",
            "range": "stddev: 0.15390636633377408",
            "extra": "mean: 8.653532227799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19978225754126236,
            "unit": "iter/sec",
            "range": "stddev: 0.0256959287752312",
            "extra": "mean: 5.005449494399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.71916698761923,
            "unit": "iter/sec",
            "range": "stddev: 0.0013344836220007025",
            "extra": "mean: 18.968433249995087 msec\nrounds: 52"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "committer": {
            "email": "maziarghorbani@gmail.com",
            "name": "Maziar Ghorbani",
            "username": "mzrghorbani"
          },
          "distinct": true,
          "id": "9db49f356e5dd9c0b7f5cf0757fd5b384599ea8d",
          "message": "Temporary fix: prevent Docker workflow failures\n\n- Add continue-on-error to Docker login step\n- Only push to Docker Hub if login actually succeeds\n- Prevents workflow failures when Docker Hub credentials are invalid\n- Stops failure notification emails to developers",
          "timestamp": "2025-07-17T17:27:23+01:00",
          "tree_id": "8cfedf63a28b1d12d8668f441c4cc2404f8e957d",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/9db49f356e5dd9c0b7f5cf0757fd5b384599ea8d"
        },
        "date": 1752769912020,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11520181876310931,
            "unit": "iter/sec",
            "range": "stddev: 0.11191287285614786",
            "extra": "mean: 8.680418510200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20072191444633652,
            "unit": "iter/sec",
            "range": "stddev: 0.01826745923039741",
            "extra": "mean: 4.982017049599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.37315613186084,
            "unit": "iter/sec",
            "range": "stddev: 0.00015720645979313793",
            "extra": "mean: 9.143011277780033 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11555124442469879,
            "unit": "iter/sec",
            "range": "stddev: 0.09688989024826922",
            "extra": "mean: 8.654169022400009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21453176114259642,
            "unit": "iter/sec",
            "range": "stddev: 0.02936209083996839",
            "extra": "mean: 4.6613144584 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.96932213989716,
            "unit": "iter/sec",
            "range": "stddev: 0.0008775857318441289",
            "extra": "mean: 18.19196528301724 msec\nrounds: 53"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "40796322+DavidPCoster@users.noreply.github.com",
            "name": "David Coster",
            "username": "DavidPCoster"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e393368c4edf0d4c4e78467e9f5a53ff0d4b58f2",
          "message": "Merge pull request #454 from UCL-CCS/Hackathon_2025_07",
          "timestamp": "2025-07-17T19:21:47+02:00",
          "tree_id": "b782cc46d60d200af1395efcb39ffc170ffa67a6",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e393368c4edf0d4c4e78467e9f5a53ff0d4b58f2"
        },
        "date": 1752773177564,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1123461603965857,
            "unit": "iter/sec",
            "range": "stddev: 0.11792672510277331",
            "extra": "mean: 8.901060761400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1955225866287632,
            "unit": "iter/sec",
            "range": "stddev: 0.011579073343583494",
            "extra": "mean: 5.114498622600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 101.56127166957428,
            "unit": "iter/sec",
            "range": "stddev: 0.00023938830150275505",
            "extra": "mean: 9.846272930231336 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11351224113259117,
            "unit": "iter/sec",
            "range": "stddev: 0.10359085436205512",
            "extra": "mean: 8.809622557199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20125998326277575,
            "unit": "iter/sec",
            "range": "stddev: 0.0520570952348109",
            "extra": "mean: 4.9686976207999916 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.0842897369508,
            "unit": "iter/sec",
            "range": "stddev: 0.00021397254535030313",
            "extra": "mean: 18.48965762264217 msec\nrounds: 53"
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
          "id": "8de9094aeb68f0c1d56cd1511c17ea0057abe206",
          "message": "Fix Docker authentication by migrating to GitHub Container Registry",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/456/commits/8de9094aeb68f0c1d56cd1511c17ea0057abe206"
        },
        "date": 1752831686673,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11699554662870137,
            "unit": "iter/sec",
            "range": "stddev: 0.10444325498353885",
            "extra": "mean: 8.547333884199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21125007700989573,
            "unit": "iter/sec",
            "range": "stddev: 0.013424658402646623",
            "extra": "mean: 4.733726084999989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.56360343097435,
            "unit": "iter/sec",
            "range": "stddev: 0.0006137935244917818",
            "extra": "mean: 9.211190199999287 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11656995834661739,
            "unit": "iter/sec",
            "range": "stddev: 0.1327361817885712",
            "extra": "mean: 8.578539567000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20971008909451136,
            "unit": "iter/sec",
            "range": "stddev: 0.02124848823534069",
            "extra": "mean: 4.768487793399982 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.612209268887575,
            "unit": "iter/sec",
            "range": "stddev: 0.00023575387712266462",
            "extra": "mean: 18.310923754730744 msec\nrounds: 53"
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
          "id": "a90296a5657b2159cbd3b394c3b884238b75143c",
          "message": "Fix Docker authentication by migrating to GitHub Container Registry",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/456/commits/a90296a5657b2159cbd3b394c3b884238b75143c"
        },
        "date": 1752835365028,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11583117758162316,
            "unit": "iter/sec",
            "range": "stddev: 0.10404351575254284",
            "extra": "mean: 8.633254196999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20436236274504985,
            "unit": "iter/sec",
            "range": "stddev: 0.03650423165064305",
            "extra": "mean: 4.893268929600015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.62747419013972,
            "unit": "iter/sec",
            "range": "stddev: 0.0011557479064713324",
            "extra": "mean: 9.121800966294119 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11696412084648554,
            "unit": "iter/sec",
            "range": "stddev: 0.09298637293729227",
            "extra": "mean: 8.549630371800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20959371260961968,
            "unit": "iter/sec",
            "range": "stddev: 0.0043767626482635255",
            "extra": "mean: 4.7711354866000075 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.20712126193749,
            "unit": "iter/sec",
            "range": "stddev: 0.00018014154443185852",
            "extra": "mean: 17.48034122222727 msec\nrounds: 54"
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
          "id": "871b72af8da00415370b4177bb328ae71a62b66f",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/871b72af8da00415370b4177bb328ae71a62b66f"
        },
        "date": 1752904666569,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11383773372868419,
            "unit": "iter/sec",
            "range": "stddev: 0.08140162625185289",
            "extra": "mean: 8.784433484800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20028206698466544,
            "unit": "iter/sec",
            "range": "stddev: 0.06482264946787097",
            "extra": "mean: 4.992958256600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.69188087173637,
            "unit": "iter/sec",
            "range": "stddev: 0.00023609192707601577",
            "extra": "mean: 9.551839088889363 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11498042370085015,
            "unit": "iter/sec",
            "range": "stddev: 0.08973160073503124",
            "extra": "mean: 8.697132675399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20783884943853442,
            "unit": "iter/sec",
            "range": "stddev: 0.008414902287705453",
            "extra": "mean: 4.811420014599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.89777149331409,
            "unit": "iter/sec",
            "range": "stddev: 0.0003122539614987723",
            "extra": "mean: 18.21567566038247 msec\nrounds: 53"
          }
        ]
      }
    ]
  }
}