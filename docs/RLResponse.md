# RLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**RLResponseResults**](RLResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.rl_response import RLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RLResponse from a JSON string
rl_response_instance = RLResponse.from_json(json)
# print the JSON string representation of the object
print(RLResponse.to_json())

# convert the object into a dict
rl_response_dict = rl_response_instance.to_dict()
# create an instance of RLResponse from a dict
rl_response_from_dict = RLResponse.from_dict(rl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


