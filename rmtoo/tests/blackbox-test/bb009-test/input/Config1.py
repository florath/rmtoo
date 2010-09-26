import os

class Config:

    basedir = "tests/blackbox-test/bb009-test/"
    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": basedir + "input/reqs",
           "commit_interval": ["FILES", 
                               "FILES"],
           #["138be32f1985aec694934263f02e47292deaac91", "FILES"]
           #["v8", "FILES"]
           # ["FILES", "FILES"]
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": [basedir + "input/topics", "ReqsDocument"],
        }

    analytics_specs = \
        { 
           "stop_on_errors": True,
           "topics": "ts_common",
        }
    
    output_specs = \
        [ 
          ["graph2",
           ["ts_common", result_is + "/req-graph2.dot"]],
        ]
