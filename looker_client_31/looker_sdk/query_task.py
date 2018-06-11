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

from looker_client_31.looker_sdk.query import Query  # noqa: F401,E501


class QueryTask(object):
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
        'id': 'str',
        'query_id': 'int',
        'query': 'Query',
        'generate_links': 'bool',
        'force_production': 'bool',
        'path_prefix': 'str',
        'cache': 'bool',
        'server_table_calcs': 'bool',
        'cache_only': 'bool',
        'cache_key': 'str',
        'status': 'str',
        'source': 'str',
        'runtime': 'float',
        'rebuild_pdts': 'bool',
        'result_source': 'str',
        'look_id': 'int',
        'dashboard_id': 'str',
        'result_format': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'query_id': 'query_id',
        'query': 'query',
        'generate_links': 'generate_links',
        'force_production': 'force_production',
        'path_prefix': 'path_prefix',
        'cache': 'cache',
        'server_table_calcs': 'server_table_calcs',
        'cache_only': 'cache_only',
        'cache_key': 'cache_key',
        'status': 'status',
        'source': 'source',
        'runtime': 'runtime',
        'rebuild_pdts': 'rebuild_pdts',
        'result_source': 'result_source',
        'look_id': 'look_id',
        'dashboard_id': 'dashboard_id',
        'result_format': 'result_format',
        'can': 'can'
    }

    def __init__(self, id=None, query_id=None, query=None, generate_links=None, force_production=None, path_prefix=None, cache=None, server_table_calcs=None, cache_only=None, cache_key=None, status=None, source=None, runtime=None, rebuild_pdts=None, result_source=None, look_id=None, dashboard_id=None, result_format=None, can=None):  # noqa: E501
        """QueryTask - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._query_id = None
        self._query = None
        self._generate_links = None
        self._force_production = None
        self._path_prefix = None
        self._cache = None
        self._server_table_calcs = None
        self._cache_only = None
        self._cache_key = None
        self._status = None
        self._source = None
        self._runtime = None
        self._rebuild_pdts = None
        self._result_source = None
        self._look_id = None
        self._dashboard_id = None
        self._result_format = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if query_id is not None:
            self.query_id = query_id
        if query is not None:
            self.query = query
        if generate_links is not None:
            self.generate_links = generate_links
        if force_production is not None:
            self.force_production = force_production
        if path_prefix is not None:
            self.path_prefix = path_prefix
        if cache is not None:
            self.cache = cache
        if server_table_calcs is not None:
            self.server_table_calcs = server_table_calcs
        if cache_only is not None:
            self.cache_only = cache_only
        if cache_key is not None:
            self.cache_key = cache_key
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if runtime is not None:
            self.runtime = runtime
        if rebuild_pdts is not None:
            self.rebuild_pdts = rebuild_pdts
        if result_source is not None:
            self.result_source = result_source
        if look_id is not None:
            self.look_id = look_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if result_format is not None:
            self.result_format = result_format
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this QueryTask.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryTask.

        Unique Id  # noqa: E501

        :param id: The id of this QueryTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def query_id(self):
        """Gets the query_id of this QueryTask.  # noqa: E501

        Id of query  # noqa: E501

        :return: The query_id of this QueryTask.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this QueryTask.

        Id of query  # noqa: E501

        :param query_id: The query_id of this QueryTask.  # noqa: E501
        :type: int
        """

        self._query_id = query_id

    @property
    def query(self):
        """Gets the query of this QueryTask.  # noqa: E501

        Query  # noqa: E501

        :return: The query of this QueryTask.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryTask.

        Query  # noqa: E501

        :param query: The query of this QueryTask.  # noqa: E501
        :type: Query
        """

        self._query = query

    @property
    def generate_links(self):
        """Gets the generate_links of this QueryTask.  # noqa: E501

        whether or not to generate links in the query response.  # noqa: E501

        :return: The generate_links of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._generate_links

    @generate_links.setter
    def generate_links(self, generate_links):
        """Sets the generate_links of this QueryTask.

        whether or not to generate links in the query response.  # noqa: E501

        :param generate_links: The generate_links of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._generate_links = generate_links

    @property
    def force_production(self):
        """Gets the force_production of this QueryTask.  # noqa: E501

        Use production models to run query (even is user is in dev mode).  # noqa: E501

        :return: The force_production of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._force_production

    @force_production.setter
    def force_production(self, force_production):
        """Sets the force_production of this QueryTask.

        Use production models to run query (even is user is in dev mode).  # noqa: E501

        :param force_production: The force_production of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._force_production = force_production

    @property
    def path_prefix(self):
        """Gets the path_prefix of this QueryTask.  # noqa: E501

        Prefix to use for drill links.  # noqa: E501

        :return: The path_prefix of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """Sets the path_prefix of this QueryTask.

        Prefix to use for drill links.  # noqa: E501

        :param path_prefix: The path_prefix of this QueryTask.  # noqa: E501
        :type: str
        """

        self._path_prefix = path_prefix

    @property
    def cache(self):
        """Gets the cache of this QueryTask.  # noqa: E501

        Whether or not to use the cache  # noqa: E501

        :return: The cache of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this QueryTask.

        Whether or not to use the cache  # noqa: E501

        :param cache: The cache of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._cache = cache

    @property
    def server_table_calcs(self):
        """Gets the server_table_calcs of this QueryTask.  # noqa: E501

        Whether or not to run table calculations on the server  # noqa: E501

        :return: The server_table_calcs of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._server_table_calcs

    @server_table_calcs.setter
    def server_table_calcs(self, server_table_calcs):
        """Sets the server_table_calcs of this QueryTask.

        Whether or not to run table calculations on the server  # noqa: E501

        :param server_table_calcs: The server_table_calcs of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._server_table_calcs = server_table_calcs

    @property
    def cache_only(self):
        """Gets the cache_only of this QueryTask.  # noqa: E501

        Retrieve any results from cache even if the results have expired.  # noqa: E501

        :return: The cache_only of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._cache_only

    @cache_only.setter
    def cache_only(self, cache_only):
        """Sets the cache_only of this QueryTask.

        Retrieve any results from cache even if the results have expired.  # noqa: E501

        :param cache_only: The cache_only of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._cache_only = cache_only

    @property
    def cache_key(self):
        """Gets the cache_key of this QueryTask.  # noqa: E501

        cache key used to cache query.  # noqa: E501

        :return: The cache_key of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """Sets the cache_key of this QueryTask.

        cache key used to cache query.  # noqa: E501

        :param cache_key: The cache_key of this QueryTask.  # noqa: E501
        :type: str
        """

        self._cache_key = cache_key

    @property
    def status(self):
        """Gets the status of this QueryTask.  # noqa: E501

        Status of query task.  # noqa: E501

        :return: The status of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryTask.

        Status of query task.  # noqa: E501

        :param status: The status of this QueryTask.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def source(self):
        """Gets the source of this QueryTask.  # noqa: E501

        Source of query task.  # noqa: E501

        :return: The source of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this QueryTask.

        Source of query task.  # noqa: E501

        :param source: The source of this QueryTask.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def runtime(self):
        """Gets the runtime of this QueryTask.  # noqa: E501

        Runtime of prior queries.  # noqa: E501

        :return: The runtime of this QueryTask.  # noqa: E501
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this QueryTask.

        Runtime of prior queries.  # noqa: E501

        :param runtime: The runtime of this QueryTask.  # noqa: E501
        :type: float
        """

        self._runtime = runtime

    @property
    def rebuild_pdts(self):
        """Gets the rebuild_pdts of this QueryTask.  # noqa: E501

        Rebuild PDTS used in query.  # noqa: E501

        :return: The rebuild_pdts of this QueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._rebuild_pdts

    @rebuild_pdts.setter
    def rebuild_pdts(self, rebuild_pdts):
        """Sets the rebuild_pdts of this QueryTask.

        Rebuild PDTS used in query.  # noqa: E501

        :param rebuild_pdts: The rebuild_pdts of this QueryTask.  # noqa: E501
        :type: bool
        """

        self._rebuild_pdts = rebuild_pdts

    @property
    def result_source(self):
        """Gets the result_source of this QueryTask.  # noqa: E501

        Source of the results of the query.  # noqa: E501

        :return: The result_source of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._result_source

    @result_source.setter
    def result_source(self, result_source):
        """Sets the result_source of this QueryTask.

        Source of the results of the query.  # noqa: E501

        :param result_source: The result_source of this QueryTask.  # noqa: E501
        :type: str
        """

        self._result_source = result_source

    @property
    def look_id(self):
        """Gets the look_id of this QueryTask.  # noqa: E501

        Id of look associated with query.  # noqa: E501

        :return: The look_id of this QueryTask.  # noqa: E501
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """Sets the look_id of this QueryTask.

        Id of look associated with query.  # noqa: E501

        :param look_id: The look_id of this QueryTask.  # noqa: E501
        :type: int
        """

        self._look_id = look_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this QueryTask.  # noqa: E501

        Id of dashboard associated with query.  # noqa: E501

        :return: The dashboard_id of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this QueryTask.

        Id of dashboard associated with query.  # noqa: E501

        :param dashboard_id: The dashboard_id of this QueryTask.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def result_format(self):
        """Gets the result_format of this QueryTask.  # noqa: E501

        The data format of the query results.  # noqa: E501

        :return: The result_format of this QueryTask.  # noqa: E501
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        """Sets the result_format of this QueryTask.

        The data format of the query results.  # noqa: E501

        :param result_format: The result_format of this QueryTask.  # noqa: E501
        :type: str
        """

        self._result_format = result_format

    @property
    def can(self):
        """Gets the can of this QueryTask.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this QueryTask.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this QueryTask.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this QueryTask.  # noqa: E501
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
        if not isinstance(other, QueryTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other