# impower_client.PropertyAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_properties_by_filter_using_get**](PropertyAPIApi.md#get_properties_by_filter_using_get) | **GET** /v2/properties | Get properties by the given filter parameters
[**get_property_by_id_using_get**](PropertyAPIApi.md#get_property_by_id_using_get) | **GET** /v2/properties/{propertyId} | Get a property by the given id

# **get_properties_by_filter_using_get**
> PageOfPropertyDto get_properties_by_filter_using_get(name=name, order=order, page=page, property_hr_id=property_hr_id, size=size, sort=sort)

Get properties by the given filter parameters

Retrieve properties by the given filter parameters

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
api_instance = impower_client.PropertyAPIApi(impower_client.ApiClient(configuration))
name = 'name_example' # str | Name of the property. (optional)
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
property_hr_id = 'property_hr_id_example' # str | Human readable id of the property. (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)

try:
    # Get properties by the given filter parameters
    api_response = api_instance.get_properties_by_filter_using_get(name=name, order=order, page=page, property_hr_id=property_hr_id, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyAPIApi->get_properties_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the property. | [optional] 
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **property_hr_id** | **str**| Human readable id of the property. | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 

### Return type

[**PageOfPropertyDto**](PageOfPropertyDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_by_id_using_get**
> PropertyDto get_property_by_id_using_get(property_id)

Get a property by the given id

Retrieves a property by the given id

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
api_instance = impower_client.PropertyAPIApi(impower_client.ApiClient(configuration))
property_id = 789 # int | Unique identifier of a property

try:
    # Get a property by the given id
    api_response = api_instance.get_property_by_id_using_get(property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertyAPIApi->get_property_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| Unique identifier of a property | 

### Return type

[**PropertyDto**](PropertyDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

