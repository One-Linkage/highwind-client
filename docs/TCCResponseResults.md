# TCCResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_tax_clearance_certificate** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**TCCResponseResultsDetails**](TCCResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.tcc_response_results import TCCResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of TCCResponseResults from a JSON string
tcc_response_results_instance = TCCResponseResults.from_json(json)
# print the JSON string representation of the object
print(TCCResponseResults.to_json())

# convert the object into a dict
tcc_response_results_dict = tcc_response_results_instance.to_dict()
# create an instance of TCCResponseResults from a dict
tcc_response_results_from_dict = TCCResponseResults.from_dict(tcc_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


