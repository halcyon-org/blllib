# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.algorithm_delete200_response import AlgorithmDelete200Response

class TestAlgorithmDelete200Response(unittest.TestCase):
    """AlgorithmDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgorithmDelete200Response:
        """Test AlgorithmDelete200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgorithmDelete200Response`
        """
        model = AlgorithmDelete200Response()
        if include_optional:
            return AlgorithmDelete200Response(
                delete_algorithm_id = ''
            )
        else:
            return AlgorithmDelete200Response(
                delete_algorithm_id = '',
        )
        """

    def testAlgorithmDelete200Response(self):
        """Test AlgorithmDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
