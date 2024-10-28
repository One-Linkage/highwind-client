# LGSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**results** | [**LGSResponseResults**](LGSResponseResults.md) |  | [optional] 

## Example

```python
from highwind_client.models.lgs_response import LGSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LGSResponse from a JSON string
lgs_response_instance = LGSResponse.from_json(json)
# print the JSON string representation of the object
print(LGSResponse.to_json())

# convert the object into a dict
lgs_response_dict = lgs_response_instance.to_dict()
# create an instance of LGSResponse from a dict
lgs_response_from_dict = LGSResponse.from_dict(lgs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


