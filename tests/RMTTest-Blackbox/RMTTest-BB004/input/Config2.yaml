class Config:

    #    basedir = "tests/BlackboxTest/Bb004Test/"
    #    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["executive", ]

    inventors = ["VincentAndJules", "Wulf"]

    reqs_spec = \
        {
           "directory": "${ENV:basedir}/input/reqs",
           "commit_interval": ["FILES", "FILES"],
           "default_language": "de_DE",
        }

    topic_specs = \
        {
          "ts_common": ["${ENV:basedir}/input/topics", "PulpFiction"],
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
            {"start_date": "2011-05-10"}]],

          ["graph",
           ["ts_common", "${ENV:rmtoo_test_dir}/req-graph1.dot"]],

          ["graph2",
           ["ts_common", "${ENV:rmtoo_test_dir}/req-graph2.dot"]],

          ["latex2",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqtopics.tex"]],

          ["html",
           ["ts_common",
            "${ENV:rmtoo_test_dir}/html", "${ENV:basedir}/input/header.html",
            "${ENV:basedir}/input/footer.html"]],

          ["xml_ganttproject_2",
           ["ts_common", "${ENV:rmtoo_test_dir}/gantt2.xml", 1]],

          ["tlp1",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqsgraph.tlp"]],
        ]
