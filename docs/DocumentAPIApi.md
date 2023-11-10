# impower_client.DocumentAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_by_upload_using_post**](DocumentAPIApi.md#create_document_by_upload_using_post) | **POST** /v2/documents/upload | Create a new document based on given the file
[**delete_document_using_delete**](DocumentAPIApi.md#delete_document_using_delete) | **DELETE** /v2/documents/{documentId} | Delete an existing document based on the given id
[**download_documents_by_filter_using_get**](DocumentAPIApi.md#download_documents_by_filter_using_get) | **GET** /v2/documents/download-zip | Download multiple documents by given filter conditions
[**download_using_get**](DocumentAPIApi.md#download_using_get) | **GET** /v2/documents/{documentId}/download | Download a single document by given id
[**get_documents_by_filter_using_get**](DocumentAPIApi.md#get_documents_by_filter_using_get) | **GET** /v2/documents | Get documents by the given filter parameters
[**update_documents_using_put**](DocumentAPIApi.md#update_documents_using_put) | **PUT** /v2/documents | Update an existing document based on the given request body

# **create_document_by_upload_using_post**
> DocumentDto create_document_by_upload_using_post(file)

Create a new document based on given the file

The newly created document will be returned as response

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Create a new document based on given the file
    api_response = api_instance.create_document_by_upload_using_post(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->create_document_by_upload_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**DocumentDto**](DocumentDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_using_delete**
> delete_document_using_delete(document_id)

Delete an existing document based on the given id

System generated documents cannot be deleted

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
document_id = 789 # int | documentId

try:
    # Delete an existing document based on the given id
    api_instance.delete_document_using_delete(document_id)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->delete_document_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| documentId | 

### Return type

void (empty response body)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_documents_by_filter_using_get**
> str download_documents_by_filter_using_get(accountant=accountant, administrator=administrator, contract_name=contract_name, document_ids=document_ids, document_name=document_name, issued_date=issued_date, max_issued_date=max_issued_date, min_issued_date=min_issued_date, property_hr_id=property_hr_id, property_id=property_id, property_name=property_name, source_id=source_id, source_type=source_type, tag_ids=tag_ids, tag_name=tag_name, unit_id=unit_id)

Download multiple documents by given filter conditions

Documents come in zip format

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
accountant = 'accountant_example' # str | Accountant name of the property. (optional)
administrator = 'administrator_example' # str | Administrator name of the property. (optional)
contract_name = 'contract_name_example' # str | Documents linked to contracts with similar name. (optional)
document_ids = [56] # list[int] | IDs of the documents to be returned. (optional)
document_name = 'document_name_example' # str | Name of the documents to be returned. (optional)
issued_date = 'issued_date_example' # str | Issued date of the document. (optional)
max_issued_date = 'max_issued_date_example' # str | Documents having issued date before. (optional)
min_issued_date = 'min_issued_date_example' # str | Documents having issued date after. (optional)
property_hr_id = 'property_hr_id_example' # str | Human readable id of the property the document belongs to. (optional)
property_id = 789 # int | ID of the property the document belongs to. (optional)
property_name = 'property_name_example' # str | Name of the property the document belongs to. (optional)
source_id = 789 # int | ID of the source entity the document belongs to. (optional)
source_type = ['source_type_example'] # list[str] | Source types of the document. (optional)
tag_ids = [56] # list[int] | IDs of tags the document is associated to. (optional)
tag_name = 'tag_name_example' # str | Similar name of tag the document is associate to. (optional)
unit_id = 789 # int | ID of the unit entity the document belongs to. (optional)

try:
    # Download multiple documents by given filter conditions
    api_response = api_instance.download_documents_by_filter_using_get(accountant=accountant, administrator=administrator, contract_name=contract_name, document_ids=document_ids, document_name=document_name, issued_date=issued_date, max_issued_date=max_issued_date, min_issued_date=min_issued_date, property_hr_id=property_hr_id, property_id=property_id, property_name=property_name, source_id=source_id, source_type=source_type, tag_ids=tag_ids, tag_name=tag_name, unit_id=unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->download_documents_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountant** | **str**| Accountant name of the property. | [optional] 
 **administrator** | **str**| Administrator name of the property. | [optional] 
 **contract_name** | **str**| Documents linked to contracts with similar name. | [optional] 
 **document_ids** | [**list[int]**](int.md)| IDs of the documents to be returned. | [optional] 
 **document_name** | **str**| Name of the documents to be returned. | [optional] 
 **issued_date** | **str**| Issued date of the document. | [optional] 
 **max_issued_date** | **str**| Documents having issued date before. | [optional] 
 **min_issued_date** | **str**| Documents having issued date after. | [optional] 
 **property_hr_id** | **str**| Human readable id of the property the document belongs to. | [optional] 
 **property_id** | **int**| ID of the property the document belongs to. | [optional] 
 **property_name** | **str**| Name of the property the document belongs to. | [optional] 
 **source_id** | **int**| ID of the source entity the document belongs to. | [optional] 
 **source_type** | [**list[str]**](str.md)| Source types of the document. | [optional] 
 **tag_ids** | [**list[int]**](int.md)| IDs of tags the document is associated to. | [optional] 
 **tag_name** | **str**| Similar name of tag the document is associate to. | [optional] 
 **unit_id** | **int**| ID of the unit entity the document belongs to. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_using_get**
> str download_using_get(document_id)

Download a single document by given id

Format of the document is PDF

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
document_id = 789 # int | Unique identifier of a document

try:
    # Download a single document by given id
    api_response = api_instance.download_using_get(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->download_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| Unique identifier of a document | 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_by_filter_using_get**
> PageOfDocumentDto get_documents_by_filter_using_get(accountant=accountant, administrator=administrator, contract_name=contract_name, document_ids=document_ids, document_name=document_name, issued_date=issued_date, max_issued_date=max_issued_date, min_issued_date=min_issued_date, order=order, page=page, property_hr_id=property_hr_id, property_id=property_id, property_name=property_name, size=size, sort=sort, source_id=source_id, source_type=source_type, tag_ids=tag_ids, tag_name=tag_name, unit_id=unit_id)

Get documents by the given filter parameters

Retrieve documents by the given filter parameters

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
accountant = 'accountant_example' # str | Accountant name of the property. (optional)
administrator = 'administrator_example' # str | Administrator name of the property. (optional)
contract_name = 'contract_name_example' # str | Documents linked to contracts with similar name. (optional)
document_ids = [56] # list[int] | IDs of the documents to be returned. (optional)
document_name = 'document_name_example' # str | Name of the documents to be returned. (optional)
issued_date = 'issued_date_example' # str | Issued date of the document. (optional)
max_issued_date = 'max_issued_date_example' # str | Documents having issued date before. (optional)
min_issued_date = 'min_issued_date_example' # str | Documents having issued date after. (optional)
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
property_hr_id = 'property_hr_id_example' # str | Human readable id of the property the document belongs to. (optional)
property_id = 789 # int | ID of the property the document belongs to. (optional)
property_name = 'property_name_example' # str | Name of the property the document belongs to. (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)
source_id = 789 # int | ID of the source entity the document belongs to. (optional)
source_type = ['source_type_example'] # list[str] | Source types of the document. (optional)
tag_ids = [56] # list[int] | IDs of tags the document is associated to. (optional)
tag_name = 'tag_name_example' # str | Similar name of tag the document is associate to. (optional)
unit_id = 789 # int | ID of the unit entity the document belongs to. (optional)

try:
    # Get documents by the given filter parameters
    api_response = api_instance.get_documents_by_filter_using_get(accountant=accountant, administrator=administrator, contract_name=contract_name, document_ids=document_ids, document_name=document_name, issued_date=issued_date, max_issued_date=max_issued_date, min_issued_date=min_issued_date, order=order, page=page, property_hr_id=property_hr_id, property_id=property_id, property_name=property_name, size=size, sort=sort, source_id=source_id, source_type=source_type, tag_ids=tag_ids, tag_name=tag_name, unit_id=unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->get_documents_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountant** | **str**| Accountant name of the property. | [optional] 
 **administrator** | **str**| Administrator name of the property. | [optional] 
 **contract_name** | **str**| Documents linked to contracts with similar name. | [optional] 
 **document_ids** | [**list[int]**](int.md)| IDs of the documents to be returned. | [optional] 
 **document_name** | **str**| Name of the documents to be returned. | [optional] 
 **issued_date** | **str**| Issued date of the document. | [optional] 
 **max_issued_date** | **str**| Documents having issued date before. | [optional] 
 **min_issued_date** | **str**| Documents having issued date after. | [optional] 
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **property_hr_id** | **str**| Human readable id of the property the document belongs to. | [optional] 
 **property_id** | **int**| ID of the property the document belongs to. | [optional] 
 **property_name** | **str**| Name of the property the document belongs to. | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 
 **source_id** | **int**| ID of the source entity the document belongs to. | [optional] 
 **source_type** | [**list[str]**](str.md)| Source types of the document. | [optional] 
 **tag_ids** | [**list[int]**](int.md)| IDs of tags the document is associated to. | [optional] 
 **tag_name** | **str**| Similar name of tag the document is associate to. | [optional] 
 **unit_id** | **int**| ID of the unit entity the document belongs to. | [optional] 

### Return type

[**PageOfDocumentDto**](PageOfDocumentDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_documents_using_put**
> list[DocumentDto] update_documents_using_put(body)

Update an existing document based on the given request body

All the need information is in the request body

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
api_instance = impower_client.DocumentAPIApi(impower_client.ApiClient(configuration))
body = [impower_client.DocumentUpdateDto()] # list[DocumentUpdateDto] | documentUpdateDtos

try:
    # Update an existing document based on the given request body
    api_response = api_instance.update_documents_using_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAPIApi->update_documents_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DocumentUpdateDto]**](DocumentUpdateDto.md)| documentUpdateDtos | 

### Return type

[**list[DocumentDto]**](DocumentDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

