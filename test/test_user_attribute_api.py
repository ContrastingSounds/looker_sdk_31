# coding: utf-8

"""
    Experimental Looker API 3.1 Preview

    This API 3.1 is in active development. Breaking changes are likely to occur to some API functions in future Looker releases until API 3.1 is officially launched and upgraded to beta status.  If you have time and interest to experiment with new or modified services exposed in this embryonic API 3.1, we welcome your participation and feedback!  For large development efforts or critical line-of-business projects, we strongly recommend you stick with the API 3.0 while API 3.1 is under construction.   # noqa: E501

    OpenAPI spec version: 3.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import looker_client_31
from looker_client_31.api.user_attribute_api import UserAttributeApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestUserAttributeApi(unittest.TestCase):
    """UserAttributeApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.user_attribute_api.UserAttributeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_user_attribute_group_values(self):
        """Test case for all_user_attribute_group_values

        Get User Attribute Group Values  # noqa: E501
        """
        pass

    def test_all_user_attributes(self):
        """Test case for all_user_attributes

        Get All User Attributes  # noqa: E501
        """
        pass

    def test_create_user_attribute(self):
        """Test case for create_user_attribute

        Create User Attribute  # noqa: E501
        """
        pass

    def test_delete_user_attribute(self):
        """Test case for delete_user_attribute

        Delete User Attribute  # noqa: E501
        """
        pass

    def test_set_user_attribute_group_values(self):
        """Test case for set_user_attribute_group_values

        Set User Attribute Group Values  # noqa: E501
        """
        pass

    def test_update_user_attribute(self):
        """Test case for update_user_attribute

        Update User Attribute  # noqa: E501
        """
        pass

    def test_user_attribute(self):
        """Test case for user_attribute

        Get User Attribute  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
