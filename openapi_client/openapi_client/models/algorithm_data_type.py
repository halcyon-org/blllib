# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlgorithmDataType(str, Enum):
    """
    AlgorithmDataType
    """

    """
    allowed enum values
    """
    IMAGE = 'image'
    CSV = 'csv'
    JSON = 'json'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlgorithmDataType from a JSON string"""
        return cls(json.loads(json_str))

