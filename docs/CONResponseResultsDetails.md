# CONResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_of_party_1** | [**AFSResponseResultsDetailsAccountantName**](AFSResponseResultsDetailsAccountantName.md) |  | [optional] 
**name_of_party_2** | [**BEEAResponseResultsDetailsFullName**](BEEAResponseResultsDetailsFullName.md) |  | [optional] 
**date_of_agreement** | [**BCLResponseResultsDetailsDateIssued**](BCLResponseResultsDetailsDateIssued.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 
**service_product_description** | [**CONResponseResultsDetailsServiceProductDescription**](CONResponseResultsDetailsServiceProductDescription.md) |  | [optional] 
**service_product_cost_optional** | [**CONResponseResultsDetailsServiceProductCostOptional**](CONResponseResultsDetailsServiceProductCostOptional.md) |  | [optional] 
**signatures_of_both_parties** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 

## Example

```python
from highwind_client.models.con_response_results_details import CONResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CONResponseResultsDetails from a JSON string
con_response_results_details_instance = CONResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(CONResponseResultsDetails.to_json())

# convert the object into a dict
con_response_results_details_dict = con_response_results_details_instance.to_dict()
# create an instance of CONResponseResultsDetails from a dict
con_response_results_details_from_dict = CONResponseResultsDetails.from_dict(con_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


