# BCLResponseResultsDetailsVerificationStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from highwind_client.models.bcl_response_results_details_verification_statement import BCLResponseResultsDetailsVerificationStatement

# TODO update the JSON string below
json = "{}"
# create an instance of BCLResponseResultsDetailsVerificationStatement from a JSON string
bcl_response_results_details_verification_statement_instance = BCLResponseResultsDetailsVerificationStatement.from_json(json)
# print the JSON string representation of the object
print(BCLResponseResultsDetailsVerificationStatement.to_json())

# convert the object into a dict
bcl_response_results_details_verification_statement_dict = bcl_response_results_details_verification_statement_instance.to_dict()
# create an instance of BCLResponseResultsDetailsVerificationStatement from a dict
bcl_response_results_details_verification_statement_from_dict = BCLResponseResultsDetailsVerificationStatement.from_dict(bcl_response_results_details_verification_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


