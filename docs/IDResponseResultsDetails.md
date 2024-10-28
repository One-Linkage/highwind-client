# IDResponseResultsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_document_type** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**full_name** | [**AFSResponseResultsDetailsAccountantName**](AFSResponseResultsDetailsAccountantName.md) |  | [optional] 
**id_number** | [**BEEAResponseResultsDetailsIdNumber**](BEEAResponseResultsDetailsIdNumber.md) |  | [optional] 
**certified_stamp** | [**AFSResponseResultsDetailsStatementOfFinancialPosition**](AFSResponseResultsDetailsStatementOfFinancialPosition.md) |  | [optional] 
**certified_stamp_date** | [**IDResponseResultsDetailsCertifiedStampDate**](IDResponseResultsDetailsCertifiedStampDate.md) |  | [optional] 
**document_recent** | [**AFSResponseResultsDetailsDocumentRecent**](AFSResponseResultsDetailsDocumentRecent.md) |  | [optional] 

## Example

```python
from highwind_client.models.id_response_results_details import IDResponseResultsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IDResponseResultsDetails from a JSON string
id_response_results_details_instance = IDResponseResultsDetails.from_json(json)
# print the JSON string representation of the object
print(IDResponseResultsDetails.to_json())

# convert the object into a dict
id_response_results_details_dict = id_response_results_details_instance.to_dict()
# create an instance of IDResponseResultsDetails from a dict
id_response_results_details_from_dict = IDResponseResultsDetails.from_dict(id_response_results_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


