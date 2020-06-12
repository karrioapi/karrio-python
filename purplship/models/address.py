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


class Address(object):
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
        'id': 'str',
        'postal_code': 'str',
        'city': 'str',
        'federal_tax_id': 'str',
        'state_tax_id': 'str',
        'person_name': 'str',
        'company_name': 'str',
        'country_code': 'str',
        'email': 'str',
        'phone_number': 'str',
        'state_code': 'str',
        'suburb': 'str',
        'residential': 'bool',
        'address_line1': 'str',
        'address_line2': 'str'
    }

    attribute_map = {
        'id': 'id',
        'postal_code': 'postalCode',
        'city': 'city',
        'federal_tax_id': 'federalTaxId',
        'state_tax_id': 'stateTaxId',
        'person_name': 'personName',
        'company_name': 'companyName',
        'country_code': 'countryCode',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'state_code': 'stateCode',
        'suburb': 'suburb',
        'residential': 'residential',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2'
    }

    def __init__(self, id=None, postal_code=None, city=None, federal_tax_id=None, state_tax_id=None, person_name=None, company_name=None, country_code=None, email=None, phone_number=None, state_code=None, suburb=None, residential=None, address_line1=None, address_line2=None):  # noqa: E501
        """Address - a model defined in PurplShip"""  # noqa: E501

        self._id = None
        self._postal_code = None
        self._city = None
        self._federal_tax_id = None
        self._state_tax_id = None
        self._person_name = None
        self._company_name = None
        self._country_code = None
        self._email = None
        self._phone_number = None
        self._state_code = None
        self._suburb = None
        self._residential = None
        self._address_line1 = None
        self._address_line2 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if federal_tax_id is not None:
            self.federal_tax_id = federal_tax_id
        if state_tax_id is not None:
            self.state_tax_id = state_tax_id
        if person_name is not None:
            self.person_name = person_name
        if company_name is not None:
            self.company_name = company_name
        self.country_code = country_code
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if state_code is not None:
            self.state_code = state_code
        if suburb is not None:
            self.suburb = suburb
        if residential is not None:
            self.residential = residential
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        A unique address identifier  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        A unique address identifier  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The address postal code  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The address postal code  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) < 1:
            raise ValueError("Invalid value for `postal_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

         The address city. <br/> **(required to create as shipment)**   # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

         The address city. <br/> **(required to create as shipment)**   # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) < 1:
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `1`")  # noqa: E501

        self._city = city

    @property
    def federal_tax_id(self):
        """Gets the federal_tax_id of this Address.  # noqa: E501

        The party frederal tax id  # noqa: E501

        :return: The federal_tax_id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._federal_tax_id

    @federal_tax_id.setter
    def federal_tax_id(self, federal_tax_id):
        """Sets the federal_tax_id of this Address.

        The party frederal tax id  # noqa: E501

        :param federal_tax_id: The federal_tax_id of this Address.  # noqa: E501
        :type: str
        """
        if federal_tax_id is not None and len(federal_tax_id) < 1:
            raise ValueError("Invalid value for `federal_tax_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._federal_tax_id = federal_tax_id

    @property
    def state_tax_id(self):
        """Gets the state_tax_id of this Address.  # noqa: E501

        The party state id  # noqa: E501

        :return: The state_tax_id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state_tax_id

    @state_tax_id.setter
    def state_tax_id(self, state_tax_id):
        """Sets the state_tax_id of this Address.

        The party state id  # noqa: E501

        :param state_tax_id: The state_tax_id of this Address.  # noqa: E501
        :type: str
        """
        if state_tax_id is not None and len(state_tax_id) < 1:
            raise ValueError("Invalid value for `state_tax_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._state_tax_id = state_tax_id

    @property
    def person_name(self):
        """Gets the person_name of this Address.  # noqa: E501

         attention to <br/> **(required to create as shipment)**   # noqa: E501

        :return: The person_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._person_name

    @person_name.setter
    def person_name(self, person_name):
        """Sets the person_name of this Address.

         attention to <br/> **(required to create as shipment)**   # noqa: E501

        :param person_name: The person_name of this Address.  # noqa: E501
        :type: str
        """
        if person_name is not None and len(person_name) < 1:
            raise ValueError("Invalid value for `person_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._person_name = person_name

    @property
    def company_name(self):
        """Gets the company_name of this Address.  # noqa: E501

        The company name if the party is a company  # noqa: E501

        :return: The company_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Address.

        The company name if the party is a company  # noqa: E501

        :param company_name: The company_name of this Address.  # noqa: E501
        :type: str
        """
        if company_name is not None and len(company_name) < 1:
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._company_name = company_name

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        The address country code  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        The address country code  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        allowed_values = ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AR", "AS", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GT", "GU", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KV", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PR", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SY", "SZ", "TC", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WS", "XB", "XC", "XE", "XM", "XN", "XS", "XY", "YE", "YT", "ZA", "ZM", "ZW"]  # noqa: E501
        if country_code not in allowed_values:
            raise ValueError(
                "Invalid value for `country_code` ({0}), must be one of {1}"  # noqa: E501
                .format(country_code, allowed_values)
            )

        self._country_code = country_code

    @property
    def email(self):
        """Gets the email of this Address.  # noqa: E501

        The party email  # noqa: E501

        :return: The email of this Address.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Address.

        The party email  # noqa: E501

        :param email: The email of this Address.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this Address.  # noqa: E501

         The party phone number.<br/> Note that the expected format is: **1 514 0000000**  Country Code | Area Code | Phone --- | --- | --- 1 | 514 | 0000000   # noqa: E501

        :return: The phone_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Address.

         The party phone number.<br/> Note that the expected format is: **1 514 0000000**  Country Code | Area Code | Phone --- | --- | --- 1 | 514 | 0000000   # noqa: E501

        :param phone_number: The phone_number of this Address.  # noqa: E501
        :type: str
        """
        if phone_number is not None and len(phone_number) < 1:
            raise ValueError("Invalid value for `phone_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def state_code(self):
        """Gets the state_code of this Address.  # noqa: E501

        The address state code  # noqa: E501

        :return: The state_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this Address.

        The address state code  # noqa: E501

        :param state_code: The state_code of this Address.  # noqa: E501
        :type: str
        """
        if state_code is not None and len(state_code) < 1:
            raise ValueError("Invalid value for `state_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._state_code = state_code

    @property
    def suburb(self):
        """Gets the suburb of this Address.  # noqa: E501

        The address suburb if known  # noqa: E501

        :return: The suburb of this Address.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this Address.

        The address suburb if known  # noqa: E501

        :param suburb: The suburb of this Address.  # noqa: E501
        :type: str
        """
        if suburb is not None and len(suburb) < 1:
            raise ValueError("Invalid value for `suburb`, length must be greater than or equal to `1`")  # noqa: E501

        self._suburb = suburb

    @property
    def residential(self):
        """Gets the residential of this Address.  # noqa: E501

        Indicate if the address is residential or commercial (enterprise)  # noqa: E501

        :return: The residential of this Address.  # noqa: E501
        :rtype: bool
        """
        return self._residential

    @residential.setter
    def residential(self, residential):
        """Sets the residential of this Address.

        Indicate if the address is residential or commercial (enterprise)  # noqa: E501

        :param residential: The residential of this Address.  # noqa: E501
        :type: bool
        """

        self._residential = residential

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

         The address line with street number <br/> **(required to create as shipment)**   # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

         The address line with street number <br/> **(required to create as shipment)**   # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """
        if address_line1 is not None and len(address_line1) < 1:
            raise ValueError("Invalid value for `address_line1`, length must be greater than or equal to `1`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        The address line with suite number  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        The address line with suite number  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """
        if address_line2 is not None and len(address_line2) < 1:
            raise ValueError("Invalid value for `address_line2`, length must be greater than or equal to `1`")  # noqa: E501

        self._address_line2 = address_line2

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other