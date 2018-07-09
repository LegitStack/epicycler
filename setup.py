# -*- coding: utf-8 -*-
#
import os
import codecs

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "epicycler", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


setup(
    name="epicycler",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/epicycler",
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=["matplotlib", "numpy", "tspsolve"],
    description="Compute and draw epicycler in Python",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    entry_points={
        "console_scripts": [
            "epicycler-image = epicycler.cli:image",
            "epicycler-poly = epicycler.cli:poly",
        ]
    },
)