#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

long_desc = """
This package contains a Sphinx extension for embedding sage cells.
It is based on Krzysztof Kajda's sage cell server extension (https://github.com/kriskda/sphinx-sagecell).

The extension defines a directive, "sagecell", for embedding sage cells.
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-sagecell",
    version="2.0",
    description="Sphinx sagecell extension",
    author="Solrun Einarsdottir",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)


# breyta
