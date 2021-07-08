# coding: utf-8

"""
    Purplship API

     ## API Reference  Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Purplship API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded  request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Purplship API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released.  The current version is `2021.6.2`.   Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses,  list shipments, and list trackers. These list API methods share a common structure, taking at least these  two parameters: limit, and offset.  Purplship utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order.  The offset parameter returns objects listed after an index.  The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Purplship API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates,  buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    OpenAPI spec version: 2021.6.2
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CommodityData(object):
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
        'weight': 'float',
        'weight_unit': 'str',
        'description': 'str',
        'quantity': 'int',
        'sku': 'str',
        'value_amount': 'float',
        'value_currency': 'str',
        'origin_country': 'str'
    }

    attribute_map = {
        'weight': 'weight',
        'weight_unit': 'weight_unit',
        'description': 'description',
        'quantity': 'quantity',
        'sku': 'sku',
        'value_amount': 'value_amount',
        'value_currency': 'value_currency',
        'origin_country': 'origin_country'
    }

    def __init__(self, weight=None, weight_unit=None, description=None, quantity=None, sku=None, value_amount=None, value_currency=None, origin_country=None):  # noqa: E501
        """CommodityData - a model defined in Swagger"""  # noqa: E501
        self._weight = None
        self._weight_unit = None
        self._description = None
        self._quantity = None
        self._sku = None
        self._value_amount = None
        self._value_currency = None
        self._origin_country = None
        self.discriminator = None
        self.weight = weight
        self.weight_unit = weight_unit
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if sku is not None:
            self.sku = sku
        if value_amount is not None:
            self.value_amount = value_amount
        if value_currency is not None:
            self.value_currency = value_currency
        if origin_country is not None:
            self.origin_country = origin_country

    @property
    def weight(self):
        """Gets the weight of this CommodityData.  # noqa: E501

        The commodity's weight  # noqa: E501

        :return: The weight of this CommodityData.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CommodityData.

        The commodity's weight  # noqa: E501

        :param weight: The weight of this CommodityData.  # noqa: E501
        :type: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def weight_unit(self):
        """Gets the weight_unit of this CommodityData.  # noqa: E501

        The commodity's weight unit  # noqa: E501

        :return: The weight_unit of this CommodityData.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, weight_unit):
        """Sets the weight_unit of this CommodityData.

        The commodity's weight unit  # noqa: E501

        :param weight_unit: The weight_unit of this CommodityData.  # noqa: E501
        :type: str
        """
        if weight_unit is None:
            raise ValueError("Invalid value for `weight_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["KG", "LB"]  # noqa: E501
        if weight_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_unit, allowed_values)
            )

        self._weight_unit = weight_unit

    @property
    def description(self):
        """Gets the description of this CommodityData.  # noqa: E501

        A description of the commodity  # noqa: E501

        :return: The description of this CommodityData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommodityData.

        A description of the commodity  # noqa: E501

        :param description: The description of this CommodityData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this CommodityData.  # noqa: E501

        The commodity's quantity (number or item)  # noqa: E501

        :return: The quantity of this CommodityData.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CommodityData.

        The commodity's quantity (number or item)  # noqa: E501

        :param quantity: The quantity of this CommodityData.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def sku(self):
        """Gets the sku of this CommodityData.  # noqa: E501

        The commodity's sku number  # noqa: E501

        :return: The sku of this CommodityData.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this CommodityData.

        The commodity's sku number  # noqa: E501

        :param sku: The sku of this CommodityData.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def value_amount(self):
        """Gets the value_amount of this CommodityData.  # noqa: E501

        The monetary value of the commodity  # noqa: E501

        :return: The value_amount of this CommodityData.  # noqa: E501
        :rtype: float
        """
        return self._value_amount

    @value_amount.setter
    def value_amount(self, value_amount):
        """Sets the value_amount of this CommodityData.

        The monetary value of the commodity  # noqa: E501

        :param value_amount: The value_amount of this CommodityData.  # noqa: E501
        :type: float
        """

        self._value_amount = value_amount

    @property
    def value_currency(self):
        """Gets the value_currency of this CommodityData.  # noqa: E501

        The currency of the commodity value amount  # noqa: E501

        :return: The value_currency of this CommodityData.  # noqa: E501
        :rtype: str
        """
        return self._value_currency

    @value_currency.setter
    def value_currency(self, value_currency):
        """Sets the value_currency of this CommodityData.

        The currency of the commodity value amount  # noqa: E501

        :param value_currency: The value_currency of this CommodityData.  # noqa: E501
        :type: str
        """

        self._value_currency = value_currency

    @property
    def origin_country(self):
        """Gets the origin_country of this CommodityData.  # noqa: E501

        The origin or manufacture country  # noqa: E501

        :return: The origin_country of this CommodityData.  # noqa: E501
        :rtype: str
        """
        return self._origin_country

    @origin_country.setter
    def origin_country(self, origin_country):
        """Sets the origin_country of this CommodityData.

        The origin or manufacture country  # noqa: E501

        :param origin_country: The origin_country of this CommodityData.  # noqa: E501
        :type: str
        """

        self._origin_country = origin_country

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
        if issubclass(CommodityData, dict):
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
        if not isinstance(other, CommodityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other