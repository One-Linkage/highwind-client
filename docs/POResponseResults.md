# POResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_purchase_order** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**POResponseResultsDetails**](POResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.po_response_results import POResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of POResponseResults from a JSON string
po_response_results_instance = POResponseResults.from_json(json)
# print the JSON string representation of the object
print(POResponseResults.to_json())

# convert the object into a dict
po_response_results_dict = po_response_results_instance.to_dict()
# create an instance of POResponseResults from a dict
po_response_results_from_dict = POResponseResults.from_dict(po_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


