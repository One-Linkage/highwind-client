# highwind-client
The Highwind AI Document Verifier provides an easy way to analyse financial related documents (financial statements, purchase orders, etc) as an API service for clients.

 ## Flow
`get_upload_url` **-->** `PUT` presigned URL **-->** Highwind AI Solution analyses `pdf` file **-->** `get_results`

## Endpoints
### 1. Upload Document: get_upload_url/{object}?document-type={type}
- This endpoint generates two items:
  - A presigned URL required to upload the file to our storage system.
  - A unique `task_id` which is associated with the presigned URL
- You need to use this presigned URL to upload the `pdf` file (currently, only `pdf` files are accepted) for analysis with a `PUT` request 
  - Content type is `application/pdf`
  - Files should be ideally kept under 5mb in size.
- `{object}` is a string field which will be the name of the file that is uploaded to the storage system.
- `{type}` is the string query parameter that determines the type of document that will be analysed. For example:
  - `?document-type=afs` for annual financial statements 
  - `?document-type=bs` for bank statements
  
### 2. Post document to presigned URL using PUT
- To use the presigned URL from step 1: Send a PUT request with the curl command. Include the full path to your file and the presigned URL itself.
- Command: ```curl -X PUT -T \"/path/to/file\" \"presigned URL\"```
  
### 3. Get Results: get_results/{object}
- This endpoint returns the summary of the `pdf` file that was uploaded via the presigned URL.
  - It takes about 1 - 2 minutes to generate the summary. For larger files it will take more time. It will return `in_progress` while it analysing the `pdf` file.
- `{object}` is a string field for you to add the generated `task_id` to look up the associated summary.
  
`OPTIONS` endpoints are for CORS purposes only.
  
