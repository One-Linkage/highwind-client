# COPResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**COPResponseResults**](COPResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.cop_response import COPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of COPResponse from a JSON string
cop_response_instance = COPResponse.from_json(json)
# print the JSON string representation of the object
print(COPResponse.to_json())

# convert the object into a dict
cop_response_dict = cop_response_instance.to_dict()
# create an instance of COPResponse from a dict
cop_response_from_dict = COPResponse.from_dict(cop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


