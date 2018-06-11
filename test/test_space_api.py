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
from looker_client_31.api.space_api import SpaceApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestSpaceApi(unittest.TestCase):
    """SpaceApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.space_api.SpaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_spaces(self):
        """Test case for all_spaces

        Get All Spaces  # noqa: E501
        """
        pass

    def test_create_space(self):
        """Test case for create_space

        Create Space  # noqa: E501
        """
        pass

    def test_delete_space(self):
        """Test case for delete_space

        Delete Space  # noqa: E501
        """
        pass

    def test_search_spaces(self):
        """Test case for search_spaces

        Search Spaces  # noqa: E501
        """
        pass

    def test_space(self):
        """Test case for space

        Get Space  # noqa: E501
        """
        pass

    def test_space_ancestors(self):
        """Test case for space_ancestors

        Get Space Ancestors  # noqa: E501
        """
        pass

    def test_space_children(self):
        """Test case for space_children

        Get Space Children  # noqa: E501
        """
        pass

    def test_space_children_search(self):
        """Test case for space_children_search

        Search Space Children  # noqa: E501
        """
        pass

    def test_space_dashboards(self):
        """Test case for space_dashboards

        Get Space Dashboards  # noqa: E501
        """
        pass

    def test_space_looks(self):
        """Test case for space_looks

        Get Space Looks  # noqa: E501
        """
        pass

    def test_space_parent(self):
        """Test case for space_parent

        Get Space Parent  # noqa: E501
        """
        pass

    def test_update_space(self):
        """Test case for update_space

        Update Space  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()