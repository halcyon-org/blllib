# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.algorithm_create200_response import AlgorithmCreate200Response

class TestAlgorithmCreate200Response(unittest.TestCase):
    """AlgorithmCreate200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgorithmCreate200Response:
        """Test AlgorithmCreate200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgorithmCreate200Response`
        """
        model = AlgorithmCreate200Response()
        if include_optional:
            return AlgorithmCreate200Response(
                algorithm_id = '',
                algorithm_name = '',
                algorithm_description = '',
                need_external = [
                    'HOGE_ID'
                    ],
                algorithm_scales = [
                    1.337
                    ],
                algorithm_data_ids = [
                    ''
                    ],
                first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                bearer_token = ''
            )
        else:
            return AlgorithmCreate200Response(
                algorithm_id = '',
                algorithm_name = '',
                algorithm_description = '',
                need_external = [
                    'HOGE_ID'
                    ],
                algorithm_scales = [
                    1.337
                    ],
                algorithm_data_ids = [
                    ''
                    ],
                first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                bearer_token = '',
        )
        """

    def testAlgorithmCreate200Response(self):
        """Test AlgorithmCreate200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
