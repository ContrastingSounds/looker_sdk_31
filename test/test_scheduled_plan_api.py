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
from looker_client_31.api.scheduled_plan_api import ScheduledPlanApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestScheduledPlanApi(unittest.TestCase):
    """ScheduledPlanApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.scheduled_plan_api.ScheduledPlanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_scheduled_plans(self):
        """Test case for all_scheduled_plans

        Get All Scheduled Plans  # noqa: E501
        """
        pass

    def test_create_scheduled_plan(self):
        """Test case for create_scheduled_plan

        Create Scheduled Plan  # noqa: E501
        """
        pass

    def test_delete_scheduled_plan(self):
        """Test case for delete_scheduled_plan

        Delete Scheduled Plan  # noqa: E501
        """
        pass

    def test_scheduled_plan(self):
        """Test case for scheduled_plan

        Get Scheduled Plan  # noqa: E501
        """
        pass

    def test_scheduled_plan_run_once(self):
        """Test case for scheduled_plan_run_once

        Run Scheduled Plan Once  # noqa: E501
        """
        pass

    def test_scheduled_plans_for_dashboard(self):
        """Test case for scheduled_plans_for_dashboard

        Scheduled Plans for Dashboard  # noqa: E501
        """
        pass

    def test_scheduled_plans_for_look(self):
        """Test case for scheduled_plans_for_look

        Scheduled Plans for Look  # noqa: E501
        """
        pass

    def test_scheduled_plans_for_lookml_dashboard(self):
        """Test case for scheduled_plans_for_lookml_dashboard

        Scheduled Plans for LookML Dashboard  # noqa: E501
        """
        pass

    def test_scheduled_plans_for_space(self):
        """Test case for scheduled_plans_for_space

        Scheduled Plans for Space  # noqa: E501
        """
        pass

    def test_update_scheduled_plan(self):
        """Test case for update_scheduled_plan

        Update Scheduled Plan  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
