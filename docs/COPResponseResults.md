# COPResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_company_profile** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**COPResponseResultsDetails**](COPResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.cop_response_results import COPResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of COPResponseResults from a JSON string
cop_response_results_instance = COPResponseResults.from_json(json)
# print the JSON string representation of the object
print(COPResponseResults.to_json())

# convert the object into a dict
cop_response_results_dict = cop_response_results_instance.to_dict()
# create an instance of COPResponseResults from a dict
cop_response_results_from_dict = COPResponseResults.from_dict(cop_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


