# coding: utf-8

"""
    Experimental Looker API 3.1 Preview

    This API 3.1 is in active development. Breaking changes are likely to occur to some API functions in future Looker releases until API 3.1 is officially launched and upgraded to beta status.  If you have time and interest to experiment with new or modified services exposed in this embryonic API 3.1, we welcome your participation and feedback!  For large development efforts or critical line-of-business projects, we strongly recommend you stick with the API 3.0 while API 3.1 is under construction.   # noqa: E501

    OpenAPI spec version: 3.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from looker_client_31.looker_sdk.db_connection_base import DBConnectionBase  # noqa: F401,E501
from looker_client_31.looker_sdk.user_public import UserPublic  # noqa: F401,E501


class SqlQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'slug': 'str',
        'last_runtime': 'float',
        'run_count': 'int',
        'browser_limit': 'int',
        'sql': 'str',
        'last_run_at': 'str',
        'connection': 'DBConnectionBase',
        'model_name': 'str',
        'creator': 'UserPublic',
        'explore_url': 'str',
        'plaintext': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'slug': 'slug',
        'last_runtime': 'last_runtime',
        'run_count': 'run_count',
        'browser_limit': 'browser_limit',
        'sql': 'sql',
        'last_run_at': 'last_run_at',
        'connection': 'connection',
        'model_name': 'model_name',
        'creator': 'creator',
        'explore_url': 'explore_url',
        'plaintext': 'plaintext',
        'can': 'can'
    }

    def __init__(self, slug=None, last_runtime=None, run_count=None, browser_limit=None, sql=None, last_run_at=None, connection=None, model_name=None, creator=None, explore_url=None, plaintext=None, can=None):  # noqa: E501
        """SqlQuery - a model defined in Swagger"""  # noqa: E501

        self._slug = None
        self._last_runtime = None
        self._run_count = None
        self._browser_limit = None
        self._sql = None
        self._last_run_at = None
        self._connection = None
        self._model_name = None
        self._creator = None
        self._explore_url = None
        self._plaintext = None
        self._can = None
        self.discriminator = None

        if slug is not None:
            self.slug = slug
        if last_runtime is not None:
            self.last_runtime = last_runtime
        if run_count is not None:
            self.run_count = run_count
        if browser_limit is not None:
            self.browser_limit = browser_limit
        if sql is not None:
            self.sql = sql
        if last_run_at is not None:
            self.last_run_at = last_run_at
        if connection is not None:
            self.connection = connection
        if model_name is not None:
            self.model_name = model_name
        if creator is not None:
            self.creator = creator
        if explore_url is not None:
            self.explore_url = explore_url
        if plaintext is not None:
            self.plaintext = plaintext
        if can is not None:
            self.can = can

    @property
    def slug(self):
        """Gets the slug of this SqlQuery.  # noqa: E501

        The identifier of the SQL query  # noqa: E501

        :return: The slug of this SqlQuery.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SqlQuery.

        The identifier of the SQL query  # noqa: E501

        :param slug: The slug of this SqlQuery.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def last_runtime(self):
        """Gets the last_runtime of this SqlQuery.  # noqa: E501

        Number of seconds this query took to run the most recent time it was run  # noqa: E501

        :return: The last_runtime of this SqlQuery.  # noqa: E501
        :rtype: float
        """
        return self._last_runtime

    @last_runtime.setter
    def last_runtime(self, last_runtime):
        """Sets the last_runtime of this SqlQuery.

        Number of seconds this query took to run the most recent time it was run  # noqa: E501

        :param last_runtime: The last_runtime of this SqlQuery.  # noqa: E501
        :type: float
        """

        self._last_runtime = last_runtime

    @property
    def run_count(self):
        """Gets the run_count of this SqlQuery.  # noqa: E501

        Number of times this query has been run  # noqa: E501

        :return: The run_count of this SqlQuery.  # noqa: E501
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count):
        """Sets the run_count of this SqlQuery.

        Number of times this query has been run  # noqa: E501

        :param run_count: The run_count of this SqlQuery.  # noqa: E501
        :type: int
        """

        self._run_count = run_count

    @property
    def browser_limit(self):
        """Gets the browser_limit of this SqlQuery.  # noqa: E501

        Maximum number of rows this query will display on the SQL Runner page  # noqa: E501

        :return: The browser_limit of this SqlQuery.  # noqa: E501
        :rtype: int
        """
        return self._browser_limit

    @browser_limit.setter
    def browser_limit(self, browser_limit):
        """Sets the browser_limit of this SqlQuery.

        Maximum number of rows this query will display on the SQL Runner page  # noqa: E501

        :param browser_limit: The browser_limit of this SqlQuery.  # noqa: E501
        :type: int
        """

        self._browser_limit = browser_limit

    @property
    def sql(self):
        """Gets the sql of this SqlQuery.  # noqa: E501

        SQL query text  # noqa: E501

        :return: The sql of this SqlQuery.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this SqlQuery.

        SQL query text  # noqa: E501

        :param sql: The sql of this SqlQuery.  # noqa: E501
        :type: str
        """

        self._sql = sql

    @property
    def last_run_at(self):
        """Gets the last_run_at of this SqlQuery.  # noqa: E501

        The most recent time this query was run  # noqa: E501

        :return: The last_run_at of this SqlQuery.  # noqa: E501
        :rtype: str
        """
        return self._last_run_at

    @last_run_at.setter
    def last_run_at(self, last_run_at):
        """Sets the last_run_at of this SqlQuery.

        The most recent time this query was run  # noqa: E501

        :param last_run_at: The last_run_at of this SqlQuery.  # noqa: E501
        :type: str
        """

        self._last_run_at = last_run_at

    @property
    def connection(self):
        """Gets the connection of this SqlQuery.  # noqa: E501

        Connection this query uses  # noqa: E501

        :return: The connection of this SqlQuery.  # noqa: E501
        :rtype: DBConnectionBase
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this SqlQuery.

        Connection this query uses  # noqa: E501

        :param connection: The connection of this SqlQuery.  # noqa: E501
        :type: DBConnectionBase
        """

        self._connection = connection

    @property
    def model_name(self):
        """Gets the model_name of this SqlQuery.  # noqa: E501

        Model name this query uses  # noqa: E501

        :return: The model_name of this SqlQuery.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this SqlQuery.

        Model name this query uses  # noqa: E501

        :param model_name: The model_name of this SqlQuery.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def creator(self):
        """Gets the creator of this SqlQuery.  # noqa: E501

        User who created this SQL query  # noqa: E501

        :return: The creator of this SqlQuery.  # noqa: E501
        :rtype: UserPublic
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this SqlQuery.

        User who created this SQL query  # noqa: E501

        :param creator: The creator of this SqlQuery.  # noqa: E501
        :type: UserPublic
        """

        self._creator = creator

    @property
    def explore_url(self):
        """Gets the explore_url of this SqlQuery.  # noqa: E501

        Explore page URL for this SQL query  # noqa: E501

        :return: The explore_url of this SqlQuery.  # noqa: E501
        :rtype: str
        """
        return self._explore_url

    @explore_url.setter
    def explore_url(self, explore_url):
        """Sets the explore_url of this SqlQuery.

        Explore page URL for this SQL query  # noqa: E501

        :param explore_url: The explore_url of this SqlQuery.  # noqa: E501
        :type: str
        """

        self._explore_url = explore_url

    @property
    def plaintext(self):
        """Gets the plaintext of this SqlQuery.  # noqa: E501

        Should this query be rendered as plain text  # noqa: E501

        :return: The plaintext of this SqlQuery.  # noqa: E501
        :rtype: bool
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """Sets the plaintext of this SqlQuery.

        Should this query be rendered as plain text  # noqa: E501

        :param plaintext: The plaintext of this SqlQuery.  # noqa: E501
        :type: bool
        """

        self._plaintext = plaintext

    @property
    def can(self):
        """Gets the can of this SqlQuery.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this SqlQuery.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this SqlQuery.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this SqlQuery.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SqlQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other