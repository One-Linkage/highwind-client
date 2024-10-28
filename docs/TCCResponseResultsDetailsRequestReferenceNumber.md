# TCCResponseResultsDetailsRequestReferenceNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.tcc_response_results_details_request_reference_number import TCCResponseResultsDetailsRequestReferenceNumber

# TODO update the JSON string below
json = "{}"
# create an instance of TCCResponseResultsDetailsRequestReferenceNumber from a JSON string
tcc_response_results_details_request_reference_number_instance = TCCResponseResultsDetailsRequestReferenceNumber.from_json(json)
# print the JSON string representation of the object
print(TCCResponseResultsDetailsRequestReferenceNumber.to_json())

# convert the object into a dict
tcc_response_results_details_request_reference_number_dict = tcc_response_results_details_request_reference_number_instance.to_dict()
# create an instance of TCCResponseResultsDetailsRequestReferenceNumber from a dict
tcc_response_results_details_request_reference_number_from_dict = TCCResponseResultsDetailsRequestReferenceNumber.from_dict(tcc_response_results_details_request_reference_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


