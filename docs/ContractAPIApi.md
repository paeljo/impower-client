# impower_client.ContractAPIApi

All URIs are relative to *https://api.app.impower.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_by_id_using_get**](ContractAPIApi.md#get_contract_by_id_using_get) | **GET** /v2/contracts/{contractId} | Get a contract by the given id
[**get_contracts_by_filter_using_get**](ContractAPIApi.md#get_contracts_by_filter_using_get) | **GET** /v2/contracts | Get contracts by the given filter parameters

# **get_contract_by_id_using_get**
> ContractDto get_contract_by_id_using_get(contract_id)

Get a contract by the given id

Retrieves a contract by the given id

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
api_instance = impower_client.ContractAPIApi(impower_client.ApiClient(configuration))
contract_id = 789 # int | Unique identifier of a contract

try:
    # Get a contract by the given id
    api_response = api_instance.get_contract_by_id_using_get(contract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractAPIApi->get_contract_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| Unique identifier of a contract | 

### Return type

[**ContractDto**](ContractDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts_by_filter_using_get**
> PageOfContractDto get_contracts_by_filter_using_get(contact_id=contact_id, contract_ids=contract_ids, order=order, page=page, property_id=property_id, size=size, sort=sort, type=type, unit_id=unit_id, valid_at_date=valid_at_date)

Get contracts by the given filter parameters

Retrieve contracts by the given filter parameters

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
api_instance = impower_client.ContractAPIApi(impower_client.ApiClient(configuration))
contact_id = 789 # int | ID of the contact instance the contract is associated with. (optional)
contract_ids = [56] # list[int] | List of contract ids to filter contracts by. (optional)
order = 'order_example' # str | Sorting direction. Possible values: ASC, DESC (optional)
page = 56 # int | Page number to be returned (optional)
property_id = 789 # int | ID of the property instance the contract belongs to. (optional)
size = 56 # int | Number of items to be returned in single page (optional)
sort = 'sort_example' # str | Sorting parameter (optional)
type = 'type_example' # str | Type of the contract. Options: OWNER | TENANT | TENANT_VACANCY | PROPERTY_OWNER (optional)
unit_id = 789 # int | ID of the unit instance the contract is associated with. (optional)
valid_at_date = 'valid_at_date_example' # str | Return valid contracts at date. Null is interpreted as beginning/end of time. (optional)

try:
    # Get contracts by the given filter parameters
    api_response = api_instance.get_contracts_by_filter_using_get(contact_id=contact_id, contract_ids=contract_ids, order=order, page=page, property_id=property_id, size=size, sort=sort, type=type, unit_id=unit_id, valid_at_date=valid_at_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractAPIApi->get_contracts_by_filter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of the contact instance the contract is associated with. | [optional] 
 **contract_ids** | [**list[int]**](int.md)| List of contract ids to filter contracts by. | [optional] 
 **order** | **str**| Sorting direction. Possible values: ASC, DESC | [optional] 
 **page** | **int**| Page number to be returned | [optional] 
 **property_id** | **int**| ID of the property instance the contract belongs to. | [optional] 
 **size** | **int**| Number of items to be returned in single page | [optional] 
 **sort** | **str**| Sorting parameter | [optional] 
 **type** | **str**| Type of the contract. Options: OWNER | TENANT | TENANT_VACANCY | PROPERTY_OWNER | [optional] 
 **unit_id** | **int**| ID of the unit instance the contract is associated with. | [optional] 
 **valid_at_date** | **str**| Return valid contracts at date. Null is interpreted as beginning/end of time. | [optional] 

### Return type

[**PageOfContractDto**](PageOfContractDto.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

