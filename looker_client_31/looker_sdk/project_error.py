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


class ProjectError(object):
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
        'code': 'str',
        'severity': 'str',
        'kind': 'str',
        'message': 'str',
        'field_name': 'str',
        'file_path': 'str',
        'line_number': 'int',
        'model_id': 'str',
        'explore': 'str',
        'help_url': 'str',
        'params': 'dict(str, str)',
        'sanitized_message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'severity': 'severity',
        'kind': 'kind',
        'message': 'message',
        'field_name': 'field_name',
        'file_path': 'file_path',
        'line_number': 'line_number',
        'model_id': 'model_id',
        'explore': 'explore',
        'help_url': 'help_url',
        'params': 'params',
        'sanitized_message': 'sanitized_message'
    }

    def __init__(self, code=None, severity=None, kind=None, message=None, field_name=None, file_path=None, line_number=None, model_id=None, explore=None, help_url=None, params=None, sanitized_message=None):  # noqa: E501
        """ProjectError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._severity = None
        self._kind = None
        self._message = None
        self._field_name = None
        self._file_path = None
        self._line_number = None
        self._model_id = None
        self._explore = None
        self._help_url = None
        self._params = None
        self._sanitized_message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if severity is not None:
            self.severity = severity
        if kind is not None:
            self.kind = kind
        if message is not None:
            self.message = message
        if field_name is not None:
            self.field_name = field_name
        if file_path is not None:
            self.file_path = file_path
        if line_number is not None:
            self.line_number = line_number
        if model_id is not None:
            self.model_id = model_id
        if explore is not None:
            self.explore = explore
        if help_url is not None:
            self.help_url = help_url
        if params is not None:
            self.params = params
        if sanitized_message is not None:
            self.sanitized_message = sanitized_message

    @property
    def code(self):
        """Gets the code of this ProjectError.  # noqa: E501

        A stable token that uniquely identifies this class of error, ignoring parameter values. Error message text may vary due to parameters or localization, but error codes do not. For example, a \"File not found\" error will have the same error code regardless of the filename in question or the user's display language  # noqa: E501

        :return: The code of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProjectError.

        A stable token that uniquely identifies this class of error, ignoring parameter values. Error message text may vary due to parameters or localization, but error codes do not. For example, a \"File not found\" error will have the same error code regardless of the filename in question or the user's display language  # noqa: E501

        :param code: The code of this ProjectError.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def severity(self):
        """Gets the severity of this ProjectError.  # noqa: E501

        Severity: fatal, error, warning, info, success  # noqa: E501

        :return: The severity of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ProjectError.

        Severity: fatal, error, warning, info, success  # noqa: E501

        :param severity: The severity of this ProjectError.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def kind(self):
        """Gets the kind of this ProjectError.  # noqa: E501

        Error classification: syntax, deprecation, model_configuration, etc  # noqa: E501

        :return: The kind of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ProjectError.

        Error classification: syntax, deprecation, model_configuration, etc  # noqa: E501

        :param kind: The kind of this ProjectError.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def message(self):
        """Gets the message of this ProjectError.  # noqa: E501

        Error message which may contain information such as dashboard or model names that may be considered sensitive in some use cases. Avoid storing or sending this message outside of Looker  # noqa: E501

        :return: The message of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProjectError.

        Error message which may contain information such as dashboard or model names that may be considered sensitive in some use cases. Avoid storing or sending this message outside of Looker  # noqa: E501

        :param message: The message of this ProjectError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def field_name(self):
        """Gets the field_name of this ProjectError.  # noqa: E501

        The field associated with this error  # noqa: E501

        :return: The field_name of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ProjectError.

        The field associated with this error  # noqa: E501

        :param field_name: The field_name of this ProjectError.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def file_path(self):
        """Gets the file_path of this ProjectError.  # noqa: E501

        Name of the file containing this error  # noqa: E501

        :return: The file_path of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ProjectError.

        Name of the file containing this error  # noqa: E501

        :param file_path: The file_path of this ProjectError.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def line_number(self):
        """Gets the line_number of this ProjectError.  # noqa: E501

        Line number in the file of this error  # noqa: E501

        :return: The line_number of this ProjectError.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ProjectError.

        Line number in the file of this error  # noqa: E501

        :param line_number: The line_number of this ProjectError.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def model_id(self):
        """Gets the model_id of this ProjectError.  # noqa: E501

        The model associated with this error  # noqa: E501

        :return: The model_id of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ProjectError.

        The model associated with this error  # noqa: E501

        :param model_id: The model_id of this ProjectError.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def explore(self):
        """Gets the explore of this ProjectError.  # noqa: E501

        The explore associated with this error  # noqa: E501

        :return: The explore of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._explore

    @explore.setter
    def explore(self, explore):
        """Sets the explore of this ProjectError.

        The explore associated with this error  # noqa: E501

        :param explore: The explore of this ProjectError.  # noqa: E501
        :type: str
        """

        self._explore = explore

    @property
    def help_url(self):
        """Gets the help_url of this ProjectError.  # noqa: E501

        A link to Looker documentation about this error  # noqa: E501

        :return: The help_url of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._help_url

    @help_url.setter
    def help_url(self, help_url):
        """Sets the help_url of this ProjectError.

        A link to Looker documentation about this error  # noqa: E501

        :param help_url: The help_url of this ProjectError.  # noqa: E501
        :type: str
        """

        self._help_url = help_url

    @property
    def params(self):
        """Gets the params of this ProjectError.  # noqa: E501

        Error parameters  # noqa: E501

        :return: The params of this ProjectError.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ProjectError.

        Error parameters  # noqa: E501

        :param params: The params of this ProjectError.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

    @property
    def sanitized_message(self):
        """Gets the sanitized_message of this ProjectError.  # noqa: E501

        A version of the error message that does not contain potentially sensitive information. Suitable for situations in which messages are stored or sent to consumers outside of Looker, such as external logs. Sanitized messages will display \"(?)\" where sensitive information would appear in the corresponding non-sanitized message  # noqa: E501

        :return: The sanitized_message of this ProjectError.  # noqa: E501
        :rtype: str
        """
        return self._sanitized_message

    @sanitized_message.setter
    def sanitized_message(self, sanitized_message):
        """Sets the sanitized_message of this ProjectError.

        A version of the error message that does not contain potentially sensitive information. Suitable for situations in which messages are stored or sent to consumers outside of Looker, such as external logs. Sanitized messages will display \"(?)\" where sensitive information would appear in the corresponding non-sanitized message  # noqa: E501

        :param sanitized_message: The sanitized_message of this ProjectError.  # noqa: E501
        :type: str
        """

        self._sanitized_message = sanitized_message

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
        if not isinstance(other, ProjectError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
