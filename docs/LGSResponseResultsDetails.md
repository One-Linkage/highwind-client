# LGSResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | [**POResponseResultsDetailsCustomerName**](POResponseResultsDetailsCustomerName.md) |  | [optional] 
**company_address** | [**LGSResponseResultsDetailsCompanyAddress**](LGSResponseResultsDetailsCompanyAddress.md) |  | [optional] 
**company_nature_of_business** | [**BCLResponseResultsDetailsVerificationStatement**](BCLResponseResultsDetailsVerificationStatement.md) |  | [optional] 
**certificate_number** | [**BEECResponseResultsDetailsEnterpriseRegistrationNumber**](BEECResponseResultsDetailsEnterpriseRegistrationNumber.md) |  | [optional] 
**certificate_issue_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**certificate_expiry_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**lgs_in_subject_line** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.lgs_response_results_details import LGSResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LGSResponseResultsDetails from a JSON string
lgs_response_results_details_instance = LGSResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(LGSResponseResultsDetails.to_json())

# convert the object into a dict
lgs_response_results_details_dict = lgs_response_results_details_instance.to_dict()
# create an instance of LGSResponseResultsDetails from a dict
lgs_response_results_details_from_dict = LGSResponseResultsDetails.from_dict(lgs_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