### Links


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import highwind_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import highwind_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import highwind_client
from highwind_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ol.highwind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = highwind_client.Configuration(
    host = "https://api.ol.highwind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with highwind_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = highwind_client.HighwindResourcesApi(api_client)
    object = 'object_example' # str | Enter `task_id` value to retrieve associated summary.

    try:
        # Return the result of the analysed PDF. Requires the `task_id` from `get_upload_url`.
        api_response = api_instance.v3_verify_get_results_object_get(object)
        print("The response of HighwindResourcesApi->v3_verify_get_results_object_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HighwindResourcesApi->v3_verify_get_results_object_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ol.highwind.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HighwindResourcesApi* | [**v3_verify_get_results_object_get**](docs/HighwindResourcesApi.md#v3_verify_get_results_object_get) | **GET** /v3/verify/get_results/{object} | Return the result of the analysed PDF. Requires the &#x60;task_id&#x60; from &#x60;get_upload_url&#x60;.
*HighwindResourcesApi* | [**v3_verify_get_results_object_options**](docs/HighwindResourcesApi.md#v3_verify_get_results_object_options) | **OPTIONS** /v3/verify/get_results/{object} | 
*HighwindResourcesApi* | [**v3_verify_get_upload_url_object_get**](docs/HighwindResourcesApi.md#v3_verify_get_upload_url_object_get) | **GET** /v3/verify/get_upload_url/{object} | Generates a presigned URL for uploading to the storage system.
*HighwindResourcesApi* | [**v3_verify_get_upload_url_object_options**](docs/HighwindResourcesApi.md#v3_verify_get_upload_url_object_options) | **OPTIONS** /v3/verify/get_upload_url/{object} | 


## Documentation For Models

 - [AFSResponse](docs/AFSResponse.md)
 - [AFSResponseResults](docs/AFSResponseResults.md)
 - [AFSResponseResultsDetails](docs/AFSResponseResultsDetails.md)
 - [AFSResponseResultsDetailsAccountantName](docs/AFSResponseResultsDetailsAccountantName.md)
 - [AFSResponseResultsDetailsCompanyName](docs/AFSResponseResultsDetailsCompanyName.md)
 - [AFSResponseResultsDetailsCompanyRegistrationNumber](docs/AFSResponseResultsDetailsCompanyRegistrationNumber.md)
 - [AFSResponseResultsDetailsDirectorName](docs/AFSResponseResultsDetailsDirectorName.md)
 - [AFSResponseResultsDetailsDocumentRecent](docs/AFSResponseResultsDetailsDocumentRecent.md)
 - [AFSResponseResultsDetailsPeriod](docs/AFSResponseResultsDetailsPeriod.md)
 - [AFSResponseResultsDetailsStatementOfFinancialPosition](docs/AFSResponseResultsDetailsStatementOfFinancialPosition.md)
 - [BCLResponse](docs/BCLResponse.md)
 - [BCLResponseResults](docs/BCLResponseResults.md)
 - [BCLResponseResultsDetails](docs/BCLResponseResultsDetails.md)
 - [BCLResponseResultsDetailsBankBranchCode](docs/BCLResponseResultsDetailsBankBranchCode.md)
 - [BCLResponseResultsDetailsDateIssued](docs/BCLResponseResultsDetailsDateIssued.md)
 - [BCLResponseResultsDetailsVerificationStatement](docs/BCLResponseResultsDetailsVerificationStatement.md)
 - [BEEAResponse](docs/BEEAResponse.md)
 - [BEEAResponseResults](docs/BEEAResponseResults.md)
 - [BEEAResponseResultsDetails](docs/BEEAResponseResultsDetails.md)
 - [BEEAResponseResultsDetailsBlackOwnershipDesignatedGroupPercentage](docs/BEEAResponseResultsDetailsBlackOwnershipDesignatedGroupPercentage.md)
 - [BEEAResponseResultsDetailsBlackOwnershipPercentage](docs/BEEAResponseResultsDetailsBlackOwnershipPercentage.md)
 - [BEEAResponseResultsDetailsFullName](docs/BEEAResponseResultsDetailsFullName.md)
 - [BEEAResponseResultsDetailsIdNumber](docs/BEEAResponseResultsDetailsIdNumber.md)
 - [BEECResponse](docs/BEECResponse.md)
 - [BEECResponseResults](docs/BEECResponseResults.md)
 - [BEECResponseResultsDetails](docs/BEECResponseResultsDetails.md)
 - [BEECResponseResultsDetailsEnterpriseRegistrationNumber](docs/BEECResponseResultsDetailsEnterpriseRegistrationNumber.md)
 - [BEECResponseResultsDetailsTotalNumberOfShareholders](docs/BEECResponseResultsDetailsTotalNumberOfShareholders.md)
 - [CIPCResponse](docs/CIPCResponse.md)
 - [CIPCResponseResults](docs/CIPCResponseResults.md)
 - [CIPCResponseResultsDetails](docs/CIPCResponseResultsDetails.md)
 - [CIPCResponseResultsDetailsCertificateType](docs/CIPCResponseResultsDetailsCertificateType.md)
 - [CIPCResponseResultsDetailsDateOfBirthOrIdNumber](docs/CIPCResponseResultsDetailsDateOfBirthOrIdNumber.md)
 - [CIPCResponseResultsDetailsEnterpriseName](docs/CIPCResponseResultsDetailsEnterpriseName.md)
 - [CIPCResponseResultsDetailsEnterprisePostalAddress](docs/CIPCResponseResultsDetailsEnterprisePostalAddress.md)
 - [CIPCResponseResultsDetailsEnterpriseStatus](docs/CIPCResponseResultsDetailsEnterpriseStatus.md)
 - [CIPCResponseResultsDetailsEnterpriseType](docs/CIPCResponseResultsDetailsEnterpriseType.md)
 - [CIPCResponseResultsDetailsFinancialYearEnd](docs/CIPCResponseResultsDetailsFinancialYearEnd.md)
 - [CIPCResponseResultsDetailsRegistrationNumber](docs/CIPCResponseResultsDetailsRegistrationNumber.md)
 - [CIPCResponseResultsDetailsTaxNumberOptional](docs/CIPCResponseResultsDetailsTaxNumberOptional.md)
 - [CONResponse](docs/CONResponse.md)
 - [CONResponseResults](docs/CONResponseResults.md)
 - [CONResponseResultsDetails](docs/CONResponseResultsDetails.md)
 - [CONResponseResultsDetailsServiceProductCostOptional](docs/CONResponseResultsDetailsServiceProductCostOptional.md)
 - [CONResponseResultsDetailsServiceProductDescription](docs/CONResponseResultsDetailsServiceProductDescription.md)
 - [COPResponse](docs/COPResponse.md)
 - [COPResponseResults](docs/COPResponseResults.md)
 - [COPResponseResultsDetails](docs/COPResponseResultsDetails.md)
 - [DocTypes](docs/DocTypes.md)
 - [EMP201Response](docs/EMP201Response.md)
 - [EMP201ResponseResults](docs/EMP201ResponseResults.md)
 - [EMP201ResponseResultsDetails](docs/EMP201ResponseResultsDetails.md)
 - [EMP201ResponseResultsDetailsDeclarationDate](docs/EMP201ResponseResultsDetailsDeclarationDate.md)
 - [EMP201ResponseResultsDetailsPayeReferenceNumber](docs/EMP201ResponseResultsDetailsPayeReferenceNumber.md)
 - [EMP201ResponseResultsDetailsSdlReferenceNumberOptional](docs/EMP201ResponseResultsDetailsSdlReferenceNumberOptional.md)
 - [IDResponse](docs/IDResponse.md)
 - [IDResponseResults](docs/IDResponseResults.md)
 - [IDResponseResultsDetails](docs/IDResponseResultsDetails.md)
 - [IDResponseResultsDetailsCertifiedStampDate](docs/IDResponseResultsDetailsCertifiedStampDate.md)
 - [IResponse](docs/IResponse.md)
 - [IResponseResults](docs/IResponseResults.md)
 - [IResponseResultsDetails](docs/IResponseResultsDetails.md)
 - [IResponseResultsDetailsInvoiceDate](docs/IResponseResultsDetailsInvoiceDate.md)
 - [IResponseResultsDetailsInvoiceNumber](docs/IResponseResultsDetailsInvoiceNumber.md)
 - [IResponseResultsDetailsTotalAmount](docs/IResponseResultsDetailsTotalAmount.md)
 - [LGSResponse](docs/LGSResponse.md)
 - [LGSResponseResults](docs/LGSResponseResults.md)
 - [LGSResponseResultsDetails](docs/LGSResponseResultsDetails.md)
 - [LGSResponseResultsDetailsCompanyAddress](docs/LGSResponseResultsDetailsCompanyAddress.md)
 - [Model3MBSResponse](docs/Model3MBSResponse.md)
 - [Model3MBSResponseResults](docs/Model3MBSResponseResults.md)
 - [Model3MBSResponseResultsDetails](docs/Model3MBSResponseResultsDetails.md)
 - [Model3MBSResponseResultsDetailsBankName](docs/Model3MBSResponseResultsDetailsBankName.md)
 - [Model3MBSResponseResultsDetailsStatementCovers3Months](docs/Model3MBSResponseResultsDetailsStatementCovers3Months.md)
 - [Model3MBSResponseResultsDetailsStatementDatePeriod](docs/Model3MBSResponseResultsDetailsStatementDatePeriod.md)
 - [Model3MMARResponse](docs/Model3MMARResponse.md)
 - [Model3MMARResponseResults](docs/Model3MMARResponseResults.md)
 - [Model3MMARResponseResultsDetails](docs/Model3MMARResponseResultsDetails.md)
 - [Model3MMARResponseResultsDetailsReportDate](docs/Model3MMARResponseResultsDetailsReportDate.md)
 - [POAResponse](docs/POAResponse.md)
 - [POAResponseResults](docs/POAResponseResults.md)
 - [POAResponseResultsDetails](docs/POAResponseResultsDetails.md)
 - [POAResponseResultsDetailsAddressCityTown](docs/POAResponseResultsDetailsAddressCityTown.md)
 - [POAResponseResultsDetailsAddressCode](docs/POAResponseResultsDetailsAddressCode.md)
 - [POAResponseResultsDetailsAddressCountry](docs/POAResponseResultsDetailsAddressCountry.md)
 - [POAResponseResultsDetailsAddressMunicipalDistrictOptional](docs/POAResponseResultsDetailsAddressMunicipalDistrictOptional.md)
 - [POAResponseResultsDetailsAddressProvince](docs/POAResponseResultsDetailsAddressProvince.md)
 - [POAResponseResultsDetailsAddressSuburb](docs/POAResponseResultsDetailsAddressSuburb.md)
 - [POAResponseResultsDetailsDocumentDate](docs/POAResponseResultsDetailsDocumentDate.md)
 - [POAResponseResultsDetailsValidDocumentType](docs/POAResponseResultsDetailsValidDocumentType.md)
 - [POResponse](docs/POResponse.md)
 - [POResponseResults](docs/POResponseResults.md)
 - [POResponseResultsDetails](docs/POResponseResultsDetails.md)
 - [POResponseResultsDetailsCustomerName](docs/POResponseResultsDetailsCustomerName.md)
 - [POResponseResultsDetailsProductService](docs/POResponseResultsDetailsProductService.md)
 - [POResponseResultsDetailsPurchaseOrderDate](docs/POResponseResultsDetailsPurchaseOrderDate.md)
 - [POResponseResultsDetailsPurchaseOrderNumber](docs/POResponseResultsDetailsPurchaseOrderNumber.md)
 - [POResponseResultsDetailsTotalAmount](docs/POResponseResultsDetailsTotalAmount.md)
 - [POResponseResultsDetailsVendorName](docs/POResponseResultsDetailsVendorName.md)
 - [RLResponse](docs/RLResponse.md)
 - [RLResponseResults](docs/RLResponseResults.md)
 - [RLResponseResultsDetails](docs/RLResponseResultsDetails.md)
 - [RLResponseResultsDetailsClientCompanyName](docs/RLResponseResultsDetailsClientCompanyName.md)
 - [RLResponseResultsDetailsServicesProductRenderedDate](docs/RLResponseResultsDetailsServicesProductRenderedDate.md)
 - [SHResponse](docs/SHResponse.md)
 - [SHResponseResults](docs/SHResponseResults.md)
 - [SHResponseResultsDetails](docs/SHResponseResultsDetails.md)
 - [SHResponseResultsDetailsAuthorisedSignature](docs/SHResponseResultsDetailsAuthorisedSignature.md)
 - [SHResponseResultsDetailsCompanyShareholderIdNumbers](docs/SHResponseResultsDetailsCompanyShareholderIdNumbers.md)
 - [SHResponseResultsDetailsCompanyShareholderNames](docs/SHResponseResultsDetailsCompanyShareholderNames.md)
 - [SHResponseResultsDetailsShareholderNumberOfShares](docs/SHResponseResultsDetailsShareholderNumberOfShares.md)
 - [TCCResponse](docs/TCCResponse.md)
 - [TCCResponseResults](docs/TCCResponseResults.md)
 - [TCCResponseResultsDetails](docs/TCCResponseResultsDetails.md)
 - [TCCResponseResultsDetailsPurposeOfRequest](docs/TCCResponseResultsDetailsPurposeOfRequest.md)
 - [TCCResponseResultsDetailsRequestReferenceNumber](docs/TCCResponseResultsDetailsRequestReferenceNumber.md)
 - [TCCResponseResultsDetailsTaxComplianceStatus](docs/TCCResponseResultsDetailsTaxComplianceStatus.md)
 - [TCCResponseResultsDetailsTaxpayerReferenceNumber](docs/TCCResponseResultsDetailsTaxpayerReferenceNumber.md)
 - [V3VerifyGetResultsObjectGet200Response](docs/V3VerifyGetResultsObjectGet200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

admin@melio.ai


