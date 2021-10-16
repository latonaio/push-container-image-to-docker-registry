# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

from setuptools import setup, find_packages

setup(
    name="push-container-image-to-docker-registry",
    version="0.0.1",
    author="XXXXXX",
    packages=find_packages("./src"),
    package_dir={"":"src"},
    install_requires=[
        "pathlib",
        "docker"
    ],
    tests_require=[]
)
