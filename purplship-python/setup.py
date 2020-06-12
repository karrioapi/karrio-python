# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "purplship-python"
VERSION = "2020.6.2"

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
    author_email="hello@purplship.com",
    url="https://github.com/PurplShip/purplship-clients",
    keywords=["PurplShip", "PurplShip Multi-carrier API", "Shipping API"],
    install_requires=REQUIRES,
    packages=find_packages(".", exclude=["tests*"]),
    include_package_data=True,
    long_description="""\
    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501
    """
)
