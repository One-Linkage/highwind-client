# Model3MMARResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_of_profit_and_loss** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**balance_sheet** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**cash_flow_statement** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**statement_date_period** | [**Model3MBSResponseResultsDetailsStatementDatePeriod**](Model3MBSResponseResultsDetailsStatementDatePeriod.md) |  | [optional] 
**report_date** | [**Model3MMARResponseResultsDetailsReportDate**](Model3MMARResponseResultsDetailsReportDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**statement_covers_3_months** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.model3_mmar_response_results_details import Model3MMARResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MMARResponseResultsDetails from a JSON string
model3_mmar_response_results_details_instance = Model3MMARResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(Model3MMARResponseResultsDetails.to_json())

# convert the object into a dict
model3_mmar_response_results_details_dict = model3_mmar_response_results_details_instance.to_dict()
# create an instance of Model3MMARResponseResultsDetails from a dict
model3_mmar_response_results_details_from_dict = Model3MMARResponseResultsDetails.from_dict(model3_mmar_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


