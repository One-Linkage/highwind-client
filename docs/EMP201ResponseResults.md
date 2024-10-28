# EMP201ResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_emp201** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**EMP201ResponseResultsDetails**](EMP201ResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.emp201_response_results import EMP201ResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of EMP201ResponseResults from a JSON string
emp201_response_results_instance = EMP201ResponseResults.from_json(json)
# print the JSON string representation of the object
print(EMP201ResponseResults.to_json())

# convert the object into a dict
emp201_response_results_dict = emp201_response_results_instance.to_dict()
# create an instance of EMP201ResponseResults from a dict
emp201_response_results_from_dict = EMP201ResponseResults.from_dict(emp201_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


