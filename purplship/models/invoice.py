# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.8.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Invoice(object):
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
        '_date': 'str',
        'identifier': 'str',
        'type': 'str',
        'copies': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'identifier': 'identifier',
        'type': 'type',
        'copies': 'copies'
    }

    def __init__(self, _date=None, identifier=None, type=None, copies=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._identifier = None
        self._type = None
        self._copies = None
        self.discriminator = None

        self._date = _date
        if identifier is not None:
            self.identifier = identifier
        if type is not None:
            self.type = type
        if copies is not None:
            self.copies = copies

    @property
    def _date(self):
        """Gets the _date of this Invoice.  # noqa: E501

        The invoice date  # noqa: E501

        :return: The _date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Invoice.

        The invoice date  # noqa: E501

        :param _date: The _date of this Invoice.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501
        if _date is not None and len(_date) < 1:
            raise ValueError("Invalid value for `_date`, length must be greater than or equal to `1`")  # noqa: E501

        self.__date = _date

    @property
    def identifier(self):
        """Gets the identifier of this Invoice.  # noqa: E501

        The internal invoice document identifier  # noqa: E501

        :return: The identifier of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Invoice.

        The internal invoice document identifier  # noqa: E501

        :param identifier: The identifier of this Invoice.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def type(self):
        """Gets the type of this Invoice.  # noqa: E501

        The invoice type  # noqa: E501

        :return: The type of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Invoice.

        The invoice type  # noqa: E501

        :param type: The type of this Invoice.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def copies(self):
        """Gets the copies of this Invoice.  # noqa: E501

        The number of invoice copies  # noqa: E501

        :return: The copies of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._copies

    @copies.setter
    def copies(self, copies):
        """Sets the copies of this Invoice.

        The number of invoice copies  # noqa: E501

        :param copies: The copies of this Invoice.  # noqa: E501
        :type: int
        """

        self._copies = copies

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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
