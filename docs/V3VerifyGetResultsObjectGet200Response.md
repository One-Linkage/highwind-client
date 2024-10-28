# V3VerifyGetResultsObjectGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**POResponseResults**](POResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.v3_verify_get_results_object_get200_response import V3VerifyGetResultsObjectGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V3VerifyGetResultsObjectGet200Response from a JSON string
v3_verify_get_results_object_get200_response_instance = V3VerifyGetResultsObjectGet200Response.from_json(json)
# print the JSON string representation of the object
print(V3VerifyGetResultsObjectGet200Response.to_json())

# convert the object into a dict
v3_verify_get_results_object_get200_response_dict = v3_verify_get_results_object_get200_response_instance.to_dict()
# create an instance of V3VerifyGetResultsObjectGet200Response from a dict
v3_verify_get_results_object_get200_response_from_dict = V3VerifyGetResultsObjectGet200Response.from_dict(v3_verify_get_results_object_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


