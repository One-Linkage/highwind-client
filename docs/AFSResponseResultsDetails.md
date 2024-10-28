# AFSResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | [**AFSResponseResultsDetailsCompanyName**](AFSResponseResultsDetailsCompanyName.md) |  | [optional] 
**company_registration_number** | [**AFSResponseResultsDetailsCompanyRegistrationNumber**](AFSResponseResultsDetailsCompanyRegistrationNumber.md) |  | [optional] 
**period** | [**AFSResponseResultsDetailsPeriod**](AFSResponseResultsDetailsPeriod.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**statement_of_financial_position** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**statement_of_profit_and_loss** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**statement_of_changes_in_equity** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**statement_of_cash_flow** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**director_name** | [**AFSResponseResultsDetailsDirectorName**](AFSResponseResultsDetailsDirectorName.md) |  | [optional] 
**director_signature** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**accountant_name** | [**AFSResponseResultsDetailsAccountantName**](AFSResponseResultsDetailsAccountantName.md) |  | [optional] 
**accountant_signature** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.afs_response_results_details import AFSResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AFSResponseResultsDetails from a JSON string
afs_response_results_details_instance = AFSResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(AFSResponseResultsDetails.to_json())

# convert the object into a dict
afs_response_results_details_dict = afs_response_results_details_instance.to_dict()
# create an instance of AFSResponseResultsDetails from a dict
afs_response_results_details_from_dict = AFSResponseResultsDetails.from_dict(afs_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


