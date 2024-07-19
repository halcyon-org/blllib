# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.koyo_koyo_data_create import KoyoKoyoDataCreate

class TestKoyoKoyoDataCreate(unittest.TestCase):
    """KoyoKoyoDataCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KoyoKoyoDataCreate:
        """Test KoyoKoyoDataCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KoyoKoyoDataCreate`
        """
        model = KoyoKoyoDataCreate()
        if include_optional:
            return KoyoKoyoDataCreate(
                version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026',
                koyo_scale = 1.337,
                content_type = 'image',
                content = 'YQ=='
            )
        else:
            return KoyoKoyoDataCreate(
                version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026',
                koyo_scale = 1.337,
                content_type = 'image',
                content = 'YQ==',
        )
        """

    def testKoyoKoyoDataCreate(self):
        """Test KoyoKoyoDataCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
