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


class LookmlModelExploreJoins(object):
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
        'name': 'str',
        'dependent_fields': 'list[str]',
        'fields': 'list[str]',
        'foreign_key': 'str',
        '_from': 'str',
        'outer_only': 'bool',
        'relationship': 'str',
        'required_joins': 'list[str]',
        'sql_foreign_key': 'str',
        'sql_on': 'str',
        'sql_table_name': 'str',
        'type': 'str',
        'view_label': 'str'
    }

    attribute_map = {
        'name': 'name',
        'dependent_fields': 'dependent_fields',
        'fields': 'fields',
        'foreign_key': 'foreign_key',
        '_from': 'from',
        'outer_only': 'outer_only',
        'relationship': 'relationship',
        'required_joins': 'required_joins',
        'sql_foreign_key': 'sql_foreign_key',
        'sql_on': 'sql_on',
        'sql_table_name': 'sql_table_name',
        'type': 'type',
        'view_label': 'view_label'
    }

    def __init__(self, name=None, dependent_fields=None, fields=None, foreign_key=None, _from=None, outer_only=None, relationship=None, required_joins=None, sql_foreign_key=None, sql_on=None, sql_table_name=None, type=None, view_label=None):  # noqa: E501
        """LookmlModelExploreJoins - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._dependent_fields = None
        self._fields = None
        self._foreign_key = None
        self.__from = None
        self._outer_only = None
        self._relationship = None
        self._required_joins = None
        self._sql_foreign_key = None
        self._sql_on = None
        self._sql_table_name = None
        self._type = None
        self._view_label = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dependent_fields is not None:
            self.dependent_fields = dependent_fields
        if fields is not None:
            self.fields = fields
        if foreign_key is not None:
            self.foreign_key = foreign_key
        if _from is not None:
            self._from = _from
        if outer_only is not None:
            self.outer_only = outer_only
        if relationship is not None:
            self.relationship = relationship
        if required_joins is not None:
            self.required_joins = required_joins
        if sql_foreign_key is not None:
            self.sql_foreign_key = sql_foreign_key
        if sql_on is not None:
            self.sql_on = sql_on
        if sql_table_name is not None:
            self.sql_table_name = sql_table_name
        if type is not None:
            self.type = type
        if view_label is not None:
            self.view_label = view_label

    @property
    def name(self):
        """Gets the name of this LookmlModelExploreJoins.  # noqa: E501

        Name of this join (and name of the view to join)  # noqa: E501

        :return: The name of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LookmlModelExploreJoins.

        Name of this join (and name of the view to join)  # noqa: E501

        :param name: The name of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dependent_fields(self):
        """Gets the dependent_fields of this LookmlModelExploreJoins.  # noqa: E501

        Fields referenced by the join  # noqa: E501

        :return: The dependent_fields of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependent_fields

    @dependent_fields.setter
    def dependent_fields(self, dependent_fields):
        """Sets the dependent_fields of this LookmlModelExploreJoins.

        Fields referenced by the join  # noqa: E501

        :param dependent_fields: The dependent_fields of this LookmlModelExploreJoins.  # noqa: E501
        :type: list[str]
        """

        self._dependent_fields = dependent_fields

    @property
    def fields(self):
        """Gets the fields of this LookmlModelExploreJoins.  # noqa: E501

        Fields of the joined view to pull into this explore  # noqa: E501

        :return: The fields of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this LookmlModelExploreJoins.

        Fields of the joined view to pull into this explore  # noqa: E501

        :param fields: The fields of this LookmlModelExploreJoins.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def foreign_key(self):
        """Gets the foreign_key of this LookmlModelExploreJoins.  # noqa: E501

        Name of the dimension in this explore whose value is in the primary key of the joined view  # noqa: E501

        :return: The foreign_key of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._foreign_key

    @foreign_key.setter
    def foreign_key(self, foreign_key):
        """Sets the foreign_key of this LookmlModelExploreJoins.

        Name of the dimension in this explore whose value is in the primary key of the joined view  # noqa: E501

        :param foreign_key: The foreign_key of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._foreign_key = foreign_key

    @property
    def _from(self):
        """Gets the _from of this LookmlModelExploreJoins.  # noqa: E501

        Name of view to join  # noqa: E501

        :return: The _from of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this LookmlModelExploreJoins.

        Name of view to join  # noqa: E501

        :param _from: The _from of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def outer_only(self):
        """Gets the outer_only of this LookmlModelExploreJoins.  # noqa: E501

        Specifies whether all queries must use an outer join  # noqa: E501

        :return: The outer_only of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: bool
        """
        return self._outer_only

    @outer_only.setter
    def outer_only(self, outer_only):
        """Sets the outer_only of this LookmlModelExploreJoins.

        Specifies whether all queries must use an outer join  # noqa: E501

        :param outer_only: The outer_only of this LookmlModelExploreJoins.  # noqa: E501
        :type: bool
        """

        self._outer_only = outer_only

    @property
    def relationship(self):
        """Gets the relationship of this LookmlModelExploreJoins.  # noqa: E501

        many_to_one, one_to_one, one_to_many, many_to_many  # noqa: E501

        :return: The relationship of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this LookmlModelExploreJoins.

        many_to_one, one_to_one, one_to_many, many_to_many  # noqa: E501

        :param relationship: The relationship of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._relationship = relationship

    @property
    def required_joins(self):
        """Gets the required_joins of this LookmlModelExploreJoins.  # noqa: E501

        Names of joins that must always be included in SQL queries  # noqa: E501

        :return: The required_joins of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_joins

    @required_joins.setter
    def required_joins(self, required_joins):
        """Sets the required_joins of this LookmlModelExploreJoins.

        Names of joins that must always be included in SQL queries  # noqa: E501

        :param required_joins: The required_joins of this LookmlModelExploreJoins.  # noqa: E501
        :type: list[str]
        """

        self._required_joins = required_joins

    @property
    def sql_foreign_key(self):
        """Gets the sql_foreign_key of this LookmlModelExploreJoins.  # noqa: E501

        SQL expression that produces a foreign key  # noqa: E501

        :return: The sql_foreign_key of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._sql_foreign_key

    @sql_foreign_key.setter
    def sql_foreign_key(self, sql_foreign_key):
        """Sets the sql_foreign_key of this LookmlModelExploreJoins.

        SQL expression that produces a foreign key  # noqa: E501

        :param sql_foreign_key: The sql_foreign_key of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._sql_foreign_key = sql_foreign_key

    @property
    def sql_on(self):
        """Gets the sql_on of this LookmlModelExploreJoins.  # noqa: E501

        SQL ON expression describing the join condition  # noqa: E501

        :return: The sql_on of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._sql_on

    @sql_on.setter
    def sql_on(self, sql_on):
        """Sets the sql_on of this LookmlModelExploreJoins.

        SQL ON expression describing the join condition  # noqa: E501

        :param sql_on: The sql_on of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._sql_on = sql_on

    @property
    def sql_table_name(self):
        """Gets the sql_table_name of this LookmlModelExploreJoins.  # noqa: E501

        SQL table name to join  # noqa: E501

        :return: The sql_table_name of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._sql_table_name

    @sql_table_name.setter
    def sql_table_name(self, sql_table_name):
        """Sets the sql_table_name of this LookmlModelExploreJoins.

        SQL table name to join  # noqa: E501

        :param sql_table_name: The sql_table_name of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._sql_table_name = sql_table_name

    @property
    def type(self):
        """Gets the type of this LookmlModelExploreJoins.  # noqa: E501

        The join type: left_outer, full_outer, inner, or cross  # noqa: E501

        :return: The type of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LookmlModelExploreJoins.

        The join type: left_outer, full_outer, inner, or cross  # noqa: E501

        :param type: The type of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def view_label(self):
        """Gets the view_label of this LookmlModelExploreJoins.  # noqa: E501

        Label to display in UI selectors  # noqa: E501

        :return: The view_label of this LookmlModelExploreJoins.  # noqa: E501
        :rtype: str
        """
        return self._view_label

    @view_label.setter
    def view_label(self, view_label):
        """Sets the view_label of this LookmlModelExploreJoins.

        Label to display in UI selectors  # noqa: E501

        :param view_label: The view_label of this LookmlModelExploreJoins.  # noqa: E501
        :type: str
        """

        self._view_label = view_label

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
        if not isinstance(other, LookmlModelExploreJoins):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other