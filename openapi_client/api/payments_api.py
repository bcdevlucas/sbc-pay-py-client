# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PaymentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment(self, payment_request, **kwargs):  # noqa: E501
        """Create payment records  # noqa: E501

        Creates payment records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payment(payment_request, async_req=True)
        >>> result = thread.get()

        :param payment_request: (required)
        :type payment_request: PaymentRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Payment
        """
        kwargs['_return_http_data_only'] = True
        return self.create_payment_with_http_info(payment_request, **kwargs)  # noqa: E501

    def create_payment_with_http_info(self, payment_request, **kwargs):  # noqa: E501
        """Create payment records  # noqa: E501

        Creates payment records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payment_with_http_info(payment_request, async_req=True)
        >>> result = thread.get()

        :param payment_request: (required)
        :type payment_request: PaymentRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Payment, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'payment_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_request' is set
        if self.api_client.client_side_validation and ('payment_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_request` when calling `create_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_request' in local_var_params:
            body_params = local_var_params['payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/payment-requests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Payment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment(self, payment_identifier, **kwargs):  # noqa: E501
        """Get Payment  # noqa: E501

        Get Payment by filing identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment(payment_identifier, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: Unique Identifier for the payment (required)
        :type payment_identifier: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Payment
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payment_with_http_info(payment_identifier, **kwargs)  # noqa: E501

    def get_payment_with_http_info(self, payment_identifier, **kwargs):  # noqa: E501
        """Get Payment  # noqa: E501

        Get Payment by filing identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_with_http_info(payment_identifier, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: Unique Identifier for the payment (required)
        :type payment_identifier: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Payment, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'payment_identifier'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_identifier' is set
        if self.api_client.client_side_validation and ('payment_identifier' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_identifier'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_identifier` when calling `get_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_identifier' in local_var_params:
            path_params['payment_identifier'] = local_var_params['payment_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/payment-requests/{payment_identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Payment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment(self, payment_identifier, payment_request, **kwargs):  # noqa: E501
        """Update payment records  # noqa: E501

        Updates payment records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_payment(payment_identifier, payment_request, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: (required)
        :type payment_identifier: str
        :param payment_request: (required)
        :type payment_request: PaymentRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Payment
        """
        kwargs['_return_http_data_only'] = True
        return self.update_payment_with_http_info(payment_identifier, payment_request, **kwargs)  # noqa: E501

    def update_payment_with_http_info(self, payment_identifier, payment_request, **kwargs):  # noqa: E501
        """Update payment records  # noqa: E501

        Updates payment records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_payment_with_http_info(payment_identifier, payment_request, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: (required)
        :type payment_identifier: str
        :param payment_request: (required)
        :type payment_request: PaymentRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Payment, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'payment_identifier',
            'payment_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_identifier' is set
        if self.api_client.client_side_validation and ('payment_identifier' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_identifier'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_identifier` when calling `update_payment`")  # noqa: E501
        # verify the required parameter 'payment_request' is set
        if self.api_client.client_side_validation and ('payment_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_request` when calling `update_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_identifier' in local_var_params:
            path_params['payment_identifier'] = local_var_params['payment_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_request' in local_var_params:
            body_params = local_var_params['payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/payment-requests/{payment_identifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Payment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
