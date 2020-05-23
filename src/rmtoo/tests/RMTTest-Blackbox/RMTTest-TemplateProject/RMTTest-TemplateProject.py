'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.tests.lib.BBHelper import BBHelper


class RMTTestTemplateproject(BBHelper):
    """Tests the template project"""

    in_test_dir = "../contrib/template_project"
    out_test_dir = "tests/RMTTest-Blackbox/RMTTest-TemplateProject"

    def rmttest_pos_001(self):
        """Blackbox: Check the template project"""
        self.artifacts_dir = "artifacts"

        cfg_file = "tests/RMTTest-Blackbox/RMTTest-TemplateProject" \
                   "/input/Config.yaml"
        self.run_test(
            cmd_line_params=[
                "-y", "file://" + cfg_file]
        )
