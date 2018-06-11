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
from looker_client_31.api.render_task_api import RenderTaskApi  # noqa: E501
from looker_client_31.rest import ApiException


class TestRenderTaskApi(unittest.TestCase):
    """RenderTaskApi unit test stubs"""

    def setUp(self):
        self.api = looker_client_31.api.render_task_api.RenderTaskApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dashboard_render_task(self):
        """Test case for create_dashboard_render_task

        Create Dashboard Render Task  # noqa: E501
        """
        pass

    def test_create_look_render_task(self):
        """Test case for create_look_render_task

        Create Look Render Task  # noqa: E501
        """
        pass

    def test_create_lookml_dashboard_render_task(self):
        """Test case for create_lookml_dashboard_render_task

        Create Lookml Dashboard Render Task  # noqa: E501
        """
        pass

    def test_create_query_render_task(self):
        """Test case for create_query_render_task

        Create Query Render Task  # noqa: E501
        """
        pass

    def test_render_task(self):
        """Test case for render_task

        Get Render Task  # noqa: E501
        """
        pass

    def test_render_task_results(self):
        """Test case for render_task_results

        Render Task Results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
