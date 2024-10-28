# Model3MBSResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_3_month_bank_statement** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**Model3MBSResponseResultsDetails**](Model3MBSResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.model3_mbs_response_results import Model3MBSResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MBSResponseResults from a JSON string
model3_mbs_response_results_instance = Model3MBSResponseResults.from_json(json)
# print the JSON string representation of the object
print(Model3MBSResponseResults.to_json())

# convert the object into a dict
model3_mbs_response_results_dict = model3_mbs_response_results_instance.to_dict()
# create an instance of Model3MBSResponseResults from a dict
model3_mbs_response_results_from_dict = Model3MBSResponseResults.from_dict(model3_mbs_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


