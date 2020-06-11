# coding: utf-8

# flake8: noqa

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
"""


from __future__ import absolute_import

# import apis into sdk package
import purplship.api as resources

# import ApiClient
from purplship.client import ApiClient
from purplship.configuration import Configuration

# import models into sdk package
from purplship.models import *


api_key = None
host = None
api_client = None

configuration = Configuration()


def init_client():
    same_api_key = api_key == configuration.api_key['Authorization']
    same_host = host == configuration.host
    
    if same_api_key and same_host and api_client is not None:
        return api_client

    configuration.host = host
    configuration.api_key['Authorization'] = api_key
    return ApiClient(configuration)


class Carriers:

    @staticmethod
    def retrieve(*args, **kwargs):
        resources.Carriers(init_client()).retrieve(*args, **kwargs)


class Rates:

    @staticmethod
    def fetch(*args, **kwargs):
        resources.Rates(init_client()).fetch(*args, **kwargs)


class Shipments:

    @staticmethod
    def create(*args, **kwargs):
        resources.Shipments(init_client()).create(*args, **kwargs)


class Tracking:

    @staticmethod
    def retrieve(*args, **kwargs):
        resources.Tracking(init_client()).retrieve(*args, **kwargs)


class Utils:

    @staticmethod
    def get_reference(*args, **kwargs):
        resources.Utils(init_client()).get_reference(*args, **kwargs)

    @staticmethod
    def print_label(*args, **kwargs):
        resources.Utils(init_client()).print_label(*args, **kwargs)
