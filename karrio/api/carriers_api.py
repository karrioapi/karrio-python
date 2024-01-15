"""
    Karrio API

     ## API Reference  Karrio is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Karrio API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Karrio API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released. The current version is `2022.4`.  Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses, list shipments, and list trackers. These list API methods share a common structure, taking at least these two parameters: limit, and offset.  Karrio utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order. The offset parameter returns objects listed after an index. The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Karrio API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates, buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    The version of the OpenAPI document: 2022.4
    Contact: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from karrio.api_client import ApiClient, Endpoint as _Endpoint
from karrio.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from karrio.model.carrier_list import CarrierList
from karrio.model.error_response import ErrorResponse


class CarriersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_services_endpoint = _Endpoint(
            settings={
                'response_type': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/v1/carriers/{carrier_name}/services',
                'operation_id': 'get_services',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'carrier_name',
                ],
                'required': [
                    'carrier_name',
                ],
                'nullable': [
                ],
                'enum': [
                    'carrier_name',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('carrier_name',): {

                        "ARAMEX": "aramex",
                        "AUSTRALIAPOST": "australiapost",
                        "CANADAPOST": "canadapost",
                        "CANPAR": "canpar",
                        "DHL_EXPRESS": "dhl_express",
                        "DHL_POLAND": "dhl_poland",
                        "DHL_UNIVERSAL": "dhl_universal",
                        "DICOM": "dicom",
                        "ESHIPPER": "eshipper",
                        "FEDEX": "fedex",
                        "FREIGHTCOM": "freightcom",
                        "GENERIC": "generic",
                        "PUROLATOR": "purolator",
                        "ROYALMAIL": "royalmail",
                        "SENDLE": "sendle",
                        "SF_EXPRESS": "sf_express",
                        "TNT": "tnt",
                        "UPS": "ups",
                        "USPS": "usps",
                        "USPS_INTERNATIONAL": "usps_international",
                        "YANWEN": "yanwen",
                        "YUNEXPRESS": "yunexpress"
                    },
                },
                'openapi_types': {
                    'carrier_name':
                        (str,),
                },
                'attribute_map': {
                    'carrier_name': 'carrier_name',
                },
                'location_map': {
                    'carrier_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_endpoint = _Endpoint(
            settings={
                'response_type': (CarrierList,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/v1/carriers',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'carrier_name',
                    'test',
                    'active',
                    'system_only',
                ],
                'required': [],
                'nullable': [
                    'test',
                    'active',
                    'system_only',
                ],
                'enum': [
                    'carrier_name',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('carrier_name',): {

                        "ARAMEX": "aramex",
                        "AUSTRALIAPOST": "australiapost",
                        "CANADAPOST": "canadapost",
                        "CANPAR": "canpar",
                        "DHL_EXPRESS": "dhl_express",
                        "DHL_POLAND": "dhl_poland",
                        "DHL_UNIVERSAL": "dhl_universal",
                        "DICOM": "dicom",
                        "ESHIPPER": "eshipper",
                        "FEDEX": "fedex",
                        "FREIGHTCOM": "freightcom",
                        "GENERIC": "generic",
                        "PUROLATOR": "purolator",
                        "ROYALMAIL": "royalmail",
                        "SENDLE": "sendle",
                        "SF_EXPRESS": "sf_express",
                        "TNT": "tnt",
                        "UPS": "ups",
                        "USPS": "usps",
                        "USPS_INTERNATIONAL": "usps_international",
                        "YANWEN": "yanwen",
                        "YUNEXPRESS": "yunexpress"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'carrier_name':
                        (str,),
                    'test':
                        (bool, none_type,),
                    'active':
                        (bool, none_type,),
                    'system_only':
                        (bool, none_type,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'carrier_name': 'carrier_name',
                    'test': 'test',
                    'active': 'active',
                    'system_only': 'system_only',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'carrier_name': 'query',
                    'test': 'query',
                    'active': 'query',
                    'system_only': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_services(
        self,
        carrier_name,
        **kwargs
    ):
        """Get carrier services  # noqa: E501

        Retrieve a carrier's services  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_services(carrier_name, async_req=True)
        >>> result = thread.get()

        Args:
            carrier_name (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['carrier_name'] = \
            carrier_name
        return self.get_services_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List all carriers  # noqa: E501

        Returns the list of configured carriers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Number of results to return per page.. [optional]
            offset (int): The initial index from which to return the results.. [optional]
            carrier_name (str): Indicates a carrier (type). [optional]
            test (bool, none_type): This flag filter out carriers in test or live mode. [optional]
            active (bool, none_type): This flag indicates whether to return active carriers only. [optional]
            system_only (bool, none_type): This flag indicates that only system carriers should be returned. [optional] if omitted the server will use the default value of False
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CarrierList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_endpoint.call_with_http_info(**kwargs)
