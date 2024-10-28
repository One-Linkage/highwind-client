# IResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | [**POResponseResultsDetailsCustomerName**](POResponseResultsDetailsCustomerName.md) |  | [optional] 
**vendor_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**invoice_number** | [**IResponseResultsDetailsInvoiceNumber**](IResponseResultsDetailsInvoiceNumber.md) |  | [optional] 
**invoice_date** | [**IResponseResultsDetailsInvoiceDate**](IResponseResultsDetailsInvoiceDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**product_service** | [**POResponseResultsDetailsProductService**](POResponseResultsDetailsProductService.md) |  | [optional] 
**total_amount** | [**IResponseResultsDetailsTotalAmount**](IResponseResultsDetailsTotalAmount.md) |  | [optional] 

## Example

```python
from highwind_client.models.i_response_results_details import IResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IResponseResultsDetails from a JSON string
i_response_results_details_instance = IResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(IResponseResultsDetails.to_json())

# convert the object into a dict
i_response_results_details_dict = i_response_results_details_instance.to_dict()
# create an instance of IResponseResultsDetails from a dict
i_response_results_details_from_dict = IResponseResultsDetails.from_dict(i_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


