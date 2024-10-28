# BCLResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bank_confirmation_letter** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**BCLResponseResultsDetails**](BCLResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.bcl_response_results import BCLResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of BCLResponseResults from a JSON string
bcl_response_results_instance = BCLResponseResults.from_json(json)
# print the JSON string representation of the object
print(BCLResponseResults.to_json())

# convert the object into a dict
bcl_response_results_dict = bcl_response_results_instance.to_dict()
# create an instance of BCLResponseResults from a dict
bcl_response_results_from_dict = BCLResponseResults.from_dict(bcl_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


