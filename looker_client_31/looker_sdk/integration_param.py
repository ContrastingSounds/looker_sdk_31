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


class IntegrationParam(object):
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
        'label': 'str',
        'description': 'str',
        'required': 'bool',
        'has_value': 'bool',
        'value': 'str',
        'user_attribute_name': 'str',
        'sensitive': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'description': 'description',
        'required': 'required',
        'has_value': 'has_value',
        'value': 'value',
        'user_attribute_name': 'user_attribute_name',
        'sensitive': 'sensitive'
    }

    def __init__(self, name=None, label=None, description=None, required=None, has_value=None, value=None, user_attribute_name=None, sensitive=None):  # noqa: E501
        """IntegrationParam - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._description = None
        self._required = None
        self._has_value = None
        self._value = None
        self._user_attribute_name = None
        self._sensitive = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required
        if has_value is not None:
            self.has_value = has_value
        if value is not None:
            self.value = value
        if user_attribute_name is not None:
            self.user_attribute_name = user_attribute_name
        if sensitive is not None:
            self.sensitive = sensitive

    @property
    def name(self):
        """Gets the name of this IntegrationParam.  # noqa: E501

        Name of the parameter.  # noqa: E501

        :return: The name of this IntegrationParam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntegrationParam.

        Name of the parameter.  # noqa: E501

        :param name: The name of this IntegrationParam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this IntegrationParam.  # noqa: E501

        Label of the parameter.  # noqa: E501

        :return: The label of this IntegrationParam.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IntegrationParam.

        Label of the parameter.  # noqa: E501

        :param label: The label of this IntegrationParam.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this IntegrationParam.  # noqa: E501

        Short description of the parameter.  # noqa: E501

        :return: The description of this IntegrationParam.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntegrationParam.

        Short description of the parameter.  # noqa: E501

        :param description: The description of this IntegrationParam.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this IntegrationParam.  # noqa: E501

        Whether the parameter is required to be set to use the destination.  # noqa: E501

        :return: The required of this IntegrationParam.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IntegrationParam.

        Whether the parameter is required to be set to use the destination.  # noqa: E501

        :param required: The required of this IntegrationParam.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def has_value(self):
        """Gets the has_value of this IntegrationParam.  # noqa: E501

        Whether the parameter has a value set.  # noqa: E501

        :return: The has_value of this IntegrationParam.  # noqa: E501
        :rtype: bool
        """
        return self._has_value

    @has_value.setter
    def has_value(self, has_value):
        """Sets the has_value of this IntegrationParam.

        Whether the parameter has a value set.  # noqa: E501

        :param has_value: The has_value of this IntegrationParam.  # noqa: E501
        :type: bool
        """

        self._has_value = has_value

    @property
    def value(self):
        """Gets the value of this IntegrationParam.  # noqa: E501

        The current value of the parameter. Always null if the value is sensitive. When writing, null values will be ignored. Set the value to an empty string to clear it.  # noqa: E501

        :return: The value of this IntegrationParam.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IntegrationParam.

        The current value of the parameter. Always null if the value is sensitive. When writing, null values will be ignored. Set the value to an empty string to clear it.  # noqa: E501

        :param value: The value of this IntegrationParam.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def user_attribute_name(self):
        """Gets the user_attribute_name of this IntegrationParam.  # noqa: E501

        When present, the param's value comes from this user attribute instead of the 'value' parameter. Set to null to use the 'value'.  # noqa: E501

        :return: The user_attribute_name of this IntegrationParam.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute_name

    @user_attribute_name.setter
    def user_attribute_name(self, user_attribute_name):
        """Sets the user_attribute_name of this IntegrationParam.

        When present, the param's value comes from this user attribute instead of the 'value' parameter. Set to null to use the 'value'.  # noqa: E501

        :param user_attribute_name: The user_attribute_name of this IntegrationParam.  # noqa: E501
        :type: str
        """

        self._user_attribute_name = user_attribute_name

    @property
    def sensitive(self):
        """Gets the sensitive of this IntegrationParam.  # noqa: E501

        Whether the parameter contains sensitive data like API credentials.  # noqa: E501

        :return: The sensitive of this IntegrationParam.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this IntegrationParam.

        Whether the parameter contains sensitive data like API credentials.  # noqa: E501

        :param sensitive: The sensitive of this IntegrationParam.  # noqa: E501
        :type: bool
        """

        self._sensitive = sensitive

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
        if not isinstance(other, IntegrationParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
