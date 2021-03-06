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


class CredentialsEmbed(object):
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
        'external_user_id': 'str',
        'external_group_id': 'str',
        'created_at': 'str',
        'logged_in_at': 'str',
        'is_disabled': 'bool',
        'type': 'str',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'external_user_id': 'external_user_id',
        'external_group_id': 'external_group_id',
        'created_at': 'created_at',
        'logged_in_at': 'logged_in_at',
        'is_disabled': 'is_disabled',
        'type': 'type',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, id=None, external_user_id=None, external_group_id=None, created_at=None, logged_in_at=None, is_disabled=None, type=None, url=None, can=None):  # noqa: E501
        """CredentialsEmbed - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._external_user_id = None
        self._external_group_id = None
        self._created_at = None
        self._logged_in_at = None
        self._is_disabled = None
        self._type = None
        self._url = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_user_id is not None:
            self.external_user_id = external_user_id
        if external_group_id is not None:
            self.external_group_id = external_group_id
        if created_at is not None:
            self.created_at = created_at
        if logged_in_at is not None:
            self.logged_in_at = logged_in_at
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this CredentialsEmbed.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this CredentialsEmbed.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CredentialsEmbed.

        Unique Id  # noqa: E501

        :param id: The id of this CredentialsEmbed.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def external_user_id(self):
        """Gets the external_user_id of this CredentialsEmbed.  # noqa: E501

        Embedder's unique id for the user  # noqa: E501

        :return: The external_user_id of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, external_user_id):
        """Sets the external_user_id of this CredentialsEmbed.

        Embedder's unique id for the user  # noqa: E501

        :param external_user_id: The external_user_id of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._external_user_id = external_user_id

    @property
    def external_group_id(self):
        """Gets the external_group_id of this CredentialsEmbed.  # noqa: E501

        Embedder's id for a group to which this user was added during the most recent login  # noqa: E501

        :return: The external_group_id of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._external_group_id

    @external_group_id.setter
    def external_group_id(self, external_group_id):
        """Sets the external_group_id of this CredentialsEmbed.

        Embedder's id for a group to which this user was added during the most recent login  # noqa: E501

        :param external_group_id: The external_group_id of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._external_group_id = external_group_id

    @property
    def created_at(self):
        """Gets the created_at of this CredentialsEmbed.  # noqa: E501

        Timestamp for the creation of this credential  # noqa: E501

        :return: The created_at of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CredentialsEmbed.

        Timestamp for the creation of this credential  # noqa: E501

        :param created_at: The created_at of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def logged_in_at(self):
        """Gets the logged_in_at of this CredentialsEmbed.  # noqa: E501

        Timestamp for most recent login using credential  # noqa: E501

        :return: The logged_in_at of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._logged_in_at

    @logged_in_at.setter
    def logged_in_at(self, logged_in_at):
        """Sets the logged_in_at of this CredentialsEmbed.

        Timestamp for most recent login using credential  # noqa: E501

        :param logged_in_at: The logged_in_at of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._logged_in_at = logged_in_at

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CredentialsEmbed.  # noqa: E501

        Has this credential been disabled?  # noqa: E501

        :return: The is_disabled of this CredentialsEmbed.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CredentialsEmbed.

        Has this credential been disabled?  # noqa: E501

        :param is_disabled: The is_disabled of this CredentialsEmbed.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def type(self):
        """Gets the type of this CredentialsEmbed.  # noqa: E501

        Short name for the type of this kind of credential  # noqa: E501

        :return: The type of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialsEmbed.

        Short name for the type of this kind of credential  # noqa: E501

        :param type: The type of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this CredentialsEmbed.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this CredentialsEmbed.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CredentialsEmbed.

        Link to get this item  # noqa: E501

        :param url: The url of this CredentialsEmbed.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this CredentialsEmbed.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this CredentialsEmbed.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this CredentialsEmbed.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this CredentialsEmbed.  # noqa: E501
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
        if not isinstance(other, CredentialsEmbed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
