# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.provider_client_data_create import ProviderClientDataCreate

class TestProviderClientDataCreate(unittest.TestCase):
    """ProviderClientDataCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProviderClientDataCreate:
        """Test ProviderClientDataCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProviderClientDataCreate`
        """
        model = ProviderClientDataCreate()
        if include_optional:
            return ProviderClientDataCreate(
                name = ''
            )
        else:
            return ProviderClientDataCreate(
                name = '',
        )
        """

    def testProviderClientDataCreate(self):
        """Test ProviderClientDataCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
