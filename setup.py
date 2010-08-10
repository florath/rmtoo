#!/usr/bin/env python

from add_data import add_data
from distutils.core import setup
import os, sys

package = 'rmtoo'
version = '11'

def adjust(input, output):
    if os.path.exists(output):
        input_time = os.path.getmtime(input)
        output_time = os.path.getmtime(output)
        setup_time = os.path.getmtime('setup.py')
        if output_time > input_time and output_time > setup_time:
            return
        os.chmod(output, 0644)
        os.remove(output)
    sys.stdout.write('adjusting %s -> %s\n' % (input, output))
    buffer = file(input).read()
    file(output, 'w').write(buffer.replace('@VERSION@', version))
    os.chmod(output, 0444)

setup(name=package, version=version,
      description='Requirements Management Tool',
      author='Andreas Florath',
      author_email='sf@flonatel.org',
      url='http://rmtoo.gnu4u.org',
      packages=['rmtoo', 'rmtoo/lib', 'rmtoo/lib/digraph',
                'rmtoo/modules', 'rmtoo/tests', 'rmtoo/outputs',
                'rmtoo/lib/analytics',
                'rmtoo/tests/lib', 'rmtoo/tests/syntax-test',
                'rmtoo/tests/unit-test', 'rmtoo/tests/unit-test/tag-tests',
                'rmtoo/tests/unit-test/digraph-test',
                'rmtoo/tests/unit-test/core-tests',
                'rmtoo/tests/unit-test/core-tests/testdata',
                'rmtoo/tests/unit-test/core-tests/testdata/modules01',
                'rmtoo/tests/unit-test/core-tests/testdata/modules02',
                'rmtoo/tests/unit-test/core-tests/testdata/modules03',
                'rmtoo/tests/unit-test/core-tests/testdata/modules04',
                'rmtoo/tests/unit-test/topic-tests',
                'rmtoo/tests/unit-test/topic-tests/testdata',
                'rmtoo/tests/unit-test/topic-tests/testdata/topicset01',
                'rmtoo/tests/output-test',

                # Blackbox Tests
                #'rmtoo/tests/blackbox-test',
                #'rmtoo/tests/blackbox-test/bb001-test',
                #'rmtoo/tests/blackbox-test/bb002-test',
                #'rmtoo/tests/blackbox-test/bb003-test',
                #'rmtoo/tests/blackbox-test/bb004-test',

                ## contrib
                'rmtoo/contrib',
                # async
                "rmtoo/contrib/async",
                'rmtoo/contrib/async/mod',
                # gitdb
                'rmtoo/contrib/gitdb',
                'rmtoo/contrib/gitdb/db',
                # git-python
                'rmtoo/contrib/git',
                'rmtoo/contrib/git/repo',
                'rmtoo/contrib/git/index',
                'rmtoo/contrib/git/objects',

                ],
      data_files=add_data,

      license="GPL V3",
      platforms="all",
      scripts=["bin/rmtoo", ],
     )
