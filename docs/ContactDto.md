# ContactDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Name of the city. | [optional] 
**company_name** | **str** | Name of the company, in case the contact is a company. | [optional] 
**country** | **str** | Country code according to ISO 3166-1 alpha-2 standard. | [optional] 
**created** | **datetime** | Creation time of the contact. | [optional] 
**details** | [**ContactDetailsDto**](ContactDetailsDto.md) |  | [optional] 
**first_name** | **str** | First name of the contact, in case the contact is a person. | [optional] 
**id** | **int** | ID of the contact instance. | [optional] 
**last_name** | **str** | Last name of the contact, in case the contact is a person. | [optional] 
**number** | **str** | Street number. | [optional] 
**postal_code** | **str** | Postal or zip code. Ensure it is specified for every person requiring physical letter contact via e-post. | [optional] 
**recipient_name** | **str** | Recipient name of the contact. | [optional] 
**salutation** | **str** | A standard formula of words used to address the contact. | [optional] 
**state** | **str** | State name, also called province, subdivision, or region. | [optional] 
**street** | **str** | Name of the street. | [optional] 
**title** | **str** | Job title of the contact. | [optional] 
**updated** | **datetime** | Last update time of the contact. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

