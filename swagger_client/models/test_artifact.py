# coding: utf-8

"""
    RADON CTT Server API

    This is API of the RADON Continuous Testing Tool (CTT) Server: <a href=\"https://github.com/radon-h2020/radon-ctt\">https://github.com/radon-h2020/radon-ctt<a/>  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TestArtifact(object):
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
        'commit_hash': 'str',
        'project_uuid': 'str',
        'sut_inputs_path': 'str',
        'sut_tosca_path': 'str',
        'ti_inputs_path': 'str',
        'ti_tosca_path': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'commit_hash': 'commit_hash',
        'project_uuid': 'project_uuid',
        'sut_inputs_path': 'sut_inputs_path',
        'sut_tosca_path': 'sut_tosca_path',
        'ti_inputs_path': 'ti_inputs_path',
        'ti_tosca_path': 'ti_tosca_path',
        'uuid': 'uuid'
    }

    def __init__(self, commit_hash=None, project_uuid=None, sut_inputs_path=None, sut_tosca_path=None, ti_inputs_path=None, ti_tosca_path=None, uuid=None):  # noqa: E501
        """TestArtifact - a model defined in Swagger"""  # noqa: E501
        self._commit_hash = None
        self._project_uuid = None
        self._sut_inputs_path = None
        self._sut_tosca_path = None
        self._ti_inputs_path = None
        self._ti_tosca_path = None
        self._uuid = None
        self.discriminator = None
        if commit_hash is not None:
            self.commit_hash = commit_hash
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if sut_inputs_path is not None:
            self.sut_inputs_path = sut_inputs_path
        if sut_tosca_path is not None:
            self.sut_tosca_path = sut_tosca_path
        if ti_inputs_path is not None:
            self.ti_inputs_path = ti_inputs_path
        if ti_tosca_path is not None:
            self.ti_tosca_path = ti_tosca_path
        if uuid is not None:
            self.uuid = uuid

    @property
    def commit_hash(self):
        """Gets the commit_hash of this TestArtifact.  # noqa: E501


        :return: The commit_hash of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this TestArtifact.


        :param commit_hash: The commit_hash of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._commit_hash = commit_hash

    @property
    def project_uuid(self):
        """Gets the project_uuid of this TestArtifact.  # noqa: E501


        :return: The project_uuid of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this TestArtifact.


        :param project_uuid: The project_uuid of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._project_uuid = project_uuid

    @property
    def sut_inputs_path(self):
        """Gets the sut_inputs_path of this TestArtifact.  # noqa: E501


        :return: The sut_inputs_path of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._sut_inputs_path

    @sut_inputs_path.setter
    def sut_inputs_path(self, sut_inputs_path):
        """Sets the sut_inputs_path of this TestArtifact.


        :param sut_inputs_path: The sut_inputs_path of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._sut_inputs_path = sut_inputs_path

    @property
    def sut_tosca_path(self):
        """Gets the sut_tosca_path of this TestArtifact.  # noqa: E501


        :return: The sut_tosca_path of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._sut_tosca_path

    @sut_tosca_path.setter
    def sut_tosca_path(self, sut_tosca_path):
        """Sets the sut_tosca_path of this TestArtifact.


        :param sut_tosca_path: The sut_tosca_path of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._sut_tosca_path = sut_tosca_path

    @property
    def ti_inputs_path(self):
        """Gets the ti_inputs_path of this TestArtifact.  # noqa: E501


        :return: The ti_inputs_path of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._ti_inputs_path

    @ti_inputs_path.setter
    def ti_inputs_path(self, ti_inputs_path):
        """Sets the ti_inputs_path of this TestArtifact.


        :param ti_inputs_path: The ti_inputs_path of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._ti_inputs_path = ti_inputs_path

    @property
    def ti_tosca_path(self):
        """Gets the ti_tosca_path of this TestArtifact.  # noqa: E501


        :return: The ti_tosca_path of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._ti_tosca_path

    @ti_tosca_path.setter
    def ti_tosca_path(self, ti_tosca_path):
        """Sets the ti_tosca_path of this TestArtifact.


        :param ti_tosca_path: The ti_tosca_path of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._ti_tosca_path = ti_tosca_path

    @property
    def uuid(self):
        """Gets the uuid of this TestArtifact.  # noqa: E501


        :return: The uuid of this TestArtifact.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TestArtifact.


        :param uuid: The uuid of this TestArtifact.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(TestArtifact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other