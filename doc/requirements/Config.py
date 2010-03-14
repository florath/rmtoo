#
# Config Class for the requirements for rmtoo
#

class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    output_specs = \
        { "latex": ["doc/latex"],
          "prios": ["doc/latex/reqsprios.tex"],
          "graph": ["reqtree.dot"],
          "stats_reqs_cnt": ["doc/latex/stats_reqs_cnt.csv"]
        }
