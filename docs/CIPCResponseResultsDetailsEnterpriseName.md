# CIPCResponseResultsDetailsEnterpriseName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.cipc_response_results_details_enterprise_name import CIPCResponseResultsDetailsEnterpriseName

# TODO update the JSON string below
json = "{}"
# create an instance of CIPCResponseResultsDetailsEnterpriseName from a JSON string
cipc_response_results_details_enterprise_name_instance = CIPCResponseResultsDetailsEnterpriseName.from_json(json)
# print the JSON string representation of the object
print(CIPCResponseResultsDetailsEnterpriseName.to_json())

# convert the object into a dict
cipc_response_results_details_enterprise_name_dict = cipc_response_results_details_enterprise_name_instance.to_dict()
# create an instance of CIPCResponseResultsDetailsEnterpriseName from a dict
cipc_response_results_details_enterprise_name_from_dict = CIPCResponseResultsDetailsEnterpriseName.from_dict(cipc_response_results_details_enterprise_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


