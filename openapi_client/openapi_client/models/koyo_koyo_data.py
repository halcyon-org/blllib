# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from openapi_client.models.koyo_data_type import KoyoDataType
from typing import Optional, Set
from typing_extensions import Self

class KoyoKoyoData(BaseModel):
    """
    The data is the result of processing by the koyo.
    """ # noqa: E501
    koyo_data_id: StrictStr
    koyo_id: Annotated[str, Field(strict=True)] = Field(description="The ID of the koyo that generated the data.")
    version: Annotated[str, Field(strict=True)] = Field(description="The version of the koyo used to generate the data.")
    koyo_scale: Union[StrictFloat, StrictInt] = Field(description="The resolution of the data.")
    content_type: KoyoDataType = Field(description="The type of data format.(enum: image, csv, json...)")
    content: Union[StrictBytes, StrictStr] = Field(description="The data content itself.")
    entry_at: datetime
    target_at: datetime = Field(description="The time at which the data is targeted. The time at which data processing began (= the primary data from which the data was processed was updated). In other words, it indicates which time the data is based on.\")")
    __properties: ClassVar[List[str]] = ["koyo_data_id", "koyo_id", "version", "koyo_scale", "content_type", "content", "entry_at", "target_at"]

    @field_validator('koyo_id')
    def koyo_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z_-]{1,64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-z_-]{1,64}$/")
        return value

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
        """Create an instance of KoyoKoyoData from a JSON string"""
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
        """Create an instance of KoyoKoyoData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "koyo_data_id": obj.get("koyo_data_id"),
            "koyo_id": obj.get("koyo_id"),
            "version": obj.get("version"),
            "koyo_scale": obj.get("koyo_scale"),
            "content_type": obj.get("content_type"),
            "content": obj.get("content"),
            "entry_at": obj.get("entry_at"),
            "target_at": obj.get("target_at")
        })
        return _obj


