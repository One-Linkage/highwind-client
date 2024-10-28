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

from highwind_client.models.model3_mbs_response import Model3MBSResponse

class TestModel3MBSResponse(unittest.TestCase):
    """Model3MBSResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model3MBSResponse:
        """Test Model3MBSResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model3MBSResponse`
        """
        model = Model3MBSResponse()
        if include_optional:
            return Model3MBSResponse(
                status = 'complete',
                results = highwind_client.models._3_mbs_response_results._3MBSResponse_results(
                    is_3_month_bank_statement = True, 
                    pages_processed = 10, 
                    details = highwind_client.models._3_mbs_response_results_details._3MBSResponse_results_details(
                        company_name = highwind_client.models.po_response_results_details_vendor_name.POResponse_results_details_vendor_name(
                            exists = True, 
                            value = 'Megaton Supplies', ), 
                        bank_name = highwind_client.models._3_mbs_response_results_details_bank_name._3MBSResponse_results_details_bank_name(
                            exists = True, 
                            value = 'Vault 76 Bank', ), 
                        account_number = highwind_client.models.emp201_response_results_details_paye_reference_number.EMP201Response_results_details_paye_reference_number(
                            exists = True, 
                            value = '1234ABC', ), 
                        statement_date_period = highwind_client.models._3_mbs_response_results_details_statement_date_period._3MBSResponse_results_details_statement_date_period(
                            exists = True, 
                            value = '2024-01-15 to 2024-02-15', ), 
                        statement_latest_date = highwind_client.models.emp201_response_results_details_declaration_date.EMP201Response_results_details_declaration_date(
                            exists = False, 
                            value = '2024-01-01', ), 
                        document_recent = highwind_client.models.afs_response_results_details_document_recent.AFSResponse_results_details_document_recent(
                            exists = False, 
                            value = 'The document is more than 1 year old.', ), 
                        statement_covers_3_months = highwind_client.models._3_mbs_response_results_details_statement_covers_3_months._3MBSResponse_results_details_statement_covers_3_months(
                            exists = True, 
                            value = 'The statement is from January 15 2024 to February 15 2024 only covers 2 months.', ), ), 
                    summary = 'This document is valid because...', )
            )
        else:
            return Model3MBSResponse(
        )
        """

    def testModel3MBSResponse(self):
        """Test Model3MBSResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
