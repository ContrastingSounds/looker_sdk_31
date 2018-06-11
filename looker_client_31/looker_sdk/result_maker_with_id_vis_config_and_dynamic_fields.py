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


class ResultMakerWithIdVisConfigAndDynamicFields(object):
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
        'id': 'int',
        'dynamic_fields': 'str',
        'sorts': 'str',
        'total': 'bool',
        'vis_config': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'dynamic_fields': 'dynamic_fields',
        'sorts': 'sorts',
        'total': 'total',
        'vis_config': 'vis_config',
        'can': 'can'
    }

    def __init__(self, id=None, dynamic_fields=None, sorts=None, total=None, vis_config=None, can=None):  # noqa: E501
        """ResultMakerWithIdVisConfigAndDynamicFields - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._dynamic_fields = None
        self._sorts = None
        self._total = None
        self._vis_config = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dynamic_fields is not None:
            self.dynamic_fields = dynamic_fields
        if sorts is not None:
            self.sorts = sorts
        if total is not None:
            self.total = total
        if vis_config is not None:
            self.vis_config = vis_config
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResultMakerWithIdVisConfigAndDynamicFields.

        Unique Id  # noqa: E501

        :param id: The id of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def dynamic_fields(self):
        """Gets the dynamic_fields of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        JSON string of dynamic field information  # noqa: E501

        :return: The dynamic_fields of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_fields

    @dynamic_fields.setter
    def dynamic_fields(self, dynamic_fields):
        """Sets the dynamic_fields of this ResultMakerWithIdVisConfigAndDynamicFields.

        JSON string of dynamic field information  # noqa: E501

        :param dynamic_fields: The dynamic_fields of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :type: str
        """

        self._dynamic_fields = dynamic_fields

    @property
    def sorts(self):
        """Gets the sorts of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        Sorts of the constituent Look, Query, or Merge Query  # noqa: E501

        :return: The sorts of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """Sets the sorts of this ResultMakerWithIdVisConfigAndDynamicFields.

        Sorts of the constituent Look, Query, or Merge Query  # noqa: E501

        :param sorts: The sorts of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :type: str
        """

        self._sorts = sorts

    @property
    def total(self):
        """Gets the total of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        Total of the constituent Look, Query, or Merge Query  # noqa: E501

        :return: The total of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: bool
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ResultMakerWithIdVisConfigAndDynamicFields.

        Total of the constituent Look, Query, or Merge Query  # noqa: E501

        :param total: The total of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :type: bool
        """

        self._total = total

    @property
    def vis_config(self):
        """Gets the vis_config of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        Vis config of the constituent Look, Query, or Merge Query  # noqa: E501

        :return: The vis_config of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: str
        """
        return self._vis_config

    @vis_config.setter
    def vis_config(self, vis_config):
        """Sets the vis_config of this ResultMakerWithIdVisConfigAndDynamicFields.

        Vis config of the constituent Look, Query, or Merge Query  # noqa: E501

        :param vis_config: The vis_config of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :type: str
        """

        self._vis_config = vis_config

    @property
    def can(self):
        """Gets the can of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ResultMakerWithIdVisConfigAndDynamicFields.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ResultMakerWithIdVisConfigAndDynamicFields.  # noqa: E501
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
        if not isinstance(other, ResultMakerWithIdVisConfigAndDynamicFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other