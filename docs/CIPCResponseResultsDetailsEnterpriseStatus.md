# CIPCResponseResultsDetailsEnterpriseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.cipc_response_results_details_enterprise_status import CIPCResponseResultsDetailsEnterpriseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CIPCResponseResultsDetailsEnterpriseStatus from a JSON string
cipc_response_results_details_enterprise_status_instance = CIPCResponseResultsDetailsEnterpriseStatus.from_json(json)
# print the JSON string representation of the object
print(CIPCResponseResultsDetailsEnterpriseStatus.to_json())

# convert the object into a dict
cipc_response_results_details_enterprise_status_dict = cipc_response_results_details_enterprise_status_instance.to_dict()
# create an instance of CIPCResponseResultsDetailsEnterpriseStatus from a dict
cipc_response_results_details_enterprise_status_from_dict = CIPCResponseResultsDetailsEnterpriseStatus.from_dict(cipc_response_results_details_enterprise_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


