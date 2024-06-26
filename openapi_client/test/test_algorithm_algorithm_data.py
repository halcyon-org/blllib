# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.algorithm_algorithm_data import AlgorithmAlgorithmData

class TestAlgorithmAlgorithmData(unittest.TestCase):
    """AlgorithmAlgorithmData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgorithmAlgorithmData:
        """Test AlgorithmAlgorithmData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgorithmAlgorithmData`
        """
        model = AlgorithmAlgorithmData()
        if include_optional:
            return AlgorithmAlgorithmData(
                algorithm_id = '',
                algorithm_data_id = '',
                algorithm_scale = 1.337,
                content_type = 'image',
                content = 'YQ==',
                entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return AlgorithmAlgorithmData(
                algorithm_id = '',
                algorithm_data_id = '',
                algorithm_scale = 1.337,
                content_type = 'image',
                content = 'YQ==',
                entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testAlgorithmAlgorithmData(self):
        """Test AlgorithmAlgorithmData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
