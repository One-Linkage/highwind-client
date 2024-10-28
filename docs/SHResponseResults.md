# SHResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_shareholders_certificate** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**SHResponseResultsDetails**](SHResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.sh_response_results import SHResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of SHResponseResults from a JSON string
sh_response_results_instance = SHResponseResults.from_json(json)
# print the JSON string representation of the object
print(SHResponseResults.to_json())

# convert the object into a dict
sh_response_results_dict = sh_response_results_instance.to_dict()
# create an instance of SHResponseResults from a dict
sh_response_results_from_dict = SHResponseResults.from_dict(sh_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


