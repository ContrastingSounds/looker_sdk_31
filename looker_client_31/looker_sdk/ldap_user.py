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


class LDAPUser(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'ldap_id': 'str',
        'all_emails': 'list[str]',
        'ldap_dn': 'str',
        'roles': 'list[str]',
        'groups': 'list[str]',
        'attributes': 'dict(str, str)',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'ldap_id': 'ldap_id',
        'all_emails': 'all_emails',
        'ldap_dn': 'ldap_dn',
        'roles': 'roles',
        'groups': 'groups',
        'attributes': 'attributes',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, email=None, first_name=None, last_name=None, ldap_id=None, all_emails=None, ldap_dn=None, roles=None, groups=None, attributes=None, url=None, can=None):  # noqa: E501
        """LDAPUser - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._ldap_id = None
        self._all_emails = None
        self._ldap_dn = None
        self._roles = None
        self._groups = None
        self._attributes = None
        self._url = None
        self._can = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if ldap_id is not None:
            self.ldap_id = ldap_id
        if all_emails is not None:
            self.all_emails = all_emails
        if ldap_dn is not None:
            self.ldap_dn = ldap_dn
        if roles is not None:
            self.roles = roles
        if groups is not None:
            self.groups = groups
        if attributes is not None:
            self.attributes = attributes
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def email(self):
        """Gets the email of this LDAPUser.  # noqa: E501

        Primary email address  # noqa: E501

        :return: The email of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LDAPUser.

        Primary email address  # noqa: E501

        :param email: The email of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this LDAPUser.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this LDAPUser.

        First name  # noqa: E501

        :param first_name: The first_name of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this LDAPUser.  # noqa: E501

        Last Name  # noqa: E501

        :return: The last_name of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this LDAPUser.

        Last Name  # noqa: E501

        :param last_name: The last_name of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def ldap_id(self):
        """Gets the ldap_id of this LDAPUser.  # noqa: E501

        LDAP's Unique ID for the user  # noqa: E501

        :return: The ldap_id of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._ldap_id

    @ldap_id.setter
    def ldap_id(self, ldap_id):
        """Sets the ldap_id of this LDAPUser.

        LDAP's Unique ID for the user  # noqa: E501

        :param ldap_id: The ldap_id of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._ldap_id = ldap_id

    @property
    def all_emails(self):
        """Gets the all_emails of this LDAPUser.  # noqa: E501

        Array of user's email addresses and aliases for use in migration  # noqa: E501

        :return: The all_emails of this LDAPUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._all_emails

    @all_emails.setter
    def all_emails(self, all_emails):
        """Sets the all_emails of this LDAPUser.

        Array of user's email addresses and aliases for use in migration  # noqa: E501

        :param all_emails: The all_emails of this LDAPUser.  # noqa: E501
        :type: list[str]
        """

        self._all_emails = all_emails

    @property
    def ldap_dn(self):
        """Gets the ldap_dn of this LDAPUser.  # noqa: E501

        LDAP's distinguished name for the user record  # noqa: E501

        :return: The ldap_dn of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._ldap_dn

    @ldap_dn.setter
    def ldap_dn(self, ldap_dn):
        """Sets the ldap_dn of this LDAPUser.

        LDAP's distinguished name for the user record  # noqa: E501

        :param ldap_dn: The ldap_dn of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._ldap_dn = ldap_dn

    @property
    def roles(self):
        """Gets the roles of this LDAPUser.  # noqa: E501

        Array of user's roles (role names only)  # noqa: E501

        :return: The roles of this LDAPUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this LDAPUser.

        Array of user's roles (role names only)  # noqa: E501

        :param roles: The roles of this LDAPUser.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def groups(self):
        """Gets the groups of this LDAPUser.  # noqa: E501

        Array of user's groups (group names only)  # noqa: E501

        :return: The groups of this LDAPUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this LDAPUser.

        Array of user's groups (group names only)  # noqa: E501

        :param groups: The groups of this LDAPUser.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def attributes(self):
        """Gets the attributes of this LDAPUser.  # noqa: E501

        Dictionary of user's attrributes (name/value)  # noqa: E501

        :return: The attributes of this LDAPUser.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LDAPUser.

        Dictionary of user's attrributes (name/value)  # noqa: E501

        :param attributes: The attributes of this LDAPUser.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def url(self):
        """Gets the url of this LDAPUser.  # noqa: E501

        Link to ldap config  # noqa: E501

        :return: The url of this LDAPUser.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LDAPUser.

        Link to ldap config  # noqa: E501

        :param url: The url of this LDAPUser.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this LDAPUser.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this LDAPUser.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this LDAPUser.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this LDAPUser.  # noqa: E501
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
        if not isinstance(other, LDAPUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
