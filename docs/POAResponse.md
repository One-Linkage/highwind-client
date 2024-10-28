# POAResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**POAResponseResults**](POAResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.poa_response import POAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of POAResponse from a JSON string
poa_response_instance = POAResponse.from_json(json)
# print the JSON string representation of the object
print(POAResponse.to_json())

# convert the object into a dict
poa_response_dict = poa_response_instance.to_dict()
# create an instance of POAResponse from a dict
poa_response_from_dict = POAResponse.from_dict(poa_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


