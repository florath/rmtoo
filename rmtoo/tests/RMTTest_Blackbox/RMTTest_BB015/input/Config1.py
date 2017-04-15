import os


class Config:

    basedir = "tests/BlackboxTest/Bb015Test/"
    result_is = os.environ["rmtoo_test_dir"]

    reqs_spec = \
        {
           "directory": basedir + "input/reqs",
           "commit_interval": ["v10",
                               "c35f8e918ab1d05ab3e2ba0be52a3f4092035663"],
           # ["138be32f1985aec694934263f02e47292deaac91", "FILES"]
           # ["v8", "FILES"]
           # ["FILES", "FILES"]
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

          ["stats_reqs_cnt",
           ["ts_common", result_is + "/stats_reqs_cnt.csv"]],

          ["latex2",
           ["ts_common", result_is + "/reqtopics.tex"]],

          ["html",
           ["ts_common",
            result_is + "/html", basedir + "input/header.html",
            basedir + "input/footer.html"]],

          ["xml_ganttproject_2",
           ["ts_common", result_is + "/gantt2.xml", 1]],

          ["oopricing1",
           ["ts_common", result_is + "/reqspricing"]],
        ]
