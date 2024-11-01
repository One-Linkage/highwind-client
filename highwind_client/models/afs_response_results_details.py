# coding: utf-8

"""
    Highwind AI Solution - Document Verifier

    The Highwind AI Document Verifier provides an easy way to analyse financial related documents (financial statements, purchase orders, etc) as an API service for clients.   ## Flow `get_upload_url` **-->** `PUT` presigned URL **-->** Highwind AI Solution analyses `pdf` file **-->** `get_results`  ## Endpoints ### 1. Upload Document: get_upload_url/{object}?document-type={type} - This endpoint generates two items:   - A presigned URL required to upload the file to our storage system.   - A unique `task_id` which is associated with the presigned URL - You need to use this presigned URL to upload the `pdf` file (currently, only `pdf` files are accepted) for analysis with a `PUT` request    - Content type is `application/pdf`   - Files should be ideally kept under 5mb in size. - `{object}` is a string field which will be the name of the file that is uploaded to the storage system. - `{type}` is the string query parameter that determines the type of document that will be analysed. For example:   - `?document-type=afs` for annual financial statements    - `?document-type=bs` for bank statements    ### 2. Post document to presigned URL using PUT - To use the presigned URL from step 1: Send a PUT request with the curl command. Include the full path to your file and the presigned URL itself. - Command: ```curl -X PUT -T \"/path/to/file\" \"presigned URL\"```    ### 3. Get Results: get_results/{object} - This endpoint returns the summary of the `pdf` file that was uploaded via the presigned URL.   - It takes about 1 - 2 minutes to generate the summary. For larger files it will take more time. It will return `in_progress` while it analysing the `pdf` file. - `{object}` is a string field for you to add the generated `task_id` to look up the associated summary.    `OPTIONS` endpoints are for CORS purposes only.    ### Links 

    The version of the OpenAPI document: 3.0
    Contact: admin@melio.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from highwind_client.models.afs_response_results_details_accountant_name import AFSResponseResultsDetailsAccountantName
from highwind_client.models.afs_response_results_details_company_name import AFSResponseResultsDetailsCompanyName
from highwind_client.models.afs_response_results_details_company_registration_number import AFSResponseResultsDetailsCompanyRegistrationNumber
from highwind_client.models.afs_response_results_details_director_name import AFSResponseResultsDetailsDirectorName
from highwind_client.models.afs_response_results_details_document_recent import AFSResponseResultsDetailsDocumentRecent
from highwind_client.models.afs_response_results_details_period import AFSResponseResultsDetailsPeriod
from highwind_client.models.afs_response_results_details_statement_of_financial_position import AFSResponseResultsDetailsStatementOfFinancialPosition
from typing import Optional, Set
from typing_extensions import Self

class AFSResponseResultsDetails(BaseModel):
    """
    AFSResponseResultsDetails
    """ # noqa: E501
    company_name: Optional[AFSResponseResultsDetailsCompanyName] = None
    company_registration_number: Optional[AFSResponseResultsDetailsCompanyRegistrationNumber] = None
    period: Optional[AFSResponseResultsDetailsPeriod] = None
    document_recent: Optional[AFSResponseResultsDetailsDocumentRecent] = None
    statement_of_financial_position: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    statement_of_profit_and_loss: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    statement_of_changes_in_equity: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    statement_of_cash_flow: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    director_name: Optional[AFSResponseResultsDetailsDirectorName] = None
    director_signature: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    accountant_name: Optional[AFSResponseResultsDetailsAccountantName] = None
    accountant_signature: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    __properties: ClassVar[List[str]] = ["company_name", "company_registration_number", "period", "document_recent", "statement_of_financial_position", "statement_of_profit_and_loss", "statement_of_changes_in_equity", "statement_of_cash_flow", "director_name", "director_signature", "accountant_name", "accountant_signature"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AFSResponseResultsDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of company_name
        if self.company_name:
            _dict['company_name'] = self.company_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_registration_number
        if self.company_registration_number:
            _dict['company_registration_number'] = self.company_registration_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of period
        if self.period:
            _dict['period'] = self.period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_recent
        if self.document_recent:
            _dict['document_recent'] = self.document_recent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_of_financial_position
        if self.statement_of_financial_position:
            _dict['statement_of_financial_position'] = self.statement_of_financial_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_of_profit_and_loss
        if self.statement_of_profit_and_loss:
            _dict['statement_of_profit_and_loss'] = self.statement_of_profit_and_loss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_of_changes_in_equity
        if self.statement_of_changes_in_equity:
            _dict['statement_of_changes_in_equity'] = self.statement_of_changes_in_equity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_of_cash_flow
        if self.statement_of_cash_flow:
            _dict['statement_of_cash_flow'] = self.statement_of_cash_flow.to_dict()
        # override the default output from pydantic by calling `to_dict()` of director_name
        if self.director_name:
            _dict['director_name'] = self.director_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of director_signature
        if self.director_signature:
            _dict['director_signature'] = self.director_signature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accountant_name
        if self.accountant_name:
            _dict['accountant_name'] = self.accountant_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accountant_signature
        if self.accountant_signature:
            _dict['accountant_signature'] = self.accountant_signature.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AFSResponseResultsDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company_name": AFSResponseResultsDetailsCompanyName.from_dict(obj["company_name"]) if obj.get("company_name") is not None else None,
            "company_registration_number": AFSResponseResultsDetailsCompanyRegistrationNumber.from_dict(obj["company_registration_number"]) if obj.get("company_registration_number") is not None else None,
            "period": AFSResponseResultsDetailsPeriod.from_dict(obj["period"]) if obj.get("period") is not None else None,
            "document_recent": AFSResponseResultsDetailsDocumentRecent.from_dict(obj["document_recent"]) if obj.get("document_recent") is not None else None,
            "statement_of_financial_position": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["statement_of_financial_position"]) if obj.get("statement_of_financial_position") is not None else None,
            "statement_of_profit_and_loss": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["statement_of_profit_and_loss"]) if obj.get("statement_of_profit_and_loss") is not None else None,
            "statement_of_changes_in_equity": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["statement_of_changes_in_equity"]) if obj.get("statement_of_changes_in_equity") is not None else None,
            "statement_of_cash_flow": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["statement_of_cash_flow"]) if obj.get("statement_of_cash_flow") is not None else None,
            "director_name": AFSResponseResultsDetailsDirectorName.from_dict(obj["director_name"]) if obj.get("director_name") is not None else None,
            "director_signature": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["director_signature"]) if obj.get("director_signature") is not None else None,
            "accountant_name": AFSResponseResultsDetailsAccountantName.from_dict(obj["accountant_name"]) if obj.get("accountant_name") is not None else None,
            "accountant_signature": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["accountant_signature"]) if obj.get("accountant_signature") is not None else None
        })
        return _obj


