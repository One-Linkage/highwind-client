# BEECResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**BEECResponseResults**](BEECResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.beec_response import BEECResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BEECResponse from a JSON string
beec_response_instance = BEECResponse.from_json(json)
# print the JSON string representation of the object
print(BEECResponse.to_json())

# convert the object into a dict
beec_response_dict = beec_response_instance.to_dict()
# create an instance of BEECResponse from a dict
beec_response_from_dict = BEECResponse.from_dict(beec_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


