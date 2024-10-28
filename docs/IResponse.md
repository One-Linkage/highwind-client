# IResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**IResponseResults**](IResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.i_response import IResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IResponse from a JSON string
i_response_instance = IResponse.from_json(json)
# print the JSON string representation of the object
print(IResponse.to_json())

# convert the object into a dict
i_response_dict = i_response_instance.to_dict()
# create an instance of IResponse from a dict
i_response_from_dict = IResponse.from_dict(i_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


