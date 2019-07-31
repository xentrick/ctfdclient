#!/usr/bin/env python3
# coding: utf-8

import re
from os import path
from setuptools import find_packages, setup

PACKAGE_NAME = "ctfdclient"

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

setup(
    name="ctfdclient",
    version="1.0",
    url="https://github.com/xentrick/ctfdclient",
    license="",
    author="nmavis",
    author_email="nmavis@cisco.com",
    description="CTFd API wrapper client",
    packages=find_packages(exclude={"tests", "tests.*", "misc"}),
    install_requires=["beautifulsoup4"],
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
