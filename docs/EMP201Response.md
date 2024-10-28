# EMP201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**EMP201ResponseResults**](EMP201ResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.emp201_response import EMP201Response

# TODO update the JSON string below
json = "{}"
# create an instance of EMP201Response from a JSON string
emp201_response_instance = EMP201Response.from_json(json)
# print the JSON string representation of the object
print(EMP201Response.to_json())

# convert the object into a dict
emp201_response_dict = emp201_response_instance.to_dict()
# create an instance of EMP201Response from a dict
emp201_response_from_dict = EMP201Response.from_dict(emp201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


