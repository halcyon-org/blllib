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


class Versions(str, Enum):
    """
    Versions
    """

    """
    allowed enum values
    """
    V0_DOT_5_DOT_0 = 'v0.5.0'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Versions from a JSON string"""
        return cls(json.loads(json_str))


