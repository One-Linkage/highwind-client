# IResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_invoice** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**IResponseResultsDetails**](IResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.i_response_results import IResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of IResponseResults from a JSON string
i_response_results_instance = IResponseResults.from_json(json)
# print the JSON string representation of the object
print(IResponseResults.to_json())

# convert the object into a dict
i_response_results_dict = i_response_results_instance.to_dict()
# create an instance of IResponseResults from a dict
i_response_results_from_dict = IResponseResults.from_dict(i_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


