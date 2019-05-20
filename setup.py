from __future__ import print_function
from setuptools import setup, find_packages
# import subprocess
# import sys

from distutils.command.build_py import build_py
from distutils.command.build_scripts import build_scripts

import os
import sys
mydir = os.path.dirname(__file__)

if os.path.exists(os.path.join(mydir, '.bzr')):

    from bzrlib.branch import Branch
    branch = Branch.open_containing('.')[0]
    revno = branch.revno()
    revid = branch.get_rev_id(revno)
    rtagdict  = branch.tags.get_reverse_tag_dict()
    if revid in rtagdict:
        version = rtagdict[revid][0]
    else:
        version = 'bzr%s' % revno
    f = open(os.path.join(mydir, 'myversion.txt'), 'w')
    print("version = %s" % version, file=f)
    f.close()
else:
    version = open(os.path.join(mydir, 'myversion.txt'), 'r').read().strip()

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="ftd2xx",
    version=version,
    packages=find_packages(),
    # metadata for upload to PyPI
    author="Satya Mishra",
    author_email="satya.devel@gmail.com",
    description="Python interface to ftd2xx.dll from FTDI using ctypes based on d2xx by Pablo Bleyer",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    keywords="ftd2xx d2xx ftdi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/snmishra/ftd2xx',  # project home page, if any
    zip_safe=False,
    test_suite="ftd2xx.tests.t_ftd2xx",
    cmdclass = {'build_py': build_py, 'build_scripts': build_scripts},
    # could also include long_description, download_url, classifiers, etc.
    install_requires=(['future',
                       'pywin32; platform_system == "Windows"'])
)
