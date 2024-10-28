# AFSResponseResultsDetailsPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.afs_response_results_details_period import AFSResponseResultsDetailsPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of AFSResponseResultsDetailsPeriod from a JSON string
afs_response_results_details_period_instance = AFSResponseResultsDetailsPeriod.from_json(json)
# print the JSON string representation of the object
print(AFSResponseResultsDetailsPeriod.to_json())

# convert the object into a dict
afs_response_results_details_period_dict = afs_response_results_details_period_instance.to_dict()
# create an instance of AFSResponseResultsDetailsPeriod from a dict
afs_response_results_details_period_from_dict = AFSResponseResultsDetailsPeriod.from_dict(afs_response_results_details_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


