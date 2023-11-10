# DocumentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Total amount present on the document. | [optional] 
**building_id** | **int** | ID of the building the document belongs to. | [optional] 
**contact_id** | **int** | ID of the contact the document belongs to. | [optional] 
**contract_id** | **int** | ID of the contract the document belongs to. | [optional] 
**created** | **datetime** | Creation time of the document. | [optional] 
**id** | **int** | ID of the document instance. | [optional] 
**issued_date** | **str** | Issued date of the document. | [optional] 
**name** | **str** | Name of the document instance. | [optional] 
**property_hr_id** | **str** | Human readable id of the property the document is assigned to. | [optional] 
**property_id** | **int** | ID of the property the document belongs to. | [optional] 
**property_name** | **str** | Name of the property the document is assigned to. | [optional] 
**source_id** | **int** | ID of the source entity the document belongs to. | [optional] 
**source_type** | **str** | Source type of the document. Together with the id identifies the business process of the same name the document originates from/is attached to. It may be null. | [optional] 
**state** | **str** | State of the document. | [optional] 
**tags** | [**list[DocumentTagSimpleDto]**](DocumentTagSimpleDto.md) |  | [optional] 
**unit_hr_id** | **str** | Human readable id of the unit the document is assigned to. | [optional] 
**unit_id** | **int** | ID of the unit the document belongs to. | [optional] 
**updated** | **datetime** | Last update time of the document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

