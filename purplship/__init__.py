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
from purplship.models.address import Address
from purplship.models.card import Card
from purplship.models.carrier_settings import CarrierSettings
from purplship.models.charge import Charge
from purplship.models.commodity import Commodity
from purplship.models.customs import Customs
from purplship.models.doc import Doc
from purplship.models.invoice import Invoice
from purplship.models.label_printing_request import LabelPrintingRequest
from purplship.models.message import Message
from purplship.models.options import Options
from purplship.models.parcel import Parcel
from purplship.models.payment import Payment
from purplship.models.rate_request import RateRequest
from purplship.models.references import References
from purplship.models.shipment_request import ShipmentRequest


api_key = None
api_key_prefix = 'Token'
host = None
api_client = None

configuration = Configuration()


def init_client():
    global api_client
    if (api_client is not None) and (host == configuration.host) and (api_key == configuration.api_key['Authorization']):
        return api_client

    configuration.host = host
    configuration.api_key['Authorization'] = f'{api_key_prefix} {api_key}'
    api_client = ApiClient(configuration)
    return api_client


class Carriers:

    @staticmethod
    def list(*args, **kwargs):
        return resources.Carriers(init_client()).list(*args, **kwargs)

    @staticmethod
    def retrieve(*args, **kwargs):
        return resources.Carriers(init_client()).retrieve(*args, **kwargs)


class Rate:

    @staticmethod
    def fetch(*args, **kwargs):
        return resources.Rate(init_client()).fetch(*args, **kwargs)


class Shipment:

    @staticmethod
    def create(*args, **kwargs):
        return resources.Shipment(init_client()).create(*args, **kwargs)


class Tracking:

    @staticmethod
    def fetch(*args, **kwargs):
        return resources.Tracking(init_client()).fetch(*args, **kwargs)


class Utils:

    @staticmethod
    def references(*args, **kwargs):
        return resources.Utils(init_client()).references(*args, **kwargs)

    @staticmethod
    def print_label(*args, **kwargs):
        return resources.Utils(init_client()).print_label(*args, **kwargs)
