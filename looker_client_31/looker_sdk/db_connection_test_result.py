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


class DBConnectionTestResult(object):
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
        'status': 'str',
        'message': 'str',
        'connection_string': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'message': 'message',
        'connection_string': 'connection_string',
        'can': 'can'
    }

    def __init__(self, name=None, status=None, message=None, connection_string=None, can=None):  # noqa: E501
        """DBConnectionTestResult - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._status = None
        self._message = None
        self._connection_string = None
        self._can = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if connection_string is not None:
            self.connection_string = connection_string
        if can is not None:
            self.can = can

    @property
    def name(self):
        """Gets the name of this DBConnectionTestResult.  # noqa: E501

        Name of test  # noqa: E501

        :return: The name of this DBConnectionTestResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DBConnectionTestResult.

        Name of test  # noqa: E501

        :param name: The name of this DBConnectionTestResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this DBConnectionTestResult.  # noqa: E501

        Result code of test  # noqa: E501

        :return: The status of this DBConnectionTestResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DBConnectionTestResult.

        Result code of test  # noqa: E501

        :param status: The status of this DBConnectionTestResult.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this DBConnectionTestResult.  # noqa: E501

        Result message of test  # noqa: E501

        :return: The message of this DBConnectionTestResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DBConnectionTestResult.

        Result message of test  # noqa: E501

        :param message: The message of this DBConnectionTestResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def connection_string(self):
        """Gets the connection_string of this DBConnectionTestResult.  # noqa: E501

        JDBC connection string. (only populated in the 'connect' test)  # noqa: E501

        :return: The connection_string of this DBConnectionTestResult.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this DBConnectionTestResult.

        JDBC connection string. (only populated in the 'connect' test)  # noqa: E501

        :param connection_string: The connection_string of this DBConnectionTestResult.  # noqa: E501
        :type: str
        """

        self._connection_string = connection_string

    @property
    def can(self):
        """Gets the can of this DBConnectionTestResult.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this DBConnectionTestResult.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this DBConnectionTestResult.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this DBConnectionTestResult.  # noqa: E501
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
        if not isinstance(other, DBConnectionTestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
