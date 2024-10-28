# Model3MMARResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**Model3MMARResponseResults**](Model3MMARResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.model3_mmar_response import Model3MMARResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MMARResponse from a JSON string
model3_mmar_response_instance = Model3MMARResponse.from_json(json)
# print the JSON string representation of the object
print(Model3MMARResponse.to_json())

# convert the object into a dict
model3_mmar_response_dict = model3_mmar_response_instance.to_dict()
# create an instance of Model3MMARResponse from a dict
model3_mmar_response_from_dict = Model3MMARResponse.from_dict(model3_mmar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


