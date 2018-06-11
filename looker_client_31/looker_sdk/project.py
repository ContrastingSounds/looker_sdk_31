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


class Project(object):
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
        'id': 'str',
        'name': 'str',
        'uses_git': 'bool',
        'git_remote_url': 'str',
        'git_service_name': 'str',
        'pull_request_mode': 'str',
        'validation_required': 'bool',
        'is_example': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'uses_git': 'uses_git',
        'git_remote_url': 'git_remote_url',
        'git_service_name': 'git_service_name',
        'pull_request_mode': 'pull_request_mode',
        'validation_required': 'validation_required',
        'is_example': 'is_example',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, uses_git=None, git_remote_url=None, git_service_name=None, pull_request_mode=None, validation_required=None, is_example=None, can=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._uses_git = None
        self._git_remote_url = None
        self._git_service_name = None
        self._pull_request_mode = None
        self._validation_required = None
        self._is_example = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if uses_git is not None:
            self.uses_git = uses_git
        if git_remote_url is not None:
            self.git_remote_url = git_remote_url
        if git_service_name is not None:
            self.git_service_name = git_service_name
        if pull_request_mode is not None:
            self.pull_request_mode = pull_request_mode
        if validation_required is not None:
            self.validation_required = validation_required
        if is_example is not None:
            self.is_example = is_example
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        Project Id  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        Project Id  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        Project display name  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        Project display name  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uses_git(self):
        """Gets the uses_git of this Project.  # noqa: E501

        If true the project is configured with a git repository  # noqa: E501

        :return: The uses_git of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._uses_git

    @uses_git.setter
    def uses_git(self, uses_git):
        """Sets the uses_git of this Project.

        If true the project is configured with a git repository  # noqa: E501

        :param uses_git: The uses_git of this Project.  # noqa: E501
        :type: bool
        """

        self._uses_git = uses_git

    @property
    def git_remote_url(self):
        """Gets the git_remote_url of this Project.  # noqa: E501

        Git remote repository url  # noqa: E501

        :return: The git_remote_url of this Project.  # noqa: E501
        :rtype: str
        """
        return self._git_remote_url

    @git_remote_url.setter
    def git_remote_url(self, git_remote_url):
        """Sets the git_remote_url of this Project.

        Git remote repository url  # noqa: E501

        :param git_remote_url: The git_remote_url of this Project.  # noqa: E501
        :type: str
        """

        self._git_remote_url = git_remote_url

    @property
    def git_service_name(self):
        """Gets the git_service_name of this Project.  # noqa: E501

        Name of the git service provider  # noqa: E501

        :return: The git_service_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._git_service_name

    @git_service_name.setter
    def git_service_name(self, git_service_name):
        """Sets the git_service_name of this Project.

        Name of the git service provider  # noqa: E501

        :param git_service_name: The git_service_name of this Project.  # noqa: E501
        :type: str
        """

        self._git_service_name = git_service_name

    @property
    def pull_request_mode(self):
        """Gets the pull_request_mode of this Project.  # noqa: E501

        The git pull request policy for this project. Valid values are: \"off\", \"links\", \"recommended\", \"required\".  # noqa: E501

        :return: The pull_request_mode of this Project.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_mode

    @pull_request_mode.setter
    def pull_request_mode(self, pull_request_mode):
        """Sets the pull_request_mode of this Project.

        The git pull request policy for this project. Valid values are: \"off\", \"links\", \"recommended\", \"required\".  # noqa: E501

        :param pull_request_mode: The pull_request_mode of this Project.  # noqa: E501
        :type: str
        """

        self._pull_request_mode = pull_request_mode

    @property
    def validation_required(self):
        """Gets the validation_required of this Project.  # noqa: E501

        Validation policy: If true, the project must pass all validation checks before project changes can be committed to the git repository  # noqa: E501

        :return: The validation_required of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._validation_required

    @validation_required.setter
    def validation_required(self, validation_required):
        """Sets the validation_required of this Project.

        Validation policy: If true, the project must pass all validation checks before project changes can be committed to the git repository  # noqa: E501

        :param validation_required: The validation_required of this Project.  # noqa: E501
        :type: bool
        """

        self._validation_required = validation_required

    @property
    def is_example(self):
        """Gets the is_example of this Project.  # noqa: E501

        If true the project is an example project and cannot be modified  # noqa: E501

        :return: The is_example of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._is_example

    @is_example.setter
    def is_example(self, is_example):
        """Sets the is_example of this Project.

        If true the project is an example project and cannot be modified  # noqa: E501

        :param is_example: The is_example of this Project.  # noqa: E501
        :type: bool
        """

        self._is_example = is_example

    @property
    def can(self):
        """Gets the can of this Project.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this Project.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this Project.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this Project.  # noqa: E501
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
