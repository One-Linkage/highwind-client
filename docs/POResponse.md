# POResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**POResponseResults**](POResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.po_response import POResponse

# TODO update the JSON string below
json = "{}"
# create an instance of POResponse from a JSON string
po_response_instance = POResponse.from_json(json)
# print the JSON string representation of the object
print(POResponse.to_json())

# convert the object into a dict
po_response_dict = po_response_instance.to_dict()
# create an instance of POResponse from a dict
po_response_from_dict = POResponse.from_dict(po_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


