# AFSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**AFSResponseResults**](AFSResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.afs_response import AFSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AFSResponse from a JSON string
afs_response_instance = AFSResponse.from_json(json)
# print the JSON string representation of the object
print(AFSResponse.to_json())

# convert the object into a dict
afs_response_dict = afs_response_instance.to_dict()
# create an instance of AFSResponse from a dict
afs_response_from_dict = AFSResponse.from_dict(afs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


