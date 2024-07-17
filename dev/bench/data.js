window.BENCHMARK_DATA = {
  "lastUpdate": 1721212802929,
  "repoUrl": "https://github.com/UCL-CCS/EasyVVUQ",
  "entries": {
    "Benchmark": [
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
          "id": "e74eed20eb0951b92f9a7bb7d943233f94d30557",
          "message": "Merge pull request #422 from UCL-CCS/dpc/further-doc-fixes\n\nadd some more libraries to autodoc_mock_imports",
          "timestamp": "2024-07-01T11:06:55+01:00",
          "tree_id": "5ddc38c2bbe3ed8923132328f54620f14af3890e",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/commit/e74eed20eb0951b92f9a7bb7d943233f94d30557"
        },
        "date": 1719828676317,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11721470975752726,
            "unit": "iter/sec",
            "range": "stddev: 0.0802701950422126",
            "extra": "mean: 8.531352439199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19750978195853766,
            "unit": "iter/sec",
            "range": "stddev: 0.03421538676473527",
            "extra": "mean: 5.063040372400013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 104.13997414161894,
            "unit": "iter/sec",
            "range": "stddev: 0.0006153536133071009",
            "extra": "mean: 9.602460613636314 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11795994359658793,
            "unit": "iter/sec",
            "range": "stddev: 0.13094116761331726",
            "extra": "mean: 8.477454036599976 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19714473334900687,
            "unit": "iter/sec",
            "range": "stddev: 0.03860307413505523",
            "extra": "mean: 5.072415493999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.56530070045482,
            "unit": "iter/sec",
            "range": "stddev: 0.0002925020542568863",
            "extra": "mean: 19.023956615382733 msec\nrounds: 52"
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
          "id": "1f6592088514aed2faeedb17d3e43237479ad076",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/1f6592088514aed2faeedb17d3e43237479ad076"
        },
        "date": 1721211051024,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11790730721665138,
            "unit": "iter/sec",
            "range": "stddev: 0.09592585995246657",
            "extra": "mean: 8.481238555999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19288345684496896,
            "unit": "iter/sec",
            "range": "stddev: 0.04424728767678711",
            "extra": "mean: 5.184477800000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 101.68458511037065,
            "unit": "iter/sec",
            "range": "stddev: 0.00016241760862616657",
            "extra": "mean: 9.834332302330568 msec\nrounds: 86"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11768461980827623,
            "unit": "iter/sec",
            "range": "stddev: 0.06509037598798263",
            "extra": "mean: 8.497287084999993 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1924789827302092,
            "unit": "iter/sec",
            "range": "stddev: 0.05401697444192741",
            "extra": "mean: 5.195372428799999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.646794185352306,
            "unit": "iter/sec",
            "range": "stddev: 0.0016684231240068057",
            "extra": "mean: 19.362286000001387 msec\nrounds: 51"
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
          "id": "2fd0f9727c7bce1503249612dc66fa0b44883133",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/2fd0f9727c7bce1503249612dc66fa0b44883133"
        },
        "date": 1721211371183,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11957286477784768,
            "unit": "iter/sec",
            "range": "stddev: 0.06513111938680144",
            "extra": "mean: 8.363101459999996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19289570194409486,
            "unit": "iter/sec",
            "range": "stddev: 0.04743675471495086",
            "extra": "mean: 5.184148687199991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.46406970487044,
            "unit": "iter/sec",
            "range": "stddev: 0.0003688596152920399",
            "extra": "mean: 9.392840258428077 msec\nrounds: 89"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11895072548826978,
            "unit": "iter/sec",
            "range": "stddev: 0.09567184755443921",
            "extra": "mean: 8.406842378599986 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1933017139266108,
            "unit": "iter/sec",
            "range": "stddev: 0.03251522581869606",
            "extra": "mean: 5.173259872799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.56696308699838,
            "unit": "iter/sec",
            "range": "stddev: 0.0005862020789539095",
            "extra": "mean: 18.32610692307832 msec\nrounds: 52"
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
          "id": "f06e892d2521b88c319e9ba433e96559957159c3",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/f06e892d2521b88c319e9ba433e96559957159c3"
        },
        "date": 1721211379411,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11613084930696536,
            "unit": "iter/sec",
            "range": "stddev: 0.06731722606790018",
            "extra": "mean: 8.610976376800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1906983136780236,
            "unit": "iter/sec",
            "range": "stddev: 0.03195195327503559",
            "extra": "mean: 5.24388486040001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 97.93986286863446,
            "unit": "iter/sec",
            "range": "stddev: 0.00017154998576231607",
            "extra": "mean: 10.21034715293902 msec\nrounds: 85"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11713496580699774,
            "unit": "iter/sec",
            "range": "stddev: 0.09880082167999886",
            "extra": "mean: 8.537160472200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1918044589692116,
            "unit": "iter/sec",
            "range": "stddev: 0.06752270465371886",
            "extra": "mean: 5.213643130999992 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.096771785357234,
            "unit": "iter/sec",
            "range": "stddev: 0.0006281153087673615",
            "extra": "mean: 19.195047326926094 msec\nrounds: 52"
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
          "id": "38c25e22c8c7640e7d861f514953302120f59560",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/38c25e22c8c7640e7d861f514953302120f59560"
        },
        "date": 1721211397341,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11611363749159956,
            "unit": "iter/sec",
            "range": "stddev: 0.09443413873605914",
            "extra": "mean: 8.612252803400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18923866053572583,
            "unit": "iter/sec",
            "range": "stddev: 0.05435798241403744",
            "extra": "mean: 5.284332478199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.80977999594766,
            "unit": "iter/sec",
            "range": "stddev: 0.000151978042909574",
            "extra": "mean: 10.019058253014892 msec\nrounds: 83"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11653441498826496,
            "unit": "iter/sec",
            "range": "stddev: 0.10240594723698632",
            "extra": "mean: 8.581156048200011 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1894398077944318,
            "unit": "iter/sec",
            "range": "stddev: 0.0311966299749448",
            "extra": "mean: 5.278721571999995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 51.4852876332051,
            "unit": "iter/sec",
            "range": "stddev: 0.00013921660487732057",
            "extra": "mean: 19.423024439996652 msec\nrounds: 50"
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
          "id": "45bae67e66582b99e9f27f13a10b5a88ed67213c",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/45bae67e66582b99e9f27f13a10b5a88ed67213c"
        },
        "date": 1721211610895,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11981023512485688,
            "unit": "iter/sec",
            "range": "stddev: 0.07162315633510444",
            "extra": "mean: 8.346532322200002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1968857484746409,
            "unit": "iter/sec",
            "range": "stddev: 0.04328348273869678",
            "extra": "mean: 5.079087784400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.25948612278657,
            "unit": "iter/sec",
            "range": "stddev: 0.000511596745356796",
            "extra": "mean: 9.684340272727031 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11905909582569922,
            "unit": "iter/sec",
            "range": "stddev: 0.06954582448900803",
            "extra": "mean: 8.399190276599995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19584485928214343,
            "unit": "iter/sec",
            "range": "stddev: 0.0500672012856334",
            "extra": "mean: 5.106082455599983 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 53.825600325031466,
            "unit": "iter/sec",
            "range": "stddev: 0.0006852920758710721",
            "extra": "mean: 18.57852014583017 msec\nrounds: 48"
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
          "id": "c344fd2b1bd1d5ce452f0d91185bfcc451e0facd",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/c344fd2b1bd1d5ce452f0d91185bfcc451e0facd"
        },
        "date": 1721211614240,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11713547580941644,
            "unit": "iter/sec",
            "range": "stddev: 0.08473276974466173",
            "extra": "mean: 8.537123301800005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.18925576331667743,
            "unit": "iter/sec",
            "range": "stddev: 0.03755080470766264",
            "extra": "mean: 5.283854940400005 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.23848139791232,
            "unit": "iter/sec",
            "range": "stddev: 0.00017513243212574587",
            "extra": "mean: 9.41278514942751 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11914876700046118,
            "unit": "iter/sec",
            "range": "stddev: 0.058150603123405246",
            "extra": "mean: 8.392869059199995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19016128441064442,
            "unit": "iter/sec",
            "range": "stddev: 0.021750821957757",
            "extra": "mean: 5.258693971799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.25263724245172,
            "unit": "iter/sec",
            "range": "stddev: 0.0002215190896459405",
            "extra": "mean: 18.43228367924422 msec\nrounds: 53"
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
          "id": "6d92d361da289a48ce8b32efd9b009e08a5d8248",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/6d92d361da289a48ce8b32efd9b009e08a5d8248"
        },
        "date": 1721211655517,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.1175001464523588,
            "unit": "iter/sec",
            "range": "stddev: 0.07967619759914864",
            "extra": "mean: 8.5106276902 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19389892866853764,
            "unit": "iter/sec",
            "range": "stddev: 0.050502215029887124",
            "extra": "mean: 5.157326071200009 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 99.64719981816627,
            "unit": "iter/sec",
            "range": "stddev: 0.00020209093698303756",
            "extra": "mean: 10.035404926829605 msec\nrounds: 82"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.1180776885481829,
            "unit": "iter/sec",
            "range": "stddev: 0.0712148221825116",
            "extra": "mean: 8.469000471600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1949804862987262,
            "unit": "iter/sec",
            "range": "stddev: 0.01188266452355935",
            "extra": "mean: 5.128718360400012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.26149147005837,
            "unit": "iter/sec",
            "range": "stddev: 0.00019458878029699733",
            "extra": "mean: 19.13454767307817 msec\nrounds: 52"
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
          "id": "f91fc4e2fea97a9fba5e2e33aae14944ab261516",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/f91fc4e2fea97a9fba5e2e33aae14944ab261516"
        },
        "date": 1721211798990,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11882375989351276,
            "unit": "iter/sec",
            "range": "stddev: 0.0717809096944665",
            "extra": "mean: 8.415825260000002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.1986542727214689,
            "unit": "iter/sec",
            "range": "stddev: 0.01229087855597408",
            "extra": "mean: 5.033871088199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 107.62903830083147,
            "unit": "iter/sec",
            "range": "stddev: 0.00009175935310050791",
            "extra": "mean: 9.291172863636698 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11901467529527014,
            "unit": "iter/sec",
            "range": "stddev: 0.07898778543734715",
            "extra": "mean: 8.402325154600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1972370453391868,
            "unit": "iter/sec",
            "range": "stddev: 0.0418494065725752",
            "extra": "mean: 5.070041473599997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.29473941806246,
            "unit": "iter/sec",
            "range": "stddev: 0.0001461989743926632",
            "extra": "mean: 18.41799059573948 msec\nrounds: 47"
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
          "id": "e3648cd8bd047e155de1f4ee780fac4535a210eb",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/e3648cd8bd047e155de1f4ee780fac4535a210eb"
        },
        "date": 1721212551440,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.12001071151957352,
            "unit": "iter/sec",
            "range": "stddev: 0.06707751283810542",
            "extra": "mean: 8.332589544199994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19819588346526124,
            "unit": "iter/sec",
            "range": "stddev: 0.026752915904118723",
            "extra": "mean: 5.0455134714 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.72616137807725,
            "unit": "iter/sec",
            "range": "stddev: 0.00044974265396217856",
            "extra": "mean: 9.640769374999277 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11932605953777863,
            "unit": "iter/sec",
            "range": "stddev: 0.0708444967155043",
            "extra": "mean: 8.380399083600008 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19968543974412664,
            "unit": "iter/sec",
            "range": "stddev: 0.03622156837585416",
            "extra": "mean: 5.007876394400023 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.355031863064305,
            "unit": "iter/sec",
            "range": "stddev: 0.000190007747087048",
            "extra": "mean: 18.397560735853908 msec\nrounds: 53"
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
          "id": "4abbf6c5fd5433cb136c7e211833c5bd01779695",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/4abbf6c5fd5433cb136c7e211833c5bd01779695"
        },
        "date": 1721212581719,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11887506759617945,
            "unit": "iter/sec",
            "range": "stddev: 0.07302319566360456",
            "extra": "mean: 8.41219290319999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19674885360816669,
            "unit": "iter/sec",
            "range": "stddev: 0.01653167346047049",
            "extra": "mean: 5.082621736600004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 103.42466085145854,
            "unit": "iter/sec",
            "range": "stddev: 0.0003981416137319461",
            "extra": "mean: 9.668873862068821 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11941210995920769,
            "unit": "iter/sec",
            "range": "stddev: 0.10193120504005217",
            "extra": "mean: 8.374360023800012 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19554588100704756,
            "unit": "iter/sec",
            "range": "stddev: 0.04639988429048122",
            "extra": "mean: 5.113889358599988 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.481069144518685,
            "unit": "iter/sec",
            "range": "stddev: 0.00012617656884731241",
            "extra": "mean: 19.054489862740223 msec\nrounds: 51"
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
          "id": "bc4ae8e4c3409a1dc39daf6f574ce03e12be0c1a",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/bc4ae8e4c3409a1dc39daf6f574ce03e12be0c1a"
        },
        "date": 1721212607533,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11802021863587998,
            "unit": "iter/sec",
            "range": "stddev: 0.08467470515067352",
            "extra": "mean: 8.473124449 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19859135788889276,
            "unit": "iter/sec",
            "range": "stddev: 0.053487688786398514",
            "extra": "mean: 5.0354658461999975 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 106.66579751616285,
            "unit": "iter/sec",
            "range": "stddev: 0.0005078787755441659",
            "extra": "mean: 9.375076390803454 msec\nrounds: 87"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11828617233305962,
            "unit": "iter/sec",
            "range": "stddev: 0.08918594508294508",
            "extra": "mean: 8.454073542799994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.1999110847791643,
            "unit": "iter/sec",
            "range": "stddev: 0.014378935457203583",
            "extra": "mean: 5.002223869199997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 54.992653406928845,
            "unit": "iter/sec",
            "range": "stddev: 0.00015153573513387384",
            "extra": "mean: 18.184247132072446 msec\nrounds: 53"
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
          "id": "39ef8e55a3531fc334acf16935b4c5ffeca1268f",
          "message": "Djgroen actions update: updating to V3 to avoid obsoletion. #424",
          "timestamp": "2024-07-01T10:07:00Z",
          "url": "https://github.com/UCL-CCS/EasyVVUQ/pull/425/commits/39ef8e55a3531fc334acf16935b4c5ffeca1268f"
        },
        "date": 1721212799467,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_db_benchmark.py::test_draw",
            "value": 0.11774977181372365,
            "unit": "iter/sec",
            "range": "stddev: 0.07527284486922145",
            "extra": "mean: 8.492585459800022 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results",
            "value": 0.19398413442887238,
            "unit": "iter/sec",
            "range": "stddev: 0.04988306215020268",
            "extra": "mean: 5.155060762799996 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result",
            "value": 102.4430978037393,
            "unit": "iter/sec",
            "range": "stddev: 0.00036633824846797527",
            "extra": "mean: 9.761516602278096 msec\nrounds: 88"
          },
          {
            "name": "tests/test_db_benchmark.py::test_draw_add",
            "value": 0.11920779223435488,
            "unit": "iter/sec",
            "range": "stddev: 0.08795146963405884",
            "extra": "mean: 8.388713365599994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_store_results_add",
            "value": 0.19488990432474476,
            "unit": "iter/sec",
            "range": "stddev: 0.013360544317383649",
            "extra": "mean: 5.131102113600003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_db_benchmark.py::test_get_collation_result_add",
            "value": 52.9393688127203,
            "unit": "iter/sec",
            "range": "stddev: 0.00013592392479327747",
            "extra": "mean: 18.889533865385253 msec\nrounds: 52"
          }
        ]
      }
    ]
  }
}