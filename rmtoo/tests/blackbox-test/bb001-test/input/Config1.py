import os

class Config:

    #basedir = "tests/blackbox-test/bb001-test/"
    #result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "${GET:basedir}/input/reqs",
           "commit_interval": ["v10",
                               "c35f8e918ab1d05ab3e2ba0be52a3f4092035663"],
           #["138be32f1985aec694934263f02e47292deaac91", "FILES"]
           #["v8", "FILES"]
           # ["FILES", "FILES"]
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": ["${GET:basedir}/input/topics", "ReqsDocument"],
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
            {"start_date": "2011-04-26"} ]],

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
            "${ENV:rmtoo_test_dir}/html", "${GET:basedir}/input/header.html",
            "${GET:basedir}/input/footer.html"]],

          ["xml_ganttproject_2",
           ["ts_common", "${ENV:rmtoo_test_dir}/gantt2.xml", 1]],

          ["oopricing1",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqspricing"]],
        ]
