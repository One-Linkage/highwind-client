# CONResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**CONResponseResults**](CONResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.con_response import CONResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CONResponse from a JSON string
con_response_instance = CONResponse.from_json(json)
# print the JSON string representation of the object
print(CONResponse.to_json())

# convert the object into a dict
con_response_dict = con_response_instance.to_dict()
# create an instance of CONResponse from a dict
con_response_from_dict = CONResponse.from_dict(con_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


