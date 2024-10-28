# POAResponseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_proof_of_address** | **bool** |  | [optional] 
**pages_processed** | **int** |  | [optional] 
**details** | [**POAResponseResultsDetails**](POAResponseResultsDetails.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.poa_response_results import POAResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of POAResponseResults from a JSON string
poa_response_results_instance = POAResponseResults.from_json(json)
# print the JSON string representation of the object
print(POAResponseResults.to_json())

# convert the object into a dict
poa_response_results_dict = poa_response_results_instance.to_dict()
# create an instance of POAResponseResults from a dict
poa_response_results_from_dict = POAResponseResults.from_dict(poa_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


