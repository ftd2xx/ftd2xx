from setuptools import setup, find_packages
import subprocess
import sys

if sys.version_info >= (3, 0):
    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
    except ImportError:
        raise ImportError("build_py_2to3 not found in distutils - it is required for Python 3.x")
    suffix = "-py3k"
else:
    from distutils.command.build_py import build_py
    from distutils.command.build_scripts import build_scripts
    suffix = ""


import os
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
    print >> f, "version = %s" % version
    f.close()
else:
    version = open(os.path.join(mydir, 'myversion.txt'), 'rU').read().strip()

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="ftd2xx" + suffix,
    version=version,
    packages=find_packages(),
    # metadata for upload to PyPI
    author="Satya Mishra",
    author_email="qufgmx@gmail.com",
    description="Python interface to ftd2xx.dll from FTDI using ctypes based on d2xx by Pablo Bleyer",
    license="BSD",
    keywords="ftd2xx d2xx ftdi",
    url='https://github.com/snmishra/ftd2xx',  # project home page, if any
    zip_safe=False,
    test_suite="ftd2xx.tests.t_ftd2xx",
    long_description=long_description,
    cmdclass = {'build_py': build_py, 'build_scripts': build_scripts},
    # could also include long_description, download_url, classifiers, etc.
)
