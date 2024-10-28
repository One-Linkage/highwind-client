# AFSResponseResultsDetailsCompanyName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.afs_response_results_details_company_name import AFSResponseResultsDetailsCompanyName

# TODO update the JSON string below
json = "{}"
# create an instance of AFSResponseResultsDetailsCompanyName from a JSON string
afs_response_results_details_company_name_instance = AFSResponseResultsDetailsCompanyName.from_json(json)
# print the JSON string representation of the object
print(AFSResponseResultsDetailsCompanyName.to_json())

# convert the object into a dict
afs_response_results_details_company_name_dict = afs_response_results_details_company_name_instance.to_dict()
# create an instance of AFSResponseResultsDetailsCompanyName from a dict
afs_response_results_details_company_name_from_dict = AFSResponseResultsDetailsCompanyName.from_dict(afs_response_results_details_company_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


