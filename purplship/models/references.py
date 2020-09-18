# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.8.2
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class References(object):
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
        'countries': 'list[str]',
        'currencies': 'list[str]',
        'states': 'object',
        'services': 'object',
        'options': 'object',
        'package_presets': 'object',
        'packaging_types': 'object'
    }

    attribute_map = {
        'countries': 'countries',
        'currencies': 'currencies',
        'states': 'states',
        'services': 'services',
        'options': 'options',
        'package_presets': 'packagePresets',
        'packaging_types': 'packagingTypes'
    }

    def __init__(self, countries=None, currencies=None, states=None, services=None, options=None, package_presets=None, packaging_types=None):  # noqa: E501
        """References - a model defined in Swagger"""  # noqa: E501

        self._countries = None
        self._currencies = None
        self._states = None
        self._services = None
        self._options = None
        self._package_presets = None
        self._packaging_types = None
        self.discriminator = None

        self.countries = countries
        self.currencies = currencies
        self.states = states
        self.services = services
        self.options = options
        self.package_presets = package_presets
        self.packaging_types = packaging_types

    @property
    def countries(self):
        """Gets the countries of this References.  # noqa: E501


        :return: The countries of this References.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this References.


        :param countries: The countries of this References.  # noqa: E501
        :type: list[str]
        """
        if countries is None:
            raise ValueError("Invalid value for `countries`, must not be `None`")  # noqa: E501

        self._countries = countries

    @property
    def currencies(self):
        """Gets the currencies of this References.  # noqa: E501


        :return: The currencies of this References.  # noqa: E501
        :rtype: list[str]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this References.


        :param currencies: The currencies of this References.  # noqa: E501
        :type: list[str]
        """
        if currencies is None:
            raise ValueError("Invalid value for `currencies`, must not be `None`")  # noqa: E501

        self._currencies = currencies

    @property
    def states(self):
        """Gets the states of this References.  # noqa: E501


        :return: The states of this References.  # noqa: E501
        :rtype: object
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this References.


        :param states: The states of this References.  # noqa: E501
        :type: object
        """
        if states is None:
            raise ValueError("Invalid value for `states`, must not be `None`")  # noqa: E501

        self._states = states

    @property
    def services(self):
        """Gets the services of this References.  # noqa: E501


        :return: The services of this References.  # noqa: E501
        :rtype: object
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this References.


        :param services: The services of this References.  # noqa: E501
        :type: object
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

        self._services = services

    @property
    def options(self):
        """Gets the options of this References.  # noqa: E501


        :return: The options of this References.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this References.


        :param options: The options of this References.  # noqa: E501
        :type: object
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def package_presets(self):
        """Gets the package_presets of this References.  # noqa: E501


        :return: The package_presets of this References.  # noqa: E501
        :rtype: object
        """
        return self._package_presets

    @package_presets.setter
    def package_presets(self, package_presets):
        """Sets the package_presets of this References.


        :param package_presets: The package_presets of this References.  # noqa: E501
        :type: object
        """
        if package_presets is None:
            raise ValueError("Invalid value for `package_presets`, must not be `None`")  # noqa: E501

        self._package_presets = package_presets

    @property
    def packaging_types(self):
        """Gets the packaging_types of this References.  # noqa: E501


        :return: The packaging_types of this References.  # noqa: E501
        :rtype: object
        """
        return self._packaging_types

    @packaging_types.setter
    def packaging_types(self, packaging_types):
        """Sets the packaging_types of this References.


        :param packaging_types: The packaging_types of this References.  # noqa: E501
        :type: object
        """
        if packaging_types is None:
            raise ValueError("Invalid value for `packaging_types`, must not be `None`")  # noqa: E501

        self._packaging_types = packaging_types

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
        if issubclass(References, dict):
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
        if not isinstance(other, References):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
