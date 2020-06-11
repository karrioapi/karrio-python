# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
    Generated by: https://github.com/purplship-api/purplship-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Message(object):
    """NOTE: This class is auto generated by the purplship code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      purplship_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    purplship_types = {
        'carrier_name': 'str',
        'carrier_id': 'str',
        'message': 'str',
        'code': 'str',
        'details': 'dict(str, str)'
    }

    attribute_map = {
        'carrier_name': 'carrierName',
        'carrier_id': 'carrierId',
        'message': 'message',
        'code': 'code',
        'details': 'details'
    }

    def __init__(self, carrier_name=None, carrier_id=None, message=None, code=None, details=None):  # noqa: E501
        """Message - a model defined in PurplShip"""  # noqa: E501

        self._carrier_name = None
        self._carrier_id = None
        self._message = None
        self._code = None
        self._details = None
        self.discriminator = None

        self.carrier_name = carrier_name
        self.carrier_id = carrier_id
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details

    @property
    def carrier_name(self):
        """Gets the carrier_name of this Message.  # noqa: E501

        The targeted carrier  # noqa: E501

        :return: The carrier_name of this Message.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this Message.

        The targeted carrier  # noqa: E501

        :param carrier_name: The carrier_name of this Message.  # noqa: E501
        :type: str
        """
        if carrier_name is None:
            raise ValueError("Invalid value for `carrier_name`, must not be `None`")  # noqa: E501
        if carrier_name is not None and len(carrier_name) < 1:
            raise ValueError("Invalid value for `carrier_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._carrier_name = carrier_name

    @property
    def carrier_id(self):
        """Gets the carrier_id of this Message.  # noqa: E501

        The targeted carrier name (unique identifier)  # noqa: E501

        :return: The carrier_id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this Message.

        The targeted carrier name (unique identifier)  # noqa: E501

        :param carrier_id: The carrier_id of this Message.  # noqa: E501
        :type: str
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501
        if carrier_id is not None and len(carrier_id) < 1:
            raise ValueError("Invalid value for `carrier_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._carrier_id = carrier_id

    @property
    def message(self):
        """Gets the message of this Message.  # noqa: E501

        The error or warning message  # noqa: E501

        :return: The message of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Message.

        The error or warning message  # noqa: E501

        :param message: The message of this Message.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) < 1:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def code(self):
        """Gets the code of this Message.  # noqa: E501

        The message code  # noqa: E501

        :return: The code of this Message.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Message.

        The message code  # noqa: E501

        :param code: The code of this Message.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def details(self):
        """Gets the details of this Message.  # noqa: E501

        any additional details  # noqa: E501

        :return: The details of this Message.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Message.

        any additional details  # noqa: E501

        :param details: The details of this Message.  # noqa: E501
        :type: dict(str, str)
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.purplship_types):
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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
