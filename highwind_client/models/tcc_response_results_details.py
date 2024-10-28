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
from highwind_client.models.afs_response_results_details_statement_of_financial_position import AFSResponseResultsDetailsStatementOfFinancialPosition
from highwind_client.models.bcl_response_results_details_date_issued import BCLResponseResultsDetailsDateIssued
from highwind_client.models.beea_response_results_details_full_name import BEEAResponseResultsDetailsFullName
from highwind_client.models.beec_response_results_details_enterprise_registration_number import BEECResponseResultsDetailsEnterpriseRegistrationNumber
from highwind_client.models.emp201_response_results_details_declaration_date import EMP201ResponseResultsDetailsDeclarationDate
from highwind_client.models.lgs_response_results_details_company_address import LGSResponseResultsDetailsCompanyAddress
from highwind_client.models.po_response_results_details_vendor_name import POResponseResultsDetailsVendorName
from highwind_client.models.tcc_response_results_details_purpose_of_request import TCCResponseResultsDetailsPurposeOfRequest
from highwind_client.models.tcc_response_results_details_request_reference_number import TCCResponseResultsDetailsRequestReferenceNumber
from highwind_client.models.tcc_response_results_details_tax_compliance_status import TCCResponseResultsDetailsTaxComplianceStatus
from highwind_client.models.tcc_response_results_details_taxpayer_reference_number import TCCResponseResultsDetailsTaxpayerReferenceNumber
from typing import Optional, Set
from typing_extensions import Self

class TCCResponseResultsDetails(BaseModel):
    """
    TCCResponseResultsDetails
    """ # noqa: E501
    trading_name: Optional[POResponseResultsDetailsVendorName] = None
    company_address: Optional[LGSResponseResultsDetailsCompanyAddress] = None
    taxpayer_name: Optional[BEEAResponseResultsDetailsFullName] = None
    taxpayer_reference_number: Optional[TCCResponseResultsDetailsTaxpayerReferenceNumber] = None
    issue_date: Optional[BCLResponseResultsDetailsDateIssued] = None
    tax_pin_number: Optional[BEECResponseResultsDetailsEnterpriseRegistrationNumber] = None
    tax_pin_expiry_date: Optional[EMP201ResponseResultsDetailsDeclarationDate] = None
    document_recent: Optional[AFSResponseResultsDetailsDocumentRecent] = None
    tax_compliance_status: Optional[TCCResponseResultsDetailsTaxComplianceStatus] = None
    purpose_of_request: Optional[TCCResponseResultsDetailsPurposeOfRequest] = None
    request_reference_number: Optional[TCCResponseResultsDetailsRequestReferenceNumber] = None
    tax_compliance_status_text_position: Optional[AFSResponseResultsDetailsStatementOfFinancialPosition] = None
    __properties: ClassVar[List[str]] = ["trading_name", "company_address", "taxpayer_name", "taxpayer_reference_number", "issue_date", "tax_pin_number", "tax_pin_expiry_date", "document_recent", "tax_compliance_status", "purpose_of_request", "request_reference_number", "tax_compliance_status_text_position"]

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
        """Create an instance of TCCResponseResultsDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of trading_name
        if self.trading_name:
            _dict['trading_name'] = self.trading_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_address
        if self.company_address:
            _dict['company_address'] = self.company_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxpayer_name
        if self.taxpayer_name:
            _dict['taxpayer_name'] = self.taxpayer_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxpayer_reference_number
        if self.taxpayer_reference_number:
            _dict['taxpayer_reference_number'] = self.taxpayer_reference_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issue_date
        if self.issue_date:
            _dict['issue_date'] = self.issue_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_pin_number
        if self.tax_pin_number:
            _dict['tax_pin_number'] = self.tax_pin_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_pin_expiry_date
        if self.tax_pin_expiry_date:
            _dict['tax_pin_expiry_date'] = self.tax_pin_expiry_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_recent
        if self.document_recent:
            _dict['document_recent'] = self.document_recent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_compliance_status
        if self.tax_compliance_status:
            _dict['tax_compliance_status'] = self.tax_compliance_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purpose_of_request
        if self.purpose_of_request:
            _dict['purpose_of_request'] = self.purpose_of_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of request_reference_number
        if self.request_reference_number:
            _dict['request_reference_number'] = self.request_reference_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_compliance_status_text_position
        if self.tax_compliance_status_text_position:
            _dict['tax_compliance_status_text_position'] = self.tax_compliance_status_text_position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TCCResponseResultsDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trading_name": POResponseResultsDetailsVendorName.from_dict(obj["trading_name"]) if obj.get("trading_name") is not None else None,
            "company_address": LGSResponseResultsDetailsCompanyAddress.from_dict(obj["company_address"]) if obj.get("company_address") is not None else None,
            "taxpayer_name": BEEAResponseResultsDetailsFullName.from_dict(obj["taxpayer_name"]) if obj.get("taxpayer_name") is not None else None,
            "taxpayer_reference_number": TCCResponseResultsDetailsTaxpayerReferenceNumber.from_dict(obj["taxpayer_reference_number"]) if obj.get("taxpayer_reference_number") is not None else None,
            "issue_date": BCLResponseResultsDetailsDateIssued.from_dict(obj["issue_date"]) if obj.get("issue_date") is not None else None,
            "tax_pin_number": BEECResponseResultsDetailsEnterpriseRegistrationNumber.from_dict(obj["tax_pin_number"]) if obj.get("tax_pin_number") is not None else None,
            "tax_pin_expiry_date": EMP201ResponseResultsDetailsDeclarationDate.from_dict(obj["tax_pin_expiry_date"]) if obj.get("tax_pin_expiry_date") is not None else None,
            "document_recent": AFSResponseResultsDetailsDocumentRecent.from_dict(obj["document_recent"]) if obj.get("document_recent") is not None else None,
            "tax_compliance_status": TCCResponseResultsDetailsTaxComplianceStatus.from_dict(obj["tax_compliance_status"]) if obj.get("tax_compliance_status") is not None else None,
            "purpose_of_request": TCCResponseResultsDetailsPurposeOfRequest.from_dict(obj["purpose_of_request"]) if obj.get("purpose_of_request") is not None else None,
            "request_reference_number": TCCResponseResultsDetailsRequestReferenceNumber.from_dict(obj["request_reference_number"]) if obj.get("request_reference_number") is not None else None,
            "tax_compliance_status_text_position": AFSResponseResultsDetailsStatementOfFinancialPosition.from_dict(obj["tax_compliance_status_text_position"]) if obj.get("tax_compliance_status_text_position") is not None else None
        })
        return _obj


