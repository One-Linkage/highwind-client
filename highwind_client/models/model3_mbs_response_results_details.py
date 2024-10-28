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
from highwind_client.models.afs_response_results_details_document_recent import AFSResponseResultsDetailsDocumentRecent
from highwind_client.models.emp201_response_results_details_declaration_date import EMP201ResponseResultsDetailsDeclarationDate
from highwind_client.models.emp201_response_results_details_paye_reference_number import EMP201ResponseResultsDetailsPayeReferenceNumber
from highwind_client.models.model3_mbs_response_results_details_bank_name import Model3MBSResponseResultsDetailsBankName
from highwind_client.models.model3_mbs_response_results_details_statement_covers3_months import Model3MBSResponseResultsDetailsStatementCovers3Months
from highwind_client.models.model3_mbs_response_results_details_statement_date_period import Model3MBSResponseResultsDetailsStatementDatePeriod
from highwind_client.models.po_response_results_details_vendor_name import POResponseResultsDetailsVendorName
from typing import Optional, Set
from typing_extensions import Self

class Model3MBSResponseResultsDetails(BaseModel):
    """
    Model3MBSResponseResultsDetails
    """ # noqa: E501
    company_name: Optional[POResponseResultsDetailsVendorName] = None
    bank_name: Optional[Model3MBSResponseResultsDetailsBankName] = None
    account_number: Optional[EMP201ResponseResultsDetailsPayeReferenceNumber] = None
    statement_date_period: Optional[Model3MBSResponseResultsDetailsStatementDatePeriod] = None
    statement_latest_date: Optional[EMP201ResponseResultsDetailsDeclarationDate] = None
    document_recent: Optional[AFSResponseResultsDetailsDocumentRecent] = None
    statement_covers_3_months: Optional[Model3MBSResponseResultsDetailsStatementCovers3Months] = None
    __properties: ClassVar[List[str]] = ["company_name", "bank_name", "account_number", "statement_date_period", "statement_latest_date", "document_recent", "statement_covers_3_months"]

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
        """Create an instance of Model3MBSResponseResultsDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_name
        if self.bank_name:
            _dict['bank_name'] = self.bank_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_number
        if self.account_number:
            _dict['account_number'] = self.account_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_date_period
        if self.statement_date_period:
            _dict['statement_date_period'] = self.statement_date_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_latest_date
        if self.statement_latest_date:
            _dict['statement_latest_date'] = self.statement_latest_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_recent
        if self.document_recent:
            _dict['document_recent'] = self.document_recent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statement_covers_3_months
        if self.statement_covers_3_months:
            _dict['statement_covers_3_months'] = self.statement_covers_3_months.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Model3MBSResponseResultsDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "company_name": POResponseResultsDetailsVendorName.from_dict(obj["company_name"]) if obj.get("company_name") is not None else None,
            "bank_name": Model3MBSResponseResultsDetailsBankName.from_dict(obj["bank_name"]) if obj.get("bank_name") is not None else None,
            "account_number": EMP201ResponseResultsDetailsPayeReferenceNumber.from_dict(obj["account_number"]) if obj.get("account_number") is not None else None,
            "statement_date_period": Model3MBSResponseResultsDetailsStatementDatePeriod.from_dict(obj["statement_date_period"]) if obj.get("statement_date_period") is not None else None,
            "statement_latest_date": EMP201ResponseResultsDetailsDeclarationDate.from_dict(obj["statement_latest_date"]) if obj.get("statement_latest_date") is not None else None,
            "document_recent": AFSResponseResultsDetailsDocumentRecent.from_dict(obj["document_recent"]) if obj.get("document_recent") is not None else None,
            "statement_covers_3_months": Model3MBSResponseResultsDetailsStatementCovers3Months.from_dict(obj["statement_covers_3_months"]) if obj.get("statement_covers_3_months") is not None else None
        })
        return _obj


