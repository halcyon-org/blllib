# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ext_info_create_request import ExtInfoCreateRequest

class TestExtInfoCreateRequest(unittest.TestCase):
    """ExtInfoCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtInfoCreateRequest:
        """Test ExtInfoCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtInfoCreateRequest`
        """
        model = ExtInfoCreateRequest()
        if include_optional:
            return ExtInfoCreateRequest(
                extinfo = openapi_client.models.external_information.External information(
                    external_name = '', 
                    external_description = '', 
                    license = '', 
                    license_description = '', 
                    first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_history = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], )
            )
        else:
            return ExtInfoCreateRequest(
                extinfo = openapi_client.models.external_information.External information(
                    external_name = '', 
                    external_description = '', 
                    license = '', 
                    license_description = '', 
                    first_entry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_history = [
                        datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                        ], ),
        )
        """

    def testExtInfoCreateRequest(self):
        """Test ExtInfoCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
