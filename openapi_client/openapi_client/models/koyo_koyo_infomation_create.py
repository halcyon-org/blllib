# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from openapi_client.models.ext_info_ext_info_id import ExtInfoExtInfoId
from typing import Optional, Set
from typing_extensions import Self

class KoyoKoyoInfomationCreate(BaseModel):
    """
    Basic information about the koyo.
    """ # noqa: E501
    koyo_name: Annotated[str, Field(min_length=1, strict=True, max_length=64)]
    koyo_description: Annotated[str, Field(strict=True, max_length=2048)]
    need_external: List[ExtInfoExtInfoId]
    koyo_params: Dict[str, StrictStr] = Field(description="Koyo parameters. The key is the parameter name and the value is the default value.")
    koyo_scales: List[Union[StrictFloat, StrictInt]] = Field(description="Koyo scales is resolution (e.g. one data per meter). Returns a list of supported scales.")
    koyo_data_ids: List[StrictStr]
    version: Annotated[str, Field(strict=True)] = Field(description="Semantic versioning")
    license: StrictStr
    ext_licenses: List[StrictStr] = Field(description="Licenses for primary information and other information used by the koyo.")
    __properties: ClassVar[List[str]] = ["koyo_name", "koyo_description", "need_external", "koyo_params", "koyo_scales", "koyo_data_ids", "version", "license", "ext_licenses"]

    @field_validator('version')
    def version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+\.\d+\.\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+\.\d+\.\d+$/")
        return value

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
        """Create an instance of KoyoKoyoInfomationCreate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KoyoKoyoInfomationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "koyo_name": obj.get("koyo_name"),
            "koyo_description": obj.get("koyo_description"),
            "need_external": obj.get("need_external"),
            "koyo_params": obj.get("koyo_params"),
            "koyo_scales": obj.get("koyo_scales"),
            "koyo_data_ids": obj.get("koyo_data_ids"),
            "version": obj.get("version"),
            "license": obj.get("license"),
            "ext_licenses": obj.get("ext_licenses")
        })
        return _obj


