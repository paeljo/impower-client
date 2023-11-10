# impower_client.UnitAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unit_by_id_using_get**](UnitAPIApi.md#get_unit_by_id_using_get) | **GET** /v2/units/{unitId} | Get a unit by the given id
[**get_units_by_filter_using_get**](UnitAPIApi.md#get_units_by_filter_using_get) | **GET** /v2/units | Get all units by given filter parameters

# **get_unit_by_id_using_get**
> UnitDto get_unit_by_id_using_get(unit_id)

Get a unit by the given id

Return the unit having the given id

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
api_instance = impower_client.UnitAPIApi(impower_client.ApiClient(configuration))
unit_id = 789 # int | Unique id of a unit

try:
    # Get a unit by the given id
    api_response = api_instance.get_unit_by_id_using_get(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitAPIApi->get_unit_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**| Unique id of a unit | 

### Return type

[**UnitDto**](UnitDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_units_by_filter_using_get**
> PageOfUnitDto get_units_by_filter_using_get(order=order, page=page, property_id=property_id, size=size, sort=sort)

Get all units by given filter parameters

Returns all units respecting the given filter criteria

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
api_instance = impower_client.UnitAPIApi(impower_client.ApiClient(configuration))
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
property_id = 789 # int | Unique identifier of the property a unit belongs to (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)

try:
    # Get all units by given filter parameters
    api_response = api_instance.get_units_by_filter_using_get(order=order, page=page, property_id=property_id, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitAPIApi->get_units_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **property_id** | **int**| Unique identifier of the property a unit belongs to | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 

### Return type

[**PageOfUnitDto**](PageOfUnitDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

