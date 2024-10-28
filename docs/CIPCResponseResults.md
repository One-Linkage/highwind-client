# CIPCResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cipc** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**CIPCResponseResultsDetails**](CIPCResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.cipc_response_results import CIPCResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of CIPCResponseResults from a JSON string
cipc_response_results_instance = CIPCResponseResults.from_json(json)
# print the JSON string representation of the object
print(CIPCResponseResults.to_json())

# convert the object into a dict
cipc_response_results_dict = cipc_response_results_instance.to_dict()
# create an instance of CIPCResponseResults from a dict
cipc_response_results_from_dict = CIPCResponseResults.from_dict(cipc_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


