# BEECResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bee_certificate** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**BEECResponseResultsDetails**](BEECResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.beec_response_results import BEECResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of BEECResponseResults from a JSON string
beec_response_results_instance = BEECResponseResults.from_json(json)
# print the JSON string representation of the object
print(BEECResponseResults.to_json())

# convert the object into a dict
beec_response_results_dict = beec_response_results_instance.to_dict()
# create an instance of BEECResponseResults from a dict
beec_response_results_from_dict = BEECResponseResults.from_dict(beec_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


