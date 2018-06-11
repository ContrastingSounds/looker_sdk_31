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


class LookmlModelExploreAccessFilter(object):
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
        'field': 'str',
        'user_attribute': 'str'
    }

    attribute_map = {
        'field': 'field',
        'user_attribute': 'user_attribute'
    }

    def __init__(self, field=None, user_attribute=None):  # noqa: E501
        """LookmlModelExploreAccessFilter - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._user_attribute = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if user_attribute is not None:
            self.user_attribute = user_attribute

    @property
    def field(self):
        """Gets the field of this LookmlModelExploreAccessFilter.  # noqa: E501

        Field to be filtered  # noqa: E501

        :return: The field of this LookmlModelExploreAccessFilter.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this LookmlModelExploreAccessFilter.

        Field to be filtered  # noqa: E501

        :param field: The field of this LookmlModelExploreAccessFilter.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def user_attribute(self):
        """Gets the user_attribute of this LookmlModelExploreAccessFilter.  # noqa: E501

        User attribute name  # noqa: E501

        :return: The user_attribute of this LookmlModelExploreAccessFilter.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute

    @user_attribute.setter
    def user_attribute(self, user_attribute):
        """Sets the user_attribute of this LookmlModelExploreAccessFilter.

        User attribute name  # noqa: E501

        :param user_attribute: The user_attribute of this LookmlModelExploreAccessFilter.  # noqa: E501
        :type: str
        """

        self._user_attribute = user_attribute

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
        if not isinstance(other, LookmlModelExploreAccessFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
