#!/usr/bin/env python

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
                'rmtoo/modules', 'rmtoo/tests',
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
                'rmtoo/tests/blackbox-test',
                'rmtoo/tests/blackbox-test/bb001-test',
                'rmtoo/tests/blackbox-test/bb001-test/input',
                'rmtoo/tests/blackbox-test/bb001-test/input/reqs',
                'rmtoo/tests/blackbox-test/bb001-test/input/topics',
                'rmtoo/tests/blackbox-test/bb001-test/result_is',
                'rmtoo/tests/blackbox-test/bb001-test/result_should',
                'rmtoo/tests/blackbox-test/bb001-test/result_should/html',
                'rmtoo/tests/blackbox-test/bb002-test',
                'rmtoo/tests/blackbox-test/bb002-test/input',
                'rmtoo/tests/blackbox-test/bb002-test/input/reqs',
                'rmtoo/tests/blackbox-test/bb002-test/input/topics',
                'rmtoo/tests/blackbox-test/bb002-test/result_is',
                'rmtoo/tests/blackbox-test/bb002-test/result_should',
                'rmtoo/tests/blackbox-test/bb002-test/result_should/html',
                'rmtoo/tests/blackbox-test/bb003-test',
                'rmtoo/tests/blackbox-test/bb003-test/input',
                'rmtoo/tests/blackbox-test/bb003-test/input/reqs',
                'rmtoo/tests/blackbox-test/bb003-test/input/topics',
                'rmtoo/tests/blackbox-test/bb003-test/result_is',
                'rmtoo/tests/blackbox-test/bb003-test/result_should',
                'rmtoo/tests/blackbox-test/bb003-test/result_should/html',
                'rmtoo/tests/blackbox-test/bb004-test',
                'rmtoo/tests/blackbox-test/bb004-test/input',
                'rmtoo/tests/blackbox-test/bb004-test/input/reqs',
                'rmtoo/tests/blackbox-test/bb004-test/input/topics',
                'rmtoo/tests/blackbox-test/bb004-test/result_is',
                'rmtoo/tests/blackbox-test/bb004-test/result_should',
                'rmtoo/tests/blackbox-test/bb004-test/result_should/html',

                ## contrib
                'rmtoo/contrib'
                # async
                'rmtoo/contrib/async-0.6.1',
                'rmtoo/contrib/async-0.6.1/mod',
                # gitdb
                'rmtoo/contrib/gitdb-0.5.1',
                'rmtoo/contrib/gitdb-0.5.1/db',
                # git-python
                'rmtoo/contrib/GitPython-0.3.0-beta2',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib/GitPython.egg-info',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib/git',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib/git/repo',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib/git/index',
                'rmtoo/contrib/GitPython-0.3.0-beta2/lib/git/objects',
                ],
      license="GPL V3",
      platforms="all",
      scripts=["bin/rmtoo", ],
     )
