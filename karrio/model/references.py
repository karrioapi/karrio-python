"""
    Karrio API

     ## API Reference  Karrio is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Karrio API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Karrio API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released. The current version is `2022.4`.  Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses, list shipments, and list trackers. These list API methods share a common structure, taking at least these two parameters: limit, and offset.  Karrio utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order. The offset parameter returns objects listed after an index. The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Karrio API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates, buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    The version of the OpenAPI document: 2022.4
    Contact: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from karrio.model_utils import (  # noqa: F401
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
from karrio.exceptions import ApiAttributeError



class References(ModelNormal):
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
    }

    validations = {
        ('app_name',): {
            'min_length': 1,
        },
        ('app_version',): {
            'min_length': 1,
        },
        ('app_website',): {
            'min_length': 1,
        },
        ('admin',): {
            'min_length': 1,
        },
        ('openapi',): {
            'min_length': 1,
        },
        ('graphql',): {
            'min_length': 1,
        },
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
            'app_name': (str,),  # noqa: E501
            'app_version': (str,),  # noqa: E501
            'app_website': (str,),  # noqa: E501
            'multi_organizations': (bool,),  # noqa: E501
            'orders_management': (bool,),  # noqa: E501
            'apps_management': (bool,),  # noqa: E501
            'allow_signup': (bool,),  # noqa: E501
            'admin': (str,),  # noqa: E501
            'openapi': (str,),  # noqa: E501
            'graphql': (str,),  # noqa: E501
            'address_auto_complete': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'countries': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'currencies': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'carriers': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'customs_content_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'incoterms': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'states': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'services': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'service_names': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'options': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'option_names': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'package_presets': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'packaging_types': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'payment_types': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'carrier_capabilities': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'service_levels': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'app_name': 'APP_NAME',  # noqa: E501
        'app_version': 'APP_VERSION',  # noqa: E501
        'app_website': 'APP_WEBSITE',  # noqa: E501
        'multi_organizations': 'MULTI_ORGANIZATIONS',  # noqa: E501
        'orders_management': 'ORDERS_MANAGEMENT',  # noqa: E501
        'apps_management': 'APPS_MANAGEMENT',  # noqa: E501
        'allow_signup': 'ALLOW_SIGNUP',  # noqa: E501
        'admin': 'ADMIN',  # noqa: E501
        'openapi': 'OPENAPI',  # noqa: E501
        'graphql': 'GRAPHQL',  # noqa: E501
        'address_auto_complete': 'ADDRESS_AUTO_COMPLETE',  # noqa: E501
        'countries': 'countries',  # noqa: E501
        'currencies': 'currencies',  # noqa: E501
        'carriers': 'carriers',  # noqa: E501
        'customs_content_type': 'customs_content_type',  # noqa: E501
        'incoterms': 'incoterms',  # noqa: E501
        'states': 'states',  # noqa: E501
        'services': 'services',  # noqa: E501
        'service_names': 'service_names',  # noqa: E501
        'options': 'options',  # noqa: E501
        'option_names': 'option_names',  # noqa: E501
        'package_presets': 'package_presets',  # noqa: E501
        'packaging_types': 'packaging_types',  # noqa: E501
        'payment_types': 'payment_types',  # noqa: E501
        'carrier_capabilities': 'carrier_capabilities',  # noqa: E501
        'service_levels': 'service_levels',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, app_name, app_version, app_website, multi_organizations, orders_management, apps_management, allow_signup, admin, openapi, graphql, address_auto_complete, countries, currencies, carriers, customs_content_type, incoterms, states, services, service_names, options, option_names, package_presets, packaging_types, payment_types, carrier_capabilities, service_levels, *args, **kwargs):  # noqa: E501
        """References - a model defined in OpenAPI

        Args:
            app_name (str):
            app_version (str):
            app_website (str):
            multi_organizations (bool):
            orders_management (bool):
            apps_management (bool):
            allow_signup (bool):
            admin (str):
            openapi (str):
            graphql (str):
            address_auto_complete ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            countries ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            currencies ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            carriers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            customs_content_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            incoterms ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            states ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            services ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            service_names ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            option_names ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            package_presets ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            packaging_types ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            payment_types ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            carrier_capabilities ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            service_levels ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.app_name = app_name
        self.app_version = app_version
        self.app_website = app_website
        self.multi_organizations = multi_organizations
        self.orders_management = orders_management
        self.apps_management = apps_management
        self.allow_signup = allow_signup
        self.admin = admin
        self.openapi = openapi
        self.graphql = graphql
        self.address_auto_complete = address_auto_complete
        self.countries = countries
        self.currencies = currencies
        self.carriers = carriers
        self.customs_content_type = customs_content_type
        self.incoterms = incoterms
        self.states = states
        self.services = services
        self.service_names = service_names
        self.options = options
        self.option_names = option_names
        self.package_presets = package_presets
        self.packaging_types = packaging_types
        self.payment_types = payment_types
        self.carrier_capabilities = carrier_capabilities
        self.service_levels = service_levels
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
    def __init__(self, app_name, app_version, app_website, multi_organizations, orders_management, apps_management, allow_signup, admin, openapi, graphql, address_auto_complete, countries, currencies, carriers, customs_content_type, incoterms, states, services, service_names, options, option_names, package_presets, packaging_types, payment_types, carrier_capabilities, service_levels, *args, **kwargs):  # noqa: E501
        """References - a model defined in OpenAPI

        Args:
            app_name (str):
            app_version (str):
            app_website (str):
            multi_organizations (bool):
            orders_management (bool):
            apps_management (bool):
            allow_signup (bool):
            admin (str):
            openapi (str):
            graphql (str):
            address_auto_complete ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            countries ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            currencies ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            carriers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            customs_content_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            incoterms ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            states ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            services ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            service_names ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            option_names ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            package_presets ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            packaging_types ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            payment_types ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            carrier_capabilities ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            service_levels ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.app_name = app_name
        self.app_version = app_version
        self.app_website = app_website
        self.multi_organizations = multi_organizations
        self.orders_management = orders_management
        self.apps_management = apps_management
        self.allow_signup = allow_signup
        self.admin = admin
        self.openapi = openapi
        self.graphql = graphql
        self.address_auto_complete = address_auto_complete
        self.countries = countries
        self.currencies = currencies
        self.carriers = carriers
        self.customs_content_type = customs_content_type
        self.incoterms = incoterms
        self.states = states
        self.services = services
        self.service_names = service_names
        self.options = options
        self.option_names = option_names
        self.package_presets = package_presets
        self.packaging_types = packaging_types
        self.payment_types = payment_types
        self.carrier_capabilities = carrier_capabilities
        self.service_levels = service_levels
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
