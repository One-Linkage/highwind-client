# RLResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_reference_letter** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**RLResponseResultsDetails**](RLResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.rl_response_results import RLResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of RLResponseResults from a JSON string
rl_response_results_instance = RLResponseResults.from_json(json)
# print the JSON string representation of the object
print(RLResponseResults.to_json())

# convert the object into a dict
rl_response_results_dict = rl_response_results_instance.to_dict()
# create an instance of RLResponseResults from a dict
rl_response_results_from_dict = RLResponseResults.from_dict(rl_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


