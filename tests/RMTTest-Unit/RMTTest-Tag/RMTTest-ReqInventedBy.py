'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqInventedBy

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqInventedBy import ReqInventedBy
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
import pytest


class RMTTestReqInventedBy(object):

    def rmttest_positive_01(self):
        "Requirement Tag Invented by - tag given"
        config, req = create_parameters()
        config.set_value('requirements.inventors',
                         ["meinereiner", "keinerseiner"])
        req["Invented by"] = RecordEntry("Invented by", "meinereiner")

        rt = ReqInventedBy(config)
        name, value = rt.rewrite("InventedBy-test", req)
        assert "Invented by" == name
        assert "meinereiner" == value

    def rmttest_negative_01(self):
        "Requirement Tag Invented by - no tag given"
        config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]

        rt = ReqInventedBy(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("InventedBy-test", req)
            assert 5 == rmte.id()

    def rmttest_negative_02(self):
        "Requirement Tag Invented by - invalid tag given"
        config, req = create_parameters()
        config.set_value('requirements.inventors',
                         ["meinereiner", "keinerseiner"])
        req["Invented by"] = RecordEntry("Invented by", "MeinNameIstHase")

        rt = ReqInventedBy(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("InventedBy-test", req)
            assert 6 == rmte.id()
