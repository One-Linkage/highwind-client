# BEECResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**enterprise_registration_number** | [**BEECResponseResultsDetailsEnterpriseRegistrationNumber**](BEECResponseResultsDetailsEnterpriseRegistrationNumber.md) |  | [optional] 
**certificate_number** | [**BEECResponseResultsDetailsEnterpriseRegistrationNumber**](BEECResponseResultsDetailsEnterpriseRegistrationNumber.md) |  | [optional] 
**certificate_issuer_name** | [**BEECResponseResultsDetailsEnterpriseRegistrationNumber**](BEECResponseResultsDetailsEnterpriseRegistrationNumber.md) |  | [optional] 
**certificate_issue_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**certificate_expiry_date** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**total_number_of_shareholders** | [**BEECResponseResultsDetailsTotalNumberOfShareholders**](BEECResponseResultsDetailsTotalNumberOfShareholders.md) |  | [optional] 
**number_of_black_shareholders** | [**BEECResponseResultsDetailsTotalNumberOfShareholders**](BEECResponseResultsDetailsTotalNumberOfShareholders.md) |  | [optional] 
**number_of_white_shareholders** | [**BEECResponseResultsDetailsTotalNumberOfShareholders**](BEECResponseResultsDetailsTotalNumberOfShareholders.md) |  | [optional] 
**black_ownership_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_ownership_female_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**white_ownership_percentage** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_youth** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_disabled** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_unemployed** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_rural** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 
**black_designated_group_owned_percentage_breakdown_veterans** | [**BEEAResponseResultsDetailsBlackOwnershipPercentage**](BEEAResponseResultsDetailsBlackOwnershipPercentage.md) |  | [optional] 

## Example

```python
from highwind_client.models.beec_response_results_details import BEECResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BEECResponseResultsDetails from a JSON string
beec_response_results_details_instance = BEECResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(BEECResponseResultsDetails.to_json())

# convert the object into a dict
beec_response_results_details_dict = beec_response_results_details_instance.to_dict()
# create an instance of BEECResponseResultsDetails from a dict
beec_response_results_details_from_dict = BEECResponseResultsDetails.from_dict(beec_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


