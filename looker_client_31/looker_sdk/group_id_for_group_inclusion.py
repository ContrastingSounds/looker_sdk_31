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


class GroupIdForGroupInclusion(object):
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
        'group_id': 'int',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'group_id': 'group_id',
        'can': 'can'
    }

    def __init__(self, group_id=None, can=None):  # noqa: E501
        """GroupIdForGroupInclusion - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._can = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if can is not None:
            self.can = can

    @property
    def group_id(self):
        """Gets the group_id of this GroupIdForGroupInclusion.  # noqa: E501

        Id of group  # noqa: E501

        :return: The group_id of this GroupIdForGroupInclusion.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupIdForGroupInclusion.

        Id of group  # noqa: E501

        :param group_id: The group_id of this GroupIdForGroupInclusion.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def can(self):
        """Gets the can of this GroupIdForGroupInclusion.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this GroupIdForGroupInclusion.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this GroupIdForGroupInclusion.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this GroupIdForGroupInclusion.  # noqa: E501
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
        if not isinstance(other, GroupIdForGroupInclusion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
