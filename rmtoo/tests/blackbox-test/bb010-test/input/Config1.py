import os

class Config:

    basedir = "tests/blackbox-test/bb010-test/"
    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": basedir + "input/reqs",
           "commit_interval": ["FILES", "FILES"],
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
           ["ts_common", result_is + "/reqsprios.tex"]],

          ["graph",
           ["ts_common", result_is + "/req-graph1.dot"]],

          ["graph2",
           ["ts_common", result_is + "/req-graph2.dot"]],

          ["latex2", 
           ["ts_common", result_is + "/reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            result_is + "/html", basedir + "input/header.html",
            basedir + "input/footer.html"]],

          ["xml_ganttproject_1",
           ["ts_common", result_is + "/gantt.xml", 1]],

          ["xml_ganttproject_2",
           ["ts_common", result_is + "/gantt2.xml", 1]],

          ["oopricing1", 
           ["ts_common", result_is + "/reqspricing"]],
        ]
