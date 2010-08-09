

class Config:

    basedir = "tests/blackbox-test/bb003-test/"

    stakeholders = ["executive", ]

    inventors = ["VincentAndJules", "Wulf"]

    reqs_spec = \
        {
           "directory": basedir + "input/reqs",
           "commit_interval": ["FILES", "FILES"],
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": [basedir + "input/topics", "PulpFiction"],
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

          ["latex2", 
           ["ts_common", basedir + "result_is/reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            basedir + "result_is/html", basedir + "input/header.html",
            basedir + "input/footer.html"]],

          ["xml_ganttproject_1",
           ["ts_common", basedir + "result_is/gantt.xml", 1]],

        ]
