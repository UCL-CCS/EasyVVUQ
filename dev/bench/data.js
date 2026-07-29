window.BENCHMARK_DATA = {
  "lastUpdate": 1785314108920,
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
          "id": "56b8819034208a2b70e948e94c6265784ed54517",
          "message": "Dpc/python notebooks as tutorial",
          "timestamp": "2025-07-23T08:06:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/461/commits/56b8819034208a2b70e948e94c6265784ed54517"
        },
        "date": 1753258362799,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11475167984334052,
            "unit": "iter/sec",
            "range": "stddev: 0.08680685754038595",
            "extra": "mean: 8.714469377400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20377523053567362,
            "unit": "iter/sec",
            "range": "stddev: 0.015251520226664013",
            "extra": "mean: 4.907367776599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.53114879446133,
            "unit": "iter/sec",
            "range": "stddev: 0.00026587187622890534",
            "extra": "mean: 9.129822986486992 msec\nrounds: 74"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11533153572470264,
            "unit": "iter/sec",
            "range": "stddev: 0.1595668632664152",
            "extra": "mean: 8.670655373800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20762781396093621,
            "unit": "iter/sec",
            "range": "stddev: 0.040725768042908395",
            "extra": "mean: 4.816310401399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.200786282555896,
            "unit": "iter/sec",
            "range": "stddev: 0.0004707027203135242",
            "extra": "mean: 18.449916847827026 msec\nrounds: 46"
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
          "id": "5ce715568bb7e370990b8407f0b2616fc2f6c49c",
          "message": "Fix packaging issue #445: Correct packaging and improve installation",
          "timestamp": "2025-07-23T08:06:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/462/commits/5ce715568bb7e370990b8407f0b2616fc2f6c49c"
        },
        "date": 1753258507065,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1160122400720436,
            "unit": "iter/sec",
            "range": "stddev: 0.07583885902326949",
            "extra": "mean: 8.619780114399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2041603595542897,
            "unit": "iter/sec",
            "range": "stddev: 0.023553012113032974",
            "extra": "mean: 4.898110495999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.52732494419772,
            "unit": "iter/sec",
            "range": "stddev: 0.00009765662514473249",
            "extra": "mean: 9.047536439562553 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11696127659462957,
            "unit": "iter/sec",
            "range": "stddev: 0.11470900422489629",
            "extra": "mean: 8.549838280799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21156745682017405,
            "unit": "iter/sec",
            "range": "stddev: 0.021783495901599677",
            "extra": "mean: 4.726624855399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.07346600336914,
            "unit": "iter/sec",
            "range": "stddev: 0.00012679138766027943",
            "extra": "mean: 17.833746890907648 msec\nrounds: 55"
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
          "id": "b813777f08d4f82b603a2e1b6bf30e6661c49a81",
          "message": "Full Integration Tests",
          "timestamp": "2025-07-23T08:06:45Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/b813777f08d4f82b603a2e1b6bf30e6661c49a81"
        },
        "date": 1753258816443,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1136649545186126,
            "unit": "iter/sec",
            "range": "stddev: 0.10635489133416126",
            "extra": "mean: 8.797786479 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19799488052533454,
            "unit": "iter/sec",
            "range": "stddev: 0.046065102778715596",
            "extra": "mean: 5.050635639400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.95163708109372,
            "unit": "iter/sec",
            "range": "stddev: 0.0003309734488699949",
            "extra": "mean: 9.528198204543708 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11453734281666426,
            "unit": "iter/sec",
            "range": "stddev: 0.09231332224905592",
            "extra": "mean: 8.730777014799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20519333458696698,
            "unit": "iter/sec",
            "range": "stddev: 0.02258924497533216",
            "extra": "mean: 4.873452649000012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.870571912691645,
            "unit": "iter/sec",
            "range": "stddev: 0.00017919136428468977",
            "extra": "mean: 18.91411353846068 msec\nrounds: 52"
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
          "id": "ed5cd7296a8d2e39428e17d63265e597586888c6",
          "message": "Merge pull request #462 from UCL-CCS/fix/packaging-issue-445\n\nFix packaging issue #445: Correct packaging and improve installation",
          "timestamp": "2025-07-23T09:44:11+01:00",
          "tree_id": "ce491facc275ee6025544b91aef13574cf2ed3ef",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ed5cd7296a8d2e39428e17d63265e597586888c6"
        },
        "date": 1753260506038,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11674416534910684,
            "unit": "iter/sec",
            "range": "stddev: 0.07539841321286335",
            "extra": "mean: 8.565738570400004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20626816718717186,
            "unit": "iter/sec",
            "range": "stddev: 0.012968977904685004",
            "extra": "mean: 4.848057815399988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.85632871757295,
            "unit": "iter/sec",
            "range": "stddev: 0.0000993178943486879",
            "extra": "mean: 8.782998813184609 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1174975016861646,
            "unit": "iter/sec",
            "range": "stddev: 0.09713339941916721",
            "extra": "mean: 8.510819257000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20920564706687603,
            "unit": "iter/sec",
            "range": "stddev: 0.003422360243234416",
            "extra": "mean: 4.7799856936000085 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.32503084973996,
            "unit": "iter/sec",
            "range": "stddev: 0.00015728487251273092",
            "extra": "mean: 17.444386600003657 msec\nrounds: 55"
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
          "id": "8ce4d0b1118688b9021cea64b0aa4e26a1cab3bc",
          "message": "Dpc/python notebooks as tutorial",
          "timestamp": "2025-07-23T08:44:17Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/461/commits/8ce4d0b1118688b9021cea64b0aa4e26a1cab3bc"
        },
        "date": 1753260555016,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11446662615365566,
            "unit": "iter/sec",
            "range": "stddev: 0.10172809290280248",
            "extra": "mean: 8.736170826399984 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20520603565657108,
            "unit": "iter/sec",
            "range": "stddev: 0.034215883877953344",
            "extra": "mean: 4.873151010400011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.7773449625134,
            "unit": "iter/sec",
            "range": "stddev: 0.00028343563026752205",
            "extra": "mean: 9.544047908045139 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11570715167777816,
            "unit": "iter/sec",
            "range": "stddev: 0.1028107728555994",
            "extra": "mean: 8.642508138000016 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20875024352688504,
            "unit": "iter/sec",
            "range": "stddev: 0.034131686926757415",
            "extra": "mean: 4.790413573200022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.5731537814941,
            "unit": "iter/sec",
            "range": "stddev: 0.00026362360892604223",
            "extra": "mean: 18.3240280377401 msec\nrounds: 53"
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
          "id": "620f4eda584b924eeaf3a74689b4bc0bc355aea6",
          "message": "Add a complete set of authors",
          "timestamp": "2025-07-23T08:44:17Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/460/commits/620f4eda584b924eeaf3a74689b4bc0bc355aea6"
        },
        "date": 1753260585089,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1150509457406924,
            "unit": "iter/sec",
            "range": "stddev: 0.0884312568486541",
            "extra": "mean: 8.691801649799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20306541941991302,
            "unit": "iter/sec",
            "range": "stddev: 0.007825507750079142",
            "extra": "mean: 4.924521382600005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.95289072021446,
            "unit": "iter/sec",
            "range": "stddev: 0.00012977092069127775",
            "extra": "mean: 9.094804087912475 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11774201374330326,
            "unit": "iter/sec",
            "range": "stddev: 0.10083755069978914",
            "extra": "mean: 8.493145039800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20960481004102904,
            "unit": "iter/sec",
            "range": "stddev: 0.00424422562474959",
            "extra": "mean: 4.770882880999989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.27791895703596,
            "unit": "iter/sec",
            "range": "stddev: 0.0025686250429804982",
            "extra": "mean: 18.42369824074421 msec\nrounds: 54"
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
          "id": "1b67706da517b49fecc8474bd4232fa135b21e99",
          "message": "Merge pull request #460 from UCL-CCS/dpc/add_authors\n\nAdd a complete set of authors",
          "timestamp": "2025-07-23T09:46:02+01:00",
          "tree_id": "e4bc6abcdd35ef29ac160690185fd672621e66f0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/1b67706da517b49fecc8474bd4232fa135b21e99"
        },
        "date": 1753260772737,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11591172150132154,
            "unit": "iter/sec",
            "range": "stddev: 0.0701373381871303",
            "extra": "mean: 8.627255182200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20792302398094273,
            "unit": "iter/sec",
            "range": "stddev: 0.005103413297651462",
            "extra": "mean: 4.809472182799993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.89787986016839,
            "unit": "iter/sec",
            "range": "stddev: 0.00010877625191882052",
            "extra": "mean: 8.93671981318713 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11720598804142085,
            "unit": "iter/sec",
            "range": "stddev: 0.12373144629281818",
            "extra": "mean: 8.531987287599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2115863647239868,
            "unit": "iter/sec",
            "range": "stddev: 0.008858944811269236",
            "extra": "mean: 4.726202472 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.83004016965882,
            "unit": "iter/sec",
            "range": "stddev: 0.000304788246031052",
            "extra": "mean: 17.911504218179953 msec\nrounds: 55"
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
          "id": "f945806b4bf8d8475d4dcf5e3c103fe342a96f1a",
          "message": "Full Integration Tests",
          "timestamp": "2025-07-23T08:46:06Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/f945806b4bf8d8475d4dcf5e3c103fe342a96f1a"
        },
        "date": 1753260878281,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1147714909223258,
            "unit": "iter/sec",
            "range": "stddev: 0.07791803905000262",
            "extra": "mean: 8.7129651446 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20089045890807478,
            "unit": "iter/sec",
            "range": "stddev: 0.008894332977506938",
            "extra": "mean: 4.977837202599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.73387808060198,
            "unit": "iter/sec",
            "range": "stddev: 0.00006568579587020048",
            "extra": "mean: 8.79245495604494 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11606562811663527,
            "unit": "iter/sec",
            "range": "stddev: 0.08059853394117193",
            "extra": "mean: 8.615815174800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20906576357125342,
            "unit": "iter/sec",
            "range": "stddev: 0.008514822862171078",
            "extra": "mean: 4.783183926999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.28888814442177,
            "unit": "iter/sec",
            "range": "stddev: 0.00013248011877967973",
            "extra": "mean: 17.15592854545982 msec\nrounds: 55"
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
          "id": "ffeeaf197504bace4d567ee3df304c96e89a80db",
          "message": "Merge pull request #461 from UCL-CCS/dpc/python_notebooks_as_tutorial\n\nDpc/python notebooks as tutorial",
          "timestamp": "2025-07-23T09:54:55+01:00",
          "tree_id": "cf9ed0d27c60e7f8cc8e42a700bea06a225de59a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ffeeaf197504bace4d567ee3df304c96e89a80db"
        },
        "date": 1753261155352,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11625423753787346,
            "unit": "iter/sec",
            "range": "stddev: 0.12826850676267437",
            "extra": "mean: 8.601836983999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20079103373013643,
            "unit": "iter/sec",
            "range": "stddev: 0.01606392704182865",
            "extra": "mean: 4.980302065400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.08926551420265,
            "unit": "iter/sec",
            "range": "stddev: 0.00011015962586934919",
            "extra": "mean: 8.92146090361607 msec\nrounds: 83"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11750047219597497,
            "unit": "iter/sec",
            "range": "stddev: 0.1316186115019866",
            "extra": "mean: 8.51060409640001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20528147716405956,
            "unit": "iter/sec",
            "range": "stddev: 0.012544148677163145",
            "extra": "mean: 4.871360113999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.96631380938975,
            "unit": "iter/sec",
            "range": "stddev: 0.0003985778182360607",
            "extra": "mean: 17.867891092591933 msec\nrounds: 54"
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
          "id": "4d248038240ca46e3b614377a2a7e0b58e8d6574",
          "message": "Bump starlette from 0.45.2 to 0.47.2",
          "timestamp": "2025-07-23T08:55:02Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/463/commits/4d248038240ca46e3b614377a2a7e0b58e8d6574"
        },
        "date": 1753261207285,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11618728195520274,
            "unit": "iter/sec",
            "range": "stddev: 0.09282177090747959",
            "extra": "mean: 8.606793989600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20835828137260096,
            "unit": "iter/sec",
            "range": "stddev: 0.019544483445858317",
            "extra": "mean: 4.799425266000009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.77009362511089,
            "unit": "iter/sec",
            "range": "stddev: 0.00021546520509684435",
            "extra": "mean: 9.454468325842438 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11686570101603745,
            "unit": "iter/sec",
            "range": "stddev: 0.0963242575308712",
            "extra": "mean: 8.55683054399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21270794467676224,
            "unit": "iter/sec",
            "range": "stddev: 0.016072358513479403",
            "extra": "mean: 4.701281851600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.999697573544374,
            "unit": "iter/sec",
            "range": "stddev: 0.00013951928978628083",
            "extra": "mean: 18.868032192303783 msec\nrounds: 52"
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
          "id": "ac9b714e907de57e095ce9502231d560f569eb96",
          "message": "Full Integration Tests",
          "timestamp": "2025-07-23T08:55:02Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/ac9b714e907de57e095ce9502231d560f569eb96"
        },
        "date": 1753263754620,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11571578393725697,
            "unit": "iter/sec",
            "range": "stddev: 0.091741017100652",
            "extra": "mean: 8.641863417199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20193190410909348,
            "unit": "iter/sec",
            "range": "stddev: 0.02299916247238455",
            "extra": "mean: 4.952164465600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.03689350314687,
            "unit": "iter/sec",
            "range": "stddev: 0.00009943286030948915",
            "extra": "mean: 9.006015644445773 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1165894639858864,
            "unit": "iter/sec",
            "range": "stddev: 0.09082930658013628",
            "extra": "mean: 8.57710436100001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20768378613612434,
            "unit": "iter/sec",
            "range": "stddev: 0.015190560000840778",
            "extra": "mean: 4.815012373400009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.207692937923326,
            "unit": "iter/sec",
            "range": "stddev: 0.00018799455838814811",
            "extra": "mean: 17.791158962962882 msec\nrounds: 54"
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
          "id": "b286c0080f6fa705800bb5d36e61a3b2a1cd7dd2",
          "message": "Full Integration Tests",
          "timestamp": "2025-07-23T08:55:02Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/295/commits/b286c0080f6fa705800bb5d36e61a3b2a1cd7dd2"
        },
        "date": 1753263858231,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11368443246063406,
            "unit": "iter/sec",
            "range": "stddev: 0.07488018197505104",
            "extra": "mean: 8.796279124199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20305424868498712,
            "unit": "iter/sec",
            "range": "stddev: 0.010529158068263086",
            "extra": "mean: 4.9247922979999945 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.46937069510824,
            "unit": "iter/sec",
            "range": "stddev: 0.000363317786173364",
            "extra": "mean: 10.053345999998154 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11235281480856747,
            "unit": "iter/sec",
            "range": "stddev: 0.16978369511146651",
            "extra": "mean: 8.900533570999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20358310353426365,
            "unit": "iter/sec",
            "range": "stddev: 0.013512383741441819",
            "extra": "mean: 4.911998995199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.92168835961605,
            "unit": "iter/sec",
            "range": "stddev: 0.00035300215328764245",
            "extra": "mean: 18.20774324074313 msec\nrounds: 54"
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
          "id": "19c4a480b64adb4a3a61a38d3d16d5654eba4866",
          "message": "fix typo (Totorial --> Tutorial)",
          "timestamp": "2025-07-23T08:55:02Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/464/commits/19c4a480b64adb4a3a61a38d3d16d5654eba4866"
        },
        "date": 1753270636385,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11488485130047357,
            "unit": "iter/sec",
            "range": "stddev: 0.12029794906821784",
            "extra": "mean: 8.70436779680001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2085880503267976,
            "unit": "iter/sec",
            "range": "stddev: 0.02634863586012592",
            "extra": "mean: 4.794138487000032 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.37510512170029,
            "unit": "iter/sec",
            "range": "stddev: 0.0002131070480104024",
            "extra": "mean: 9.142848355549582 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11650580893744686,
            "unit": "iter/sec",
            "range": "stddev: 0.09376859662222414",
            "extra": "mean: 8.583263007400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21387541003446142,
            "unit": "iter/sec",
            "range": "stddev: 0.009127623253340905",
            "extra": "mean: 4.675619323599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.70493312939323,
            "unit": "iter/sec",
            "range": "stddev: 0.00019717925648255117",
            "extra": "mean: 18.279887074072576 msec\nrounds: 54"
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
          "id": "780a987525991071decac38dee09f72fe885b27a",
          "message": "Merge pull request #295 from UCL-CCS/test-full\n\nFull Integration Tests",
          "timestamp": "2025-07-23T13:36:21+02:00",
          "tree_id": "a3e1c49a97c61d431fcb8327de986712df3f8d6b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/780a987525991071decac38dee09f72fe885b27a"
        },
        "date": 1753270843826,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11546654271061736,
            "unit": "iter/sec",
            "range": "stddev: 0.08908394577479299",
            "extra": "mean: 8.660517380399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20413190629227068,
            "unit": "iter/sec",
            "range": "stddev: 0.01557921076935254",
            "extra": "mean: 4.898793227199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.61442921248332,
            "unit": "iter/sec",
            "range": "stddev: 0.00012948986859257774",
            "extra": "mean: 9.040411880434363 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11661521610562221,
            "unit": "iter/sec",
            "range": "stddev: 0.09072866152932074",
            "extra": "mean: 8.575210280400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20981182943201748,
            "unit": "iter/sec",
            "range": "stddev: 0.011321393029965826",
            "extra": "mean: 4.7661754949999935 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.639423352262234,
            "unit": "iter/sec",
            "range": "stddev: 0.0001507977213416705",
            "extra": "mean: 17.655546981483507 msec\nrounds: 54"
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
          "id": "71e31079347b5241b1711dea31b8f7665e8e90e4",
          "message": "Bump starlette from 0.45.2 to 0.47.2",
          "timestamp": "2025-07-23T11:36:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/463/commits/71e31079347b5241b1711dea31b8f7665e8e90e4"
        },
        "date": 1753270886159,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11450627810808925,
            "unit": "iter/sec",
            "range": "stddev: 0.0880360796097624",
            "extra": "mean: 8.733145610200001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19814679056214546,
            "unit": "iter/sec",
            "range": "stddev: 0.021641995598151664",
            "extra": "mean: 5.046763549199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.59186438161925,
            "unit": "iter/sec",
            "range": "stddev: 0.0001387126945935152",
            "extra": "mean: 8.881636390801708 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11545134692298553,
            "unit": "iter/sec",
            "range": "stddev: 0.09880362834735365",
            "extra": "mean: 8.661657283800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2050350422436146,
            "unit": "iter/sec",
            "range": "stddev: 0.003972243591459496",
            "extra": "mean: 4.877215080199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.572343449001146,
            "unit": "iter/sec",
            "range": "stddev: 0.00019902419279827296",
            "extra": "mean: 17.6764818113197 msec\nrounds: 53"
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
          "id": "4a5ff21b828262bfac5be8bb2cb2cc92cfe0d37c",
          "message": "fix typo (Totorial --> Tutorial)",
          "timestamp": "2025-07-23T11:36:27Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/464/commits/4a5ff21b828262bfac5be8bb2cb2cc92cfe0d37c"
        },
        "date": 1753270947402,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11546243726628355,
            "unit": "iter/sec",
            "range": "stddev: 0.08790930493814941",
            "extra": "mean: 8.660825318399997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2046560605738486,
            "unit": "iter/sec",
            "range": "stddev: 0.022700255197953895",
            "extra": "mean: 4.886246697000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.9433964884019,
            "unit": "iter/sec",
            "range": "stddev: 0.0005388122550012163",
            "extra": "mean: 8.933086107527627 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11664057669531722,
            "unit": "iter/sec",
            "range": "stddev: 0.11378681164861403",
            "extra": "mean: 8.5733458144 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20917272284043248,
            "unit": "iter/sec",
            "range": "stddev: 0.007153768069569352",
            "extra": "mean: 4.780738073399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.69049046203688,
            "unit": "iter/sec",
            "range": "stddev: 0.00015841319657642245",
            "extra": "mean: 17.33387932727055 msec\nrounds: 55"
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
          "id": "4afbbe1c06304c7bbd30921c6a6ea7a03a20998a",
          "message": "Merge pull request #463 from UCL-CCS/dependabot/pip/starlette-0.47.2",
          "timestamp": "2025-07-23T13:52:21+02:00",
          "tree_id": "fbeb7aa0d8e593979dc2512b99f287c7c7c75dec",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/4afbbe1c06304c7bbd30921c6a6ea7a03a20998a"
        },
        "date": 1753271800388,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11570937100083763,
            "unit": "iter/sec",
            "range": "stddev: 0.09440333902502293",
            "extra": "mean: 8.642342373399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20114826114063908,
            "unit": "iter/sec",
            "range": "stddev: 0.020280477194777796",
            "extra": "mean: 4.9714573435999965 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.0121360794403,
            "unit": "iter/sec",
            "range": "stddev: 0.0003006349133026509",
            "extra": "mean: 9.089906219781927 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11618332503197627,
            "unit": "iter/sec",
            "range": "stddev: 0.12243236275269201",
            "extra": "mean: 8.6070871162 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21199592111724125,
            "unit": "iter/sec",
            "range": "stddev: 0.03751587737208544",
            "extra": "mean: 4.717071888599992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.764761483062486,
            "unit": "iter/sec",
            "range": "stddev: 0.00018587197390731804",
            "extra": "mean: 17.616563055556586 msec\nrounds: 54"
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
          "id": "844fdcb560cb14f146dd364462e5a7f47b45158a",
          "message": "Merge pull request #464 from UCL-CCS/typo-fix",
          "timestamp": "2025-07-23T14:01:37+02:00",
          "tree_id": "c63a5f1ac7f3b22923e5a1adc2a49d0ea67e79ba",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/844fdcb560cb14f146dd364462e5a7f47b45158a"
        },
        "date": 1753272359669,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11442154184884248,
            "unit": "iter/sec",
            "range": "stddev: 0.07508036095722413",
            "extra": "mean: 8.739613046999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20264642365850857,
            "unit": "iter/sec",
            "range": "stddev: 0.014460148220064818",
            "extra": "mean: 4.934703420600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.63146441893319,
            "unit": "iter/sec",
            "range": "stddev: 0.0001323071228530852",
            "extra": "mean: 9.466876233335281 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11613644096218086,
            "unit": "iter/sec",
            "range": "stddev: 0.11570477308553856",
            "extra": "mean: 8.610561781600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2076593835171694,
            "unit": "iter/sec",
            "range": "stddev: 0.013348231116828532",
            "extra": "mean: 4.815578198600013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.19853940984182,
            "unit": "iter/sec",
            "range": "stddev: 0.00014512156505115063",
            "extra": "mean: 18.11642138889098 msec\nrounds: 54"
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
          "id": "5350756f7be975549a796be165e6b280205fb459",
          "message": "Feature/add contributing guidelines issue 230",
          "timestamp": "2025-07-23T12:01:41Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/465/commits/5350756f7be975549a796be165e6b280205fb459"
        },
        "date": 1753290698519,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11440927385115375,
            "unit": "iter/sec",
            "range": "stddev: 0.061790307234901524",
            "extra": "mean: 8.7405501874 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1998767992748717,
            "unit": "iter/sec",
            "range": "stddev: 0.007533960267029776",
            "extra": "mean: 5.003081916600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.32274732235425,
            "unit": "iter/sec",
            "range": "stddev: 0.0002256471747825207",
            "extra": "mean: 9.231671322221283 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11601410317147862,
            "unit": "iter/sec",
            "range": "stddev: 0.11135655101025481",
            "extra": "mean: 8.61964168720001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20740386540659617,
            "unit": "iter/sec",
            "range": "stddev: 0.008309237497668426",
            "extra": "mean: 4.82151091080001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.25937100351453,
            "unit": "iter/sec",
            "range": "stddev: 0.0002544091391296388",
            "extra": "mean: 18.096478150943838 msec\nrounds: 53"
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
          "id": "765d9887c0d99d3206e9ce46b7cece2b3f6351e6",
          "message": "Merge pull request #465 from UCL-CCS/feature/add-contributing-guidelines-issue-230\n\nFeature/add contributing guidelines issue 230",
          "timestamp": "2025-08-01T14:28:30+02:00",
          "tree_id": "c0cf584afdec7d381a5bf753dce84ea2eef5876b",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/765d9887c0d99d3206e9ce46b7cece2b3f6351e6"
        },
        "date": 1754051571113,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11635292745885217,
            "unit": "iter/sec",
            "range": "stddev: 0.06998394177302396",
            "extra": "mean: 8.594540952599981 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20279819108327463,
            "unit": "iter/sec",
            "range": "stddev: 0.015332083605758173",
            "extra": "mean: 4.931010452600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.12203496333326,
            "unit": "iter/sec",
            "range": "stddev: 0.00018069028290665658",
            "extra": "mean: 9.080834733329842 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11613072505443632,
            "unit": "iter/sec",
            "range": "stddev: 0.08884258074445385",
            "extra": "mean: 8.610985589999974 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20942631490768218,
            "unit": "iter/sec",
            "range": "stddev: 0.042366614916353976",
            "extra": "mean: 4.774949129199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.882753593636565,
            "unit": "iter/sec",
            "range": "stddev: 0.00035295029604617964",
            "extra": "mean: 17.89460854545062 msec\nrounds: 55"
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
          "id": "04b5bc456b374ff2e1aa10d9ca790644ce7f8688",
          "message": "Fix for security vulnerability.",
          "timestamp": "2025-08-01T12:28:35Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/466/commits/04b5bc456b374ff2e1aa10d9ca790644ce7f8688"
        },
        "date": 1755246710926,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11497747736101614,
            "unit": "iter/sec",
            "range": "stddev: 0.07034947443757232",
            "extra": "mean: 8.697355542600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19961274307833643,
            "unit": "iter/sec",
            "range": "stddev: 0.02588902679307477",
            "extra": "mean: 5.009700205400003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.78946081150845,
            "unit": "iter/sec",
            "range": "stddev: 0.00006095461469385892",
            "extra": "mean: 8.489723894739965 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11610779128269189,
            "unit": "iter/sec",
            "range": "stddev: 0.09840804533088254",
            "extra": "mean: 8.612686443799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.207655678160019,
            "unit": "iter/sec",
            "range": "stddev: 0.01863125229916888",
            "extra": "mean: 4.815664126600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.13228770614438,
            "unit": "iter/sec",
            "range": "stddev: 0.0003930472149907909",
            "extra": "mean: 16.91123477193139 msec\nrounds: 57"
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
          "id": "13397acf4f5be04cd2d1a526c092f441eae55bde",
          "message": "Merge pull request #467 from UCL-CCS/dependabot/pip/starlette-0.49.1\n\nBump starlette from 0.47.2 to 0.49.1",
          "timestamp": "2025-10-29T09:18:56Z",
          "tree_id": "cba27314b17935d576247eb6080f8e7ab6a06cf0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/13397acf4f5be04cd2d1a526c092f441eae55bde"
        },
        "date": 1761729799480,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11306250479218401,
            "unit": "iter/sec",
            "range": "stddev: 0.06735054579608318",
            "extra": "mean: 8.844665186199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1996611052389954,
            "unit": "iter/sec",
            "range": "stddev: 0.03371565589704448",
            "extra": "mean: 5.008486749600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.32365333759606,
            "unit": "iter/sec",
            "range": "stddev: 0.00019376710062852671",
            "extra": "mean: 9.064239351646092 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11414836261102847,
            "unit": "iter/sec",
            "range": "stddev: 0.13233682614540462",
            "extra": "mean: 8.760528641200017 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.204519286998049,
            "unit": "iter/sec",
            "range": "stddev: 0.010248223656240275",
            "extra": "mean: 4.889514405599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.84616365074789,
            "unit": "iter/sec",
            "range": "stddev: 0.00013731272827846927",
            "extra": "mean: 17.906332944440457 msec\nrounds: 54"
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
          "id": "8a66a6ee87275b184bb03cafd51a3cc9c0a077b0",
          "message": "Merge pull request #469 from UCL-CCS/dependabot/pip/bokeh-3.8.2\n\nBump bokeh from 3.6.2 to 3.8.2",
          "timestamp": "2026-01-07T09:53:07Z",
          "tree_id": "59505b89656650fa70214d8300e81898603eeb97",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/8a66a6ee87275b184bb03cafd51a3cc9c0a077b0"
        },
        "date": 1767779847377,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11500777542796989,
            "unit": "iter/sec",
            "range": "stddev: 0.09916294193683765",
            "extra": "mean: 8.695064279600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19776295767179014,
            "unit": "iter/sec",
            "range": "stddev: 0.04126220194106634",
            "extra": "mean: 5.056558679 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.27731121823052,
            "unit": "iter/sec",
            "range": "stddev: 0.0001812711827448148",
            "extra": "mean: 8.827893152173115 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11655287080312775,
            "unit": "iter/sec",
            "range": "stddev: 0.1160971530895607",
            "extra": "mean: 8.579797246599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20212814012939043,
            "unit": "iter/sec",
            "range": "stddev: 0.009307443122279851",
            "extra": "mean: 4.947356658800004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.619126619997225,
            "unit": "iter/sec",
            "range": "stddev: 0.0002543710992606136",
            "extra": "mean: 17.66187611320044 msec\nrounds: 53"
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
          "id": "d48a887980948f8118804d7cdb466a4d9ae746da",
          "message": "Merge pull request #468 from UCL-CCS/dependabot/pip/urllib3-2.6.0\n\nBump urllib3 from 2.5.0 to 2.6.0",
          "timestamp": "2026-01-07T09:54:04Z",
          "tree_id": "2913a330ec696507ebb795c92bb4ffbb151bb96a",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/d48a887980948f8118804d7cdb466a4d9ae746da"
        },
        "date": 1767779908321,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1145918934974633,
            "unit": "iter/sec",
            "range": "stddev: 0.0900593643011386",
            "extra": "mean: 8.726620788599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19313221461649438,
            "unit": "iter/sec",
            "range": "stddev: 0.026734575027532563",
            "extra": "mean: 5.177800099199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.93096555697369,
            "unit": "iter/sec",
            "range": "stddev: 0.00020061203251180143",
            "extra": "mean: 8.854967236559222 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11593270260618706,
            "unit": "iter/sec",
            "range": "stddev: 0.07163283586034598",
            "extra": "mean: 8.625693851000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.198380808626861,
            "unit": "iter/sec",
            "range": "stddev: 0.020552475329546134",
            "extra": "mean: 5.040810181800009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.97976765014737,
            "unit": "iter/sec",
            "range": "stddev: 0.00022933338308270731",
            "extra": "mean: 17.24739578181904 msec\nrounds: 55"
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
          "id": "805b41f8313ed5b8d24a16917d80b8811e28166a",
          "message": "Merge pull request #470 from UCL-CCS/dependabot/pip/fonttools-4.60.2",
          "timestamp": "2026-01-07T14:02:52+01:00",
          "tree_id": "7002c553602c0253c7997523bfcfcf34ccecd77c",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/805b41f8313ed5b8d24a16917d80b8811e28166a"
        },
        "date": 1767791227637,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11412143303964713,
            "unit": "iter/sec",
            "range": "stddev: 0.11787296831361477",
            "extra": "mean: 8.762595888999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19717654621274303,
            "unit": "iter/sec",
            "range": "stddev: 0.017683188086287983",
            "extra": "mean: 5.071597100200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 112.73421797497983,
            "unit": "iter/sec",
            "range": "stddev: 0.0003528582862163577",
            "extra": "mean: 8.870421225806874 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11538988195457543,
            "unit": "iter/sec",
            "range": "stddev: 0.08193524386303755",
            "extra": "mean: 8.666271106800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20041282862204593,
            "unit": "iter/sec",
            "range": "stddev: 0.01400408497153455",
            "extra": "mean: 4.989700543999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.90016842688682,
            "unit": "iter/sec",
            "range": "stddev: 0.00015193375027456693",
            "extra": "mean: 17.574640421054955 msec\nrounds: 57"
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
          "id": "c8401625335472765c458e82698b0716d3bb5562",
          "message": "Merge pull request #471 from UCL-CCS/dependabot/pip/urllib3-2.6.3\n\nBump urllib3 from 2.6.0 to 2.6.3",
          "timestamp": "2026-01-08T08:29:00Z",
          "tree_id": "0eb7f1e58802824a39a44623d79640a041b1d676",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c8401625335472765c458e82698b0716d3bb5562"
        },
        "date": 1767861193008,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11422202579158906,
            "unit": "iter/sec",
            "range": "stddev: 0.07445675377974162",
            "extra": "mean: 8.754878869199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20092946005894313,
            "unit": "iter/sec",
            "range": "stddev: 0.056848105436791904",
            "extra": "mean: 4.976870986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 119.11056181497595,
            "unit": "iter/sec",
            "range": "stddev: 0.00005978506181356033",
            "extra": "mean: 8.395561105264372 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11592219229394421,
            "unit": "iter/sec",
            "range": "stddev: 0.07750787326543557",
            "extra": "mean: 8.626475916400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20645101193099008,
            "unit": "iter/sec",
            "range": "stddev: 0.01317030943553209",
            "extra": "mean: 4.8437640999999925 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.542024185105916,
            "unit": "iter/sec",
            "range": "stddev: 0.0014679048104258537",
            "extra": "mean: 16.794860666664135 msec\nrounds: 57"
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
          "id": "72d014fa85d16f9e9f81a3ee23c792a54bb64b35",
          "message": "Merge pull request #472 from UCL-CCS/dependabot/pip/pyasn1-0.6.2\n\nBump pyasn1 from 0.6.1 to 0.6.2",
          "timestamp": "2026-01-16T20:59:59Z",
          "tree_id": "2761af5d8fe9390e272817fbd2368012c60e2f60",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/72d014fa85d16f9e9f81a3ee23c792a54bb64b35"
        },
        "date": 1768597456995,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11531444239421162,
            "unit": "iter/sec",
            "range": "stddev: 0.08638763493869712",
            "extra": "mean: 8.671940645399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1954704506764969,
            "unit": "iter/sec",
            "range": "stddev: 0.029944193835145887",
            "extra": "mean: 5.115862763599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 108.68841664948792,
            "unit": "iter/sec",
            "range": "stddev: 0.00015134701338413551",
            "extra": "mean: 9.200612455556564 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11652004987941082,
            "unit": "iter/sec",
            "range": "stddev: 0.09118560072951647",
            "extra": "mean: 8.582213971199996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1996814547966001,
            "unit": "iter/sec",
            "range": "stddev: 0.008639949777973258",
            "extra": "mean: 5.007976334199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.232246917324034,
            "unit": "iter/sec",
            "range": "stddev: 0.00018968416720519237",
            "extra": "mean: 17.783390400000535 msec\nrounds: 55"
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
          "id": "4da9656a4a861bd7597a08484859a1ac015e6194",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/4da9656a4a861bd7597a08484859a1ac015e6194"
        },
        "date": 1777371653641,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.14465655210236508,
            "unit": "iter/sec",
            "range": "stddev: 0.10661703187593466",
            "extra": "mean: 6.912925722800014 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.22998730298470973,
            "unit": "iter/sec",
            "range": "stddev: 0.0402741070322658",
            "extra": "mean: 4.348066119400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.9542070770664,
            "unit": "iter/sec",
            "range": "stddev: 0.0002453330262240178",
            "extra": "mean: 10.004581390245864 msec\nrounds: 82"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.14701731152674744,
            "unit": "iter/sec",
            "range": "stddev: 0.09594678368029813",
            "extra": "mean: 6.801920056999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.23703404707341402,
            "unit": "iter/sec",
            "range": "stddev: 0.019742143476862983",
            "extra": "mean: 4.218803215599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 50.38018987093492,
            "unit": "iter/sec",
            "range": "stddev: 0.0004068256987945822",
            "extra": "mean: 19.849071679996086 msec\nrounds: 50"
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
          "id": "e882cabde890086a61dca1fede71cfa7bc834a18",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/e882cabde890086a61dca1fede71cfa7bc834a18"
        },
        "date": 1777372068747,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.13704801463529057,
            "unit": "iter/sec",
            "range": "stddev: 0.06729549317085001",
            "extra": "mean: 7.296712781000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.22116628938950267,
            "unit": "iter/sec",
            "range": "stddev: 0.01736020140261729",
            "extra": "mean: 4.52148472880001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 138.94069840367618,
            "unit": "iter/sec",
            "range": "stddev: 0.00021885297179644235",
            "extra": "mean: 7.197315196261755 msec\nrounds: 107"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.13867176567497175,
            "unit": "iter/sec",
            "range": "stddev: 0.05725714070848985",
            "extra": "mean: 7.2112732907999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.23005197687115092,
            "unit": "iter/sec",
            "range": "stddev: 0.02701271861458186",
            "extra": "mean: 4.346843759400019 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 71.28447272144975,
            "unit": "iter/sec",
            "range": "stddev: 0.0002935404646494873",
            "extra": "mean: 14.02830043939003 msec\nrounds: 66"
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
          "id": "6100dc555176c85bffb9d97c4801ca18d3a1b59e",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/6100dc555176c85bffb9d97c4801ca18d3a1b59e"
        },
        "date": 1777372293697,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12725075560060106,
            "unit": "iter/sec",
            "range": "stddev: 0.030972748543445384",
            "extra": "mean: 7.8584995058 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20917691305725591,
            "unit": "iter/sec",
            "range": "stddev: 0.051190814737605984",
            "extra": "mean: 4.780642305999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.42265676384325,
            "unit": "iter/sec",
            "range": "stddev: 0.00015557920290433638",
            "extra": "mean: 8.816580642103059 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1281218064813349,
            "unit": "iter/sec",
            "range": "stddev: 0.03966148730631613",
            "extra": "mean: 7.805072590399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21032531486442943,
            "unit": "iter/sec",
            "range": "stddev: 0.13033871384370116",
            "extra": "mean: 4.75453941740002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.042084992056886,
            "unit": "iter/sec",
            "range": "stddev: 0.00022186429308515828",
            "extra": "mean: 16.937071245612906 msec\nrounds: 57"
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
          "id": "42705c1f5d16438f26f0b392edecb512b979cef2",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/42705c1f5d16438f26f0b392edecb512b979cef2"
        },
        "date": 1777373368340,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.13237158606748883,
            "unit": "iter/sec",
            "range": "stddev: 0.044553782121682976",
            "extra": "mean: 7.554491335400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.22186999019212314,
            "unit": "iter/sec",
            "range": "stddev: 0.03599069700500231",
            "extra": "mean: 4.507144022199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.75725342908176,
            "unit": "iter/sec",
            "range": "stddev: 0.00014613236606289583",
            "extra": "mean: 8.492045889998963 msec\nrounds: 100"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.13266127624288632,
            "unit": "iter/sec",
            "range": "stddev: 0.02948925140442409",
            "extra": "mean: 7.537994721000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.22817925804369102,
            "unit": "iter/sec",
            "range": "stddev: 0.038683861127420074",
            "extra": "mean: 4.382519290200003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 62.02185081944906,
            "unit": "iter/sec",
            "range": "stddev: 0.0004853101276870486",
            "extra": "mean: 16.123349864406435 msec\nrounds: 59"
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
          "id": "a93a1ff0b5dc5566db16917ffe8c9f95ef9a6bb4",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/a93a1ff0b5dc5566db16917ffe8c9f95ef9a6bb4"
        },
        "date": 1777374045447,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12468199196822241,
            "unit": "iter/sec",
            "range": "stddev: 0.026660650942361804",
            "extra": "mean: 8.0204044242 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20748343589664117,
            "unit": "iter/sec",
            "range": "stddev: 0.016429812671748638",
            "extra": "mean: 4.819661847599991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.14668617426378,
            "unit": "iter/sec",
            "range": "stddev: 0.000729117672436297",
            "extra": "mean: 8.76065730435078 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12394921809587846,
            "unit": "iter/sec",
            "range": "stddev: 0.07092152003661613",
            "extra": "mean: 8.06782015540001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2103940888539253,
            "unit": "iter/sec",
            "range": "stddev: 0.013697352410181577",
            "extra": "mean: 4.7529852451999774 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.94463540743347,
            "unit": "iter/sec",
            "range": "stddev: 0.00024242408304133228",
            "extra": "mean: 17.257852999998583 msec\nrounds: 57"
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
          "id": "438c414ccc786dc394187321e0238d6781ceb43b",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/438c414ccc786dc394187321e0238d6781ceb43b"
        },
        "date": 1777377392338,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.16453110245326316,
            "unit": "iter/sec",
            "range": "stddev: 0.03853620782009584",
            "extra": "mean: 6.077878195000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.24968839716998636,
            "unit": "iter/sec",
            "range": "stddev: 0.00793503797646811",
            "extra": "mean: 4.004991867200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.44005089563738,
            "unit": "iter/sec",
            "range": "stddev: 0.0002618445420793275",
            "extra": "mean: 9.39495980681635 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.16380909926588694,
            "unit": "iter/sec",
            "range": "stddev: 0.04979010409480438",
            "extra": "mean: 6.104666984199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2512079122702908,
            "unit": "iter/sec",
            "range": "stddev: 0.022228945185590574",
            "extra": "mean: 3.9807663340000032 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.25420763991383,
            "unit": "iter/sec",
            "range": "stddev: 0.0005794933369775347",
            "extra": "mean: 18.777858958331468 msec\nrounds: 48"
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
          "id": "c4b4c2c2c9b03dce9fae172198c3cf120db5acec",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/c4b4c2c2c9b03dce9fae172198c3cf120db5acec"
        },
        "date": 1777377684782,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12573117059949523,
            "unit": "iter/sec",
            "range": "stddev: 0.07390897320729964",
            "extra": "mean: 7.953477210400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20753220065308658,
            "unit": "iter/sec",
            "range": "stddev: 0.023651186453122832",
            "extra": "mean: 4.818529350400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 115.19259213945921,
            "unit": "iter/sec",
            "range": "stddev: 0.00009199068115306333",
            "extra": "mean: 8.681113788891379 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1263897149925343,
            "unit": "iter/sec",
            "range": "stddev: 0.04492120970984064",
            "extra": "mean: 7.912036197399994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2120143334791912,
            "unit": "iter/sec",
            "range": "stddev: 0.007634584595592739",
            "extra": "mean: 4.716662235000013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.585702904709024,
            "unit": "iter/sec",
            "range": "stddev: 0.0001500900332109281",
            "extra": "mean: 17.069010875000043 msec\nrounds: 56"
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
          "id": "be4d00d7262cc044d0a61f0d8ba35789ced368d1",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/be4d00d7262cc044d0a61f0d8ba35789ced368d1"
        },
        "date": 1777377884318,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12819559701369532,
            "unit": "iter/sec",
            "range": "stddev: 0.0488152795999876",
            "extra": "mean: 7.800579920799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21138375488293662,
            "unit": "iter/sec",
            "range": "stddev: 0.02501601055208151",
            "extra": "mean: 4.730732503799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.65993039753263,
            "unit": "iter/sec",
            "range": "stddev: 0.00017455662832697438",
            "extra": "mean: 8.798175368420852 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12882194065478672,
            "unit": "iter/sec",
            "range": "stddev: 0.04142888508050737",
            "extra": "mean: 7.762652813000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21709441060030998,
            "unit": "iter/sec",
            "range": "stddev: 0.021489531619016785",
            "extra": "mean: 4.606290863200013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.49752703920327,
            "unit": "iter/sec",
            "range": "stddev: 0.00015716583155929383",
            "extra": "mean: 17.392052345454346 msec\nrounds: 55"
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
          "id": "2346c66cd9d0ba346776afb20f864b1fc8a4f3de",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/2346c66cd9d0ba346776afb20f864b1fc8a4f3de"
        },
        "date": 1777377931243,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.21244267209637652,
            "unit": "iter/sec",
            "range": "stddev: 0.03181121138296134",
            "extra": "mean: 4.707152240800008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.33647014023472355,
            "unit": "iter/sec",
            "range": "stddev: 0.009844602194144517",
            "extra": "mean: 2.9720319292 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 142.74033478539818,
            "unit": "iter/sec",
            "range": "stddev: 0.00014458140672474003",
            "extra": "mean: 7.005728279280289 msec\nrounds: 111"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.21090329467485672,
            "unit": "iter/sec",
            "range": "stddev: 0.03950876768694525",
            "extra": "mean: 4.741509617200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.3341705039856048,
            "unit": "iter/sec",
            "range": "stddev: 0.025031907513943116",
            "extra": "mean: 2.9924843398000123 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 70.03981381379383,
            "unit": "iter/sec",
            "range": "stddev: 0.0001523878940772838",
            "extra": "mean: 14.277593636364827 msec\nrounds: 66"
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
          "id": "6d7bf552893d8920a7adbaacf3807827d7a19755",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/6d7bf552893d8920a7adbaacf3807827d7a19755"
        },
        "date": 1777378476857,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1631773731049581,
            "unit": "iter/sec",
            "range": "stddev: 0.051846353146942734",
            "extra": "mean: 6.1283006398000115 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2572990700936756,
            "unit": "iter/sec",
            "range": "stddev: 0.012829472718253255",
            "extra": "mean: 3.886527843400006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.06546372099064,
            "unit": "iter/sec",
            "range": "stddev: 0.00012330799453106733",
            "extra": "mean: 9.340080033706945 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1640677354604,
            "unit": "iter/sec",
            "range": "stddev: 0.033661897542548086",
            "extra": "mean: 6.095043594000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.26012701852377285,
            "unit": "iter/sec",
            "range": "stddev: 0.008674969076485335",
            "extra": "mean: 3.8442757914000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.586294749314696,
            "unit": "iter/sec",
            "range": "stddev: 0.00010966557853159339",
            "extra": "mean: 19.016361673077036 msec\nrounds: 52"
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
          "id": "784a65eb03021c9620ec02f2643355a03361ec42",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/784a65eb03021c9620ec02f2643355a03361ec42"
        },
        "date": 1777379088872,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12840461472711073,
            "unit": "iter/sec",
            "range": "stddev: 0.04787473960745954",
            "extra": "mean: 7.787882095399993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2152087976556938,
            "unit": "iter/sec",
            "range": "stddev: 0.011724264452851952",
            "extra": "mean: 4.6466501876 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 115.63431178354132,
            "unit": "iter/sec",
            "range": "stddev: 0.00009870628897059829",
            "extra": "mean: 8.647952191490743 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12899582745573904,
            "unit": "iter/sec",
            "range": "stddev: 0.06209110981555023",
            "extra": "mean: 7.752188731400008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21581006214587417,
            "unit": "iter/sec",
            "range": "stddev: 0.05304354338779971",
            "extra": "mean: 4.6337042399999975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.6119116588264,
            "unit": "iter/sec",
            "range": "stddev: 0.00013578666293852744",
            "extra": "mean: 17.061378339285227 msec\nrounds: 56"
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
          "id": "9195198b1ffeaafd04d43c1d62af2e977bb61509",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/9195198b1ffeaafd04d43c1d62af2e977bb61509"
        },
        "date": 1777379486959,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12598747774950336,
            "unit": "iter/sec",
            "range": "stddev: 0.03928991314787392",
            "extra": "mean: 7.9372967684 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2132078235481362,
            "unit": "iter/sec",
            "range": "stddev: 0.024296332365021538",
            "extra": "mean: 4.690259406799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.40841639289779,
            "unit": "iter/sec",
            "range": "stddev: 0.00015675979108591243",
            "extra": "mean: 8.975982536843143 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12687274148139474,
            "unit": "iter/sec",
            "range": "stddev: 0.04096211877149712",
            "extra": "mean: 7.881913706000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2162991364473883,
            "unit": "iter/sec",
            "range": "stddev: 0.008799236517890207",
            "extra": "mean: 4.623226964399999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.05021347584814,
            "unit": "iter/sec",
            "range": "stddev: 0.00018636495201822178",
            "extra": "mean: 17.528418196425225 msec\nrounds: 56"
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
          "id": "6f1743187f309310eacb829bf38ffcec9c6f298e",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/6f1743187f309310eacb829bf38ffcec9c6f298e"
        },
        "date": 1777380271997,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.16480844464668673,
            "unit": "iter/sec",
            "range": "stddev: 0.06194353920009553",
            "extra": "mean: 6.067650247799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2590249521085717,
            "unit": "iter/sec",
            "range": "stddev: 0.016434233815736717",
            "extra": "mean: 3.8606319270000085 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.53026003820035,
            "unit": "iter/sec",
            "range": "stddev: 0.00011556539482895379",
            "extra": "mean: 9.129897068182206 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.16576121594354798,
            "unit": "iter/sec",
            "range": "stddev: 0.04215354675674436",
            "extra": "mean: 6.0327742789999945 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.26263911138577134,
            "unit": "iter/sec",
            "range": "stddev: 0.0102348503880544",
            "extra": "mean: 3.8075060288000033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.14763513937993,
            "unit": "iter/sec",
            "range": "stddev: 0.00018836829733713414",
            "extra": "mean: 18.468027226414 msec\nrounds: 53"
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
          "id": "099f99c7288270f20646c5aa01c28cc79b1450ef",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/099f99c7288270f20646c5aa01c28cc79b1450ef"
        },
        "date": 1777380463242,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12781473893197198,
            "unit": "iter/sec",
            "range": "stddev: 0.02532636649162055",
            "extra": "mean: 7.82382382780001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21240125444228453,
            "unit": "iter/sec",
            "range": "stddev: 0.007801128743325742",
            "extra": "mean: 4.7080701224 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.47865035916283,
            "unit": "iter/sec",
            "range": "stddev: 0.00008748895751504621",
            "extra": "mean: 8.81223029032311 msec\nrounds: 93"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12868213460193495,
            "unit": "iter/sec",
            "range": "stddev: 0.05241214103866672",
            "extra": "mean: 7.771086507799998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2126637956507277,
            "unit": "iter/sec",
            "range": "stddev: 0.020750986841090616",
            "extra": "mean: 4.702257838200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.51185277373794,
            "unit": "iter/sec",
            "range": "stddev: 0.00017239534237253025",
            "extra": "mean: 17.090554350875607 msec\nrounds: 57"
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
          "id": "8c66f142f18c085551f7a241585576b34033e5e1",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/8c66f142f18c085551f7a241585576b34033e5e1"
        },
        "date": 1777409369392,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12568380462374795,
            "unit": "iter/sec",
            "range": "stddev: 0.04204066498294485",
            "extra": "mean: 7.956474607000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21416653358668797,
            "unit": "iter/sec",
            "range": "stddev: 0.010328924315420544",
            "extra": "mean: 4.669263601800003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 114.31013306014749,
            "unit": "iter/sec",
            "range": "stddev: 0.00019546343066778263",
            "extra": "mean: 8.748130836955827 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12643117810265106,
            "unit": "iter/sec",
            "range": "stddev: 0.04589449461159544",
            "extra": "mean: 7.909441444800012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21489614738555457,
            "unit": "iter/sec",
            "range": "stddev: 0.0040153074718582305",
            "extra": "mean: 4.653410552799983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.275013002063126,
            "unit": "iter/sec",
            "range": "stddev: 0.00023976038484250652",
            "extra": "mean: 17.4596206545423 msec\nrounds: 55"
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
          "id": "b14ccc33d4c817d5a4cf147793eaf78db68b9648",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/b14ccc33d4c817d5a4cf147793eaf78db68b9648"
        },
        "date": 1777410485801,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.15635824001286372,
            "unit": "iter/sec",
            "range": "stddev: 0.06607626147687208",
            "extra": "mean: 6.395569558199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2495490644288214,
            "unit": "iter/sec",
            "range": "stddev: 0.015772847513628507",
            "extra": "mean: 4.007228006599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.87622155894599,
            "unit": "iter/sec",
            "range": "stddev: 0.00011817994042626901",
            "extra": "mean: 9.269883441862836 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1565530913934694,
            "unit": "iter/sec",
            "range": "stddev: 0.04034304432807227",
            "extra": "mean: 6.387609411599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2539242626908877,
            "unit": "iter/sec",
            "range": "stddev: 0.023325784829555378",
            "extra": "mean: 3.938182154799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.05467698340417,
            "unit": "iter/sec",
            "range": "stddev: 0.0002614951209615983",
            "extra": "mean: 19.210569692302872 msec\nrounds: 52"
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
          "id": "324b5351f32beeeec12d3a68d72ee562eb610392",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/324b5351f32beeeec12d3a68d72ee562eb610392"
        },
        "date": 1777411225940,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12731226286496614,
            "unit": "iter/sec",
            "range": "stddev: 0.0402091299060822",
            "extra": "mean: 7.8547028974 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20544657597305516,
            "unit": "iter/sec",
            "range": "stddev: 0.008763154512576043",
            "extra": "mean: 4.867445442999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 117.89380098607728,
            "unit": "iter/sec",
            "range": "stddev: 0.0001062577180026586",
            "extra": "mean: 8.482210189474639 msec\nrounds: 95"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12838202059677428,
            "unit": "iter/sec",
            "range": "stddev: 0.055393145759173174",
            "extra": "mean: 7.78925269560001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20990413596164068,
            "unit": "iter/sec",
            "range": "stddev: 0.01921176052555464",
            "extra": "mean: 4.7640795423999975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 59.78976960368539,
            "unit": "iter/sec",
            "range": "stddev: 0.00016633546329034477",
            "extra": "mean: 16.725269333340275 msec\nrounds: 57"
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
          "id": "da7ae653062ec8970746892c59e7ed48767967f7",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/da7ae653062ec8970746892c59e7ed48767967f7"
        },
        "date": 1777412731222,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12647347431162043,
            "unit": "iter/sec",
            "range": "stddev: 0.06782232513245383",
            "extra": "mean: 7.906796309999999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21092906489165558,
            "unit": "iter/sec",
            "range": "stddev: 0.021804296615340113",
            "extra": "mean: 4.7409303242000025 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.13994782491788,
            "unit": "iter/sec",
            "range": "stddev: 0.00022733711846382827",
            "extra": "mean: 9.079357851064476 msec\nrounds: 94"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12669105481127357,
            "unit": "iter/sec",
            "range": "stddev: 0.05181544883496126",
            "extra": "mean: 7.893217098000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21569762956724187,
            "unit": "iter/sec",
            "range": "stddev: 0.01674590066088738",
            "extra": "mean: 4.6361195624000064 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 58.10448289594179,
            "unit": "iter/sec",
            "range": "stddev: 0.00017759340541081248",
            "extra": "mean: 17.210376035716227 msec\nrounds: 56"
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
          "id": "760835d49a3ebddd4e499846a8e8ec2ae824176e",
          "message": "try to find the latest working version of the dependencies",
          "timestamp": "2026-04-25T10:31:47Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/476/commits/760835d49a3ebddd4e499846a8e8ec2ae824176e"
        },
        "date": 1777413493746,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12778467074075853,
            "unit": "iter/sec",
            "range": "stddev: 0.03712837081750888",
            "extra": "mean: 7.825664801600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20907047980660773,
            "unit": "iter/sec",
            "range": "stddev: 0.014177196225702486",
            "extra": "mean: 4.783076027399995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.07393839200829,
            "unit": "iter/sec",
            "range": "stddev: 0.00009261613671579194",
            "extra": "mean: 8.843770847824974 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1273995757160256,
            "unit": "iter/sec",
            "range": "stddev: 0.07377207253326316",
            "extra": "mean: 7.849319704400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.20815543636860703,
            "unit": "iter/sec",
            "range": "stddev: 0.013574066562860481",
            "extra": "mean: 4.804102248999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.27274148581591,
            "unit": "iter/sec",
            "range": "stddev: 0.0001391393845599055",
            "extra": "mean: 17.460313127278162 msec\nrounds: 55"
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
          "id": "cb911305da687b70ba37486117d7871f0456e0a0",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-06T18:47:12Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/cb911305da687b70ba37486117d7871f0456e0a0"
        },
        "date": 1784798335249,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.15125450835298282,
            "unit": "iter/sec",
            "range": "stddev: 0.07765878755268074",
            "extra": "mean: 6.6113731807999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2502473763507637,
            "unit": "iter/sec",
            "range": "stddev: 0.00677746022036503",
            "extra": "mean: 3.996045891 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 145.04516556797202,
            "unit": "iter/sec",
            "range": "stddev: 0.00015783391082394084",
            "extra": "mean: 6.894404209090123 msec\nrounds: 110"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.15150812483919948,
            "unit": "iter/sec",
            "range": "stddev: 0.06085581262423313",
            "extra": "mean: 6.600306096200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.25482381395729253,
            "unit": "iter/sec",
            "range": "stddev: 0.11399876606479518",
            "extra": "mean: 3.924280013200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 68.81890930472781,
            "unit": "iter/sec",
            "range": "stddev: 0.0007054726405840921",
            "extra": "mean: 14.530889985077119 msec\nrounds: 67"
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
            "email": "djgroennl@gmail.com",
            "name": "Derek Groen",
            "username": "djgroen"
          },
          "distinct": true,
          "id": "cd3d769eef362957baddc48ca748d9f0e51ed6e3",
          "message": "Remove dead pytest-pep8 dependency.",
          "timestamp": "2026-07-23T10:23:55+01:00",
          "tree_id": "585204e4c6462287adb59ec7e6e7d59a6b20fe74",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/cd3d769eef362957baddc48ca748d9f0e51ed6e3"
        },
        "date": 1784798918018,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.13008417213069243,
            "unit": "iter/sec",
            "range": "stddev: 0.07112851559397937",
            "extra": "mean: 7.687330315599996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21055943615931966,
            "unit": "iter/sec",
            "range": "stddev: 0.007522384309490707",
            "extra": "mean: 4.7492528391999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.4234157847514,
            "unit": "iter/sec",
            "range": "stddev: 0.00011039345478836861",
            "extra": "mean: 9.056050230770818 msec\nrounds: 91"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12993168144374828,
            "unit": "iter/sec",
            "range": "stddev: 0.045350444995318345",
            "extra": "mean: 7.696352336000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21676276306556705,
            "unit": "iter/sec",
            "range": "stddev: 0.018655916546533993",
            "extra": "mean: 4.61333849900002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.3922241685662,
            "unit": "iter/sec",
            "range": "stddev: 0.00015329328669174487",
            "extra": "mean: 17.73294128301848 msec\nrounds: 53"
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
          "id": "fe03baa20d7c6681bed2d98bf0ec3fdb2466af3b",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-23T09:24:17Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/fe03baa20d7c6681bed2d98bf0ec3fdb2466af3b"
        },
        "date": 1784799074065,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1963792896734087,
            "unit": "iter/sec",
            "range": "stddev: 0.056711117741273964",
            "extra": "mean: 5.092186664199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.28616781188657303,
            "unit": "iter/sec",
            "range": "stddev: 0.025543936417236547",
            "extra": "mean: 3.494453109200015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 154.62742185144313,
            "unit": "iter/sec",
            "range": "stddev: 0.00010465336286566497",
            "extra": "mean: 6.46715820535856 msec\nrounds: 112"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.19978767649390577,
            "unit": "iter/sec",
            "range": "stddev: 0.06240306979960454",
            "extra": "mean: 5.005313728800002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.29160144908160457,
            "unit": "iter/sec",
            "range": "stddev: 0.02287938805738357",
            "extra": "mean: 3.4293382394000047 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 82.20036997552792,
            "unit": "iter/sec",
            "range": "stddev: 0.00019876188378436006",
            "extra": "mean: 12.165395366197409 msec\nrounds: 71"
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
          "id": "b04dbac6ed03a5aa84923d6f0b631a832c429e1d",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-23T09:24:17Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/b04dbac6ed03a5aa84923d6f0b631a832c429e1d"
        },
        "date": 1784799751129,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.24434667021034506,
            "unit": "iter/sec",
            "range": "stddev: 0.09506331621096653",
            "extra": "mean: 4.092546049999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.38472125348245806,
            "unit": "iter/sec",
            "range": "stddev: 0.0169515961431226",
            "extra": "mean: 2.5992845233999957 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 188.72142124519343,
            "unit": "iter/sec",
            "range": "stddev: 0.00008777952564823135",
            "extra": "mean: 5.298815541987496 msec\nrounds: 131"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.2469923587463689,
            "unit": "iter/sec",
            "range": "stddev: 0.05517523329774798",
            "extra": "mean: 4.048708247799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.36997540942532214,
            "unit": "iter/sec",
            "range": "stddev: 0.1850609672869718",
            "extra": "mean: 2.702882339000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 97.18916282519604,
            "unit": "iter/sec",
            "range": "stddev: 0.00020092214692535795",
            "extra": "mean: 10.289213024692838 msec\nrounds: 81"
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
          "id": "cd9a67ad25101cecfd996dcaae179e69f8be2f30",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-23T09:40:49Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/cd9a67ad25101cecfd996dcaae179e69f8be2f30"
        },
        "date": 1784800479224,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.161569701998327,
            "unit": "iter/sec",
            "range": "stddev: 0.08607787507947488",
            "extra": "mean: 6.189279225199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.25635375046960257,
            "unit": "iter/sec",
            "range": "stddev: 0.016110136311252767",
            "extra": "mean: 3.9008596447999935 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.78924393807424,
            "unit": "iter/sec",
            "range": "stddev: 0.00023537855687228172",
            "extra": "mean: 9.728644376472444 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.16384012208453633,
            "unit": "iter/sec",
            "range": "stddev: 0.07262370077207365",
            "extra": "mean: 6.103511077000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.26112101815946387,
            "unit": "iter/sec",
            "range": "stddev: 0.025048519467260822",
            "extra": "mean: 3.829641930200006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 49.50424768178269,
            "unit": "iter/sec",
            "range": "stddev: 0.0021460152652409093",
            "extra": "mean: 20.20028677999676 msec\nrounds: 50"
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
          "id": "cbd30a6a3355c4242debe66ca0f557513a9ce7bc",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-23T09:40:49Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/cbd30a6a3355c4242debe66ca0f557513a9ce7bc"
        },
        "date": 1784807011504,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12714766822549597,
            "unit": "iter/sec",
            "range": "stddev: 0.0895624037972852",
            "extra": "mean: 7.864870932799988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20891252314369071,
            "unit": "iter/sec",
            "range": "stddev: 0.018318435448555666",
            "extra": "mean: 4.7866924632000005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.56007900319538,
            "unit": "iter/sec",
            "range": "stddev: 0.00014290468728789957",
            "extra": "mean: 9.656230563218715 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12804700490246204,
            "unit": "iter/sec",
            "range": "stddev: 0.0639135962612653",
            "extra": "mean: 7.809632101599999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21384555116095982,
            "unit": "iter/sec",
            "range": "stddev: 0.008266901212049774",
            "extra": "mean: 4.676272172000006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.402336972776794,
            "unit": "iter/sec",
            "range": "stddev: 0.00015049715927617212",
            "extra": "mean: 18.049780111105655 msec\nrounds: 54"
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
          "id": "ff7ebd061821ed79c64b09baa99a9baef8aec0f0",
          "message": "Security/pip/various",
          "timestamp": "2026-07-23T09:40:49Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/486/commits/ff7ebd061821ed79c64b09baa99a9baef8aec0f0"
        },
        "date": 1784821179523,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1622897188511863,
            "unit": "iter/sec",
            "range": "stddev: 0.062342746888157656",
            "extra": "mean: 6.1618197818 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2568063054782548,
            "unit": "iter/sec",
            "range": "stddev: 0.003989826590422283",
            "extra": "mean: 3.893985383799992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.4656710535949,
            "unit": "iter/sec",
            "range": "stddev: 0.0002714980797091205",
            "extra": "mean: 9.572522627906748 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1624193685347754,
            "unit": "iter/sec",
            "range": "stddev: 0.07984698334104356",
            "extra": "mean: 6.156901168999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2602603053928876,
            "unit": "iter/sec",
            "range": "stddev: 0.003702641940353311",
            "extra": "mean: 3.8423070260000087 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.53754486817725,
            "unit": "iter/sec",
            "range": "stddev: 0.000174575337599912",
            "extra": "mean: 19.03400706121908 msec\nrounds: 49"
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
          "id": "2fc7fe16d9e952c9da5bf62c9b740855fbd562a2",
          "message": "Merge pull request #486 from UCL-CCS/security/pip/various\n\nSecurity/pip/various",
          "timestamp": "2026-07-23T18:03:06+02:00",
          "tree_id": "8f1e33d9d2ca5a9e9587042ab8ce44dae54230e0",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/2fc7fe16d9e952c9da5bf62c9b740855fbd562a2"
        },
        "date": 1784822859427,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12716695586123747,
            "unit": "iter/sec",
            "range": "stddev: 0.08990589093486803",
            "extra": "mean: 7.863678054000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20775101494254944,
            "unit": "iter/sec",
            "range": "stddev: 0.025224512249341902",
            "extra": "mean: 4.813454222000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.80797086469099,
            "unit": "iter/sec",
            "range": "stddev: 0.00010208523587208802",
            "extra": "mean: 9.726872260869088 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12753762088601012,
            "unit": "iter/sec",
            "range": "stddev: 0.06536599316078949",
            "extra": "mean: 7.840823696199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21337228943711217,
            "unit": "iter/sec",
            "range": "stddev: 0.02234780042939563",
            "extra": "mean: 4.686644187200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.32988636652822,
            "unit": "iter/sec",
            "range": "stddev: 0.00010878376772929221",
            "extra": "mean: 19.481827659998316 msec\nrounds: 50"
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
          "id": "fb27f2eb45e3f765c37f16b20d0a16161059b1e2",
          "message": "Merge pull request #487 from UCL-CCS/dependabot/pip/setuptools-83.0.0\n\nBump setuptools from 80.10.2 to 83.0.0",
          "timestamp": "2026-07-28T15:33:26+01:00",
          "tree_id": "3c13ba76610974263da45b8fa092c1ecd2b353a9",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/fb27f2eb45e3f765c37f16b20d0a16161059b1e2"
        },
        "date": 1785249442386,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1705385115480351,
            "unit": "iter/sec",
            "range": "stddev: 0.07021277925501178",
            "extra": "mean: 5.863778163200005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.24986733879585502,
            "unit": "iter/sec",
            "range": "stddev: 0.015451724235623033",
            "extra": "mean: 4.002123706200007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 128.831416649436,
            "unit": "iter/sec",
            "range": "stddev: 0.00015274027573532553",
            "extra": "mean: 7.762081843135409 msec\nrounds: 102"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.16946382568825039,
            "unit": "iter/sec",
            "range": "stddev: 0.09317546164755698",
            "extra": "mean: 5.9009643854000045 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.25524727448394785,
            "unit": "iter/sec",
            "range": "stddev: 0.02825487117155443",
            "extra": "mean: 3.9177695512000015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 63.969078585541524,
            "unit": "iter/sec",
            "range": "stddev: 0.00021943200243544045",
            "extra": "mean: 15.632552822576109 msec\nrounds: 62"
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
          "id": "cfd633d7058bda0b6e1d47a7af102b117f4eca28",
          "message": "Bump starlette from 1.0.0 to 1.3.1",
          "timestamp": "2026-07-23T16:05:02Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/485/commits/cfd633d7058bda0b6e1d47a7af102b117f4eca28"
        },
        "date": 1785249537875,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12871052789787532,
            "unit": "iter/sec",
            "range": "stddev: 0.07613624648048335",
            "extra": "mean: 7.7693722210000145 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.21298067050208447,
            "unit": "iter/sec",
            "range": "stddev: 0.011134072468532558",
            "extra": "mean: 4.6952617702 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 111.78410284715432,
            "unit": "iter/sec",
            "range": "stddev: 0.00011552180393139013",
            "extra": "mean: 8.94581585869441 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12885367962356603,
            "unit": "iter/sec",
            "range": "stddev: 0.06981778329326438",
            "extra": "mean: 7.760740732600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21465586301355538,
            "unit": "iter/sec",
            "range": "stddev: 0.010775370097890471",
            "extra": "mean: 4.658619550199989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.87642462841475,
            "unit": "iter/sec",
            "range": "stddev: 0.00013168437817162555",
            "extra": "mean: 17.581977181814842 msec\nrounds: 55"
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
          "id": "ab42c2c6206d00bfe8cbc3b60c6fd071a9aceb3f",
          "message": "Merge pull request #485 from UCL-CCS/dependabot/pip/starlette-1.3.1\n\nBump starlette from 1.0.0 to 1.3.1",
          "timestamp": "2026-07-29T04:12:46+01:00",
          "tree_id": "3c13ba76610974263da45b8fa092c1ecd2b353a9",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/ab42c2c6206d00bfe8cbc3b60c6fd071a9aceb3f"
        },
        "date": 1785295036955,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1275991463955499,
            "unit": "iter/sec",
            "range": "stddev: 0.04843948260924374",
            "extra": "mean: 7.837043023000001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20816461227220606,
            "unit": "iter/sec",
            "range": "stddev: 0.01847121028080625",
            "extra": "mean: 4.803890483999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 109.08551801851951,
            "unit": "iter/sec",
            "range": "stddev: 0.00019108014797238447",
            "extra": "mean: 9.16711968888693 msec\nrounds: 90"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12768020538013525,
            "unit": "iter/sec",
            "range": "stddev: 0.07404311586791361",
            "extra": "mean: 7.832067602200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21126082253379827,
            "unit": "iter/sec",
            "range": "stddev: 0.03265841133581351",
            "extra": "mean: 4.733485309800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 56.31942859480939,
            "unit": "iter/sec",
            "range": "stddev: 0.00013286326562424132",
            "extra": "mean: 17.755861963630856 msec\nrounds: 55"
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
          "id": "01d5acdde69f3b2852953f66f3862673d57ccdd9",
          "message": "Bump bleach from 6.3.0 to 6.4.0",
          "timestamp": "2026-07-29T03:12:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/488/commits/01d5acdde69f3b2852953f66f3862673d57ccdd9"
        },
        "date": 1785297396203,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.16393238793719553,
            "unit": "iter/sec",
            "range": "stddev: 0.045803912901542315",
            "extra": "mean: 6.1000758457999895 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2626758001449189,
            "unit": "iter/sec",
            "range": "stddev: 0.004623038819150842",
            "extra": "mean: 3.8069742223999983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.43497834575415,
            "unit": "iter/sec",
            "range": "stddev: 0.0001602899283369723",
            "extra": "mean: 9.395407558138443 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.16296703217974137,
            "unit": "iter/sec",
            "range": "stddev: 0.058981237458625865",
            "extra": "mean: 6.136210413999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.262358059971798,
            "unit": "iter/sec",
            "range": "stddev: 0.00989365167628723",
            "extra": "mean: 3.8115848245999926 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.59658466442814,
            "unit": "iter/sec",
            "range": "stddev: 0.0002651130683949739",
            "extra": "mean: 18.65790527999252 msec\nrounds: 50"
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
          "id": "c38c3960e2b2e746b56bd877e53afdd7dabf59be",
          "message": "Bump pillow from 12.2.0 to 12.3.0",
          "timestamp": "2026-07-29T03:12:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/478/commits/c38c3960e2b2e746b56bd877e53afdd7dabf59be"
        },
        "date": 1785299409019,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1279014385964277,
            "unit": "iter/sec",
            "range": "stddev: 0.06682390211732102",
            "extra": "mean: 7.818520346399998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20966267765747867,
            "unit": "iter/sec",
            "range": "stddev: 0.024259433603101333",
            "extra": "mean: 4.769566100999998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 110.27906409647656,
            "unit": "iter/sec",
            "range": "stddev: 0.00017124462900389788",
            "extra": "mean: 9.067904304348827 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12796965826544132,
            "unit": "iter/sec",
            "range": "stddev: 0.058772322493240166",
            "extra": "mean: 7.814352351600002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2148210627886772,
            "unit": "iter/sec",
            "range": "stddev: 0.013033472555032807",
            "extra": "mean: 4.6550370201999955 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.51153119911643,
            "unit": "iter/sec",
            "range": "stddev: 0.00031799089959244766",
            "extra": "mean: 18.014275203706088 msec\nrounds: 54"
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
          "id": "6abc32bd555ce982a5ea47dd2a89c762d41a4dad",
          "message": "update action versions to get rid of messages about 'Node.js 20 is de…",
          "timestamp": "2026-07-29T03:12:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/490/commits/6abc32bd555ce982a5ea47dd2a89c762d41a4dad"
        },
        "date": 1785311383453,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12898776715782004,
            "unit": "iter/sec",
            "range": "stddev: 0.06020211565953819",
            "extra": "mean: 7.7526731568 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2067866777193207,
            "unit": "iter/sec",
            "range": "stddev: 0.025646913363567458",
            "extra": "mean: 4.835901476000004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 113.25488422735356,
            "unit": "iter/sec",
            "range": "stddev: 0.00013230353076028182",
            "extra": "mean: 8.829641271740208 msec\nrounds: 92"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12924370497168985,
            "unit": "iter/sec",
            "range": "stddev: 0.0684827923038554",
            "extra": "mean: 7.737320747800015 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2113772697332733,
            "unit": "iter/sec",
            "range": "stddev: 0.016854400128301996",
            "extra": "mean: 4.730877644799989 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 57.33088272233192,
            "unit": "iter/sec",
            "range": "stddev: 0.0003087257967045937",
            "extra": "mean: 17.442606018177933 msec\nrounds: 55"
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
          "id": "a5b60debbea37b7062f80682b7397d0b6510daa2",
          "message": "update action versions to get rid of messages about 'Node.js 20 is de…",
          "timestamp": "2026-07-29T03:12:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/490/commits/a5b60debbea37b7062f80682b7397d0b6510daa2"
        },
        "date": 1785312930870,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1591444156960828,
            "unit": "iter/sec",
            "range": "stddev: 0.06922678697205817",
            "extra": "mean: 6.2836009396000065 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.2543810144564664,
            "unit": "iter/sec",
            "range": "stddev: 0.011596072402868786",
            "extra": "mean: 3.931110983799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.30933972881661,
            "unit": "iter/sec",
            "range": "stddev: 0.00024702633135889477",
            "extra": "mean: 9.586869235293788 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.15840599587548257,
            "unit": "iter/sec",
            "range": "stddev: 0.04797065224005487",
            "extra": "mean: 6.312892352799986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2561013648710446,
            "unit": "iter/sec",
            "range": "stddev: 0.015110027795810211",
            "extra": "mean: 3.9047039069999983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.74802268750288,
            "unit": "iter/sec",
            "range": "stddev: 0.0003871667578297591",
            "extra": "mean: 19.324409862746304 msec\nrounds: 51"
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
          "id": "c8420e7304c61132c04d540a586acd0b468aca3f",
          "message": "Merge pull request #490 from UCL-CCS/fix/action-versions\n\nupdate action versions to get rid of messages about 'Node.js 20 is de…",
          "timestamp": "2026-07-29T09:30:03+01:00",
          "tree_id": "24098526889db8e9426b393dc00712065dff5f21",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/c8420e7304c61132c04d540a586acd0b468aca3f"
        },
        "date": 1785314086430,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12574157903456493,
            "unit": "iter/sec",
            "range": "stddev: 0.06381647460923348",
            "extra": "mean: 7.952818850199992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20810811536646975,
            "unit": "iter/sec",
            "range": "stddev: 0.035143857907549265",
            "extra": "mean: 4.805194637599987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.04271519952525,
            "unit": "iter/sec",
            "range": "stddev: 0.00023553047836091074",
            "extra": "mean: 9.704713215909194 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12679071819108184,
            "unit": "iter/sec",
            "range": "stddev: 0.09092085249483467",
            "extra": "mean: 7.8870126635999895 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.21262146502923268,
            "unit": "iter/sec",
            "range": "stddev: 0.017363466411574466",
            "extra": "mean: 4.703194006600006 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.70344699157751,
            "unit": "iter/sec",
            "range": "stddev: 0.0003344166759414769",
            "extra": "mean: 17.952210392854187 msec\nrounds: 56"
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
          "id": "cb05abb7c04fda195d3ccaf6ee9b1420cb7b11b6",
          "message": "Bump bleach from 6.3.0 to 6.4.0",
          "timestamp": "2026-07-29T03:12:51Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/488/commits/cb05abb7c04fda195d3ccaf6ee9b1420cb7b11b6"
        },
        "date": 1785314106651,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12729209963333635,
            "unit": "iter/sec",
            "range": "stddev: 0.04427989947633213",
            "extra": "mean: 7.855947092400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.20722072888136567,
            "unit": "iter/sec",
            "range": "stddev: 0.01130940485925492",
            "extra": "mean: 4.825772042199998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 105.18692136676133,
            "unit": "iter/sec",
            "range": "stddev: 0.00022214640349908947",
            "extra": "mean: 9.506885333331908 msec\nrounds: 84"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.12729622977565977,
            "unit": "iter/sec",
            "range": "stddev: 0.06378823326432594",
            "extra": "mean: 7.855692205200012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.2131314841092645,
            "unit": "iter/sec",
            "range": "stddev: 0.047735319764903285",
            "extra": "mean: 4.691939364000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 55.3736856630386,
            "unit": "iter/sec",
            "range": "stddev: 0.00017680894816896956",
            "extra": "mean: 18.059119381816593 msec\nrounds: 55"
          }
        ]
      }
    ]
  }
}