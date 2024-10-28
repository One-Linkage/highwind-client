# SHResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**SHResponseResults**](SHResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.sh_response import SHResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SHResponse from a JSON string
sh_response_instance = SHResponse.from_json(json)
# print the JSON string representation of the object
print(SHResponse.to_json())

# convert the object into a dict
sh_response_dict = sh_response_instance.to_dict()
# create an instance of SHResponse from a dict
sh_response_from_dict = SHResponse.from_dict(sh_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


