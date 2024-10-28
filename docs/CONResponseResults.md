# CONResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_contract** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**CONResponseResultsDetails**](CONResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.con_response_results import CONResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of CONResponseResults from a JSON string
con_response_results_instance = CONResponseResults.from_json(json)
# print the JSON string representation of the object
print(CONResponseResults.to_json())

# convert the object into a dict
con_response_results_dict = con_response_results_instance.to_dict()
# create an instance of CONResponseResults from a dict
con_response_results_from_dict = CONResponseResults.from_dict(con_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


