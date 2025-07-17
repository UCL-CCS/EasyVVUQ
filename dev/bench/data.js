window.BENCHMARK_DATA = {
  "lastUpdate": 1752748214379,
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
      }
    ]
  }
}