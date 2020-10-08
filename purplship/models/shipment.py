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

class Shipment(object):
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
        'id': 'str',
        'status': 'str',
        'carrier_name': 'str',
        'carrier_id': 'str',
        'label': 'str',
        'tracking_number': 'str',
        'selected_rate': 'Rate',
        'selected_rate_id': 'str',
        'rates': 'list[Rate]',
        'tracking_url': 'str',
        'shipper': 'Address',
        'recipient': 'Address',
        'parcels': 'list[Parcel]',
        'services': 'list[str]',
        'options': 'object',
        'payment': 'Payment',
        'customs': 'Customs',
        'doc_images': 'list[Doc]',
        'reference': 'str',
        'carrier_ids': 'list[str]',
        'meta': 'object'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'carrier_name': 'carrierName',
        'carrier_id': 'carrierId',
        'label': 'label',
        'tracking_number': 'trackingNumber',
        'selected_rate': 'selectedRate',
        'selected_rate_id': 'selectedRateId',
        'rates': 'rates',
        'tracking_url': 'trackingUrl',
        'shipper': 'shipper',
        'recipient': 'recipient',
        'parcels': 'parcels',
        'services': 'services',
        'options': 'options',
        'payment': 'payment',
        'customs': 'customs',
        'doc_images': 'docImages',
        'reference': 'reference',
        'carrier_ids': 'carrierIds',
        'meta': 'meta'
    }

    def __init__(self, id=None, status='created', carrier_name=None, carrier_id=None, label=None, tracking_number=None, selected_rate=None, selected_rate_id=None, rates=None, tracking_url=None, shipper=None, recipient=None, parcels=None, services=None, options=None, payment=None, customs=None, doc_images=None, reference=None, carrier_ids=None, meta=None):  # noqa: E501
        """Shipment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._carrier_name = None
        self._carrier_id = None
        self._label = None
        self._tracking_number = None
        self._selected_rate = None
        self._selected_rate_id = None
        self._rates = None
        self._tracking_url = None
        self._shipper = None
        self._recipient = None
        self._parcels = None
        self._services = None
        self._options = None
        self._payment = None
        self._customs = None
        self._doc_images = None
        self._reference = None
        self._carrier_ids = None
        self._meta = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if label is not None:
            self.label = label
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if selected_rate is not None:
            self.selected_rate = selected_rate
        if selected_rate_id is not None:
            self.selected_rate_id = selected_rate_id
        if rates is not None:
            self.rates = rates
        if tracking_url is not None:
            self.tracking_url = tracking_url
        self.shipper = shipper
        self.recipient = recipient
        self.parcels = parcels
        if services is not None:
            self.services = services
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
        if carrier_ids is not None:
            self.carrier_ids = carrier_ids
        if meta is not None:
            self.meta = meta

    @property
    def id(self):
        """Gets the id of this Shipment.  # noqa: E501

        A unique identifier  # noqa: E501

        :return: The id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Shipment.

        A unique identifier  # noqa: E501

        :param id: The id of this Shipment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this Shipment.  # noqa: E501

        The current Shipment status  # noqa: E501

        :return: The status of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Shipment.

        The current Shipment status  # noqa: E501

        :param status: The status of this Shipment.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "cancelled", "purchased"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def carrier_name(self):
        """Gets the carrier_name of this Shipment.  # noqa: E501

        The shipment carrier  # noqa: E501

        :return: The carrier_name of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this Shipment.

        The shipment carrier  # noqa: E501

        :param carrier_name: The carrier_name of this Shipment.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def carrier_id(self):
        """Gets the carrier_id of this Shipment.  # noqa: E501

        The shipment carrier configured identifier  # noqa: E501

        :return: The carrier_id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this Shipment.

        The shipment carrier configured identifier  # noqa: E501

        :param carrier_id: The carrier_id of this Shipment.  # noqa: E501
        :type: str
        """

        self._carrier_id = carrier_id

    @property
    def label(self):
        """Gets the label of this Shipment.  # noqa: E501

        The shipment label in base64 string  # noqa: E501

        :return: The label of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Shipment.

        The shipment label in base64 string  # noqa: E501

        :param label: The label of this Shipment.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def tracking_number(self):
        """Gets the tracking_number of this Shipment.  # noqa: E501

        The shipment tracking number  # noqa: E501

        :return: The tracking_number of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this Shipment.

        The shipment tracking number  # noqa: E501

        :param tracking_number: The tracking_number of this Shipment.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def selected_rate(self):
        """Gets the selected_rate of this Shipment.  # noqa: E501


        :return: The selected_rate of this Shipment.  # noqa: E501
        :rtype: Rate
        """
        return self._selected_rate

    @selected_rate.setter
    def selected_rate(self, selected_rate):
        """Sets the selected_rate of this Shipment.


        :param selected_rate: The selected_rate of this Shipment.  # noqa: E501
        :type: Rate
        """

        self._selected_rate = selected_rate

    @property
    def selected_rate_id(self):
        """Gets the selected_rate_id of this Shipment.  # noqa: E501

        The shipment selected rate.  # noqa: E501

        :return: The selected_rate_id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._selected_rate_id

    @selected_rate_id.setter
    def selected_rate_id(self, selected_rate_id):
        """Sets the selected_rate_id of this Shipment.

        The shipment selected rate.  # noqa: E501

        :param selected_rate_id: The selected_rate_id of this Shipment.  # noqa: E501
        :type: str
        """

        self._selected_rate_id = selected_rate_id

    @property
    def rates(self):
        """Gets the rates of this Shipment.  # noqa: E501

        The list for shipment rates fetched previously  # noqa: E501

        :return: The rates of this Shipment.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this Shipment.

        The list for shipment rates fetched previously  # noqa: E501

        :param rates: The rates of this Shipment.  # noqa: E501
        :type: list[Rate]
        """

        self._rates = rates

    @property
    def tracking_url(self):
        """Gets the tracking_url of this Shipment.  # noqa: E501

        The shipment tracking url  # noqa: E501

        :return: The tracking_url of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this Shipment.

        The shipment tracking url  # noqa: E501

        :param tracking_url: The tracking_url of this Shipment.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def shipper(self):
        """Gets the shipper of this Shipment.  # noqa: E501


        :return: The shipper of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """Sets the shipper of this Shipment.


        :param shipper: The shipper of this Shipment.  # noqa: E501
        :type: Address
        """
        if shipper is None:
            raise ValueError("Invalid value for `shipper`, must not be `None`")  # noqa: E501

        self._shipper = shipper

    @property
    def recipient(self):
        """Gets the recipient of this Shipment.  # noqa: E501


        :return: The recipient of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Shipment.


        :param recipient: The recipient of this Shipment.  # noqa: E501
        :type: Address
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def parcels(self):
        """Gets the parcels of this Shipment.  # noqa: E501

        The shipment's parcels  # noqa: E501

        :return: The parcels of this Shipment.  # noqa: E501
        :rtype: list[Parcel]
        """
        return self._parcels

    @parcels.setter
    def parcels(self, parcels):
        """Sets the parcels of this Shipment.

        The shipment's parcels  # noqa: E501

        :param parcels: The parcels of this Shipment.  # noqa: E501
        :type: list[Parcel]
        """
        if parcels is None:
            raise ValueError("Invalid value for `parcels`, must not be `None`")  # noqa: E501

        self._parcels = parcels

    @property
    def services(self):
        """Gets the services of this Shipment.  # noqa: E501

         The requested carrier service for the shipment.  Please consult [the reference](#operation/all_references) for specific carriers services.<br/> Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.   # noqa: E501

        :return: The services of this Shipment.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Shipment.

         The requested carrier service for the shipment.  Please consult [the reference](#operation/all_references) for specific carriers services.<br/> Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.   # noqa: E501

        :param services: The services of this Shipment.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def options(self):
        """Gets the options of this Shipment.  # noqa: E501

         The options available for the shipment.<br/> Please consult [the reference](#operation/all_references) for additional specific carriers options.   # noqa: E501

        :return: The options of this Shipment.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Shipment.

         The options available for the shipment.<br/> Please consult [the reference](#operation/all_references) for additional specific carriers options.   # noqa: E501

        :param options: The options of this Shipment.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def payment(self):
        """Gets the payment of this Shipment.  # noqa: E501


        :return: The payment of this Shipment.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Shipment.


        :param payment: The payment of this Shipment.  # noqa: E501
        :type: Payment
        """

        self._payment = payment

    @property
    def customs(self):
        """Gets the customs of this Shipment.  # noqa: E501


        :return: The customs of this Shipment.  # noqa: E501
        :rtype: Customs
        """
        return self._customs

    @customs.setter
    def customs(self, customs):
        """Sets the customs of this Shipment.


        :param customs: The customs of this Shipment.  # noqa: E501
        :type: Customs
        """

        self._customs = customs

    @property
    def doc_images(self):
        """Gets the doc_images of this Shipment.  # noqa: E501

         The list of documents to attach for a paperless interantional trade.  eg: Invoices...   # noqa: E501

        :return: The doc_images of this Shipment.  # noqa: E501
        :rtype: list[Doc]
        """
        return self._doc_images

    @doc_images.setter
    def doc_images(self, doc_images):
        """Sets the doc_images of this Shipment.

         The list of documents to attach for a paperless interantional trade.  eg: Invoices...   # noqa: E501

        :param doc_images: The doc_images of this Shipment.  # noqa: E501
        :type: list[Doc]
        """

        self._doc_images = doc_images

    @property
    def reference(self):
        """Gets the reference of this Shipment.  # noqa: E501

        The shipment reference  # noqa: E501

        :return: The reference of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Shipment.

        The shipment reference  # noqa: E501

        :param reference: The reference of this Shipment.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def carrier_ids(self):
        """Gets the carrier_ids of this Shipment.  # noqa: E501

         The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*   # noqa: E501

        :return: The carrier_ids of this Shipment.  # noqa: E501
        :rtype: list[str]
        """
        return self._carrier_ids

    @carrier_ids.setter
    def carrier_ids(self, carrier_ids):
        """Sets the carrier_ids of this Shipment.

         The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*   # noqa: E501

        :param carrier_ids: The carrier_ids of this Shipment.  # noqa: E501
        :type: list[str]
        """

        self._carrier_ids = carrier_ids

    @property
    def meta(self):
        """Gets the meta of this Shipment.  # noqa: E501

        provider specific metadata  # noqa: E501

        :return: The meta of this Shipment.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Shipment.

        provider specific metadata  # noqa: E501

        :param meta: The meta of this Shipment.  # noqa: E501
        :type: object
        """

        self._meta = meta

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
        if issubclass(Shipment, dict):
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
        if not isinstance(other, Shipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
