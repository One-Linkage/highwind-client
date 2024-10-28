# BEEAResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**BEEAResponseResults**](BEEAResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.beea_response import BEEAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BEEAResponse from a JSON string
beea_response_instance = BEEAResponse.from_json(json)
# print the JSON string representation of the object
print(BEEAResponse.to_json())

# convert the object into a dict
beea_response_dict = beea_response_instance.to_dict()
# create an instance of BEEAResponse from a dict
beea_response_from_dict = BEEAResponse.from_dict(beea_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


