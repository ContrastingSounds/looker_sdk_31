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
from looker_client_31.api.datagroup_api import DatagroupApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestDatagroupApi(unittest.TestCase):
    """DatagroupApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.datagroup_api.DatagroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_datagroups(self):
        """Test case for all_datagroups

        Get All Datagroups  # noqa: E501
        """
        pass

    def test_datagroup(self):
        """Test case for datagroup

        Get Datagroup  # noqa: E501
        """
        pass

    def test_update_datagroup(self):
        """Test case for update_datagroup

        Update Datagroup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
