# coding: utf-8

"""
    Purplship API

     ## API Reference  Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Purplship API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded  request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Purplship API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released.  The current version is `2021.6.2`.   Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses,  list shipments, and list trackers. These list API methods share a common structure, taking at least these  two parameters: limit, and offset.  Purplship utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order.  The offset parameter returns objects listed after an index.  The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Purplship API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates,  buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    OpenAPI spec version: 2021.6.2
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from purplship.api_client import ApiClient


class CustomsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_commodity(self, body, id, **kwargs):  # noqa: E501
        """Add a commodity  # noqa: E501

        Add a customs commodity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_commodity(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommodityData body: (required)
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_commodity_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_commodity_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def add_commodity_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Add a commodity  # noqa: E501

        Add a customs commodity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_commodity_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommodityData body: (required)
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_commodity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_commodity`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_commodity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/customs_info/{id}/commodities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, body, **kwargs):  # noqa: E501
        """Create a customs info  # noqa: E501

        Create a new customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomsData body: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a customs info  # noqa: E501

        Create a new customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomsData body: (required)
        :return: Customs
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
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create`")  # noqa: E501

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
            '/v1/customs_info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def discard(self, id, **kwargs):  # noqa: E501
        """Discard a customs info  # noqa: E501

        Discard a customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discard(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discard_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.discard_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def discard_with_http_info(self, id, **kwargs):  # noqa: E501
        """Discard a customs info  # noqa: E501

        Discard a customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discard_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method discard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `discard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/customs_info/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def discard_commodity(self, ck, id, **kwargs):  # noqa: E501
        """Discard a commodity  # noqa: E501

        Discard a customs commodity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discard_commodity(ck, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ck: (required)
        :param str id: (required)
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discard_commodity_with_http_info(ck, id, **kwargs)  # noqa: E501
        else:
            (data) = self.discard_commodity_with_http_info(ck, id, **kwargs)  # noqa: E501
            return data

    def discard_commodity_with_http_info(self, ck, id, **kwargs):  # noqa: E501
        """Discard a commodity  # noqa: E501

        Discard a customs commodity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discard_commodity_with_http_info(ck, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ck: (required)
        :param str id: (required)
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ck', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method discard_commodity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ck' is set
        if ('ck' not in params or
                params['ck'] is None):
            raise ValueError("Missing the required parameter `ck` when calling `discard_commodity`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `discard_commodity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ck' in params:
            path_params['ck'] = params['ck']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/customs_info/{id}/commodities/{ck}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List all customs info  # noqa: E501

        Retrieve all stored customs declarations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: CustomsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List all customs info  # noqa: E501

        Retrieve all stored customs declarations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: CustomsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/v1/customs_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve(self, id, **kwargs):  # noqa: E501
        """Retrieve a customs info  # noqa: E501

        Retrieve customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def retrieve_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a customs info  # noqa: E501

        Retrieve customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/customs_info/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, body, id, **kwargs):  # noqa: E501
        """Update a customs info  # noqa: E501

        modify an existing customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomsData body: (required)
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a customs info  # noqa: E501

        modify an existing customs declaration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomsData body: (required)
        :param str id: (required)
        :return: Customs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v1/customs_info/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
