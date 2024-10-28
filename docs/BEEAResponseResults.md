# BEEAResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bee_affidavit** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**BEEAResponseResultsDetails**](BEEAResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.beea_response_results import BEEAResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of BEEAResponseResults from a JSON string
beea_response_results_instance = BEEAResponseResults.from_json(json)
# print the JSON string representation of the object
print(BEEAResponseResults.to_json())

# convert the object into a dict
beea_response_results_dict = beea_response_results_instance.to_dict()
# create an instance of BEEAResponseResults from a dict
beea_response_results_from_dict = BEEAResponseResults.from_dict(beea_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


