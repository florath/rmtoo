class Config:

    #    basedir = "tests/BlackboxTest/Bb018Test/"
    #    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "${ENV:basedir}/input/reqs",
           "commit_interval": ["FILES", "FILES"],
           "default_language": "en_GB",
           "dependency_notation": set(["Solved by", ]),
        }

    topic_specs = \
        {
          "ts_common": ["${ENV:basedir}/input/topics", "ReqsDocument"],
        }

    analytics_specs = \
        {
           "stop_on_errors": False,
           "topics": "ts_common",
        }

    constraints_specs = \
        {
           "search_dirs": ["../rmtoo/collection/constraints"]
        }

    output_specs = \
        [
            #          ["prios",
            #           ["ts_common", result_is + "/reqsprios.tex"]],

            #          ["graph",
            #           ["ts_common", result_is + "/req-graph1.dot"]],

            #          ["graph2",
            #           ["ts_common", result_is + "/req-graph2.dot"]],

            #          ["stats_reqs_cnt",
            #           ["ts_common", result_is + "/stats_reqs_cnt.csv"]],

            ["latex2",
             ["ts_common", "${ENV:rmtoo_test_dir}/reqtopics.tex"]],

            #          ["html",
            #           ["ts_common",
            #            result_is + "/html", basedir + "input/header.html",
            #            basedir + "input/footer.html"]],
        ]
