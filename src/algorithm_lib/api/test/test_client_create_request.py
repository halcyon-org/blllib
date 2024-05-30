# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from algorithm_lib.models.client_create_request import ClientCreateRequest

class TestClientCreateRequest(unittest.TestCase):
    """ClientCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientCreateRequest:
        """Test ClientCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientCreateRequest`
        """
        model = ClientCreateRequest()
        if include_optional:
            return ClientCreateRequest(
                client = algorithm_lib.models.provider/client_data_create.Provider.ClientDataCreate(
                    name = '', )
            )
        else:
            return ClientCreateRequest(
                client = algorithm_lib.models.provider/client_data_create.Provider.ClientDataCreate(
                    name = '', ),
        )
        """

    def testClientCreateRequest(self):
        """Test ClientCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
