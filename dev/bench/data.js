window.BENCHMARK_DATA = {
  "lastUpdate": 1753258347261,
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
          "id": "835fe98c3a1628cf026e9fc983bd064f566635be",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/835fe98c3a1628cf026e9fc983bd064f566635be"
        },
        "date": 1752905229345,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11420256115082361,
            "unit": "iter/sec",
            "range": "stddev: 0.10015309151300757",
            "extra": "mean: 8.7563710474 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2089953802953903,
            "unit": "iter/sec",
            "range": "stddev: 0.04912340096097534",
            "extra": "mean: 4.784794757599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.55785323353304,
            "unit": "iter/sec",
            "range": "stddev: 0.00021640321059524816",
            "extra": "mean: 9.656438104649608 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11627780891578131,
            "unit": "iter/sec",
            "range": "stddev: 0.10460382610598307",
            "extra": "mean: 8.600093253599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21005423074850332,
            "unit": "iter/sec",
            "range": "stddev: 0.010065827275398875",
            "extra": "mean: 4.760675357199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.991424239857125,
            "unit": "iter/sec",
            "range": "stddev: 0.00016274653216088121",
            "extra": "mean: 18.870977980770274 msec\nrounds: 52"
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
          "id": "645ef5dcb3878cd3a0787aa88632f2092c49441d",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/645ef5dcb3878cd3a0787aa88632f2092c49441d"
        },
        "date": 1752909429060,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11543500269491898,
            "unit": "iter/sec",
            "range": "stddev: 0.1057959169626412",
            "extra": "mean: 8.662883671799978 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19651084627667612,
            "unit": "iter/sec",
            "range": "stddev: 0.025327159397036288",
            "extra": "mean: 5.088777637200019 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.59253537970525,
            "unit": "iter/sec",
            "range": "stddev: 0.00011163231902179853",
            "extra": "mean: 9.124709055551092 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1160708659726249,
            "unit": "iter/sec",
            "range": "stddev: 0.09174139158939755",
            "extra": "mean: 8.615426374399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20340511257866775,
            "unit": "iter/sec",
            "range": "stddev: 0.016891517167010917",
            "extra": "mean: 4.916297271600024 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.90557240720912,
            "unit": "iter/sec",
            "range": "stddev: 0.00026674616579211875",
            "extra": "mean: 17.887304555548173 msec\nrounds: 54"
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
          "id": "f168ca35eefbd37ab971107cd2aaebc84b706771",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/f168ca35eefbd37ab971107cd2aaebc84b706771"
        },
        "date": 1752965640613,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1165916344724087,
            "unit": "iter/sec",
            "range": "stddev: 0.08373759339034643",
            "extra": "mean: 8.5769446884 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2060191058411238,
            "unit": "iter/sec",
            "range": "stddev: 0.010694063719301795",
            "extra": "mean: 4.853918746599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.12935951595098,
            "unit": "iter/sec",
            "range": "stddev: 0.00009683916667806851",
            "extra": "mean: 8.839438358695935 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11834098594790182,
            "unit": "iter/sec",
            "range": "stddev: 0.08559988915013969",
            "extra": "mean: 8.450157753800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2121024181462891,
            "unit": "iter/sec",
            "range": "stddev: 0.013940292182777437",
            "extra": "mean: 4.714703437799988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.51979317034015,
            "unit": "iter/sec",
            "range": "stddev: 0.0003452137821843267",
            "extra": "mean: 17.69291683333281 msec\nrounds: 54"
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
          "id": "55eb6068a3aec15a7a1b1e557d0c9cb37ec0692a",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/55eb6068a3aec15a7a1b1e557d0c9cb37ec0692a"
        },
        "date": 1753013290267,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11563157657475354,
            "unit": "iter/sec",
            "range": "stddev: 0.09441380252518586",
            "extra": "mean: 8.648156754599984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20928548713594639,
            "unit": "iter/sec",
            "range": "stddev: 0.03496115039015805",
            "extra": "mean: 4.778162182600011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.6074717438404,
            "unit": "iter/sec",
            "range": "stddev: 0.00010557084544717061",
            "extra": "mean: 9.040980543483844 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11615713878954692,
            "unit": "iter/sec",
            "range": "stddev: 0.12006100817425269",
            "extra": "mean: 8.609027481399972 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2105030029319975,
            "unit": "iter/sec",
            "range": "stddev: 0.009305654105626221",
            "extra": "mean: 4.750526054600027 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.966042292944344,
            "unit": "iter/sec",
            "range": "stddev: 0.00020812498186753524",
            "extra": "mean: 17.86797777776883 msec\nrounds: 54"
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
          "id": "d34d261d28c062b131fbb45d493a24f9eab65169",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/d34d261d28c062b131fbb45d493a24f9eab65169"
        },
        "date": 1753034734894,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11563149203212245,
            "unit": "iter/sec",
            "range": "stddev: 0.10124393555240158",
            "extra": "mean: 8.6481630776 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20377020442840435,
            "unit": "iter/sec",
            "range": "stddev: 0.01830027345964891",
            "extra": "mean: 4.907488819599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.75493793105466,
            "unit": "iter/sec",
            "range": "stddev: 0.00020262191874028957",
            "extra": "mean: 8.94815046666603 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11631891562351594,
            "unit": "iter/sec",
            "range": "stddev: 0.10562183291569514",
            "extra": "mean: 8.597054010000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20864284898393187,
            "unit": "iter/sec",
            "range": "stddev: 0.009078583843644772",
            "extra": "mean: 4.792879338400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.225810777685155,
            "unit": "iter/sec",
            "range": "stddev: 0.0002849364788945149",
            "extra": "mean: 17.785426055552392 msec\nrounds: 54"
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
          "id": "2a36dc00d6d9a491ecd83129dbc1bc355b63b146",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/2a36dc00d6d9a491ecd83129dbc1bc355b63b146"
        },
        "date": 1753044521530,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11548172347908904,
            "unit": "iter/sec",
            "range": "stddev: 0.07641380322285966",
            "extra": "mean: 8.659378903200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20325247774239896,
            "unit": "iter/sec",
            "range": "stddev: 0.011562731246928347",
            "extra": "mean: 4.919989222800001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.53157034982428,
            "unit": "iter/sec",
            "range": "stddev: 0.00010324082144712771",
            "extra": "mean: 8.886395141304108 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11679646832752658,
            "unit": "iter/sec",
            "range": "stddev: 0.09527141708649846",
            "extra": "mean: 8.561902721200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2127369542393102,
            "unit": "iter/sec",
            "range": "stddev: 0.009333579520523988",
            "extra": "mean: 4.700640768200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.905279698960264,
            "unit": "iter/sec",
            "range": "stddev: 0.00015649177266991324",
            "extra": "mean: 17.57306185454478 msec\nrounds: 55"
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
          "id": "7202950d5acb3443e03e45067420e4806d728116",
          "message": "Include the python notebooks in tutorials as part of the documentation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/457/commits/7202950d5acb3443e03e45067420e4806d728116"
        },
        "date": 1753091417047,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11611043552619307,
            "unit": "iter/sec",
            "range": "stddev: 0.07505088273330174",
            "extra": "mean: 8.612490302599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2075059552392438,
            "unit": "iter/sec",
            "range": "stddev: 0.008141528789037714",
            "extra": "mean: 4.819138799400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.94200302006006,
            "unit": "iter/sec",
            "range": "stddev: 0.00011996499655535014",
            "extra": "mean: 9.095704758240029 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11701711685583846,
            "unit": "iter/sec",
            "range": "stddev: 0.09891131623929955",
            "extra": "mean: 8.545758320399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21211219077634091,
            "unit": "iter/sec",
            "range": "stddev: 0.011410546954414607",
            "extra": "mean: 4.714486217599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.30717682943904,
            "unit": "iter/sec",
            "range": "stddev: 0.00012886623881591116",
            "extra": "mean: 17.75972542592778 msec\nrounds: 54"
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
          "id": "db4b145352d5388cdb381189401cc1b08c947086",
          "message": "Dpc/add authors",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/459/commits/db4b145352d5388cdb381189401cc1b08c947086"
        },
        "date": 1753094357078,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11561725240496099,
            "unit": "iter/sec",
            "range": "stddev: 0.08765942990398763",
            "extra": "mean: 8.6492282008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2063640929785989,
            "unit": "iter/sec",
            "range": "stddev: 0.02955546472593116",
            "extra": "mean: 4.845804255799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.80344594952149,
            "unit": "iter/sec",
            "range": "stddev: 0.0000973562657001671",
            "extra": "mean: 9.02499007526867 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1168659597569605,
            "unit": "iter/sec",
            "range": "stddev: 0.0888096873929197",
            "extra": "mean: 8.5568115992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21147795390226068,
            "unit": "iter/sec",
            "range": "stddev: 0.025247848563328786",
            "extra": "mean: 4.728625284800006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.33226353010879,
            "unit": "iter/sec",
            "range": "stddev: 0.0001980768791377477",
            "extra": "mean: 17.751816407404156 msec\nrounds: 54"
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
          "id": "835a2c9fa1f108967a463df4cc3c6b7789493677",
          "message": "Add a complete set of authors",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/460/commits/835a2c9fa1f108967a463df4cc3c6b7789493677"
        },
        "date": 1753094702247,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11418039248046298,
            "unit": "iter/sec",
            "range": "stddev: 0.11491411852731477",
            "extra": "mean: 8.758071138800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19646147127841976,
            "unit": "iter/sec",
            "range": "stddev: 0.05478595314707033",
            "extra": "mean: 5.0900565565999845 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.02313436927548,
            "unit": "iter/sec",
            "range": "stddev: 0.0004088997532451528",
            "extra": "mean: 9.34377418390283 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11602142571186423,
            "unit": "iter/sec",
            "range": "stddev: 0.11041285770910975",
            "extra": "mean: 8.619097669799975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20336340665588284,
            "unit": "iter/sec",
            "range": "stddev: 0.042022432377514685",
            "extra": "mean: 4.91730550960001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.52731991547676,
            "unit": "iter/sec",
            "range": "stddev: 0.00026514146209603417",
            "extra": "mean: 18.339430611115827 msec\nrounds: 54"
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
          "id": "7202950d5acb3443e03e45067420e4806d728116",
          "message": "Dpc/python notebooks as tutorial",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/461/commits/7202950d5acb3443e03e45067420e4806d728116"
        },
        "date": 1753095126449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11542718781627385,
            "unit": "iter/sec",
            "range": "stddev: 0.10345438273721921",
            "extra": "mean: 8.663470183399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20174780128300993,
            "unit": "iter/sec",
            "range": "stddev: 0.0239045627628823",
            "extra": "mean: 4.956683511 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.73934531017477,
            "unit": "iter/sec",
            "range": "stddev: 0.00026010000183518075",
            "extra": "mean: 9.112501967034081 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1161743879200399,
            "unit": "iter/sec",
            "range": "stddev: 0.092440018177357",
            "extra": "mean: 8.6077492458 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2075613918560146,
            "unit": "iter/sec",
            "range": "stddev: 0.009420049240682835",
            "extra": "mean: 4.817851677799984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.7016033215311,
            "unit": "iter/sec",
            "range": "stddev: 0.0002697380347690999",
            "extra": "mean: 18.280999811323444 msec\nrounds: 53"
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
          "id": "4fe2e7c7d7a0d31c20122e6f5396569fe53be515",
          "message": "Fix packaging issue #445: Correct packaging and improve installation",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/462/commits/4fe2e7c7d7a0d31c20122e6f5396569fe53be515"
        },
        "date": 1753117749459,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11564061374095483,
            "unit": "iter/sec",
            "range": "stddev: 0.099584246908589",
            "extra": "mean: 8.6474809122 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20360458490836722,
            "unit": "iter/sec",
            "range": "stddev: 0.032626134204680336",
            "extra": "mean: 4.911480753000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.96039146920857,
            "unit": "iter/sec",
            "range": "stddev: 0.00011258593859160073",
            "extra": "mean: 8.698648179776281 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1166944645235216,
            "unit": "iter/sec",
            "range": "stddev: 0.105881630441232",
            "extra": "mean: 8.569386766399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21181100385851273,
            "unit": "iter/sec",
            "range": "stddev: 0.008575916986625895",
            "extra": "mean: 4.721190031600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.75974126236126,
            "unit": "iter/sec",
            "range": "stddev: 0.00025901730660353174",
            "extra": "mean: 17.61812118518454 msec\nrounds: 54"
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
          "id": "46d743bb8b12860bd1aed0dc2e63802234c22e43",
          "message": "Dpc/python notebooks as tutorial",
          "timestamp": "2025-07-17T17:21:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/461/commits/46d743bb8b12860bd1aed0dc2e63802234c22e43"
        },
        "date": 1753197777144,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11555803443358026,
            "unit": "iter/sec",
            "range": "stddev: 0.08803173547383981",
            "extra": "mean: 8.653660517 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2050772149398184,
            "unit": "iter/sec",
            "range": "stddev: 0.007539567549471547",
            "extra": "mean: 4.876212114999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.69129484565109,
            "unit": "iter/sec",
            "range": "stddev: 0.00026621851467303534",
            "extra": "mean: 9.034134087910063 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11557129203854208,
            "unit": "iter/sec",
            "range": "stddev: 0.12495267648042822",
            "extra": "mean: 8.652667823999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2111150305503212,
            "unit": "iter/sec",
            "range": "stddev: 0.011976479020550329",
            "extra": "mean: 4.7367541638000095 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.849994546348555,
            "unit": "iter/sec",
            "range": "stddev: 0.00024348222686428197",
            "extra": "mean: 17.590151203703666 msec\nrounds: 54"
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
          "id": "66330a5148ed5332dc5b648689974a895f3a1f2c",
          "message": "Merge pull request #456 from UCL-CCS/fix/migrate-docker-to-ghcr\n\nFix Docker authentication by migrating to GitHub Container Registry",
          "timestamp": "2025-07-23T10:06:40+02:00",
          "tree_id": "71ae32a2bf45dc130b75ac2ca8836d9f161dd0b0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/66330a5148ed5332dc5b648689974a895f3a1f2c"
        },
        "date": 1753258259667,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1152903616597131,
            "unit": "iter/sec",
            "range": "stddev: 0.10000527686350932",
            "extra": "mean: 8.6737519564 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2049927457536118,
            "unit": "iter/sec",
            "range": "stddev: 0.05900021123709417",
            "extra": "mean: 4.878221404000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.73625154654914,
            "unit": "iter/sec",
            "range": "stddev: 0.00006963193898965903",
            "extra": "mean: 8.87026121838987 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11630777041113016,
            "unit": "iter/sec",
            "range": "stddev: 0.09875550808360191",
            "extra": "mean: 8.597877824199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20825754046586215,
            "unit": "iter/sec",
            "range": "stddev: 0.006003093093190035",
            "extra": "mean: 4.801746903199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.40916178889483,
            "unit": "iter/sec",
            "range": "stddev: 0.0002017054576647617",
            "extra": "mean: 17.72761672549561 msec\nrounds: 51"
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
          "id": "37f343d83e8c2c30a3e77eb3fc3e1c40b208e958",
          "message": "Add a complete set of authors",
          "timestamp": "2025-07-23T08:06:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/460/commits/37f343d83e8c2c30a3e77eb3fc3e1c40b208e958"
        },
        "date": 1753258346768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1142038880196058,
            "unit": "iter/sec",
            "range": "stddev: 0.09284859447962512",
            "extra": "mean: 8.756269312200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20572273943955327,
            "unit": "iter/sec",
            "range": "stddev: 0.014149205385932255",
            "extra": "mean: 4.860911354400014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.48981826931595,
            "unit": "iter/sec",
            "range": "stddev: 0.00021156696829629764",
            "extra": "mean: 9.050607700001164 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11551032926283548,
            "unit": "iter/sec",
            "range": "stddev: 0.13332546341068813",
            "extra": "mean: 8.657234434200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2062268249955399,
            "unit": "iter/sec",
            "range": "stddev: 0.012382577667043681",
            "extra": "mean: 4.849029703199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.43920417984891,
            "unit": "iter/sec",
            "range": "stddev: 0.0002954496660080854",
            "extra": "mean: 18.03777696295794 msec\nrounds: 54"
          }
        ]
      }
    ]
  }
}