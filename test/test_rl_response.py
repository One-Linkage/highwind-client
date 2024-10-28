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

from highwind_client.models.rl_response import RLResponse

class TestRLResponse(unittest.TestCase):
    """RLResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RLResponse:
        """Test RLResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RLResponse`
        """
        model = RLResponse()
        if include_optional:
            return RLResponse(
                status = 'complete',
                results = highwind_client.models.rl_response_results.RLResponse_results(
                    is_reference_letter = True, 
                    pages_processed = 10, 
                    details = highwind_client.models.rl_response_results_details.RLResponse_results_details(
                        vendor_company_name = highwind_client.models.po_response_results_details_vendor_name.POResponse_results_details_vendor_name(
                            exists = True, 
                            value = 'Megaton Supplies', ), 
                        client_company_name = highwind_client.models.rl_response_results_details_client_company_name.RLResponse_results_details_client_company_name(
                            exists = True, 
                            value = 'City of Shady Sands', ), 
                        document_date = highwind_client.models.poa_response_results_details_document_date.POAResponse_results_details_document_date(
                            exists = True, 
                            value = '2023-12-30', ), 
                        document_recent = highwind_client.models.afs_response_results_details_document_recent.AFSResponse_results_details_document_recent(
                            exists = False, 
                            value = 'The document is more than 1 year old.', ), 
                        services_product_description = highwind_client.models.bcl_response_results_details_verification_statement.BCLResponse_results_details_verification_statement(
                            exists = True, 
                            value = 'Summary', ), 
                        services_product_rendered_date = highwind_client.models.rl_response_results_details_services_product_rendered_date.RLResponse_results_details_services_product_rendered_date(
                            exists = True, 
                            value = 'From August 2024 to September 2024', ), ), 
                    summary = 'This document is valid because...', )
            )
        else:
            return RLResponse(
        )
        """

    def testRLResponse(self):
        """Test RLResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
