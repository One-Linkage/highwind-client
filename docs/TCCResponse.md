# TCCResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**TCCResponseResults**](TCCResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.tcc_response import TCCResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TCCResponse from a JSON string
tcc_response_instance = TCCResponse.from_json(json)
# print the JSON string representation of the object
print(TCCResponse.to_json())

# convert the object into a dict
tcc_response_dict = tcc_response_instance.to_dict()
# create an instance of TCCResponse from a dict
tcc_response_from_dict = TCCResponse.from_dict(tcc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


