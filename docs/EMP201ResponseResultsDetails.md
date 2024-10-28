# EMP201ResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emp201_text_top_right_corner** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**company_trading_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**paye_reference_number** | [**EMP201ResponseResultsDetailsPayeReferenceNumber**](EMP201ResponseResultsDetailsPayeReferenceNumber.md) |  | [optional] 
**sdl_reference_number_optional** | [**EMP201ResponseResultsDetailsSdlReferenceNumberOptional**](EMP201ResponseResultsDetailsSdlReferenceNumberOptional.md) |  | [optional] 
**uif_reference_number** | [**EMP201ResponseResultsDetailsPayeReferenceNumber**](EMP201ResponseResultsDetailsPayeReferenceNumber.md) |  | [optional] 
**declaration_date** | [**EMP201ResponseResultsDetailsDeclarationDate**](EMP201ResponseResultsDetailsDeclarationDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**certificate_number_bottom_left_corner** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**company_trading_contact_details** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.emp201_response_results_details import EMP201ResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EMP201ResponseResultsDetails from a JSON string
emp201_response_results_details_instance = EMP201ResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(EMP201ResponseResultsDetails.to_json())

# convert the object into a dict
emp201_response_results_details_dict = emp201_response_results_details_instance.to_dict()
# create an instance of EMP201ResponseResultsDetails from a dict
emp201_response_results_details_from_dict = EMP201ResponseResultsDetails.from_dict(emp201_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


