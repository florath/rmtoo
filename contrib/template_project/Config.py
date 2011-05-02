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
           "directory": "requirements",
           "commit_interval": 
           # This is used for all-day work:
            ["FILES", "FILES"],
           # This is used for releases (epoch -> HEAD)
           #  ["v10", "HEAD"],
           "default_language": "en_GB",
           "dependency_notation": set(["Solved by", ])
        }

    topic_specs = \
        {
          "ts_common": ["topics", "ReqsDocument"],
        }

    analytics_specs = \
        { 
           "stop_on_errors": False,
           "topics": "ts_common",
        }

    output_specs = \
        [ 
          ["prios", 
           ["ts_common", "artifacts/reqsprios.tex"]],

          ["graph",
           ["ts_common", "artifacts/req-graph1.dot"]],

          ["graph2",
           ["ts_common", "artifacts/req-graph2.dot"]],

          ["stats_reqs_cnt", 
           ["ts_common", "artifacts/stats_reqs_cnt.csv"]],

          ["latex2", 
           ["ts_common", "artifacts/reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            "artifacts/html", "html/header.html",
            "html/footer.html"]],

          ["version1",
           ["ts_common", "artifacts/reqs-version.txt"]],

          ["stats_burndown1",
           ["ts_common", "artifacts/stats_burndown.csv", "2011-05-01"]],

          ["stats_sprint_burndown1",
           ["ts_common", "artifacts/stats_sprint_burndown.csv", "2011-05-01"]],

        ]
