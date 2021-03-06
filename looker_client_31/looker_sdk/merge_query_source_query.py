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

from looker_client_31.looker_sdk.merge_fields import MergeFields  # noqa: F401,E501


class MergeQuerySourceQuery(object):
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
        'query_id': 'int',
        'name': 'str',
        'merge_fields': 'list[MergeFields]',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'query_id': 'query_id',
        'name': 'name',
        'merge_fields': 'merge_fields',
        'can': 'can'
    }

    def __init__(self, query_id=None, name=None, merge_fields=None, can=None):  # noqa: E501
        """MergeQuerySourceQuery - a model defined in Swagger"""  # noqa: E501

        self._query_id = None
        self._name = None
        self._merge_fields = None
        self._can = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if name is not None:
            self.name = name
        if merge_fields is not None:
            self.merge_fields = merge_fields
        if can is not None:
            self.can = can

    @property
    def query_id(self):
        """Gets the query_id of this MergeQuerySourceQuery.  # noqa: E501

        Id of the query to merge  # noqa: E501

        :return: The query_id of this MergeQuerySourceQuery.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this MergeQuerySourceQuery.

        Id of the query to merge  # noqa: E501

        :param query_id: The query_id of this MergeQuerySourceQuery.  # noqa: E501
        :type: int
        """

        self._query_id = query_id

    @property
    def name(self):
        """Gets the name of this MergeQuerySourceQuery.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this MergeQuerySourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MergeQuerySourceQuery.

        Display name  # noqa: E501

        :param name: The name of this MergeQuerySourceQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def merge_fields(self):
        """Gets the merge_fields of this MergeQuerySourceQuery.  # noqa: E501

        An array defining which fields of the source query are mapped onto fields of the merge query  # noqa: E501

        :return: The merge_fields of this MergeQuerySourceQuery.  # noqa: E501
        :rtype: list[MergeFields]
        """
        return self._merge_fields

    @merge_fields.setter
    def merge_fields(self, merge_fields):
        """Sets the merge_fields of this MergeQuerySourceQuery.

        An array defining which fields of the source query are mapped onto fields of the merge query  # noqa: E501

        :param merge_fields: The merge_fields of this MergeQuerySourceQuery.  # noqa: E501
        :type: list[MergeFields]
        """

        self._merge_fields = merge_fields

    @property
    def can(self):
        """Gets the can of this MergeQuerySourceQuery.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this MergeQuerySourceQuery.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this MergeQuerySourceQuery.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this MergeQuerySourceQuery.  # noqa: E501
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
        if not isinstance(other, MergeQuerySourceQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
