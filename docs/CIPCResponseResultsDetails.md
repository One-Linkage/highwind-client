# CIPCResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_issue_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**certificate_type** | [**CIPCResponseResultsDetailsCertificateType**](CIPCResponseResultsDetailsCertificateType.md) |  | [optional] 
**enterprise_name** | [**CIPCResponseResultsDetailsEnterpriseName**](CIPCResponseResultsDetailsEnterpriseName.md) |  | [optional] 
**registration_number** | [**CIPCResponseResultsDetailsRegistrationNumber**](CIPCResponseResultsDetailsRegistrationNumber.md) |  | [optional] 
**registration_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**business_start_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**enterprise_type** | [**CIPCResponseResultsDetailsEnterpriseType**](CIPCResponseResultsDetailsEnterpriseType.md) |  | [optional] 
**enterprise_status** | [**CIPCResponseResultsDetailsEnterpriseStatus**](CIPCResponseResultsDetailsEnterpriseStatus.md) |  | [optional] 
**financial_year_end** | [**CIPCResponseResultsDetailsFinancialYearEnd**](CIPCResponseResultsDetailsFinancialYearEnd.md) |  | [optional] 
**tax_number_optional** | [**CIPCResponseResultsDetailsTaxNumberOptional**](CIPCResponseResultsDetailsTaxNumberOptional.md) |  | [optional] 
**enterprise_postal_address** | [**CIPCResponseResultsDetailsEnterprisePostalAddress**](CIPCResponseResultsDetailsEnterprisePostalAddress.md) |  | [optional] 
**enterprise_address_of_registered_office** | [**LGSResponseResultsDetailsCompanyAddress**](LGSResponseResultsDetailsCompanyAddress.md) |  | [optional] 
**director_full_names** | [**BEEAResponseResultsDetailsFullName**](BEEAResponseResultsDetailsFullName.md) |  | [optional] 
**date_of_birth_or_id_number** | [**CIPCResponseResultsDetailsDateOfBirthOrIdNumber**](CIPCResponseResultsDetailsDateOfBirthOrIdNumber.md) |  | [optional] 

## Example

```python
from highwind_client.models.cipc_response_results_details import CIPCResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CIPCResponseResultsDetails from a JSON string
cipc_response_results_details_instance = CIPCResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(CIPCResponseResultsDetails.to_json())

# convert the object into a dict
cipc_response_results_details_dict = cipc_response_results_details_instance.to_dict()
# create an instance of CIPCResponseResultsDetails from a dict
cipc_response_results_details_from_dict = CIPCResponseResultsDetails.from_dict(cipc_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


