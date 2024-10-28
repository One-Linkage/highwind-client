# COPResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | [**POResponseResultsDetailsCustomerName**](POResponseResultsDetailsCustomerName.md) |  | [optional] 
**company_address_optional** | [**LGSResponseResultsDetailsCompanyAddress**](LGSResponseResultsDetailsCompanyAddress.md) |  | [optional] 
**company_services_products** | [**BCLResponseResultsDetailsVerificationStatement**](BCLResponseResultsDetailsVerificationStatement.md) |  | [optional] 

## Example

```python
from highwind_client.models.cop_response_results_details import COPResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of COPResponseResultsDetails from a JSON string
cop_response_results_details_instance = COPResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(COPResponseResultsDetails.to_json())

# convert the object into a dict
cop_response_results_details_dict = cop_response_results_details_instance.to_dict()
# create an instance of COPResponseResultsDetails from a dict
cop_response_results_details_from_dict = COPResponseResultsDetails.from_dict(cop_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


