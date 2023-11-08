# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UploadsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_upload(self, **kwargs):  # noqa: E501
        """Upload Activity  # noqa: E501

        Uploads a new data file to create an activity from. Requires activity:write scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_upload(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file:
        :param str name:
        :param str description:
        :param str trainer:
        :param str commute:
        :param str data_type:
        :param str external_id:
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_upload_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_upload_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_upload_with_http_info(self, **kwargs):  # noqa: E501
        """Upload Activity  # noqa: E501

        Uploads a new data file to create an activity from. Requires activity:write scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_upload_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file:
        :param str name:
        :param str description:
        :param str trainer:
        :param str commute:
        :param str data_type:
        :param str external_id:
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'name', 'description', 'trainer', 'commute', 'data_type', 'external_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_upload" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'trainer' in params:
            form_params.append(('trainer', params['trainer']))  # noqa: E501
        if 'commute' in params:
            form_params.append(('commute', params['commute']))  # noqa: E501
        if 'data_type' in params:
            form_params.append(('data_type', params['data_type']))  # noqa: E501
        if 'external_id' in params:
            form_params.append(('external_id', params['external_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/uploads', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Upload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_upload_by_id(self, upload_id, **kwargs):  # noqa: E501
        """Get Upload  # noqa: E501

        Returns an upload for a given identifier. Requires activity:write scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upload_by_id(upload_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int upload_id: The identifier of the upload. (required)
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_upload_by_id_with_http_info(upload_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_upload_by_id_with_http_info(upload_id, **kwargs)  # noqa: E501
            return data

    def get_upload_by_id_with_http_info(self, upload_id, **kwargs):  # noqa: E501
        """Get Upload  # noqa: E501

        Returns an upload for a given identifier. Requires activity:write scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upload_by_id_with_http_info(upload_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int upload_id: The identifier of the upload. (required)
        :return: Upload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['upload_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_upload_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'upload_id' is set
        if ('upload_id' not in params or
                params['upload_id'] is None):
            raise ValueError("Missing the required parameter `upload_id` when calling `get_upload_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'upload_id' in params:
            path_params['uploadId'] = params['upload_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/uploads/{uploadId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Upload',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
