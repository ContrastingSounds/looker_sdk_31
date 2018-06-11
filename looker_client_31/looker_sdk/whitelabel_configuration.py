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


class WhitelabelConfiguration(object):
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
        'logo_file': 'str',
        'logo_url': 'str',
        'favicon_file': 'str',
        'favicon_url': 'str',
        'default_title': 'str',
        'show_help_menu': 'bool',
        'show_docs': 'bool',
        'show_email_sub_options': 'bool',
        'allow_looker_mentions': 'bool',
        'allow_looker_links': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'logo_file': 'logo_file',
        'logo_url': 'logo_url',
        'favicon_file': 'favicon_file',
        'favicon_url': 'favicon_url',
        'default_title': 'default_title',
        'show_help_menu': 'show_help_menu',
        'show_docs': 'show_docs',
        'show_email_sub_options': 'show_email_sub_options',
        'allow_looker_mentions': 'allow_looker_mentions',
        'allow_looker_links': 'allow_looker_links',
        'can': 'can'
    }

    def __init__(self, id=None, logo_file=None, logo_url=None, favicon_file=None, favicon_url=None, default_title=None, show_help_menu=None, show_docs=None, show_email_sub_options=None, allow_looker_mentions=None, allow_looker_links=None, can=None):  # noqa: E501
        """WhitelabelConfiguration - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._logo_file = None
        self._logo_url = None
        self._favicon_file = None
        self._favicon_url = None
        self._default_title = None
        self._show_help_menu = None
        self._show_docs = None
        self._show_email_sub_options = None
        self._allow_looker_mentions = None
        self._allow_looker_links = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if logo_file is not None:
            self.logo_file = logo_file
        if logo_url is not None:
            self.logo_url = logo_url
        if favicon_file is not None:
            self.favicon_file = favicon_file
        if favicon_url is not None:
            self.favicon_url = favicon_url
        if default_title is not None:
            self.default_title = default_title
        if show_help_menu is not None:
            self.show_help_menu = show_help_menu
        if show_docs is not None:
            self.show_docs = show_docs
        if show_email_sub_options is not None:
            self.show_email_sub_options = show_email_sub_options
        if allow_looker_mentions is not None:
            self.allow_looker_mentions = allow_looker_mentions
        if allow_looker_links is not None:
            self.allow_looker_links = allow_looker_links
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this WhitelabelConfiguration.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this WhitelabelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhitelabelConfiguration.

        Unique Id  # noqa: E501

        :param id: The id of this WhitelabelConfiguration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def logo_file(self):
        """Gets the logo_file of this WhitelabelConfiguration.  # noqa: E501

        Customer logo image. Expected base64 encoded data (write-only)  # noqa: E501

        :return: The logo_file of this WhitelabelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._logo_file

    @logo_file.setter
    def logo_file(self, logo_file):
        """Sets the logo_file of this WhitelabelConfiguration.

        Customer logo image. Expected base64 encoded data (write-only)  # noqa: E501

        :param logo_file: The logo_file of this WhitelabelConfiguration.  # noqa: E501
        :type: str
        """

        self._logo_file = logo_file

    @property
    def logo_url(self):
        """Gets the logo_url of this WhitelabelConfiguration.  # noqa: E501

        Logo image url (read-only)  # noqa: E501

        :return: The logo_url of this WhitelabelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this WhitelabelConfiguration.

        Logo image url (read-only)  # noqa: E501

        :param logo_url: The logo_url of this WhitelabelConfiguration.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def favicon_file(self):
        """Gets the favicon_file of this WhitelabelConfiguration.  # noqa: E501

        Custom favicon image. Expected base64 encoded data (write-only)  # noqa: E501

        :return: The favicon_file of this WhitelabelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._favicon_file

    @favicon_file.setter
    def favicon_file(self, favicon_file):
        """Sets the favicon_file of this WhitelabelConfiguration.

        Custom favicon image. Expected base64 encoded data (write-only)  # noqa: E501

        :param favicon_file: The favicon_file of this WhitelabelConfiguration.  # noqa: E501
        :type: str
        """

        self._favicon_file = favicon_file

    @property
    def favicon_url(self):
        """Gets the favicon_url of this WhitelabelConfiguration.  # noqa: E501

        Favicon image url (read-only)  # noqa: E501

        :return: The favicon_url of this WhitelabelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._favicon_url

    @favicon_url.setter
    def favicon_url(self, favicon_url):
        """Sets the favicon_url of this WhitelabelConfiguration.

        Favicon image url (read-only)  # noqa: E501

        :param favicon_url: The favicon_url of this WhitelabelConfiguration.  # noqa: E501
        :type: str
        """

        self._favicon_url = favicon_url

    @property
    def default_title(self):
        """Gets the default_title of this WhitelabelConfiguration.  # noqa: E501

        Default page title  # noqa: E501

        :return: The default_title of this WhitelabelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._default_title

    @default_title.setter
    def default_title(self, default_title):
        """Sets the default_title of this WhitelabelConfiguration.

        Default page title  # noqa: E501

        :param default_title: The default_title of this WhitelabelConfiguration.  # noqa: E501
        :type: str
        """

        self._default_title = default_title

    @property
    def show_help_menu(self):
        """Gets the show_help_menu of this WhitelabelConfiguration.  # noqa: E501

        Boolean to toggle showing help menus  # noqa: E501

        :return: The show_help_menu of this WhitelabelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._show_help_menu

    @show_help_menu.setter
    def show_help_menu(self, show_help_menu):
        """Sets the show_help_menu of this WhitelabelConfiguration.

        Boolean to toggle showing help menus  # noqa: E501

        :param show_help_menu: The show_help_menu of this WhitelabelConfiguration.  # noqa: E501
        :type: bool
        """

        self._show_help_menu = show_help_menu

    @property
    def show_docs(self):
        """Gets the show_docs of this WhitelabelConfiguration.  # noqa: E501

        Boolean to toggle showing docs  # noqa: E501

        :return: The show_docs of this WhitelabelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._show_docs

    @show_docs.setter
    def show_docs(self, show_docs):
        """Sets the show_docs of this WhitelabelConfiguration.

        Boolean to toggle showing docs  # noqa: E501

        :param show_docs: The show_docs of this WhitelabelConfiguration.  # noqa: E501
        :type: bool
        """

        self._show_docs = show_docs

    @property
    def show_email_sub_options(self):
        """Gets the show_email_sub_options of this WhitelabelConfiguration.  # noqa: E501

        Boolean to toggle showing email subscription options.  # noqa: E501

        :return: The show_email_sub_options of this WhitelabelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._show_email_sub_options

    @show_email_sub_options.setter
    def show_email_sub_options(self, show_email_sub_options):
        """Sets the show_email_sub_options of this WhitelabelConfiguration.

        Boolean to toggle showing email subscription options.  # noqa: E501

        :param show_email_sub_options: The show_email_sub_options of this WhitelabelConfiguration.  # noqa: E501
        :type: bool
        """

        self._show_email_sub_options = show_email_sub_options

    @property
    def allow_looker_mentions(self):
        """Gets the allow_looker_mentions of this WhitelabelConfiguration.  # noqa: E501

        Boolean to toggle mentions of Looker in emails  # noqa: E501

        :return: The allow_looker_mentions of this WhitelabelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_looker_mentions

    @allow_looker_mentions.setter
    def allow_looker_mentions(self, allow_looker_mentions):
        """Sets the allow_looker_mentions of this WhitelabelConfiguration.

        Boolean to toggle mentions of Looker in emails  # noqa: E501

        :param allow_looker_mentions: The allow_looker_mentions of this WhitelabelConfiguration.  # noqa: E501
        :type: bool
        """

        self._allow_looker_mentions = allow_looker_mentions

    @property
    def allow_looker_links(self):
        """Gets the allow_looker_links of this WhitelabelConfiguration.  # noqa: E501

        Boolean to toggle links to Looker in emails  # noqa: E501

        :return: The allow_looker_links of this WhitelabelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_looker_links

    @allow_looker_links.setter
    def allow_looker_links(self, allow_looker_links):
        """Sets the allow_looker_links of this WhitelabelConfiguration.

        Boolean to toggle links to Looker in emails  # noqa: E501

        :param allow_looker_links: The allow_looker_links of this WhitelabelConfiguration.  # noqa: E501
        :type: bool
        """

        self._allow_looker_links = allow_looker_links

    @property
    def can(self):
        """Gets the can of this WhitelabelConfiguration.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this WhitelabelConfiguration.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this WhitelabelConfiguration.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this WhitelabelConfiguration.  # noqa: E501
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
        if not isinstance(other, WhitelabelConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
