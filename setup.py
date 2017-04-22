#!/usr/bin/env python

from setuptools import setup
import os
import sys

package = 'rmtoo'
version = '24.0.0'

add_data = []

for dadi, destpath_prefix in [('rmtoo/tests', None),
                              ('rmtoo/collection', None),
                              ('doc', 'rmtoo'),
                              ('contrib', 'rmtoo')]:
    for (path, dirs, files) in os.walk(dadi):
        if path.endswith("__pycache__"):
            continue
        l = []
        for filename in files:
            if filename.endswith(".pyc"):
                continue
            l.append(os.path.join(path, filename))
        dpath = os.path.join(destpath_prefix, path) \
                if destpath_prefix is not None else path
        add_data.append((dpath, l))

add_data.append(
    ("rmtoo/doc/readme",
     ["Readme-Windows.txt", "gpl-3.0.txt", "Readme-GitPython.txt",
      "Readme-Hacking.txt", "Readme-OS-X.txt", "Readme-Overview.txt",
      "Readme-RmtooOnRmtoo.txt", "Readme-Windows.txt",
    "requirements.txt", "RequirementVsConstraint.txt", "RMTEx.txt",
      "Roadmap.txt", "Readme.rst"]))

def adjust(input, output):
    if os.path.exists(output):
        input_time = os.path.getmtime(input)
        output_time = os.path.getmtime(output)
        setup_time = os.path.getmtime('setup.py')
        if output_time > input_time and output_time > setup_time:
            return
        os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
                 | os.stat.S_IREAD | os.stat.S_IWRITE)
        os.remove(output)
    sys.stdout.write('adjusting %s -> %s\n' % (input, output))
    buffer = open(input).read()
    file(output, 'w').write(buffer.replace('@VERSION@', version))
    os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
                 | os.stat.S_IREAD | os.stat.S_IWRITE)


setup(name=package, version=version,
      description='Free and OpenSource Requirements Management Tool',
      keywords='requirements management',
      author='Andreas Florath',
      author_email='rmtoo@florath.net',
      url='http://rmtoo.florath.net',
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: Manufacturing",
          "Intended Audience :: Telecommunications Industry",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: MacOS",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: OS Independent",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Topic :: Software Development :: Quality Assurance",
          "Topic :: Scientific/Engineering",
      ],
      packages=['rmtoo', 'rmtoo/lib',
                'rmtoo/inputs', 'rmtoo/tests', 'rmtoo/outputs',
                'rmtoo/lib/analytics',
                'rmtoo/lib/configuration',
                'rmtoo/lib/digraph',
                'rmtoo/lib/logging',
                'rmtoo/lib/main',
                'rmtoo/lib/storagebackend', 'rmtoo/lib/xmlutils/',
                'rmtoo/lib/storagebackend/txtfile',
                'rmtoo/lib/vcs',
                'rmtoo/lib/xmlutils',
                'rmtoo/tests/lib', 'rmtoo/tests/RMTTest-Syntax',
                'rmtoo/tests/RMTTest-Unit',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Tag',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Digraph',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules01',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules02',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules03',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules04',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules05',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules06',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules07',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Core/testdata/modules08',
                'rmtoo/tests/RMTTest-Unit/RMTTest-Topic',
                'rmtoo/tests/RMTTest-Output',

                # Blackbox Tests
                # are included with the 'add_data' statement.
                ],
      data_files=add_data,
      install_requires=[
          "numpy>=1.12.0",
          "scipy>=0.19.0",
          "six>=1.10.0",
          "future>=0.16.0",
          "gitdb==0.6.4",
          "gitpython==1.0.2",
          "odfpy==1.3.4"],
      license="GPL V3",
      platforms="all",

      entry_points={
          'console_scripts': [
              "rmtoo = rmtoo.lib.RmtooMain:main",
              "rmtoo-configuration-convert = "
              "rmtoo.lib.main.ConfigurationConvert:main",
              "rmtoo-normalize-dependencies = "
              "rmtoo.lib.main.NormalizeDependencies:main",
              "rmtoo-pricing-graph = rmtoo.lib.main.PricingGraph:main",
          ]
      })
