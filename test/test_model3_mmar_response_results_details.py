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

from highwind_client.models.model3_mmar_response_results_details import Model3MMARResponseResultsDetails

class TestModel3MMARResponseResultsDetails(unittest.TestCase):
    """Model3MMARResponseResultsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model3MMARResponseResultsDetails:
        """Test Model3MMARResponseResultsDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model3MMARResponseResultsDetails`
        """
        model = Model3MMARResponseResultsDetails()
        if include_optional:
            return Model3MMARResponseResultsDetails(
                statement_of_profit_and_loss = highwind_client.models.afs_response_results_details_statement_of_financial_position.AFSResponse_results_details_statement_of_financial_position(
                    exists = True, ),
                balance_sheet = highwind_client.models.afs_response_results_details_statement_of_financial_position.AFSResponse_results_details_statement_of_financial_position(
                    exists = True, ),
                cash_flow_statement = highwind_client.models.afs_response_results_details_statement_of_financial_position.AFSResponse_results_details_statement_of_financial_position(
                    exists = True, ),
                statement_date_period = highwind_client.models._3_mbs_response_results_details_statement_date_period._3MBSResponse_results_details_statement_date_period(
                    exists = True, 
                    value = '2024-01-15 to 2024-02-15', ),
                report_date = highwind_client.models._3_mmar_response_results_details_report_date._3MMARResponse_results_details_report_date(
                    exists = True, 
                    value = '2024-02-10', ),
                document_recent = highwind_client.models.afs_response_results_details_document_recent.AFSResponse_results_details_document_recent(
                    exists = False, 
                    value = 'The document is more than 1 year old.', ),
                statement_covers_3_months = highwind_client.models.afs_response_results_details_statement_of_financial_position.AFSResponse_results_details_statement_of_financial_position(
                    exists = True, )
            )
        else:
            return Model3MMARResponseResultsDetails(
        )
        """

    def testModel3MMARResponseResultsDetails(self):
        """Test Model3MMARResponseResultsDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
