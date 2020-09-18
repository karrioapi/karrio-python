# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
"""


from setuptools import setup, find_packages  # noqa: H301

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "purplship-python"
VERSION = "2020.8.2"

DEV_REQUIRES = [
    "wheel",
    "twine"
]

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="PurplShip Multi-carrier Shipping API Python client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="hello@purplship.com",
    url="https://github.com/PurplShip/purplship-python-client",
    keywords=["PurplShip", "PurplShip Multi-carrier API", "Shipping API"],
    install_requires=REQUIRES,
    extras_require={'dev': DEV_REQUIRES},
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    python_requires='>=3.4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
