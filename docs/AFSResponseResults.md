# AFSResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_afs** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**AFSResponseResultsDetails**](AFSResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.afs_response_results import AFSResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of AFSResponseResults from a JSON string
afs_response_results_instance = AFSResponseResults.from_json(json)
# print the JSON string representation of the object
print(AFSResponseResults.to_json())

# convert the object into a dict
afs_response_results_dict = afs_response_results_instance.to_dict()
# create an instance of AFSResponseResults from a dict
afs_response_results_from_dict = AFSResponseResults.from_dict(afs_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


