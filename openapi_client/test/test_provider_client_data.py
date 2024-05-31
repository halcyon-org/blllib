# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.provider_client_data import ProviderClientData

class TestProviderClientData(unittest.TestCase):
    """ProviderClientData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProviderClientData:
        """Test ProviderClientData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProviderClientData`
        """
        model = ProviderClientData()
        if include_optional:
            return ProviderClientData(
                client_id = '',
                name = '',
                api_key = ''
            )
        else:
            return ProviderClientData(
                client_id = '',
                name = '',
                api_key = '',
        )
        """

    def testProviderClientData(self):
        """Test ProviderClientData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()