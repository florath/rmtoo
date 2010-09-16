#
# Config Class for the requirements for rmtoo
#

class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "doc/requirements",
           "commit_interval": 
           # This is used for all-day work:
           # ["FILES", "FILES"],
           # This is used for releases (epoch -> HEAD)
             ["7018a441475fb5837be18725a4b40e8d9ef100b1", "HEAD"],
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": ["doc/topics", "ReqsDocument"],
        }

    analytics_specs = \
        { 
           "stop_on_errors": False,
           "topics": "ts_common",
        }

    output_specs = \
        [ 
          ["prios", 
           ["ts_common", "doc/latex2/reqsprios.tex"]],

          ["graph",
           ["ts_common", "req-graph1.dot"]],

          ["graph2",
           ["ts_common", "req-graph2.dot"]],

          ["stats_reqs_cnt", 
           ["ts_common", "doc/latex2/stats_reqs_cnt.csv"]],

          ["latex2", 
           ["ts_common", "doc/latex2/reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            "doc/html/reqs", "doc/html/header.html",
            "doc/html/footer.html"]],
        ]
