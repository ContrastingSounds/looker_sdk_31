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


class LookmlModelExploreFieldTimeInterval(object):
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
        'count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'count': 'count'
    }

    def __init__(self, name=None, count=None):  # noqa: E501
        """LookmlModelExploreFieldTimeInterval - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if count is not None:
            self.count = count

    @property
    def name(self):
        """Gets the name of this LookmlModelExploreFieldTimeInterval.  # noqa: E501

        The type of time interval this field represents a grouping of. Valid values are: \"day\", \"hour\", \"minute\", \"month\", \"year\".  # noqa: E501

        :return: The name of this LookmlModelExploreFieldTimeInterval.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LookmlModelExploreFieldTimeInterval.

        The type of time interval this field represents a grouping of. Valid values are: \"day\", \"hour\", \"minute\", \"month\", \"year\".  # noqa: E501

        :param name: The name of this LookmlModelExploreFieldTimeInterval.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def count(self):
        """Gets the count of this LookmlModelExploreFieldTimeInterval.  # noqa: E501

        The number of intervals this field represents a grouping of.  # noqa: E501

        :return: The count of this LookmlModelExploreFieldTimeInterval.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this LookmlModelExploreFieldTimeInterval.

        The number of intervals this field represents a grouping of.  # noqa: E501

        :param count: The count of this LookmlModelExploreFieldTimeInterval.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, LookmlModelExploreFieldTimeInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
