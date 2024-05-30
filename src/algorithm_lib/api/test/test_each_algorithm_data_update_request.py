# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from algorithm_lib.models.each_algorithm_data_update_request import EachAlgorithmDataUpdateRequest

class TestEachAlgorithmDataUpdateRequest(unittest.TestCase):
    """EachAlgorithmDataUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EachAlgorithmDataUpdateRequest:
        """Test EachAlgorithmDataUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EachAlgorithmDataUpdateRequest`
        """
        model = EachAlgorithmDataUpdateRequest()
        if include_optional:
            return EachAlgorithmDataUpdateRequest(
                update_data = algorithm_lib.models.algorithm/algorithm_data_create_or_update.Algorithm.AlgorithmDataCreateOrUpdate(
                    algorithm_id = '', 
                    algorithm_scale = 1.337, 
                    content_type = 'image', 
                    content = 'YQ==', )
            )
        else:
            return EachAlgorithmDataUpdateRequest(
                update_data = algorithm_lib.models.algorithm/algorithm_data_create_or_update.Algorithm.AlgorithmDataCreateOrUpdate(
                    algorithm_id = '', 
                    algorithm_scale = 1.337, 
                    content_type = 'image', 
                    content = 'YQ==', ),
        )
        """

    def testEachAlgorithmDataUpdateRequest(self):
        """Test EachAlgorithmDataUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
