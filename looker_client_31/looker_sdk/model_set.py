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


class ModelSet(object):
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
        'name': 'str',
        'models': 'list[str]',
        'built_in': 'bool',
        'all_access': 'bool',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'models': 'models',
        'built_in': 'built_in',
        'all_access': 'all_access',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, models=None, built_in=None, all_access=None, url=None, can=None):  # noqa: E501
        """ModelSet - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._models = None
        self._built_in = None
        self._all_access = None
        self._url = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if models is not None:
            self.models = models
        if built_in is not None:
            self.built_in = built_in
        if all_access is not None:
            self.all_access = all_access
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this ModelSet.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this ModelSet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelSet.

        Unique Id  # noqa: E501

        :param id: The id of this ModelSet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelSet.  # noqa: E501

        Name of ModelSet  # noqa: E501

        :return: The name of this ModelSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelSet.

        Name of ModelSet  # noqa: E501

        :param name: The name of this ModelSet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def models(self):
        """Gets the models of this ModelSet.  # noqa: E501


        :return: The models of this ModelSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ModelSet.


        :param models: The models of this ModelSet.  # noqa: E501
        :type: list[str]
        """

        self._models = models

    @property
    def built_in(self):
        """Gets the built_in of this ModelSet.  # noqa: E501


        :return: The built_in of this ModelSet.  # noqa: E501
        :rtype: bool
        """
        return self._built_in

    @built_in.setter
    def built_in(self, built_in):
        """Sets the built_in of this ModelSet.


        :param built_in: The built_in of this ModelSet.  # noqa: E501
        :type: bool
        """

        self._built_in = built_in

    @property
    def all_access(self):
        """Gets the all_access of this ModelSet.  # noqa: E501


        :return: The all_access of this ModelSet.  # noqa: E501
        :rtype: bool
        """
        return self._all_access

    @all_access.setter
    def all_access(self, all_access):
        """Sets the all_access of this ModelSet.


        :param all_access: The all_access of this ModelSet.  # noqa: E501
        :type: bool
        """

        self._all_access = all_access

    @property
    def url(self):
        """Gets the url of this ModelSet.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this ModelSet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ModelSet.

        Link to get this item  # noqa: E501

        :param url: The url of this ModelSet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this ModelSet.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ModelSet.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ModelSet.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ModelSet.  # noqa: E501
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
        if not isinstance(other, ModelSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
