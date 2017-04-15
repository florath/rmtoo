#
# Config Class for the requirements for rmtoo
#

import os


class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "doc/requirements",
           "commit_interval": ["FILES", "FILES"],
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


files = os.listdir("doc/topics")
for fi in files:
    # Use only the files ending in .tic
    if not fi.endswith(".tic"):
        continue
    name = fi[:-4]
    # Add topic_spec for each topic
    Config.topic_specs["st_%s" % name] = ["doc/topics", name]
    Config.output_specs.append(
        ["graph2", ["st_%s" % name, "graphs/st_%s.dot" % name]])

#
# for i in *.dot; do echo $i; k=`basename $i .dot`; \
#    dot -Tpng -o $k.png $k.dot; done
#
