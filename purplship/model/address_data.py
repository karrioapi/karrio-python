"""
    Purplship API

     ## API Reference  Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Purplship API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded  request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Purplship API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released.  The current version is `2021.10`.   Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses,  list shipments, and list trackers. These list API methods share a common structure, taking at least these  two parameters: limit, and offset.  Purplship utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order.  The offset parameter returns objects listed after an index.  The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Purplship API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates,  buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    The version of the OpenAPI document: 2021.10
    Contact: hello@purplship.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from purplship.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from purplship.exceptions import ApiAttributeError



class AddressData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('country_code',): {
            'AD': "AD",
            'AE': "AE",
            'AF': "AF",
            'AG': "AG",
            'AI': "AI",
            'AL': "AL",
            'AM': "AM",
            'AN': "AN",
            'AO': "AO",
            'AR': "AR",
            'AS': "AS",
            'AT': "AT",
            'AU': "AU",
            'AW': "AW",
            'AZ': "AZ",
            'BA': "BA",
            'BB': "BB",
            'BD': "BD",
            'BE': "BE",
            'BF': "BF",
            'BG': "BG",
            'BH': "BH",
            'BI': "BI",
            'BJ': "BJ",
            'BM': "BM",
            'BN': "BN",
            'BO': "BO",
            'BR': "BR",
            'BS': "BS",
            'BT': "BT",
            'BW': "BW",
            'BY': "BY",
            'BZ': "BZ",
            'CA': "CA",
            'CD': "CD",
            'CF': "CF",
            'CG': "CG",
            'CH': "CH",
            'CI': "CI",
            'CK': "CK",
            'CL': "CL",
            'CM': "CM",
            'CN': "CN",
            'CO': "CO",
            'CR': "CR",
            'CU': "CU",
            'CV': "CV",
            'CY': "CY",
            'CZ': "CZ",
            'DE': "DE",
            'DJ': "DJ",
            'DK': "DK",
            'DM': "DM",
            'DO': "DO",
            'DZ': "DZ",
            'EC': "EC",
            'EE': "EE",
            'EG': "EG",
            'ER': "ER",
            'ES': "ES",
            'ET': "ET",
            'FI': "FI",
            'FJ': "FJ",
            'FK': "FK",
            'FM': "FM",
            'FO': "FO",
            'FR': "FR",
            'GA': "GA",
            'GB': "GB",
            'GD': "GD",
            'GE': "GE",
            'GF': "GF",
            'GG': "GG",
            'GH': "GH",
            'GI': "GI",
            'GL': "GL",
            'GM': "GM",
            'GN': "GN",
            'GP': "GP",
            'GQ': "GQ",
            'GR': "GR",
            'GT': "GT",
            'GU': "GU",
            'GW': "GW",
            'GY': "GY",
            'HK': "HK",
            'HN': "HN",
            'HR': "HR",
            'HT': "HT",
            'HU': "HU",
            'IC': "IC",
            'ID': "ID",
            'IE': "IE",
            'IL': "IL",
            'IN': "IN",
            'IQ': "IQ",
            'IR': "IR",
            'IS': "IS",
            'IT': "IT",
            'JE': "JE",
            'JM': "JM",
            'JO': "JO",
            'JP': "JP",
            'KE': "KE",
            'KG': "KG",
            'KH': "KH",
            'KI': "KI",
            'KM': "KM",
            'KN': "KN",
            'KP': "KP",
            'KR': "KR",
            'KV': "KV",
            'KW': "KW",
            'KY': "KY",
            'KZ': "KZ",
            'LA': "LA",
            'LB': "LB",
            'LC': "LC",
            'LI': "LI",
            'LK': "LK",
            'LR': "LR",
            'LS': "LS",
            'LT': "LT",
            'LU': "LU",
            'LV': "LV",
            'LY': "LY",
            'MA': "MA",
            'MC': "MC",
            'MD': "MD",
            'ME': "ME",
            'MG': "MG",
            'MH': "MH",
            'MK': "MK",
            'ML': "ML",
            'MM': "MM",
            'MN': "MN",
            'MO': "MO",
            'MP': "MP",
            'MQ': "MQ",
            'MR': "MR",
            'MS': "MS",
            'MT': "MT",
            'MU': "MU",
            'MV': "MV",
            'MW': "MW",
            'MX': "MX",
            'MY': "MY",
            'MZ': "MZ",
            'NA': "NA",
            'NC': "NC",
            'NE': "NE",
            'NG': "NG",
            'NI': "NI",
            'NL': "NL",
            'NO': "NO",
            'NP': "NP",
            'NR': "NR",
            'NU': "NU",
            'NZ': "NZ",
            'OM': "OM",
            'PA': "PA",
            'PE': "PE",
            'PF': "PF",
            'PG': "PG",
            'PH': "PH",
            'PK': "PK",
            'PL': "PL",
            'PR': "PR",
            'PT': "PT",
            'PW': "PW",
            'PY': "PY",
            'QA': "QA",
            'RE': "RE",
            'RO': "RO",
            'RS': "RS",
            'RU': "RU",
            'RW': "RW",
            'SA': "SA",
            'SB': "SB",
            'SC': "SC",
            'SD': "SD",
            'SE': "SE",
            'SG': "SG",
            'SH': "SH",
            'SI': "SI",
            'SK': "SK",
            'SL': "SL",
            'SM': "SM",
            'SN': "SN",
            'SO': "SO",
            'SR': "SR",
            'SS': "SS",
            'ST': "ST",
            'SV': "SV",
            'SY': "SY",
            'SZ': "SZ",
            'TC': "TC",
            'TD': "TD",
            'TG': "TG",
            'TH': "TH",
            'TJ': "TJ",
            'TL': "TL",
            'TN': "TN",
            'TO': "TO",
            'TR': "TR",
            'TT': "TT",
            'TV': "TV",
            'TW': "TW",
            'TZ': "TZ",
            'UA': "UA",
            'UG': "UG",
            'US': "US",
            'UY': "UY",
            'UZ': "UZ",
            'VA': "VA",
            'VC': "VC",
            'VE': "VE",
            'VG': "VG",
            'VI': "VI",
            'VN': "VN",
            'VU': "VU",
            'WS': "WS",
            'XB': "XB",
            'XC': "XC",
            'XE': "XE",
            'XM': "XM",
            'XN': "XN",
            'XS': "XS",
            'XY': "XY",
            'YE': "YE",
            'YT': "YT",
            'ZA': "ZA",
            'ZM': "ZM",
            'ZW': "ZW",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'country_code': (str,),  # noqa: E501
            'postal_code': (str, none_type,),  # noqa: E501
            'city': (str, none_type,),  # noqa: E501
            'federal_tax_id': (str, none_type,),  # noqa: E501
            'state_tax_id': (str, none_type,),  # noqa: E501
            'person_name': (str, none_type,),  # noqa: E501
            'company_name': (str, none_type,),  # noqa: E501
            'email': (str, none_type,),  # noqa: E501
            'phone_number': (str, none_type,),  # noqa: E501
            'state_code': (str, none_type,),  # noqa: E501
            'suburb': (str, none_type,),  # noqa: E501
            'residential': (bool, none_type,),  # noqa: E501
            'address_line1': (str, none_type,),  # noqa: E501
            'address_line2': (str, none_type,),  # noqa: E501
            'validate_location': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'country_code': 'country_code',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'city': 'city',  # noqa: E501
        'federal_tax_id': 'federal_tax_id',  # noqa: E501
        'state_tax_id': 'state_tax_id',  # noqa: E501
        'person_name': 'person_name',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'email': 'email',  # noqa: E501
        'phone_number': 'phone_number',  # noqa: E501
        'state_code': 'state_code',  # noqa: E501
        'suburb': 'suburb',  # noqa: E501
        'residential': 'residential',  # noqa: E501
        'address_line1': 'address_line1',  # noqa: E501
        'address_line2': 'address_line2',  # noqa: E501
        'validate_location': 'validate_location',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, country_code, *args, **kwargs):  # noqa: E501
        """AddressData - a model defined in OpenAPI

        Args:
            country_code (str): The address country code

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            postal_code (str, none_type):  The address postal code  **(required for shipment purchase)** . [optional]  # noqa: E501
            city (str, none_type):  The address city.  **(required for shipment purchase)** . [optional]  # noqa: E501
            federal_tax_id (str, none_type): The party frederal tax id. [optional]  # noqa: E501
            state_tax_id (str, none_type): The party state id. [optional]  # noqa: E501
            person_name (str, none_type):  attention to  **(required for shipment purchase)** . [optional]  # noqa: E501
            company_name (str, none_type): The company name if the party is a company. [optional]  # noqa: E501
            email (str, none_type): The party email. [optional]  # noqa: E501
            phone_number (str, none_type): The party phone number.. [optional]  # noqa: E501
            state_code (str, none_type): The address state code. [optional]  # noqa: E501
            suburb (str, none_type): The address suburb if known. [optional]  # noqa: E501
            residential (bool, none_type): Indicate if the address is residential or commercial (enterprise). [optional] if omitted the server will use the default value of False  # noqa: E501
            address_line1 (str, none_type):  The address line with street number <br/> **(required for shipment purchase)** . [optional]  # noqa: E501
            address_line2 (str, none_type): The address line with suite number. [optional]  # noqa: E501
            validate_location (bool, none_type): Indicate if the address should be validated. [optional] if omitted the server will use the default value of False  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.country_code = country_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, country_code, *args, **kwargs):  # noqa: E501
        """AddressData - a model defined in OpenAPI

        Args:
            country_code (str): The address country code

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            postal_code (str, none_type):  The address postal code  **(required for shipment purchase)** . [optional]  # noqa: E501
            city (str, none_type):  The address city.  **(required for shipment purchase)** . [optional]  # noqa: E501
            federal_tax_id (str, none_type): The party frederal tax id. [optional]  # noqa: E501
            state_tax_id (str, none_type): The party state id. [optional]  # noqa: E501
            person_name (str, none_type):  attention to  **(required for shipment purchase)** . [optional]  # noqa: E501
            company_name (str, none_type): The company name if the party is a company. [optional]  # noqa: E501
            email (str, none_type): The party email. [optional]  # noqa: E501
            phone_number (str, none_type): The party phone number.. [optional]  # noqa: E501
            state_code (str, none_type): The address state code. [optional]  # noqa: E501
            suburb (str, none_type): The address suburb if known. [optional]  # noqa: E501
            residential (bool, none_type): Indicate if the address is residential or commercial (enterprise). [optional] if omitted the server will use the default value of False  # noqa: E501
            address_line1 (str, none_type):  The address line with street number <br/> **(required for shipment purchase)** . [optional]  # noqa: E501
            address_line2 (str, none_type): The address line with suite number. [optional]  # noqa: E501
            validate_location (bool, none_type): Indicate if the address should be validated. [optional] if omitted the server will use the default value of False  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.country_code = country_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
