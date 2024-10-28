# CIPCResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**CIPCResponseResults**](CIPCResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.cipc_response import CIPCResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CIPCResponse from a JSON string
cipc_response_instance = CIPCResponse.from_json(json)
# print the JSON string representation of the object
print(CIPCResponse.to_json())

# convert the object into a dict
cipc_response_dict = cipc_response_instance.to_dict()
# create an instance of CIPCResponse from a dict
cipc_response_from_dict = CIPCResponse.from_dict(cipc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


