# POAResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_document_type** | [**POAResponseResultsDetailsValidDocumentType**](POAResponseResultsDetailsValidDocumentType.md) |  | [optional] 
**document_date** | [**POAResponseResultsDetailsDocumentDate**](POAResponseResultsDetailsDocumentDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**address_street_number** | [**LGSResponseResultsDetailsCompanyAddress**](LGSResponseResultsDetailsCompanyAddress.md) |  | [optional] 
**address_suburb** | [**POAResponseResultsDetailsAddressSuburb**](POAResponseResultsDetailsAddressSuburb.md) |  | [optional] 
**address_municipal_district_optional** | [**POAResponseResultsDetailsAddressMunicipalDistrictOptional**](POAResponseResultsDetailsAddressMunicipalDistrictOptional.md) |  | [optional] 
**address_city_town** | [**POAResponseResultsDetailsAddressCityTown**](POAResponseResultsDetailsAddressCityTown.md) |  | [optional] 
**address_province** | [**POAResponseResultsDetailsAddressProvince**](POAResponseResultsDetailsAddressProvince.md) |  | [optional] 
**address_code** | [**POAResponseResultsDetailsAddressCode**](POAResponseResultsDetailsAddressCode.md) |  | [optional] 
**address_country** | [**POAResponseResultsDetailsAddressCountry**](POAResponseResultsDetailsAddressCountry.md) |  | [optional] 

## Example

```python
from highwind_client.models.poa_response_results_details import POAResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of POAResponseResultsDetails from a JSON string
poa_response_results_details_instance = POAResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(POAResponseResultsDetails.to_json())

# convert the object into a dict
poa_response_results_details_dict = poa_response_results_details_instance.to_dict()
# create an instance of POAResponseResultsDetails from a dict
poa_response_results_details_from_dict = POAResponseResultsDetails.from_dict(poa_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


