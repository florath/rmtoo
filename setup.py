#!/usr/bin/env python
"""
Setup for rmToo
"""
import os
import sys

from setuptools import setup

PACKAGE = 'rmtoo'
VERSION = '24.3.0'

ADD_DATA = []

for dadi, destpath_prefix in [('contrib', 'rmtoo')]:
    for (path, dirs, files) in os.walk(dadi):
        if path.endswith("__pycache__"):
            continue
        if path.startswith("doc/man"):
            # Handled separately
            continue
        l = []
        for filename in files:
            if filename.endswith(".pyc"):
                continue
            l.append(os.path.join(path, filename))
        dpath = os.path.join(destpath_prefix, path) \
                if destpath_prefix is not None else path
        ADD_DATA.append((dpath, l))

# pylint: disable=deprecated-lambda,cell-var-from-loop
for man_name in os.listdir("share/man"):
    man_dir = "share/man/%s" % man_name
    ADD_DATA.append(
        (man_dir,
         list(map(lambda x: os.path.join(man_dir, x),
                  os.listdir(man_dir)))))

ADD_DATA.append(
    ("rmtoo/doc/readme",
     ["Readme-Windows.txt", "gpl-3.0.txt", "Readme-GitPython.txt",
      "Readme-Hacking.txt", "Readme-OS-X.txt", "Readme-Overview.txt",
      "Readme-RmtooOnRmtoo.txt", "Readme-Windows.txt",
      "requirements.txt", "RequirementVsConstraint.txt", "RMTEx.txt",
      "Roadmap.txt", "Readme.rst",
      "contrib/vmsetup/Readme-PreinstalledVM.rst",
      "contrib/vmsetup/Readme-PreinstalledVMGui.rst"]))

def adjust(input_filename, output):
    """Function to adjust the version number

    The version number seen in this file is the master.  Use
    this function to possible adjust other parts that also needs
    an up to date version number.
    """
    if os.path.exists(output):
        input_time = os.path.getmtime(input_filename)
        output_time = os.path.getmtime(output)
        setup_time = os.path.getmtime('setup.py')
        if output_time > input_time and output_time > setup_time:
            return
        # stat HAS these members
        # pylint: disable=no-member
        os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
                 | os.stat.S_IREAD | os.stat.S_IWRITE)
        os.remove(output)
    sys.stdout.write('adjusting %s -> %s\n' % (input_filename, output))
    file_buffer = open(input_filename).read()
    file(output, 'w').write(file_buffer.replace('@VERSION@', VERSION))
    # pylint: disable=no-member
    os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
             | os.stat.S_IREAD | os.stat.S_IWRITE)


