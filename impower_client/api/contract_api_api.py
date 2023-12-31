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


class ContractAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_contract_by_id_using_get(self, contract_id, **kwargs):  # noqa: E501
        """Get a contract by the given id  # noqa: E501

        Retrieves a contract by the given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contract_by_id_using_get(contract_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contract_id: Unique identifier of a contract (required)
        :return: ContractDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_contract_by_id_using_get_with_http_info(contract_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contract_by_id_using_get_with_http_info(contract_id, **kwargs)  # noqa: E501
            return data

    def get_contract_by_id_using_get_with_http_info(self, contract_id, **kwargs):  # noqa: E501
        """Get a contract by the given id  # noqa: E501

        Retrieves a contract by the given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contract_by_id_using_get_with_http_info(contract_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contract_id: Unique identifier of a contract (required)
        :return: ContractDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contract_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params or
                params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `get_contract_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'contract_id' in params:
            path_params['contractId'] = params['contract_id']  # noqa: E501

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
            '/v2/contracts/{contractId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContractDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_contracts_by_filter_using_get(self, **kwargs):  # noqa: E501
        """Get contracts by the given filter parameters  # noqa: E501

        Retrieve contracts by the given filter parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contracts_by_filter_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: ID of the contact instance the contract is associated with.
        :param list[int] contract_ids: List of contract ids to filter contracts by.
        :param str order: Sorting direction. Possible values: ASC, DESC
        :param int page: Page number to be returned
        :param int property_id: ID of the property instance the contract belongs to.
        :param int size: Number of items to be returned in single page
        :param str sort: Sorting parameter
        :param str type: Type of the contract. Options: OWNER | TENANT | TENANT_VACANCY | PROPERTY_OWNER
        :param int unit_id: ID of the unit instance the contract is associated with.
        :param str valid_at_date: Return valid contracts at date. Null is interpreted as beginning/end of time.
        :return: PageOfContractDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_contracts_by_filter_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_contracts_by_filter_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_contracts_by_filter_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get contracts by the given filter parameters  # noqa: E501

        Retrieve contracts by the given filter parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contracts_by_filter_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: ID of the contact instance the contract is associated with.
        :param list[int] contract_ids: List of contract ids to filter contracts by.
        :param str order: Sorting direction. Possible values: ASC, DESC
        :param int page: Page number to be returned
        :param int property_id: ID of the property instance the contract belongs to.
        :param int size: Number of items to be returned in single page
        :param str sort: Sorting parameter
        :param str type: Type of the contract. Options: OWNER | TENANT | TENANT_VACANCY | PROPERTY_OWNER
        :param int unit_id: ID of the unit instance the contract is associated with.
        :param str valid_at_date: Return valid contracts at date. Null is interpreted as beginning/end of time.
        :return: PageOfContractDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id', 'contract_ids', 'order', 'page', 'property_id', 'size', 'sort', 'type', 'unit_id', 'valid_at_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contracts_by_filter_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'contact_id' in params:
            query_params.append(('contactId', params['contact_id']))  # noqa: E501
        if 'contract_ids' in params:
            query_params.append(('contractIds', params['contract_ids']))  # noqa: E501
            collection_formats['contractIds'] = 'multi'  # noqa: E501
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
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'unit_id' in params:
            query_params.append(('unitId', params['unit_id']))  # noqa: E501
        if 'valid_at_date' in params:
            query_params.append(('validAtDate', params['valid_at_date']))  # noqa: E501

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
            '/v2/contracts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfContractDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
