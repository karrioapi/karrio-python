# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.9.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShipmentData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'shipper': 'AddressData',
        'recipient': 'AddressData',
        'parcels': 'list[ParcelData]',
        'options': 'object',
        'payment': 'PaymentData',
        'customs': 'CustomsData',
        'doc_images': 'list[Doc]',
        'reference': 'str',
        'services': 'list[str]',
        'carrier_ids': 'list[str]'
    }

    attribute_map = {
        'shipper': 'shipper',
        'recipient': 'recipient',
        'parcels': 'parcels',
        'options': 'options',
        'payment': 'payment',
        'customs': 'customs',
        'doc_images': 'docImages',
        'reference': 'reference',
        'services': 'services',
        'carrier_ids': 'carrierIds'
    }

    def __init__(self, shipper=None, recipient=None, parcels=None, options=None, payment=None, customs=None, doc_images=None, reference=None, services=None, carrier_ids=None):  # noqa: E501
        """ShipmentData - a model defined in Swagger"""  # noqa: E501
        self._shipper = None
        self._recipient = None
        self._parcels = None
        self._options = None
        self._payment = None
        self._customs = None
        self._doc_images = None
        self._reference = None
        self._services = None
        self._carrier_ids = None
        self.discriminator = None
        self.shipper = shipper
        self.recipient = recipient
        self.parcels = parcels
        if options is not None:
            self.options = options
        if payment is not None:
            self.payment = payment
        if customs is not None:
            self.customs = customs
        if doc_images is not None:
            self.doc_images = doc_images
        if reference is not None:
            self.reference = reference
        if services is not None:
            self.services = services
        if carrier_ids is not None:
            self.carrier_ids = carrier_ids

    @property
    def shipper(self):
        """Gets the shipper of this ShipmentData.  # noqa: E501


        :return: The shipper of this ShipmentData.  # noqa: E501
        :rtype: AddressData
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """Sets the shipper of this ShipmentData.


        :param shipper: The shipper of this ShipmentData.  # noqa: E501
        :type: AddressData
        """
        if shipper is None:
            raise ValueError("Invalid value for `shipper`, must not be `None`")  # noqa: E501

        self._shipper = shipper

    @property
    def recipient(self):
        """Gets the recipient of this ShipmentData.  # noqa: E501


        :return: The recipient of this ShipmentData.  # noqa: E501
        :rtype: AddressData
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this ShipmentData.


        :param recipient: The recipient of this ShipmentData.  # noqa: E501
        :type: AddressData
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def parcels(self):
        """Gets the parcels of this ShipmentData.  # noqa: E501

        The shipment's parcels  # noqa: E501

        :return: The parcels of this ShipmentData.  # noqa: E501
        :rtype: list[ParcelData]
        """
        return self._parcels

    @parcels.setter
    def parcels(self, parcels):
        """Sets the parcels of this ShipmentData.

        The shipment's parcels  # noqa: E501

        :param parcels: The parcels of this ShipmentData.  # noqa: E501
        :type: list[ParcelData]
        """
        if parcels is None:
            raise ValueError("Invalid value for `parcels`, must not be `None`")  # noqa: E501

        self._parcels = parcels

    @property
    def options(self):
        """Gets the options of this ShipmentData.  # noqa: E501

         The options available for the shipment.<br/> Please consult [the reference](#operation/all_references) for additional specific carriers options.   # noqa: E501

        :return: The options of this ShipmentData.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ShipmentData.

         The options available for the shipment.<br/> Please consult [the reference](#operation/all_references) for additional specific carriers options.   # noqa: E501

        :param options: The options of this ShipmentData.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def payment(self):
        """Gets the payment of this ShipmentData.  # noqa: E501


        :return: The payment of this ShipmentData.  # noqa: E501
        :rtype: PaymentData
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ShipmentData.


        :param payment: The payment of this ShipmentData.  # noqa: E501
        :type: PaymentData
        """

        self._payment = payment

    @property
    def customs(self):
        """Gets the customs of this ShipmentData.  # noqa: E501


        :return: The customs of this ShipmentData.  # noqa: E501
        :rtype: CustomsData
        """
        return self._customs

    @customs.setter
    def customs(self, customs):
        """Sets the customs of this ShipmentData.


        :param customs: The customs of this ShipmentData.  # noqa: E501
        :type: CustomsData
        """

        self._customs = customs

    @property
    def doc_images(self):
        """Gets the doc_images of this ShipmentData.  # noqa: E501

         The list of documents to attach for a paperless interantional trade.  eg: Invoices...   # noqa: E501

        :return: The doc_images of this ShipmentData.  # noqa: E501
        :rtype: list[Doc]
        """
        return self._doc_images

    @doc_images.setter
    def doc_images(self, doc_images):
        """Sets the doc_images of this ShipmentData.

         The list of documents to attach for a paperless interantional trade.  eg: Invoices...   # noqa: E501

        :param doc_images: The doc_images of this ShipmentData.  # noqa: E501
        :type: list[Doc]
        """

        self._doc_images = doc_images

    @property
    def reference(self):
        """Gets the reference of this ShipmentData.  # noqa: E501

        The shipment reference  # noqa: E501

        :return: The reference of this ShipmentData.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ShipmentData.

        The shipment reference  # noqa: E501

        :param reference: The reference of this ShipmentData.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def services(self):
        """Gets the services of this ShipmentData.  # noqa: E501

         The requested carrier service for the shipment.  Please consult [the reference](#operation/all_references) for specific carriers services.<br/> Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.   # noqa: E501

        :return: The services of this ShipmentData.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ShipmentData.

         The requested carrier service for the shipment.  Please consult [the reference](#operation/all_references) for specific carriers services.<br/> Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.   # noqa: E501

        :param services: The services of this ShipmentData.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def carrier_ids(self):
        """Gets the carrier_ids of this ShipmentData.  # noqa: E501

         The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*   # noqa: E501

        :return: The carrier_ids of this ShipmentData.  # noqa: E501
        :rtype: list[str]
        """
        return self._carrier_ids

    @carrier_ids.setter
    def carrier_ids(self, carrier_ids):
        """Sets the carrier_ids of this ShipmentData.

         The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*   # noqa: E501

        :param carrier_ids: The carrier_ids of this ShipmentData.  # noqa: E501
        :type: list[str]
        """

        self._carrier_ids = carrier_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ShipmentData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShipmentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
