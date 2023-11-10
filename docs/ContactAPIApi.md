# impower_client.ContactAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact_by_id_using_get**](ContactAPIApi.md#get_contact_by_id_using_get) | **GET** /v2/contacts/{contactId} | Get a contact by the given id
[**get_contacts_by_filter_using_get**](ContactAPIApi.md#get_contacts_by_filter_using_get) | **GET** /v2/contacts | Get contacts by the given filter parameters

# **get_contact_by_id_using_get**
> ContactDto get_contact_by_id_using_get(contact_id)

Get a contact by the given id

Retrieves a contact by the given id

### Example
```python
from __future__ import print_function
import time
import impower_client
from impower_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = impower_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = impower_client.ContactAPIApi(impower_client.ApiClient(configuration))
contact_id = 789 # int | Unique identifier of a contact

try:
    # Get a contact by the given id
    api_response = api_instance.get_contact_by_id_using_get(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactAPIApi->get_contact_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Unique identifier of a contact | 

### Return type

[**ContactDto**](ContactDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_by_filter_using_get**
> PageOfContactDto get_contacts_by_filter_using_get(contact_ids=contact_ids, email=email, name=name, order=order, page=page, size=size, sort=sort)

Get contacts by the given filter parameters

Retrieve contacts by the given filter parameters

### Example
```python
from __future__ import print_function
import time
import impower_client
from impower_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = impower_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = impower_client.ContactAPIApi(impower_client.ApiClient(configuration))
contact_ids = [56] # list[int] | List of contact ids to filter contacts by. (optional)
email = 'email_example' # str | Email address of the contact. (optional)
name = 'name_example' # str | Any name of the contact. Might be first name, last name or company name. (optional)
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)

try:
    # Get contacts by the given filter parameters
    api_response = api_instance.get_contacts_by_filter_using_get(contact_ids=contact_ids, email=email, name=name, order=order, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactAPIApi->get_contacts_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_ids** | [**list[int]**](int.md)| List of contact ids to filter contacts by. | [optional] 
 **email** | **str**| Email address of the contact. | [optional] 
 **name** | **str**| Any name of the contact. Might be first name, last name or company name. | [optional] 
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 

### Return type

[**PageOfContactDto**](PageOfContactDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

