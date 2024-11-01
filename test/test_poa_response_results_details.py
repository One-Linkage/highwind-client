# coding: utf-8

"""
    Highwind AI Solution - Document Verifier

    The Highwind AI Document Verifier provides an easy way to analyse financial related documents (financial statements, purchase orders, etc) as an API service for clients.   ## Flow `get_upload_url` **-->** `PUT` presigned URL **-->** Highwind AI Solution analyses `pdf` file **-->** `get_results`  ## Endpoints ### 1. Upload Document: get_upload_url/{object}?document-type={type} - This endpoint generates two items:   - A presigned URL required to upload the file to our storage system.   - A unique `task_id` which is associated with the presigned URL - You need to use this presigned URL to upload the `pdf` file (currently, only `pdf` files are accepted) for analysis with a `PUT` request    - Content type is `application/pdf`   - Files should be ideally kept under 5mb in size. - `{object}` is a string field which will be the name of the file that is uploaded to the storage system. - `{type}` is the string query parameter that determines the type of document that will be analysed. For example:   - `?document-type=afs` for annual financial statements    - `?document-type=bs` for bank statements    ### 2. Post document to presigned URL using PUT - To use the presigned URL from step 1: Send a PUT request with the curl command. Include the full path to your file and the presigned URL itself. - Command: ```curl -X PUT -T \"/path/to/file\" \"presigned URL\"```    ### 3. Get Results: get_results/{object} - This endpoint returns the summary of the `pdf` file that was uploaded via the presigned URL.   - It takes about 1 - 2 minutes to generate the summary. For larger files it will take more time. It will return `in_progress` while it analysing the `pdf` file. - `{object}` is a string field for you to add the generated `task_id` to look up the associated summary.    `OPTIONS` endpoints are for CORS purposes only.    ### Links 

    The version of the OpenAPI document: 3.0
    Contact: admin@melio.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from highwind_client.models.poa_response_results_details import POAResponseResultsDetails

class TestPOAResponseResultsDetails(unittest.TestCase):
    """POAResponseResultsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> POAResponseResultsDetails:
        """Test POAResponseResultsDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `POAResponseResultsDetails`
        """
        model = POAResponseResultsDetails()
        if include_optional:
            return POAResponseResultsDetails(
                valid_document_type = highwind_client.models.poa_response_results_details_valid_document_type.POAResponse_results_details_valid_document_type(
                    exists = True, 
                    value = 'utility bill | property managing agent statement | active lease | rental agreement | mortgage statement | body corporate/governing body letter or statement | affidavit from the director confirming the address', ),
                document_date = highwind_client.models.poa_response_results_details_document_date.POAResponse_results_details_document_date(
                    exists = True, 
                    value = '2023-12-30', ),
                document_recent = highwind_client.models.afs_response_results_details_document_recent.AFSResponse_results_details_document_recent(
                    exists = False, 
                    value = 'The document is more than 1 year old.', ),
                address_street_number = highwind_client.models.lgs_response_results_details_company_address.LGSResponse_results_details_company_address(
                    exists = True, 
                    value = '123 Happy Street', ),
                address_suburb = highwind_client.models.poa_response_results_details_address_suburb.POAResponse_results_details_address_suburb(
                    exists = True, 
                    value = 'Newtown', ),
                address_municipal_district_optional = highwind_client.models.poa_response_results_details_address_municipal_district_optional.POAResponse_results_details_address_municipal_district_optional(
                    exists = True, 
                    value = 'West Rand District', ),
                address_city_town = highwind_client.models.poa_response_results_details_address_city_town.POAResponse_results_details_address_city_town(
                    exists = True, 
                    value = 'Johannesburg', ),
                address_province = highwind_client.models.poa_response_results_details_address_province.POAResponse_results_details_address_province(
                    exists = True, 
                    value = 'Gauteng', ),
                address_code = highwind_client.models.poa_response_results_details_address_code.POAResponse_results_details_address_code(
                    exists = True, 
                    value = '2001', ),
                address_country = highwind_client.models.poa_response_results_details_address_country.POAResponse_results_details_address_country(
                    exists = True, 
                    value = 'South Africa', )
            )
        else:
            return POAResponseResultsDetails(
        )
        """

    def testPOAResponseResultsDetails(self):
        """Test POAResponseResultsDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
