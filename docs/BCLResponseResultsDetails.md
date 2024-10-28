# BCLResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | [**Model3MBSResponseResultsDetailsBankName**](Model3MBSResponseResultsDetailsBankName.md) |  | [optional] 
**bank_branch_code** | [**BCLResponseResultsDetailsBankBranchCode**](BCLResponseResultsDetailsBankBranchCode.md) |  | [optional] 
**company_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**company_account_number** | [**BCLResponseResultsDetailsBankBranchCode**](BCLResponseResultsDetailsBankBranchCode.md) |  | [optional] 
**date_issued** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**verification_statement** | [**BCLResponseResultsDetailsVerificationStatement**](BCLResponseResultsDetailsVerificationStatement.md) |  | [optional] 

## Example

```python
from highwind_client.models.bcl_response_results_details import BCLResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BCLResponseResultsDetails from a JSON string
bcl_response_results_details_instance = BCLResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(BCLResponseResultsDetails.to_json())

# convert the object into a dict
bcl_response_results_details_dict = bcl_response_results_details_instance.to_dict()
# create an instance of BCLResponseResultsDetails from a dict
bcl_response_results_details_from_dict = BCLResponseResultsDetails.from_dict(bcl_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


