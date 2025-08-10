# (c) 2018 Kristoffer Nordstroem, see COPYING
import os
import pytest
import distutils.file_util

from rmtoo.lib.Import import Import
from rmtoo.imports.xls import XlsImport
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.lib.Encoding import Encoding

LDIR = Encoding.to_unicode(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope='function')
def tmpdir():
    tmpdir = create_tmp_dir()
    yield tmpdir
    delete_tmp_dir(tmpdir)


@pytest.fixture
def def_cfg(tmpdir):
    def_cfg_imp_dest = {'topics': {'ts_common': {
        'sources': [['dummydriver', {
            'requirements_dirs': [tmpdir],
            'topics_dirs': [tmpdir]
        }]]}}, 'tmpdir': tmpdir}
    return def_cfg_imp_dest


class RMTTestImport:
    '''Test-Class to import the modified artifacts again'''

    def rmttest_invalid_config_parser(self):
        '''Just figure out where it blows up '''
        with pytest.raises(AssertionError):
            Import(None)

    def rmttest_config_parser_wo_cfg(self, def_cfg):
        '''Assert the default configuration is loaded, ignore the import
        destination directory configuration'''
        cfg = {'import': {}, "dummy": "the universe is mind-bogglingly big"}
        cfg.update(def_cfg)
        importer = Import(cfg)
        assert not importer._config
        assert not importer._import_obj

    def rmttest_config_parser_input_dir(self, def_cfg):
        importer = Import(def_cfg)
        assert (importer._input_dir['requirements_dirs'][0]
                == def_cfg['tmpdir'])
        assert (importer._input_dir['topics_dirs'][0]
                == def_cfg['tmpdir'])

    def rmttest_config_parser(self, def_cfg):
        '''Assert the default configuration is loaded, ignore the import
        destination directory configuration'''
        cfg = {"import": {"xls": {
            'import_filename': "asdf.xls"}}}
        cfg.update(def_cfg)
        importer = Import(cfg)
        assert len(importer._import_obj) == 1
        assert isinstance(importer._import_obj[0], XlsImport)

    def rmttest_config_run_with_default_cfg(self, def_cfg):
        tmpdir = def_cfg['tmpdir']
        src_fn = os.path.join(LDIR, "test-reqs.xlsx")
        tmp_fn = os.path.join(tmpdir, "test-reqs.xlsx")
        distutils.file_util.copy_file(src_fn, tmp_fn)

        cfg = {"import": {"xls": {
            'import_filename': tmp_fn}}}
        cfg.update(def_cfg)
        importer = Import(cfg)
        importer.process_all()

        assert os.path.isfile(os.path.join(tmpdir, 'AutomaticGeneration.req'))
        assert os.path.isfile(os.path.join(tmpdir, 'Completed.req'))
        assert os.path.isfile(os.path.join(tmpdir, 'TestNewlines.req'))

    def rmttest_error_double_ids(self, def_cfg):
        tmpdir = def_cfg['tmpdir']
        src_fn = os.path.join(LDIR, "test-reqs-doubleid.xlsx")
        tmp_fn = os.path.join(tmpdir, "test-reqs-doubleid.xlsx")
        distutils.file_util.copy_file(src_fn, tmp_fn)

        cfg = {"import": {"xls": {
            'import_filename': tmp_fn}}}
        cfg.update(def_cfg)
        importer = Import(cfg)
        with pytest.raises(AssertionError):
            importer.process_all()

        assert not os.path.isfile(os.path.join(tmpdir,
                                               'AutomaticGeneration.req'))
        assert not os.path.isfile(os.path.join(tmpdir, 'Completed.req'))
        assert not os.path.isfile(os.path.join(tmpdir, 'TestNewlines.req'))
