# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.client_delete200_response import ClientDelete200Response

class TestClientDelete200Response(unittest.TestCase):
    """ClientDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDelete200Response:
        """Test ClientDelete200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientDelete200Response`
        """
        model = ClientDelete200Response()
        if include_optional:
            return ClientDelete200Response(
                delete_client_id = ''
            )
        else:
            return ClientDelete200Response(
                delete_client_id = '',
        )
        """

    def testClientDelete200Response(self):
        """Test ClientDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
