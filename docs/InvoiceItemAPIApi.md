# impower_client.InvoiceItemAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_invoice_item_using_put**](InvoiceItemAPIApi.md#update_invoice_item_using_put) | **PUT** /v2/invoice-items/{invoiceItemId} | Update booking text of the given invoice booking item

# **update_invoice_item_using_put**
> InvoiceItemDto update_invoice_item_using_put(body, invoice_item_id)

Update booking text of the given invoice booking item

Update booking text

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
api_instance = impower_client.InvoiceItemAPIApi(impower_client.ApiClient(configuration))
body = impower_client.InvoiceItemUpdateDto() # InvoiceItemUpdateDto | updateDto
invoice_item_id = 789 # int | Unique id of invoice booking item

try:
    # Update booking text of the given invoice booking item
    api_response = api_instance.update_invoice_item_using_put(body, invoice_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceItemAPIApi->update_invoice_item_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceItemUpdateDto**](InvoiceItemUpdateDto.md)| updateDto | 
 **invoice_item_id** | **int**| Unique id of invoice booking item | 

### Return type

[**InvoiceItemDto**](InvoiceItemDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

