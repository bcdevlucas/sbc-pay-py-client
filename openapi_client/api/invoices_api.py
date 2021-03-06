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


class InvoicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_invoice(self, payment_identifier, invoice_id, **kwargs):  # noqa: E501
        """Get Invoice  # noqa: E501

        Get an invoice for the payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice(payment_identifier, invoice_id, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: Unique Identifier for the payment (required)
        :type payment_identifier: str
        :param invoice_id: Unique Identifier for the invoice (required)
        :type invoice_id: str
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
        :rtype: Invoice
        """
        kwargs['_return_http_data_only'] = True
        return self.get_invoice_with_http_info(payment_identifier, invoice_id, **kwargs)  # noqa: E501

    def get_invoice_with_http_info(self, payment_identifier, invoice_id, **kwargs):  # noqa: E501
        """Get Invoice  # noqa: E501

        Get an invoice for the payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice_with_http_info(payment_identifier, invoice_id, async_req=True)
        >>> result = thread.get()

        :param payment_identifier: Unique Identifier for the payment (required)
        :type payment_identifier: str
        :param invoice_id: Unique Identifier for the invoice (required)
        :type invoice_id: str
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
        :rtype: tuple(Invoice, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'payment_identifier',
            'invoice_id'
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
                    " to method get_invoice" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_identifier' is set
        if self.api_client.client_side_validation and ('payment_identifier' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_identifier'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_identifier` when calling `get_invoice`")  # noqa: E501
        # verify the required parameter 'invoice_id' is set
        if self.api_client.client_side_validation and ('invoice_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['invoice_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `invoice_id` when calling `get_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_identifier' in local_var_params:
            path_params['payment_identifier'] = local_var_params['payment_identifier']  # noqa: E501
        if 'invoice_id' in local_var_params:
            path_params['invoice_id'] = local_var_params['invoice_id']  # noqa: E501

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
            '/api/v1/payment-requests/{payment_identifier}/invoices/{invoice_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Invoice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invoices(self, payment_identifier, **kwargs):  # noqa: E501
        """Get Invoices  # noqa: E501

        Get Invoices for the payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoices(payment_identifier, async_req=True)
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
        :rtype: Invoices
        """
        kwargs['_return_http_data_only'] = True
        return self.get_invoices_with_http_info(payment_identifier, **kwargs)  # noqa: E501

    def get_invoices_with_http_info(self, payment_identifier, **kwargs):  # noqa: E501
        """Get Invoices  # noqa: E501

        Get Invoices for the payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoices_with_http_info(payment_identifier, async_req=True)
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
        :rtype: tuple(Invoices, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_invoices" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_identifier' is set
        if self.api_client.client_side_validation and ('payment_identifier' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_identifier'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_identifier` when calling `get_invoices`")  # noqa: E501

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
            '/api/v1/payment-requests/{payment_identifier}/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Invoices',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
