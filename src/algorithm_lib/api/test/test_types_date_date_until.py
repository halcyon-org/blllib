# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from algorithm_lib.models.types_date_date_until import TypesDateDateUntil

class TestTypesDateDateUntil(unittest.TestCase):
    """TypesDateDateUntil unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TypesDateDateUntil:
        """Test TypesDateDateUntil
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TypesDateDateUntil`
        """
        model = TypesDateDateUntil()
        if include_optional:
            return TypesDateDateUntil(
                before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return TypesDateDateUntil(
        )
        """

    def testTypesDateDateUntil(self):
        """Test TypesDateDateUntil"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
