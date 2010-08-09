

class Config:

    basedir = "tests/blackbox-test/bb002-test/"

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": basedir + "input/reqs",
           "commit_interval": ["a92e470b9bdc87673530bbe9cc8a57afe6d832e2", 
                               "a92e470b9bdc87673530bbe9cc8a57afe6d832e2"],
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": [basedir + "input/topics", "ReqsDocument"],
        }

    analytics_specs = \
        {
           "stop_on_errors": False,
           "topics": "ts_common",
        }
    
    output_specs = \
        [ 
          ["prios", 
           ["ts_common", basedir + "result_is/reqsprios.tex"]],

          ["graph",
           ["ts_common", basedir + "result_is/req-graph1.dot"]],

          ["graph2",
           ["ts_common", basedir + "result_is/req-graph2.dot"]],

          ["stats_reqs_cnt", 
           ["ts_common", basedir + "result_is/stats_reqs_cnt.csv"]],

          ["latex2", 
           ["ts_common", basedir + "result_is/reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            basedir + "result_is/html", basedir + "input/header.html",
            basedir + "input/footer.html"]],

          ["xml_ganttproject_1",
           ["ts_common", basedir + "result_is/gantt.xml", 1]],
        ]
