# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2021.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from purplship.api_client import ApiClient


class ProxyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def buy_label(self, body, **kwargs):  # noqa: E501
        """Buy a shipment label  # noqa: E501

        Once the shipping rates are retrieved, provide the required info to submit the shipment by specifying your preferred rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.buy_label(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShippingRequest body: (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.buy_label_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.buy_label_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def buy_label_with_http_info(self, body, **kwargs):  # noqa: E501
        """Buy a shipment label  # noqa: E501

        Once the shipping rates are retrieved, provide the required info to submit the shipment by specifying your preferred rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.buy_label_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShippingRequest body: (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method buy_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `buy_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/shipping', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_pickup(self, body, carrier_name, **kwargs):  # noqa: E501
        """Cancel a pickup  # noqa: E501

        Cancel a pickup previously scheduled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_pickup(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupCancelRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: OperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
            return data

    def cancel_pickup_with_http_info(self, body, carrier_name, **kwargs):  # noqa: E501
        """Cancel a pickup  # noqa: E501

        Cancel a pickup previously scheduled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_pickup_with_http_info(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupCancelRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: OperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'carrier_name', 'test']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_pickup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `cancel_pickup`")  # noqa: E501
        # verify the required parameter 'carrier_name' is set
        if ('carrier_name' not in params or
                params['carrier_name'] is None):
            raise ValueError("Missing the required parameter `carrier_name` when calling `cancel_pickup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier_name' in params:
            path_params['carrier_name'] = params['carrier_name']  # noqa: E501

        query_params = []
        if 'test' in params:
            query_params.append(('test', params['test']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/pickups/{carrier_name}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch(self, body, **kwargs):  # noqa: E501
        """Fetch shipment rates  # noqa: E501

         The Shipping process begins by fetching rates for your shipment. Use this service to fetch a shipping rates available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RateRequest body: (required)
        :return: RateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def fetch_with_http_info(self, body, **kwargs):  # noqa: E501
        """Fetch shipment rates  # noqa: E501

         The Shipping process begins by fetching rates for your shipment. Use this service to fetch a shipping rates available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RateRequest body: (required)
        :return: RateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fetch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/rates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedule_pickup(self, body, carrier_name, **kwargs):  # noqa: E501
        """Schedule a pickup  # noqa: E501

        Schedule one or many parcels pickup  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_pickup(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: PickupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedule_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
        else:
            (data) = self.schedule_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
            return data

    def schedule_pickup_with_http_info(self, body, carrier_name, **kwargs):  # noqa: E501
        """Schedule a pickup  # noqa: E501

        Schedule one or many parcels pickup  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_pickup_with_http_info(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: PickupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'carrier_name', 'test']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedule_pickup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedule_pickup`")  # noqa: E501
        # verify the required parameter 'carrier_name' is set
        if ('carrier_name' not in params or
                params['carrier_name'] is None):
            raise ValueError("Missing the required parameter `carrier_name` when calling `schedule_pickup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier_name' in params:
            path_params['carrier_name'] = params['carrier_name']  # noqa: E501

        query_params = []
        if 'test' in params:
            query_params.append(('test', params['test']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/pickups/{carrier_name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PickupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def track_shipment(self, carrier_name, tracking_number, **kwargs):  # noqa: E501
        """Track a shipment  # noqa: E501

        You can track a shipment by specifying the carrier and the shipment tracking number.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_shipment(carrier_name, tracking_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str carrier_name: (required)
        :param str tracking_number: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: TrackingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.track_shipment_with_http_info(carrier_name, tracking_number, **kwargs)  # noqa: E501
        else:
            (data) = self.track_shipment_with_http_info(carrier_name, tracking_number, **kwargs)  # noqa: E501
            return data

    def track_shipment_with_http_info(self, carrier_name, tracking_number, **kwargs):  # noqa: E501
        """Track a shipment  # noqa: E501

        You can track a shipment by specifying the carrier and the shipment tracking number.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_shipment_with_http_info(carrier_name, tracking_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str carrier_name: (required)
        :param str tracking_number: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: TrackingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['carrier_name', 'tracking_number', 'test']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track_shipment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'carrier_name' is set
        if ('carrier_name' not in params or
                params['carrier_name'] is None):
            raise ValueError("Missing the required parameter `carrier_name` when calling `track_shipment`")  # noqa: E501
        # verify the required parameter 'tracking_number' is set
        if ('tracking_number' not in params or
                params['tracking_number'] is None):
            raise ValueError("Missing the required parameter `tracking_number` when calling `track_shipment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier_name' in params:
            path_params['carrier_name'] = params['carrier_name']  # noqa: E501
        if 'tracking_number' in params:
            path_params['tracking_number'] = params['tracking_number']  # noqa: E501

        query_params = []
        if 'test' in params:
            query_params.append(('test', params['test']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/tracking/{carrier_name}/{tracking_number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrackingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pickup(self, body, carrier_name, **kwargs):  # noqa: E501
        """Update a pickup  # noqa: E501

        Modify a scheduled pickup  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pickup(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupUpdateRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: PickupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_pickup_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
            return data

    def update_pickup_with_http_info(self, body, carrier_name, **kwargs):  # noqa: E501
        """Update a pickup  # noqa: E501

        Modify a scheduled pickup  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pickup_with_http_info(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PickupUpdateRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: PickupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'carrier_name', 'test']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pickup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_pickup`")  # noqa: E501
        # verify the required parameter 'carrier_name' is set
        if ('carrier_name' not in params or
                params['carrier_name'] is None):
            raise ValueError("Missing the required parameter `carrier_name` when calling `update_pickup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier_name' in params:
            path_params['carrier_name'] = params['carrier_name']  # noqa: E501

        query_params = []
        if 'test' in params:
            query_params.append(('test', params['test']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/pickups/{carrier_name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PickupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def void_label(self, body, carrier_name, **kwargs):  # noqa: E501
        """Void a shipment label  # noqa: E501

        Cancel a shipment and the label previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.void_label(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShipmentCancelRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: OperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.void_label_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
        else:
            (data) = self.void_label_with_http_info(body, carrier_name, **kwargs)  # noqa: E501
            return data

    def void_label_with_http_info(self, body, carrier_name, **kwargs):  # noqa: E501
        """Void a shipment label  # noqa: E501

        Cancel a shipment and the label previously created  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.void_label_with_http_info(body, carrier_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShipmentCancelRequest body: (required)
        :param str carrier_name: (required)
        :param bool test:  The test flag indicates whether to use a carrier configured for test.  
        :return: OperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'carrier_name', 'test']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `void_label`")  # noqa: E501
        # verify the required parameter 'carrier_name' is set
        if ('carrier_name' not in params or
                params['carrier_name'] is None):
            raise ValueError("Missing the required parameter `carrier_name` when calling `void_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier_name' in params:
            path_params['carrier_name'] = params['carrier_name']  # noqa: E501

        query_params = []
        if 'test' in params:
            query_params.append(('test', params['test']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/proxy/shipping/{carrier_name}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)