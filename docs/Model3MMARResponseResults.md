# Model3MMARResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_3_month_management_account_report** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**Model3MMARResponseResultsDetails**](Model3MMARResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.model3_mmar_response_results import Model3MMARResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MMARResponseResults from a JSON string
model3_mmar_response_results_instance = Model3MMARResponseResults.from_json(json)
# print the JSON string representation of the object
print(Model3MMARResponseResults.to_json())

# convert the object into a dict
model3_mmar_response_results_dict = model3_mmar_response_results_instance.to_dict()
# create an instance of Model3MMARResponseResults from a dict
model3_mmar_response_results_from_dict = Model3MMARResponseResults.from_dict(model3_mmar_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


