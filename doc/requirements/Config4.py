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
            # "commit_interval":
            #  ["138be32f1985aec694934263f02e47292deaac91", "FILES"],
            # "commit_interval":
            # ["v5", "FILES"]
            "commit_interval": ["FILES", "FILES"],
            "default_language": "en_GB",
        }

    topic_specs = \
        {
            "ts_common": ["doc/topics", "ReqsDocument"],
            # "ts_input_only": ["doc/topics", "Input"],
        }

    analytics_specs = \
        {
            "stop_on_errors": False,
            "topics": "ts_common",
        }

    output_specs = \
        [
            ["xml_ganttproject_2",
             ["ts_common", "rmtoo.gan", 1.0]],
        ]
