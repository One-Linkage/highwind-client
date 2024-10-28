# IDResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_certified_id** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**IDResponseResultsDetails**](IDResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.id_response_results import IDResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of IDResponseResults from a JSON string
id_response_results_instance = IDResponseResults.from_json(json)
# print the JSON string representation of the object
print(IDResponseResults.to_json())

# convert the object into a dict
id_response_results_dict = id_response_results_instance.to_dict()
# create an instance of IDResponseResults from a dict
id_response_results_from_dict = IDResponseResults.from_dict(id_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


