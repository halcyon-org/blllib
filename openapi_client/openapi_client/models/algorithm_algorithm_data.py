# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.5.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from openapi_client.models.algorithm_data_type import AlgorithmDataType
from typing import Optional, Set
from typing_extensions import Self

class AlgorithmAlgorithmData(BaseModel):
    """
    AlgorithmAlgorithmData
    """ # noqa: E501
    algorithm_id: StrictStr
    algorithm_data_id: StrictStr
    algorithm_scale: Union[StrictFloat, StrictInt]
    content_type: AlgorithmDataType
    content: Union[StrictBytes, StrictStr]
    entry_at: datetime
    target_at: datetime
    __properties: ClassVar[List[str]] = ["algorithm_id", "algorithm_data_id", "algorithm_scale", "content_type", "content", "entry_at", "target_at"]

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
        """Create an instance of AlgorithmAlgorithmData from a JSON string"""
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
        """Create an instance of AlgorithmAlgorithmData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "algorithm_id": obj.get("algorithm_id"),
            "algorithm_data_id": obj.get("algorithm_data_id"),
            "algorithm_scale": obj.get("algorithm_scale"),
            "content_type": obj.get("content_type"),
            "content": obj.get("content"),
            "entry_at": obj.get("entry_at"),
            "target_at": obj.get("target_at")
        })
        return _obj


