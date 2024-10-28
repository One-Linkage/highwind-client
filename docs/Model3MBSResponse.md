# Model3MBSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**Model3MBSResponseResults**](Model3MBSResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.model3_mbs_response import Model3MBSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MBSResponse from a JSON string
model3_mbs_response_instance = Model3MBSResponse.from_json(json)
# print the JSON string representation of the object
print(Model3MBSResponse.to_json())

# convert the object into a dict
model3_mbs_response_dict = model3_mbs_response_instance.to_dict()
# create an instance of Model3MBSResponse from a dict
model3_mbs_response_from_dict = Model3MBSResponse.from_dict(model3_mbs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


