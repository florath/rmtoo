#!/usr/bin/env python

from distutils.core import setup
import os, sys

package = 'rmtoo'
version = '19'

add_data = []
for dadi in ['rmtoo/tests', 'rmtoo/collection']:
    for (path, dirs, files) in os.walk(dadi):
        add_data.append((
            'share/pyshared/' + path,
            [path + '/' + filename for filename in files]))

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
      url='http://www.flonatel.de/projekte/rmtoo',
      packages=['rmtoo', 'rmtoo/lib', 'rmtoo/lib/digraph',
                'rmtoo/modules', 'rmtoo/tests', 'rmtoo/outputs',
                'rmtoo/lib/analytics', 'rmtoo/lib/main/',
                'rmtoo/lib/storagebackend',
                'rmtoo/lib/storagebackend/txtfile',
                'rmtoo/tests/lib', 'rmtoo/tests/syntax-test',
                'rmtoo/tests/unit-test', 'rmtoo/tests/unit-test/tag-tests',
                'rmtoo/tests/unit-test/digraph-test',
                'rmtoo/tests/unit-test/core-tests',
                'rmtoo/tests/unit-test/core-tests/testdata',
                'rmtoo/tests/unit-test/core-tests/testdata/modules01',
                'rmtoo/tests/unit-test/core-tests/testdata/modules02',
                'rmtoo/tests/unit-test/core-tests/testdata/modules03',
                'rmtoo/tests/unit-test/core-tests/testdata/modules04',
                'rmtoo/tests/unit-test/core-tests/testdata/modules05',
                'rmtoo/tests/unit-test/core-tests/testdata/modules06',
                'rmtoo/tests/unit-test/core-tests/testdata/modules07',
                'rmtoo/tests/unit-test/core-tests/testdata/modules08',
                'rmtoo/tests/unit-test/topic-tests',
                'rmtoo/tests/unit-test/topic-tests/testdata',
                'rmtoo/tests/unit-test/topic-tests/testdata/topicset01',
                'rmtoo/tests/output-test',

                # Blackbox Tests
                # are included with the 'add_data' statement.

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
                # odf
                'rmtoo/contrib/odf',
                ],
      data_files=add_data,

      license="GPL V3",
      platforms="all",
      scripts=["bin/rmtoo", "bin/rmtoo-normalize-dependencies"],
     )
