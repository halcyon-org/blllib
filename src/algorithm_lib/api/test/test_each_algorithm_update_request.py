# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from algorithm_lib.models.each_algorithm_update_request import EachAlgorithmUpdateRequest

class TestEachAlgorithmUpdateRequest(unittest.TestCase):
    """EachAlgorithmUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EachAlgorithmUpdateRequest:
        """Test EachAlgorithmUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EachAlgorithmUpdateRequest`
        """
        model = EachAlgorithmUpdateRequest()
        if include_optional:
            return EachAlgorithmUpdateRequest(
                update_algorithm = algorithm_lib.models.algorithm/algorithm_infomation_create_or_update.Algorithm.AlgorithmInfomationCreateOrUpdate(
                    algorithm_id = null, 
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
                        ], )
            )
        else:
            return EachAlgorithmUpdateRequest(
                update_algorithm = algorithm_lib.models.algorithm/algorithm_infomation_create_or_update.Algorithm.AlgorithmInfomationCreateOrUpdate(
                    algorithm_id = null, 
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
                        ], ),
        )
        """

    def testEachAlgorithmUpdateRequest(self):
        """Test EachAlgorithmUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
