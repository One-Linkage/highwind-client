# BEEAResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | [**BEEAResponseResultsDetailsFullName**](BEEAResponseResultsDetailsFullName.md) |  | [optional] 
**id_number** | [**BEEAResponseResultsDetailsIdNumber**](BEEAResponseResultsDetailsIdNumber.md) |  | [optional] 
**deponent_signature** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**deponent_signature_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**enterprise_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**enterprise_registration_number** | [**BCLResponseResultsDetailsBankBranchCode**](BCLResponseResultsDetailsBankBranchCode.md) |  | [optional] 
**nature_of_business** | [**BCLResponseResultsDetailsVerificationStatement**](BCLResponseResultsDetailsVerificationStatement.md) |  | [optional] 
**commissioner_of_oaths_stamp_signature** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**commissioner_of_oaths_stamp_signature_date** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**black_ownership_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_ownership_female_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_ownership_designated_group_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipDesignatedGroupPercentage**](BEEAResponseResultsDetailsBlackOwnershipDesignatedGroupPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_youth** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_disabled** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_unemployed** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_rural** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_veterans** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 

## Example

```python
from highwind_client.models.beea_response_results_details import BEEAResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BEEAResponseResultsDetails from a JSON string
beea_response_results_details_instance = BEEAResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(BEEAResponseResultsDetails.to_json())

# convert the object into a dict
beea_response_results_details_dict = beea_response_results_details_instance.to_dict()
# create an instance of BEEAResponseResultsDetails from a dict
beea_response_results_details_from_dict = BEEAResponseResultsDetails.from_dict(beea_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


