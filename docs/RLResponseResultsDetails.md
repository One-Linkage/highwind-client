# RLResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_company_name** | [**POResponseResultsDetailsVendorName**](POResponseResultsDetailsVendorName.md) |  | [optional] 
**client_company_name** | [**RLResponseResultsDetailsClientCompanyName**](RLResponseResultsDetailsClientCompanyName.md) |  | [optional] 
**document_date** | [**POAResponseResultsDetailsDocumentDate**](POAResponseResultsDetailsDocumentDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**services_product_description** | [**BCLResponseResultsDetailsVerificationStatement**](BCLResponseResultsDetailsVerificationStatement.md) |  | [optional] 
**services_product_rendered_date** | [**RLResponseResultsDetailsServicesProductRenderedDate**](RLResponseResultsDetailsServicesProductRenderedDate.md) |  | [optional] 

## Example

```python
from highwind_client.models.rl_response_results_details import RLResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RLResponseResultsDetails from a JSON string
rl_response_results_details_instance = RLResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(RLResponseResultsDetails.to_json())

# convert the object into a dict
rl_response_results_details_dict = rl_response_results_details_instance.to_dict()
# create an instance of RLResponseResultsDetails from a dict
rl_response_results_details_from_dict = RLResponseResultsDetails.from_dict(rl_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


