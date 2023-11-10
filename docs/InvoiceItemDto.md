# InvoiceItemDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_code** | **str** | Account code of the booking item. | [optional] 
**account_id** | **int** | Account id of the booking item. | [optional] 
**account_name** | **str** | Account name of the booking item. | [optional] 
**amount** | **float** | Amount corresponding to the booking item. | [optional] 
**booking_text** | **str** | Booking text of the booking item. | [optional] 
**created** | **datetime** | Creation time of the invoice item. | [optional] 
**id** | **int** | Unique identifier of the booking item. | [optional] 
**labor_cost_amount** | **float** | Amount relevant for income tax declaration according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html). | [optional] 
**labor_cost_type** | **str** | Depending on the selected type: percentages of the amounts will be reported on the 35a annexes of multiple reports according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html).   Ex: Housemoney Settlement (Hausgeldabrechnung) or Opscost Report (Nebenkostenabrechnung).   1. HOUSEHOLD_RELATED_SERVICES - haushaltsnahe Dienstleistungen  2. TECHNICIAN_SERVICE - haushaltsnahe Handwerkerleistungen  3. MARGINAL_EMPLOYMENT - haushaltsnahe geringfügige Beschäftigungsverhältnisse  4. INSURABLE_EMPLOYMENT - sozialversicherungspflichtigen haushaltsnahen Beschäftigungsverhältnissen | [optional] 
**updated** | **datetime** | Last update time of the invoice item. | [optional] 
**vat_amount** | **float** | Corresponding vat amount of the booking item. | [optional] 
**vat_percentage** | **float** | Corresponding vat percentage of the vat amount of the total amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

