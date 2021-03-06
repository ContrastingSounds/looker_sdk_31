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
from looker_client_31.api.role_api import RoleApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestRoleApi(unittest.TestCase):
    """RoleApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.role_api.RoleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_model_sets(self):
        """Test case for all_model_sets

        Get All Model Sets  # noqa: E501
        """
        pass

    def test_all_permission_sets(self):
        """Test case for all_permission_sets

        Get All Permission Sets  # noqa: E501
        """
        pass

    def test_all_permissions(self):
        """Test case for all_permissions

        Get All Permissions  # noqa: E501
        """
        pass

    def test_all_roles(self):
        """Test case for all_roles

        Get All Roles  # noqa: E501
        """
        pass

    def test_create_model_set(self):
        """Test case for create_model_set

        Create Model Set  # noqa: E501
        """
        pass

    def test_create_permission_set(self):
        """Test case for create_permission_set

        Create Permission Set  # noqa: E501
        """
        pass

    def test_create_role(self):
        """Test case for create_role

        Create Role  # noqa: E501
        """
        pass

    def test_delete_model_set(self):
        """Test case for delete_model_set

        Delete Model Set  # noqa: E501
        """
        pass

    def test_delete_permission_set(self):
        """Test case for delete_permission_set

        Delete Permission Set  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete Role  # noqa: E501
        """
        pass

    def test_model_set(self):
        """Test case for model_set

        Get Model Set  # noqa: E501
        """
        pass

    def test_permission_set(self):
        """Test case for permission_set

        Get Permission Set  # noqa: E501
        """
        pass

    def test_role(self):
        """Test case for role

        Get Role  # noqa: E501
        """
        pass

    def test_role_groups(self):
        """Test case for role_groups

        Get Role Groups  # noqa: E501
        """
        pass

    def test_role_users(self):
        """Test case for role_users

        Get Role Users  # noqa: E501
        """
        pass

    def test_set_role_groups(self):
        """Test case for set_role_groups

        Update Role Groups  # noqa: E501
        """
        pass

    def test_set_role_users(self):
        """Test case for set_role_users

        Update Role Users  # noqa: E501
        """
        pass

    def test_update_model_set(self):
        """Test case for update_model_set

        Update Model Set  # noqa: E501
        """
        pass

    def test_update_permission_set(self):
        """Test case for update_permission_set

        Update Permission Set  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
