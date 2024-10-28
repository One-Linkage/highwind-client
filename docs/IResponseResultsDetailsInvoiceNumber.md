# IResponseResultsDetailsInvoiceNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.i_response_results_details_invoice_number import IResponseResultsDetailsInvoiceNumber

# TODO update the JSON string below
json = "{}"
# create an instance of IResponseResultsDetailsInvoiceNumber from a JSON string
i_response_results_details_invoice_number_instance = IResponseResultsDetailsInvoiceNumber.from_json(json)
# print the JSON string representation of the object
print(IResponseResultsDetailsInvoiceNumber.to_json())

# convert the object into a dict
i_response_results_details_invoice_number_dict = i_response_results_details_invoice_number_instance.to_dict()
# create an instance of IResponseResultsDetailsInvoiceNumber from a dict
i_response_results_details_invoice_number_from_dict = IResponseResultsDetailsInvoiceNumber.from_dict(i_response_results_details_invoice_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


