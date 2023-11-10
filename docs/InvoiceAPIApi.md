# impower_client.InvoiceAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_by_id_using_get**](InvoiceAPIApi.md#get_invoice_by_id_using_get) | **GET** /v2/invoices/{invoiceId} | Get a invoice by the given id
[**get_invoices_by_filter_using_get**](InvoiceAPIApi.md#get_invoices_by_filter_using_get) | **GET** /v2/invoices | Get invoices by the given filter parameters
[**update_invoice_using_put**](InvoiceAPIApi.md#update_invoice_using_put) | **PUT** /v2/invoices/{invoiceId} | Update an invoice based on provided fields
[**upload_invoice_using_post**](InvoiceAPIApi.md#upload_invoice_using_post) | **POST** /v2/invoices/upload | Upload invoice PDF document

# **get_invoice_by_id_using_get**
> InvoiceDto get_invoice_by_id_using_get(invoice_id)

Get a invoice by the given id

Retrieves an invoice by the given id

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
api_instance = impower_client.InvoiceAPIApi(impower_client.ApiClient(configuration))
invoice_id = 789 # int | Unique identifier of an invoice

try:
    # Get a invoice by the given id
    api_response = api_instance.get_invoice_by_id_using_get(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceAPIApi->get_invoice_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| Unique identifier of an invoice | 

### Return type

[**InvoiceDto**](InvoiceDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_filter_using_get**
> PageOfInvoiceDto get_invoices_by_filter_using_get(counterpart_contact_id=counterpart_contact_id, issued_date=issued_date, order=order, page=page, property_id=property_id, size=size, sort=sort, states=states)

Get invoices by the given filter parameters

Retrieves invoices by the given filter parameters

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
api_instance = impower_client.InvoiceAPIApi(impower_client.ApiClient(configuration))
counterpart_contact_id = 789 # int | Unique identifier of the counterpart contact (optional)
issued_date = 'issued_date_example' # str | Date of the invoices to be retrieved (optional)
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
property_id = 789 # int | Unique identifier of the property an invoice belongs to (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)
states = ['states_example'] # list[str] | States of the invoices to be retrieved (optional)

try:
    # Get invoices by the given filter parameters
    api_response = api_instance.get_invoices_by_filter_using_get(counterpart_contact_id=counterpart_contact_id, issued_date=issued_date, order=order, page=page, property_id=property_id, size=size, sort=sort, states=states)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceAPIApi->get_invoices_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterpart_contact_id** | **int**| Unique identifier of the counterpart contact | [optional] 
 **issued_date** | **str**| Date of the invoices to be retrieved | [optional] 
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **property_id** | **int**| Unique identifier of the property an invoice belongs to | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 
 **states** | [**list[str]**](str.md)| States of the invoices to be retrieved | [optional] 

### Return type

[**PageOfInvoiceDto**](PageOfInvoiceDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_using_put**
> InvoiceDto update_invoice_using_put(body, invoice_id)

Update an invoice based on provided fields

Update invoice

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
api_instance = impower_client.InvoiceAPIApi(impower_client.ApiClient(configuration))
body = impower_client.InvoiceUpdateDto() # InvoiceUpdateDto | updateDto
invoice_id = 789 # int | Unique id of an invoice

try:
    # Update an invoice based on provided fields
    api_response = api_instance.update_invoice_using_put(body, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceAPIApi->update_invoice_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceUpdateDto**](InvoiceUpdateDto.md)| updateDto | 
 **invoice_id** | **int**| Unique id of an invoice | 

### Return type

[**InvoiceDto**](InvoiceDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_invoice_using_post**
> InvoiceDto upload_invoice_using_post(file)

Upload invoice PDF document

By default, the document will go though an OCR analysis

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
api_instance = impower_client.InvoiceAPIApi(impower_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Upload invoice PDF document
    api_response = api_instance.upload_invoice_using_post(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceAPIApi->upload_invoice_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**InvoiceDto**](InvoiceDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

