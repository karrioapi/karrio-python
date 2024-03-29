# coding: utf-8

"""
    Karrio Open Source Multi-carrier Shipping API

    OpenAPI spec version: 2021.11
    Contact: hello@karrio.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301


with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "karrio-python"
VERSION = "2022.3"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]
    

setup(
    name=NAME,
    version=VERSION,
    description="karrio universal Shipping API Python client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="hello@karrio.io",
    url="https://github.com/karrioapi/karrio-python",
    keywords=["Karrio", "Multi-carrier API", "Shipping API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
