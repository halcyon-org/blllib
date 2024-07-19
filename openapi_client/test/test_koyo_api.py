# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.koyo_api import KoyoApi


class TestKoyoApi(unittest.TestCase):
    """KoyoApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KoyoApi()

    def tearDown(self) -> None:
        pass

    def test_each_koyo_data_new(self) -> None:
        """Test case for each_koyo_data_new

        Post new data of own koyo
        """
        pass

    def test_each_koyo_get(self) -> None:
        """Test case for each_koyo_get

        Get koyos' basic information
        """
        pass

    def test_each_koyo_update(self) -> None:
        """Test case for each_koyo_update

        Update information on own koyo
        """
        pass

    def test_koyo_list(self) -> None:
        """Test case for koyo_list

        Get a list of koyos' basic information
        """
        pass


if __name__ == '__main__':
    unittest.main()
