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

from highwind_client.models.tcc_response import TCCResponse

class TestTCCResponse(unittest.TestCase):
    """TCCResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TCCResponse:
        """Test TCCResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TCCResponse`
        """
        model = TCCResponse()
        if include_optional:
            return TCCResponse(
                status = 'complete',
                results = highwind_client.models.tcc_response_results.TCCResponse_results(
                    is_tax_clearance_certificate = True, 
                    pages_processed = 10, 
                    details = highwind_client.models.tcc_response_results_details.TCCResponse_results_details(
                        trading_name = highwind_client.models.po_response_results_details_vendor_name.POResponse_results_details_vendor_name(
                            exists = True, 
                            value = 'Megaton Supplies', ), 
                        company_address = highwind_client.models.lgs_response_results_details_company_address.LGSResponse_results_details_company_address(
                            exists = True, 
                            value = '123 Happy Street', ), 
                        taxpayer_name = highwind_client.models.beea_response_results_details_full_name.BEEAResponse_results_details_full_name(
                            exists = True, 
                            value = 'Moira Brown', ), 
                        taxpayer_reference_number = highwind_client.models.tcc_response_results_details_taxpayer_reference_number.TCCResponse_results_details_taxpayer_reference_number(
                            exists = True, 
                            value = '12345678', ), 
                        issue_date = highwind_client.models.bcl_response_results_details_date_issued.BCLResponse_results_details_date_issued(
                            exists = True, 
                            value = '2024-01-01', ), 
                        tax_pin_number = highwind_client.models.beec_response_results_details_enterprise_registration_number.BEECResponse_results_details_enterprise_registration_number(
                            exists = True, 
                            value = '123ABC', ), 
                        tax_pin_expiry_date = highwind_client.models.emp201_response_results_details_declaration_date.EMP201Response_results_details_declaration_date(
                            exists = False, 
                            value = '2024-01-01', ), 
                        document_recent = highwind_client.models.afs_response_results_details_document_recent.AFSResponse_results_details_document_recent(
                            exists = False, 
                            value = 'The document is more than 1 year old.', ), 
                        tax_compliance_status = highwind_client.models.tcc_response_results_details_tax_compliance_status.TCCResponse_results_details_tax_compliance_status(
                            exists = False, 
                            value = 'PIN Issued.', ), 
                        purpose_of_request = highwind_client.models.tcc_response_results_details_purpose_of_request.TCCResponse_results_details_purpose_of_request(
                            exists = False, 
                            value = 'Good Standing', ), 
                        request_reference_number = highwind_client.models.tcc_response_results_details_request_reference_number.TCCResponse_results_details_request_reference_number(
                            exists = False, 
                            value = '123ABC', ), 
                        tax_compliance_status_text_position = highwind_client.models.afs_response_results_details_statement_of_financial_position.AFSResponse_results_details_statement_of_financial_position(
                            exists = True, ), ), 
                    summary = 'This document is valid because...', )
            )
        else:
            return TCCResponse(
        )
        """

    def testTCCResponse(self):
        """Test TCCResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
