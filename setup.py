from __future__ import print_function

import os
import subprocess
from distutils.command.build_py import build_py
from distutils.command.build_scripts import build_scripts

from setuptools import find_packages, setup

# import sys


mydir = os.path.dirname(__file__)

version = ""

try:
    version = (
        subprocess.check_output(["git", "tag", "--points-at", "HEAD"])
        .decode("ascii")
        .strip()
    )
    if version.startswith("v"):
        version = version[1:]
except subprocess.CalledProcessError:
    pass

if version == "":
    with open(os.path.join(mydir, "myversion.txt"), "r") as f:
        version = f.read().strip()

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="ftd2xx",
    version=version,
    packages=find_packages(),
    # metadata for upload to PyPI
    author="Satya Mishra",
    author_email="satya.devel@gmail.com",
    description=(
        "Python interface to ftd2xx.dll from FTDI using ctypes"
        "based on d2xx by Pablo Bleyer"
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    keywords="ftd2xx d2xx ftdi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/snmishra/ftd2xx",  # project home page, if any
    zip_safe=False,
    test_suite="ftd2xx.tests.t_ftd2xx",
    cmdclass={"build_py": build_py, "build_scripts": build_scripts},  # type: ignore
    # could also include long_description, download_url, classifiers, etc.
    install_requires=(['pywin32; platform_system == "Windows"']),
    extras_require={"aio": ["async_timeout"]},
)
