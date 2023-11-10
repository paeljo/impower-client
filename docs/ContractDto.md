# ContractDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**list[ContactSimpleDto]**](ContactSimpleDto.md) | List of the contacts associated to the contract. | [optional] 
**contract_number** | **str** | Number of the contract. | [optional] 
**created** | **datetime** | Creation time of the contract. | [optional] 
**end_date** | **str** | Date the validity period of the contract ends to. Null is interpreted as end of time. | [optional] 
**id** | **int** | ID of the contract instance. | [optional] 
**name** | **str** | Name of the contract consisting of the unit key and name of the mailing contact. | [optional] 
**property_id** | **int** | ID of the property instance the contract belongs to. | [optional] 
**start_date** | **str** | Date the validity period of the contract starts from. Null is interpreted as beginning of time. | [optional] 
**type** | **str** | Type of the contract.  1. OWNER - a contract of such type proves ownership of the unit.  2. TENANT - represents an agreement between a unit owner and a tenant.  3. TENANT_VACANCY - used for vacancy periods of a unit.  4. PROPERTY_OWNER - a contract of such type proves ownership of the property. | [optional] 
**unit_id** | **int** | ID of the unit instance the contract belongs to. | [optional] 
**updated** | **datetime** | Last update time of the contract. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

