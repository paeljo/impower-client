# impower_client.ErrorCodeAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error_code_using_get**](ErrorCodeAPIApi.md#error_code_using_get) | **GET** /api/v1/error-codes/{value} | Get details of a specific error code
[**error_codes_using_get**](ErrorCodeAPIApi.md#error_codes_using_get) | **GET** /api/v1/error-codes | Get all predefined error code values

# **error_code_using_get**
> ErrorCodeDetailsDto error_code_using_get(value)

Get details of a specific error code

Retrieves the description of a specific error code

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
api_instance = impower_client.ErrorCodeAPIApi(impower_client.ApiClient(configuration))
value = 'value_example' # str | value

try:
    # Get details of a specific error code
    api_response = api_instance.error_code_using_get(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorCodeAPIApi->error_code_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| value | 

### Return type

[**ErrorCodeDetailsDto**](ErrorCodeDetailsDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **error_codes_using_get**
> list[str] error_codes_using_get()

Get all predefined error code values

Returns a list of all predefined error codes

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
api_instance = impower_client.ErrorCodeAPIApi(impower_client.ApiClient(configuration))

try:
    # Get all predefined error code values
    api_response = api_instance.error_codes_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorCodeAPIApi->error_codes_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

