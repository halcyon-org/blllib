# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.main_api import MainApi


class TestMainApi(unittest.TestCase):
    """MainApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MainApi()

    def tearDown(self) -> None:
        pass

    def test_algorithm_create(self) -> None:
        """Test case for algorithm_create

        """
        pass

    def test_algorithm_delete(self) -> None:
        """Test case for algorithm_delete

        """
        pass

    def test_algorithm_list(self) -> None:
        """Test case for algorithm_list

        """
        pass

    def test_client_create(self) -> None:
        """Test case for client_create

        """
        pass

    def test_client_delete(self) -> None:
        """Test case for client_delete

        """
        pass

    def test_clients_get_client(self) -> None:
        """Test case for clients_get_client

        """
        pass

    def test_data_list(self) -> None:
        """Test case for data_list

        """
        pass

    def test_each_algorithm_data_get(self) -> None:
        """Test case for each_algorithm_data_get

        """
        pass

    def test_each_algorithm_data_update(self) -> None:
        """Test case for each_algorithm_data_update

        """
        pass

    def test_each_algorithm_get(self) -> None:
        """Test case for each_algorithm_get

        """
        pass

    def test_each_algorithm_update(self) -> None:
        """Test case for each_algorithm_update

        """
        pass

    def test_each_data_get(self) -> None:
        """Test case for each_data_get

        """
        pass

    def test_each_ext_info_get(self) -> None:
        """Test case for each_ext_info_get

        """
        pass

    def test_ext_info_create(self) -> None:
        """Test case for ext_info_create

        """
        pass

    def test_ext_info_delete(self) -> None:
        """Test case for ext_info_delete

        """
        pass

    def test_ext_info_list(self) -> None:
        """Test case for ext_info_list

        """
        pass

    def test_hoge_get(self) -> None:
        """Test case for hoge_get

        """
        pass

    def test_status_get(self) -> None:
        """Test case for status_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
