#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="fdispatch",
    version="0.1.0",
    packages=find_packages(),
    scripts=['fdispatch/fdispatch.py'],
    install_requires=[],
    package_data={},
    author="Rudy Baraglia",
    author_email="baraglia.rudy@gmail.com",
    description="fdispatch script allow to sub-divide a corpus of files into different sub-sets.",
    license="AGPL V3",
    keywords="util files corpus dispatch sub-set subset corpora",
    url="",
    project_urls={
        "github" : ""
    },
    long_description="Refer to README"

)