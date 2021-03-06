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


class SamlUserAttributeWrite(object):
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
        'required': 'bool',
        'user_attribute_ids': 'list[int]',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'required': 'required',
        'user_attribute_ids': 'user_attribute_ids',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, name=None, required=None, user_attribute_ids=None, url=None, can=None):  # noqa: E501
        """SamlUserAttributeWrite - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._required = None
        self._user_attribute_ids = None
        self._url = None
        self._can = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if user_attribute_ids is not None:
            self.user_attribute_ids = user_attribute_ids
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def name(self):
        """Gets the name of this SamlUserAttributeWrite.  # noqa: E501

        Name of User Attribute in Saml  # noqa: E501

        :return: The name of this SamlUserAttributeWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SamlUserAttributeWrite.

        Name of User Attribute in Saml  # noqa: E501

        :param name: The name of this SamlUserAttributeWrite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this SamlUserAttributeWrite.  # noqa: E501

        Required to be in Saml assertion for login to be allowed to succeed  # noqa: E501

        :return: The required of this SamlUserAttributeWrite.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SamlUserAttributeWrite.

        Required to be in Saml assertion for login to be allowed to succeed  # noqa: E501

        :param required: The required of this SamlUserAttributeWrite.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def user_attribute_ids(self):
        """Gets the user_attribute_ids of this SamlUserAttributeWrite.  # noqa: E501

        Looker User Attribute Ids  # noqa: E501

        :return: The user_attribute_ids of this SamlUserAttributeWrite.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_attribute_ids

    @user_attribute_ids.setter
    def user_attribute_ids(self, user_attribute_ids):
        """Sets the user_attribute_ids of this SamlUserAttributeWrite.

        Looker User Attribute Ids  # noqa: E501

        :param user_attribute_ids: The user_attribute_ids of this SamlUserAttributeWrite.  # noqa: E501
        :type: list[int]
        """

        self._user_attribute_ids = user_attribute_ids

    @property
    def url(self):
        """Gets the url of this SamlUserAttributeWrite.  # noqa: E501

        Link to saml config  # noqa: E501

        :return: The url of this SamlUserAttributeWrite.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SamlUserAttributeWrite.

        Link to saml config  # noqa: E501

        :param url: The url of this SamlUserAttributeWrite.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this SamlUserAttributeWrite.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this SamlUserAttributeWrite.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this SamlUserAttributeWrite.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this SamlUserAttributeWrite.  # noqa: E501
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
        if not isinstance(other, SamlUserAttributeWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
