# POResponseResultsDetailsCustomerName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.po_response_results_details_customer_name import POResponseResultsDetailsCustomerName

# TODO update the JSON string below
json = "{}"
# create an instance of POResponseResultsDetailsCustomerName from a JSON string
po_response_results_details_customer_name_instance = POResponseResultsDetailsCustomerName.from_json(json)
# print the JSON string representation of the object
print(POResponseResultsDetailsCustomerName.to_json())

# convert the object into a dict
po_response_results_details_customer_name_dict = po_response_results_details_customer_name_instance.to_dict()
# create an instance of POResponseResultsDetailsCustomerName from a dict
po_response_results_details_customer_name_from_dict = POResponseResultsDetailsCustomerName.from_dict(po_response_results_details_customer_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