setup(name=PACKAGE, version=VERSION,
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
      packages=[
          "rmtoo",
          "rmtoo/inputs",
          "rmtoo/lib",
          "rmtoo/lib/digraph",
          "rmtoo/lib/vcs",
          "rmtoo/lib/logging",
          "rmtoo/lib/analytics",
          "rmtoo/lib/xmlutils",
          "rmtoo/lib/main",
          "rmtoo/lib/configuration",
          "rmtoo/lib/storagebackend",
          "rmtoo/lib/storagebackend/txtfile",
          "rmtoo/outputs",
          "rmtoo/collection",
          "rmtoo/collection/constraints",
      ],
      include_package_data=True,
      data_files=ADD_DATA,
      install_requires=[
          "numpy>=1.12.0",
          "scipy>=0.19.0",
          "six>=1.10.0",
          "future>=0.16.0",
          "gitdb==0.6.4",
          "gitpython==1.0.2",
          "pyyaml>=3.12",
          "stevedore>=1.21",
          "pylint>=1.7.1",
          "odfpy==1.3.4",
          "jinja2>=2.10"],
      license="GPL V3",
      platforms="all",

      entry_points={
          'console_scripts': [
              "rmtoo = rmtoo.lib.RmtooMain:main",
              "rmtoo-normalize-dependencies = "
              "rmtoo.lib.main.NormalizeDependencies:main",
              "rmtoo-pricing-graph = rmtoo.lib.main.PricingGraph:main",
          ],
          # Used for / with stevedore
          'rmtoo.input.plugin': [
              "RDepDependsOn = rmtoo.inputs.RDepDependsOn:RDepDependsOn",
              "RDepConstraints = rmtoo.inputs.RDepConstraints:RDepConstraints",
              "RDepMasterNodes = rmtoo.inputs.RDepMasterNodes:RDepMasterNodes",
              "RDepNoDirectedCircles = rmtoo.inputs.RDepNoDirectedCircles:RDepNoDirectedCircles",
              "RDepOneComponent = rmtoo.inputs.RDepOneComponent:RDepOneComponent",
              "RDepPriority = rmtoo.inputs.RDepPriority:RDepPriority",
              "RDepSolvedBy = rmtoo.inputs.RDepSolvedBy:RDepSolvedBy",
              "ReqCE3 = rmtoo.inputs.ReqCE3:ReqCE3",
              "ReqClass = rmtoo.inputs.ReqClass:ReqClass",
              "ReqConstraints = rmtoo.inputs.ReqConstraints:ReqConstraints",
              "ReqDescription = rmtoo.inputs.ReqDescription:ReqDescription",
              "ReqEffortEst = rmtoo.inputs.ReqEffortEst:ReqEffortEst",
              "ReqExpectedResult = rmtoo.inputs.ReqExpectedResult:ReqExpectedResult",
              "ReqHistory = rmtoo.inputs.ReqHistory:ReqHistory",
              "ReqInventedBy = rmtoo.inputs.ReqInventedBy:ReqInventedBy",
              "ReqInventedOn = rmtoo.inputs.ReqInventedOn:ReqInventedOn",
              "ReqName = rmtoo.inputs.ReqName:ReqName",
              "ReqNote = rmtoo.inputs.ReqNote:ReqNote",
              "ReqOwner = rmtoo.inputs.ReqOwner:ReqOwner",
              "ReqPriority = rmtoo.inputs.ReqPriority:ReqPriority",
              "ReqRationale = rmtoo.inputs.ReqRationale:ReqRationale",
              "ReqStatus = rmtoo.inputs.ReqStatus:ReqStatus",
              "ReqTestCase = rmtoo.inputs.ReqTestCase:ReqTestCase",
              "ReqTopic = rmtoo.inputs.ReqTopic:ReqTopic",
              "ReqType = rmtoo.inputs.ReqType:ReqType"
          ],
          "rmtoo.output.plugin" : [
              "graph2 = rmtoo.outputs.graph2:graph2",
              "graph = rmtoo.outputs.graph:graph",
              "html = rmtoo.outputs.html:Html",
              "latex2 = rmtoo.outputs.latex2:latex2",
              "LatexJinja2 = rmtoo.outputs.LatexJinja2:LatexJinja2",
              "oopricing1 = rmtoo.outputs.oopricing1:oopricing1",
              "prios = rmtoo.outputs.prios:prios",
              "stats_burndown1 = rmtoo.outputs.stats_burndown1:stats_burndown1",
              "stats_reqs_cnt = rmtoo.outputs.stats_reqs_cnt:stats_reqs_cnt",
              "stats_sprint_burndown1 = rmtoo.outputs.stats_sprint_burndown1:stats_sprint_burndown1",
              "tlp1 = rmtoo.outputs.tlp1:Tlp1",
              "version1 = rmtoo.outputs.version1:version1",
              "xml1 = rmtoo.outputs.xml1:Xml1",
              "xml_ganttproject_2 = rmtoo.outputs.xml_ganttproject_2:xml_ganttproject_2"
          ],
          "rmtoo.output.markup" : [
              "latex = rmtoo.lib.Markup:LaTeX",
              "txt = rmtoo.lib.Markup:Txt",
              "html = rmtoo.lib.Markup:Html"
          ],
          "rmtoo.input.requirement_status" : [
              "not done = rmtoo.lib.RequirementStatus:RequirementStatusNotDone",
              "assigned = rmtoo.lib.RequirementStatus:RequirementStatusAssigned",
              "finished = rmtoo.lib.RequirementStatus:RequirementStatusFinished"
          ]
      })
