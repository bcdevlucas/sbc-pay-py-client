# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Links]**](Links.md) |  | [optional] 
**id** | **int** | Unique identifier for invoice | [optional] 
**created_by** | **str** | username of the account | [optional] 
**created_name** | **str** | invoice creation date | [optional] 
**updated_name** | **str** | username of the account | [optional] 
**updated_on** | **str** | invoice update date | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) |  | [optional] 
**paid** | **float** | amount paid | [optional] 
**refund** | **float** | refund amount | [optional] 
**service_fees** | **float** | service fees amount | [optional] 
**total** | **float** | total amount | [optional] 
**references** | [**list[InvoiceReference]**](InvoiceReference.md) |  | [optional] 
**status_code** | **str** | Status of payment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


