# IDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**IDResponseResults**](IDResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.id_response import IDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IDResponse from a JSON string
id_response_instance = IDResponse.from_json(json)
# print the JSON string representation of the object
print(IDResponse.to_json())

# convert the object into a dict
id_response_dict = id_response_instance.to_dict()
# create an instance of IDResponse from a dict
id_response_from_dict = IDResponse.from_dict(id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


