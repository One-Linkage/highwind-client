# TCCResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**company_address** | [**LGSResponseResultsDetailsCompanyAddress**](LGSResponseResultsDetailsCompanyAddress.md) |  | [optional] 
**taxpayer_name** | [**BEEAResponseResultsDetailsFullName**](BEEAResponseResultsDetailsFullName.md) |  | [optional] 
**taxpayer_reference_number** | [**TCCResponseResultsDetailsTaxpayerReferenceNumber**](TCCResponseResultsDetailsTaxpayerReferenceNumber.md) |  | [optional] 
**issue_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**tax_pin_number** | [**BEECResponseResultsDetailsEnterpriseRegistrationNumber**](BEECResponseResultsDetailsEnterpriseRegistrationNumber.md) |  | [optional] 
**tax_pin_expiry_date** | [**EMP201ResponseResultsDetailsDeclarationDate**](EMP201ResponseResultsDetailsDeclarationDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**tax_compliance_status** | [**TCCResponseResultsDetailsTaxComplianceStatus**](TCCResponseResultsDetailsTaxComplianceStatus.md) |  | [optional] 
**purpose_of_request** | [**TCCResponseResultsDetailsPurposeOfRequest**](TCCResponseResultsDetailsPurposeOfRequest.md) |  | [optional] 
**request_reference_number** | [**TCCResponseResultsDetailsRequestReferenceNumber**](TCCResponseResultsDetailsRequestReferenceNumber.md) |  | [optional] 
**tax_compliance_status_text_position** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.tcc_response_results_details import TCCResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TCCResponseResultsDetails from a JSON string
tcc_response_results_details_instance = TCCResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(TCCResponseResultsDetails.to_json())

# convert the object into a dict
tcc_response_results_details_dict = tcc_response_results_details_instance.to_dict()
# create an instance of TCCResponseResultsDetails from a dict
tcc_response_results_details_from_dict = TCCResponseResultsDetails.from_dict(tcc_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


