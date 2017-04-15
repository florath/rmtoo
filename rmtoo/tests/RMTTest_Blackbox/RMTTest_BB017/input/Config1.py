class Config:

    #    basedir = "tests/BlackboxTest/Bb017Test/"
    #    result_is = os.environ["rmtoo_test_dir"]

    stakeholders = ["development", "management", "users", "customers"]

    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "${ENV:basedir}/input/reqs",
           "commit_interval": ["FILES", "FILES"],
           "default_language": "en_GB",
           "dependency_notation": set(["Solved by", ]),
        }

    topic_specs = \
        {
          "ts_common": ["${ENV:basedir}/input/topics", "ReqsDocument"],
        }

    analytics_specs = \
        {
           "stop_on_errors": False,
           "topics": "ts_common",
        }

    constraints_specs = \
        {
           "search_dirs": ["../rmtoo/collection/constraints"]
        }

    output_specs = \
        [
          ["latex2",
           ["ts_common", "${ENV:rmtoo_test_dir}/reqtopics.tex"]],
        ]
