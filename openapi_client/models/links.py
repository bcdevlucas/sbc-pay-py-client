# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Links(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_self': 'str',
        'collection': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'collection': 'collection'
    }

    def __init__(self, _self=None, collection=None, local_vars_configuration=None):  # noqa: E501
        """Links - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__self = None
        self._collection = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if collection is not None:
            self.collection = collection

    @property
    def _self(self):
        """Gets the _self of this Links.  # noqa: E501

        Self link  # noqa: E501

        :return: The _self of this Links.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Links.

        Self link  # noqa: E501

        :param _self: The _self of this Links.  # noqa: E501
        :type _self: str
        """

        self.__self = _self

    @property
    def collection(self):
        """Gets the collection of this Links.  # noqa: E501

        collection link  # noqa: E501

        :return: The collection of this Links.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this Links.

        collection link  # noqa: E501

        :param collection: The collection of this Links.  # noqa: E501
        :type collection: str
        """

        self._collection = collection

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Links):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Links):
            return True

        return self.to_dict() != other.to_dict()
