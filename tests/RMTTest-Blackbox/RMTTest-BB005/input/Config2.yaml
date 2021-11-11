class Config:

    #    basedir = "tests/BlackboxTest/Bb005Test/"
    #    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "${ENV:basedir}/input/reqs",
           "commit_interval": ["FILES", "FILES"],
           "default_language": "en_GB",
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

    output_specs = \
        [
          ["prios",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqsprios.tex",
            {"start_date": "2011-05-11"}]],

          ["graph",
           ["ts_common", "${ENV:rmtoo_test_dir}/req-graph1.dot"]],

          ["graph2",
           ["ts_common", "${ENV:rmtoo_test_dir}/req-graph2.dot"]],

          ["stats_reqs_cnt",
           ["ts_common", "${ENV:rmtoo_test_dir}/stats_reqs_cnt.csv"]],

          ["latex2",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqtopics.tex"]],

          ["html",
           ["ts_common",
            "${ENV:rmtoo_test_dir}/html", "${ENV:basedir}/input/header.html",
            "${ENV:basedir}/input/footer.html"]],

          ["oopricing1",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqspricing"]],

        ]
