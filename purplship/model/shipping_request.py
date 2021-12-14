"""
    Purplship API

     ## API Reference  Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Purplship API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded  request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Purplship API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released.  The current version is `2021.11`.   Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses,  list shipments, and list trackers. These list API methods share a common structure, taking at least these  two parameters: limit, and offset.  Purplship utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order.  The offset parameter returns objects listed after an index.  The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Purplship API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates,  buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    The version of the OpenAPI document: 2021.11
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
    OpenApiModel
)
from purplship.exceptions import ApiAttributeError


def lazy_import():
    from purplship.model.address_data import AddressData
    from purplship.model.customs_data import CustomsData
    from purplship.model.parcel_data import ParcelData
    from purplship.model.payment import Payment
    from purplship.model.rate import Rate
    globals()['AddressData'] = AddressData
    globals()['CustomsData'] = CustomsData
    globals()['ParcelData'] = ParcelData
    globals()['Payment'] = Payment
    globals()['Rate'] = Rate


class ShippingRequest(ModelNormal):
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
        ('label_type',): {
            'PDF': "PDF",
            'ZPL': "ZPL",
        },
    }

    validations = {
        ('selected_rate_id',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'shipper': (AddressData,),  # noqa: E501
            'recipient': (AddressData,),  # noqa: E501
            'parcels': ([ParcelData],),  # noqa: E501
            'payment': (Payment,),  # noqa: E501
            'selected_rate_id': (str,),  # noqa: E501
            'rates': ([Rate],),  # noqa: E501
            'options': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'customs': (CustomsData,),  # noqa: E501
            'reference': (str, none_type,),  # noqa: E501
            'label_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'shipper': 'shipper',  # noqa: E501
        'recipient': 'recipient',  # noqa: E501
        'parcels': 'parcels',  # noqa: E501
        'payment': 'payment',  # noqa: E501
        'selected_rate_id': 'selected_rate_id',  # noqa: E501
        'rates': 'rates',  # noqa: E501
        'options': 'options',  # noqa: E501
        'customs': 'customs',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'label_type': 'label_type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, shipper, recipient, parcels, payment, selected_rate_id, rates, *args, **kwargs):  # noqa: E501
        """ShippingRequest - a model defined in OpenAPI

        Args:
            shipper (AddressData):
            recipient (AddressData):
            parcels ([ParcelData]): The shipment's parcels
            payment (Payment):
            selected_rate_id (str): The shipment selected rate.
            rates ([Rate]): The list for shipment rates fetched previously

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
            options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type):  <details> <summary>The options available for the shipment.</summary>  ``` {     \"currency\": \"USD\",     \"insurance\": 100.00,     \"cash_on_delivery\": 30.00,     \"shipment_date\": \"2020-01-01\",     \"dangerous_good\": true,     \"declared_value\": 150.00,     \"email_notification\": true,     \"email_notification_to\": shipper@mail.com,     \"signature_confirmation\": true, } ```  Please check the docs for carrier specific options. </details> . [optional]  # noqa: E501
            customs (CustomsData): [optional]  # noqa: E501
            reference (str, none_type): The shipment reference. [optional]  # noqa: E501
            label_type (str): The shipment label file type.. [optional] if omitted the server will use the default value of "PDF"  # noqa: E501
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

        self.shipper = shipper
        self.recipient = recipient
        self.parcels = parcels
        self.payment = payment
        self.selected_rate_id = selected_rate_id
        self.rates = rates
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
    def __init__(self, shipper, recipient, parcels, payment, selected_rate_id, rates, *args, **kwargs):  # noqa: E501
        """ShippingRequest - a model defined in OpenAPI

        Args:
            shipper (AddressData):
            recipient (AddressData):
            parcels ([ParcelData]): The shipment's parcels
            payment (Payment):
            selected_rate_id (str): The shipment selected rate.
            rates ([Rate]): The list for shipment rates fetched previously

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
            options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type):  <details> <summary>The options available for the shipment.</summary>  ``` {     \"currency\": \"USD\",     \"insurance\": 100.00,     \"cash_on_delivery\": 30.00,     \"shipment_date\": \"2020-01-01\",     \"dangerous_good\": true,     \"declared_value\": 150.00,     \"email_notification\": true,     \"email_notification_to\": shipper@mail.com,     \"signature_confirmation\": true, } ```  Please check the docs for carrier specific options. </details> . [optional]  # noqa: E501
            customs (CustomsData): [optional]  # noqa: E501
            reference (str, none_type): The shipment reference. [optional]  # noqa: E501
            label_type (str): The shipment label file type.. [optional] if omitted the server will use the default value of "PDF"  # noqa: E501
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

        self.shipper = shipper
        self.recipient = recipient
        self.parcels = parcels
        self.payment = payment
        self.selected_rate_id = selected_rate_id
        self.rates = rates
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
