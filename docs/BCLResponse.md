# BCLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**BCLResponseResults**](BCLResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.bcl_response import BCLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BCLResponse from a JSON string
bcl_response_instance = BCLResponse.from_json(json)
# print the JSON string representation of the object
print(BCLResponse.to_json())

# convert the object into a dict
bcl_response_dict = bcl_response_instance.to_dict()
# create an instance of BCLResponse from a dict
bcl_response_from_dict = BCLResponse.from_dict(bcl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


