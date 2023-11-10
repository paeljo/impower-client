# PropertyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Creation time of the property instance. | [optional] 
**id** | **int** | ID of the property instance. | [optional] 
**name** | **str** | Name of the property instance. | [optional] 
**property_hr_id** | **str** | Human readable id of the property instance. | [optional] 
**state** | **str** | Current state of the property.  1. DRAFT - property not activated yet, therefore no bookings/bank orders/reports can be generated.  2. READY - property has been activated and can be used for bookings/bank orders/reports generation.  3. DISABLED - property has been deactivated, and can no longer generate bookings/bank orders/reports.  | [optional] 
**type** | **str** | Administration type of the property. OWNER - Home Owner Association. RENTAL - Tenant Management. | [optional] 
**updated** | **datetime** | Update time of the property instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

