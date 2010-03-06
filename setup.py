#!/usr/bin/env python

from distutils.core import setup
import os, sys

package = 'rmtoo'
version = '6'

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
      url='http://www.gnu4u.org/rmtoo',
      packages=['rmtoo', 'rmtoo/lib', 'rmtoo/modules'],
      license="GPL V3",
      platforms="all",
      scripts=["bin/rmtoo", ],
     )
