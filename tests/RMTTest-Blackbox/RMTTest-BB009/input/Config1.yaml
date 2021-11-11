class Config:

    #    basedir = "tests/BlackboxTest/Bb009Test/"
    #    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "${ENV:basedir}/input/reqs",
           "commit_interval": ["FILES",
                               "FILES"],
           # ["138be32f1985aec694934263f02e47292deaac91", "FILES"]
           # ["v8", "FILES"]
           # ["FILES", "FILES"]
           "default_language": "en_GB",
        }

    topic_specs = \
        {
          "ts_common": ["${ENV:basedir}/input/topics", "A1"],
        }

    analytics_specs = \
        {
           "stop_on_errors": True,
           "topics": "ts_common",
        }

    output_specs = \
        [
          ["graph2",
           ["ts_common", "${ENV:rmtoo_test_dir}/req-graph2.dot"]],
        ]
