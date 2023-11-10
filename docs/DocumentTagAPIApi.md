# impower_client.DocumentTagAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_tag_using_post**](DocumentTagAPIApi.md#create_document_tag_using_post) | **POST** /v2/document-tags | Create a new document tag
[**delete_document_tag_using_delete**](DocumentTagAPIApi.md#delete_document_tag_using_delete) | **DELETE** /v2/document-tags/{tagId} | Delete an existing document tag based on the given id
[**get_document_tags_using_get**](DocumentTagAPIApi.md#get_document_tags_using_get) | **GET** /v2/document-tags | Get document tags
[**update_document_tag_using_put**](DocumentTagAPIApi.md#update_document_tag_using_put) | **PUT** /v2/document-tags/{tagId} | Update an existing document tag based on the given id

# **create_document_tag_using_post**
> DocumentTagDto create_document_tag_using_post(body)

Create a new document tag

The newly created document tag will be returned as response

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
api_instance = impower_client.DocumentTagAPIApi(impower_client.ApiClient(configuration))
body = impower_client.DocumentTagCreateDto() # DocumentTagCreateDto | createDto

try:
    # Create a new document tag
    api_response = api_instance.create_document_tag_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTagAPIApi->create_document_tag_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentTagCreateDto**](DocumentTagCreateDto.md)| createDto | 

### Return type

[**DocumentTagDto**](DocumentTagDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_tag_using_delete**
> delete_document_tag_using_delete(tag_id)

Delete an existing document tag based on the given id

System generated tags cannot be deleted

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
api_instance = impower_client.DocumentTagAPIApi(impower_client.ApiClient(configuration))
tag_id = 789 # int | Unique identifier of the document tag to be deleted

try:
    # Delete an existing document tag based on the given id
    api_instance.delete_document_tag_using_delete(tag_id)
except ApiException as e:
    print("Exception when calling DocumentTagAPIApi->delete_document_tag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| Unique identifier of the document tag to be deleted | 

### Return type

void (empty response body)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_tags_using_get**
> list[DocumentTagDto] get_document_tags_using_get(filter=filter)

Get document tags

Standard and domain specific document tags will be returned as response

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
api_instance = impower_client.DocumentTagAPIApi(impower_client.ApiClient(configuration))
filter = 'filter_example' # str | filter (optional)

try:
    # Get document tags
    api_response = api_instance.get_document_tags_using_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTagAPIApi->get_document_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| filter | [optional] 

### Return type

[**list[DocumentTagDto]**](DocumentTagDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_tag_using_put**
> DocumentTagDto update_document_tag_using_put(body, tag_id)

Update an existing document tag based on the given id

The updated document tag will be returned as response

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
api_instance = impower_client.DocumentTagAPIApi(impower_client.ApiClient(configuration))
body = impower_client.DocumentTagUpdateDto() # DocumentTagUpdateDto | updateDto
tag_id = 789 # int | Unique identifier of a document tag

try:
    # Update an existing document tag based on the given id
    api_response = api_instance.update_document_tag_using_put(body, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTagAPIApi->update_document_tag_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentTagUpdateDto**](DocumentTagUpdateDto.md)| updateDto | 
 **tag_id** | **int**| Unique identifier of a document tag | 

### Return type

[**DocumentTagDto**](DocumentTagDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

