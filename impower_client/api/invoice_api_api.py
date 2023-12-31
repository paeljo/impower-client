# coding: utf-8

"""
    Impower ERP

     # Setup  Enquire a `Bearer Token` from Api Support  # Authentication  Use API calls with an `Authorization: Bearer TOKEN` header  # Webhooks  The application supports sending secured notification events to registered endpoints.  The events one may receive are sent as  ``` POST https://your.webhook.url/path/somewhere Authorization: Bearer TOKEN  {   \"connectionId\": 0,   \"entityType\": \"properties|contacts|invoices|etc.\",   \"entityId\": 0,   \"eventType\": \"CREATE|UPDATE|DELETE\" } ```  <!-- Style overrides --> <style> code {   display: block; } </style>   # noqa: E501

    OpenAPI spec version: 2.201.52181d67
    Contact: support+api@impower.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from impower_client.api_client import ApiClient


class InvoiceAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_invoice_by_id_using_get(self, invoice_id, **kwargs):  # noqa: E501
        """Get a invoice by the given id  # noqa: E501

        Retrieves an invoice by the given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoice_by_id_using_get(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int invoice_id: Unique identifier of an invoice (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invoice_by_id_using_get_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_invoice_by_id_using_get_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def get_invoice_by_id_using_get_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """Get a invoice by the given id  # noqa: E501

        Retrieves an invoice by the given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoice_by_id_using_get_with_http_info(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int invoice_id: Unique identifier of an invoice (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invoice_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `get_invoice_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_id' in params:
            path_params['invoiceId'] = params['invoice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/v2/invoices/{invoiceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invoices_by_filter_using_get(self, **kwargs):  # noqa: E501
        """Get invoices by the given filter parameters  # noqa: E501

        Retrieves invoices by the given filter parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoices_by_filter_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int counterpart_contact_id: Unique identifier of the counterpart contact
        :param str issued_date: Date of the invoices to be retrieved
        :param str order: Sorting direction. Possible values: ASC, DESC
        :param int page: Page number to be returned
        :param int property_id: Unique identifier of the property an invoice belongs to
        :param int size: Number of items to be returned in single page
        :param str sort: Sorting parameter
        :param list[str] states: States of the invoices to be retrieved
        :return: PageOfInvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invoices_by_filter_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_invoices_by_filter_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_invoices_by_filter_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get invoices by the given filter parameters  # noqa: E501

        Retrieves invoices by the given filter parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoices_by_filter_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int counterpart_contact_id: Unique identifier of the counterpart contact
        :param str issued_date: Date of the invoices to be retrieved
        :param str order: Sorting direction. Possible values: ASC, DESC
        :param int page: Page number to be returned
        :param int property_id: Unique identifier of the property an invoice belongs to
        :param int size: Number of items to be returned in single page
        :param str sort: Sorting parameter
        :param list[str] states: States of the invoices to be retrieved
        :return: PageOfInvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['counterpart_contact_id', 'issued_date', 'order', 'page', 'property_id', 'size', 'sort', 'states']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invoices_by_filter_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'counterpart_contact_id' in params:
            query_params.append(('counterpartContactId', params['counterpart_contact_id']))  # noqa: E501
        if 'issued_date' in params:
            query_params.append(('issuedDate', params['issued_date']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'property_id' in params:
            query_params.append(('propertyId', params['property_id']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'states' in params:
            query_params.append(('states', params['states']))  # noqa: E501
            collection_formats['states'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/v2/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfInvoiceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_invoice_using_put(self, body, invoice_id, **kwargs):  # noqa: E501
        """Update an invoice based on provided fields  # noqa: E501

        Update invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_invoice_using_put(body, invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvoiceUpdateDto body: updateDto (required)
        :param int invoice_id: Unique id of an invoice (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_invoice_using_put_with_http_info(body, invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_invoice_using_put_with_http_info(body, invoice_id, **kwargs)  # noqa: E501
            return data

    def update_invoice_using_put_with_http_info(self, body, invoice_id, **kwargs):  # noqa: E501
        """Update an invoice based on provided fields  # noqa: E501

        Update invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_invoice_using_put_with_http_info(body, invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvoiceUpdateDto body: updateDto (required)
        :param int invoice_id: Unique id of an invoice (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'invoice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_invoice_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_invoice_using_put`")  # noqa: E501
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `update_invoice_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_id' in params:
            path_params['invoiceId'] = params['invoice_id']  # noqa: E501

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
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/v2/invoices/{invoiceId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_invoice_using_post(self, file, **kwargs):  # noqa: E501
        """Upload invoice PDF document  # noqa: E501

        By default, the document will go though an OCR analysis  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_invoice_using_post(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_invoice_using_post_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_invoice_using_post_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def upload_invoice_using_post_with_http_info(self, file, **kwargs):  # noqa: E501
        """Upload invoice PDF document  # noqa: E501

        By default, the document will go though an OCR analysis  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_invoice_using_post_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: (required)
        :return: InvoiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_invoice_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_invoice_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/v2/invoices/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
