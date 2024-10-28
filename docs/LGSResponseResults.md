# LGSResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_certified_lgs** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**LGSResponseResultsDetails**](LGSResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.lgs_response_results import LGSResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of LGSResponseResults from a JSON string
lgs_response_results_instance = LGSResponseResults.from_json(json)
# print the JSON string representation of the object
print(LGSResponseResults.to_json())

# convert the object into a dict
lgs_response_results_dict = lgs_response_results_instance.to_dict()
# create an instance of LGSResponseResults from a dict
lgs_response_results_from_dict = LGSResponseResults.from_dict(lgs_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


