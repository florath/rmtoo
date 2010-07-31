

class Config:

    basedir = "tests/blackbox-test/bb001-test/"

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        [
           basedir + "input/reqs",
           ["v10", "c35f8e918ab1d05ab3e2ba0be52a3f4092035663"]
           #["138be32f1985aec694934263f02e47292deaac91", "FILES"]
           #["v8", "FILES"]
           # ["FILES", "FILES"]
        ]

    topic_specs = \
        {
          "ts_common": [basedir + "input/topics", "ReqsDocument"],
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
        ]
