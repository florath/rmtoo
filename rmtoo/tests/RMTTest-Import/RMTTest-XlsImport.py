# (c) 2018 Kristoffer Nordstroem, see COPYING
from __future__ import unicode_literals
import os
import re
import codecs
import pytest
import distutils.file_util

from rmtoo.lib.Requirement import Requirement
from rmtoo.imports.xls import XlsImport
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Encoding import Encoding

LDIR = os.path.dirname(os.path.abspath(__file__))
LIPSUM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
    "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
    "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
    "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
    "occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum.")


@pytest.fixture(scope='function')
def tmpdir():
    tmpdir = create_tmp_dir()
    yield tmpdir
    delete_tmp_dir(tmpdir)


@pytest.fixture
def dest_dir(tmpdir):
    dest_dirs = {u'requirements_dirs': [Encoding.to_unicode(tmpdir)],
                 u'topics_dirs': [Encoding.to_unicode(tmpdir)]}
    return dest_dirs


class RMTTestXlsImport:
    '''Test-Class to import the xls artifact'''

    imp_fn = os.path.join(LDIR, 'test-reqs.xlsx')
    config = {u'import_filename': imp_fn,
              u'requirement_ws': u'Requirements',
              u'topics_sheet': u'Topics'}

    def rmttest_invalid_config_parser(self):
        '''Just figure out where it blows up'''
        dest_dirs = {u'requirements_dirs': [Encoding.to_unicode(tmpdir)],
                     u'topics_dirs': [Encoding.to_unicode(tmpdir)]}
        importer = XlsImport({}, dest_dirs)
        assert not importer.useable

    def rmttest_config_run_with_default_cfg(self, dest_dir):
        tmpdir = dest_dir['requirements_dirs'][0]
        tmp_fn = os.path.join(tmpdir, 'test-reqs.xlsx')
        config = dict(self.config)
        distutils.file_util.copy_file(config[u'import_filename'], tmp_fn)
        config[u'import_filename'] = tmp_fn

        importer = XlsImport(config, dest_dir)
        assert importer.useable
        importer.run()

        assert os.path.isfile(os.path.join(tmpdir, 'AutomaticGeneration.req'))
        completed_filename = os.path.join(tmpdir, 'Completed.req')
        assert os.path.isfile(completed_filename)

        # Assert ID is filename and not written to file
        id_occ = [re.findall(r'^ID:', line)
                  for line in open(completed_filename)]
        for i in id_occ:
            assert not i

    def rmttest_treat_newlines_correctly(self, dest_dir):
        tmpdir = dest_dir['requirements_dirs'][0]

        config = dict(self.config)
        tmp_fn = os.path.join(tmpdir, 'test-reqs.xlsx')
        distutils.file_util.copy_file(config[u'import_filename'], tmp_fn)
        config[u'import_filename'] = tmp_fn

        importer = XlsImport(config, dest_dir)
        importer.run()

        newlines_filename = os.path.join(tmpdir, 'TestNewlines.req')
        assert os.path.isfile(newlines_filename)
        with codecs.open(newlines_filename, encoding='utf-8') as nl_fh:
            req_content = nl_fh.read()
        nl_req = Requirement(req_content, 'TestNewlines.req',
                             newlines_filename, None, None)

        # Test Description
        parsed_desc = "\n".join(nl_req.record[2].
                                get_content_trimmed_with_nl())
        assert parsed_desc == LIPSUM + "\n\nASDF"

        parsed_note = "\n".join(nl_req.record[10].
                                get_content_trimmed_with_nl())
        assert parsed_note == "Lipsum\n\nHandle it well"

        parsed_invon = "\n".join(nl_req.record[7].
                                 get_content_trimmed_with_nl())
        assert parsed_invon == "2010-03-06"

    def rmttest_future_invented_on(self, dest_dir, record_property):
        '''Ensure future InventedOn are not imported'''
        record_property('req', 'Import/XlsFutureInventedOn-deadbeef')
        tmpdir = dest_dir['requirements_dirs'][0]

        lcfg = dict(self.config)
        imp_fn = os.path.join(LDIR, 'test-reqs-future.xlsx')
        tmp_fn = os.path.join(tmpdir, 'test-reqs-future.xlsx')
        distutils.file_util.copy_file(imp_fn, tmp_fn)
        lcfg[u'import_filename'] = tmp_fn

        importer = XlsImport(lcfg, dest_dir)
        assert importer.useable
        with pytest.raises(RMTException):
            importer.run()

    def rmttest_set_solvedby(self, dest_dir, record_property):
        '''Esnure stuff'''
        record_property('req', 'Import/XlsDefaultSolvedby-deadbeef')
        tmpdir = dest_dir['requirements_dirs'][0]

        lcfg = dict(self.config)
        imp_fn = os.path.join(LDIR, 'test-reqs-solvedby.xlsx')
        tmp_fn = os.path.join(tmpdir, 'test-reqs-solvedby.xlsx')
        distutils.file_util.copy_file(imp_fn, tmp_fn)
        lcfg[u'import_filename'] = tmp_fn

        importer = XlsImport(lcfg, dest_dir)
        assert importer.useable
        importer.run()

        assert importer._entries[0]['ID'] == 'SW-101'
        assert importer._entries[0]['Solved by'] == 'SW-102 SW-104 SW-105'

    def rmttest_defcfg_import_topics(self, dest_dir):
        tmpdir = dest_dir['requirements_dirs'][0]
        tmp_fn = os.path.join(tmpdir, 'test-reqs.xlsx')
        config = dict(self.config)
        distutils.file_util.copy_file(config[u'import_filename'], tmp_fn)
        config[u'import_filename'] = tmp_fn

        importer = XlsImport(config, dest_dir)
        assert importer.useable
        importer.run()

        assert importer._topics['GUI'][0] == ('Name', 'GUI')
        assert os.path.isfile(os.path.join(tmpdir, 'rmtoo.tic'))
        completed_filename = os.path.join(tmpdir, 'GUI.tic')
        assert os.path.isfile(completed_filename)

        # Assert ID is filename and not written to file
        found = False
        id_occ = [re.findall(r'^Name:.*', line)
                  for line in open(completed_filename)]
        for i in id_occ:
            if i and i[0] == 'Name: GUI':
                found = True
        assert found


class RMTTestXlsImportRegressionTests:
    """Regression tests for the xls import functionality"""
    imp_fn = os.path.join(LDIR, 'test-reqs.xlsx')
    config = {u'import_filename': imp_fn,
              u'requirement_ws': u'Specification',
              u'topics_sheet': u'Topics'}

    def rmttest_regression_test_import_empty(self, dest_dir):
        imp_fn = os.path.join(LDIR, 'regression-import_empty.xlsx')
        tmpdir = dest_dir['requirements_dirs'][0]
        tmp_fn = os.path.join(tmpdir, 'regression-import_empty.xlsx')
        config = dict(self.config)
        config[u'import_filename'] = tmp_fn
        distutils.file_util.copy_file(imp_fn, tmp_fn)

        importer = XlsImport(config, dest_dir)
        assert importer.useable
        importer.run()
        assert importer._entries[0]['Solved by'] == 'SW-AS-100 SW-AS-101'
