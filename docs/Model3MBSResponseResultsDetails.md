# Model3MBSResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**bank_name** | [**Model3MBSResponseResultsDetailsBankName**](Model3MBSResponseResultsDetailsBankName.md) |  | [optional] 
**account_number** | [**EMP201ResponseResultsDetailsPayeReferenceNumber**](EMP201ResponseResultsDetailsPayeReferenceNumber.md) |  | [optional] 
**statement_date_period** | [**Model3MBSResponseResultsDetailsStatementDatePeriod**](Model3MBSResponseResultsDetailsStatementDatePeriod.md) |  | [optional] 
**statement_latest_date** | [**EMP201ResponseResultsDetailsDeclarationDate**](EMP201ResponseResultsDetailsDeclarationDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**statement_covers_3_months** | [**Model3MBSResponseResultsDetailsStatementCovers3Months**](Model3MBSResponseResultsDetailsStatementCovers3Months.md) |  | [optional] 

## Example

```python
from highwind_client.models.model3_mbs_response_results_details import Model3MBSResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of Model3MBSResponseResultsDetails from a JSON string
model3_mbs_response_results_details_instance = Model3MBSResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(Model3MBSResponseResultsDetails.to_json())

# convert the object into a dict
model3_mbs_response_results_details_dict = model3_mbs_response_results_details_instance.to_dict()
# create an instance of Model3MBSResponseResultsDetails from a dict
model3_mbs_response_results_details_from_dict = Model3MBSResponseResultsDetails.from_dict(model3_mbs_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


