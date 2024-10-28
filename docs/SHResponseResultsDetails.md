# SHResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**company_shareholder_names** | [**SHResponseResultsDetailsCompanyShareholderNames**](SHResponseResultsDetailsCompanyShareholderNames.md) |  | [optional] 
**company_shareholder_id_numbers** | [**SHResponseResultsDetailsCompanyShareholderIdNumbers**](SHResponseResultsDetailsCompanyShareholderIdNumbers.md) |  | [optional] 
**shareholder_number_of_shares** | [**SHResponseResultsDetailsShareholderNumberOfShares**](SHResponseResultsDetailsShareholderNumberOfShares.md) |  | [optional] 
**certificate_number** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**certificate_issue_date** | [**RLResponseResultsDetailsServicesProductRenderedDate**](RLResponseResultsDetailsServicesProductRenderedDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**authorised_signature** | [**SHResponseResultsDetailsAuthorisedSignature**](SHResponseResultsDetailsAuthorisedSignature.md) |  | [optional] 

## Example

```python
from highwind_client.models.sh_response_results_details import SHResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SHResponseResultsDetails from a JSON string
sh_response_results_details_instance = SHResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(SHResponseResultsDetails.to_json())

# convert the object into a dict
sh_response_results_details_dict = sh_response_results_details_instance.to_dict()
# create an instance of SHResponseResultsDetails from a dict
sh_response_results_details_from_dict = SHResponseResultsDetails.from_dict(sh_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


