# POResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | [**POResponseResultsDetailsCustomerName**](POResponseResultsDetailsCustomerName.md) |  | [optional] 
**vendor_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**purchase_order_number** | [**POResponseResultsDetailsPurchaseOrderNumber**](POResponseResultsDetailsPurchaseOrderNumber.md) |  | [optional] 
**purchase_order_date** | [**POResponseResultsDetailsPurchaseOrderDate**](POResponseResultsDetailsPurchaseOrderDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**product_service** | [**POResponseResultsDetailsProductService**](POResponseResultsDetailsProductService.md) |  | [optional] 
**total_amount** | [**POResponseResultsDetailsTotalAmount**](POResponseResultsDetailsTotalAmount.md) |  | [optional] 

## Example

```python
from highwind_client.models.po_response_results_details import POResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of POResponseResultsDetails from a JSON string
po_response_results_details_instance = POResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(POResponseResultsDetails.to_json())

# convert the object into a dict
po_response_results_details_dict = po_response_results_details_instance.to_dict()
# create an instance of POResponseResultsDetails from a dict
po_response_results_details_from_dict = POResponseResultsDetails.from_dict(po_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


