window.BENCHMARK_DATA = {
  "lastUpdate": 1721211657027,
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
      }
    ]
  }
}