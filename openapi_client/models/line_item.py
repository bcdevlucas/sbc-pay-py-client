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


class LineItem(object):
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
        'id': 'int',
        'quantity': 'int',
        'filing_fees': 'float',
        'service_fees': 'float',
        'future_effective_fees': 'float',
        'priority_fees': 'float',
        'processing_fees': 'float',
        'description': 'float',
        'gst': 'float',
        'pst': 'float',
        'status_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'quantity': 'quantity',
        'filing_fees': 'filingFees',
        'service_fees': 'serviceFees',
        'future_effective_fees': 'futureEffectiveFees',
        'priority_fees': 'priorityFees',
        'processing_fees': 'processingFees',
        'description': 'description',
        'gst': 'gst',
        'pst': 'pst',
        'status_code': 'statusCode'
    }

    def __init__(self, id=None, quantity=None, filing_fees=None, service_fees=None, future_effective_fees=None, priority_fees=None, processing_fees=None, description=None, gst=None, pst=None, status_code=None, local_vars_configuration=None):  # noqa: E501
        """LineItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._quantity = None
        self._filing_fees = None
        self._service_fees = None
        self._future_effective_fees = None
        self._priority_fees = None
        self._processing_fees = None
        self._description = None
        self._gst = None
        self._pst = None
        self._status_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if quantity is not None:
            self.quantity = quantity
        if filing_fees is not None:
            self.filing_fees = filing_fees
        if service_fees is not None:
            self.service_fees = service_fees
        if future_effective_fees is not None:
            self.future_effective_fees = future_effective_fees
        if priority_fees is not None:
            self.priority_fees = priority_fees
        if processing_fees is not None:
            self.processing_fees = processing_fees
        if description is not None:
            self.description = description
        if gst is not None:
            self.gst = gst
        if pst is not None:
            self.pst = pst
        if status_code is not None:
            self.status_code = status_code

    @property
    def id(self):
        """Gets the id of this LineItem.  # noqa: E501

        Unique identifier for payment line item  # noqa: E501

        :return: The id of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LineItem.

        Unique identifier for payment line item  # noqa: E501

        :param id: The id of this LineItem.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501

        Quantity of fee  # noqa: E501

        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.

        Quantity of fee  # noqa: E501

        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def filing_fees(self):
        """Gets the filing_fees of this LineItem.  # noqa: E501

        Fees for filing  # noqa: E501

        :return: The filing_fees of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._filing_fees

    @filing_fees.setter
    def filing_fees(self, filing_fees):
        """Sets the filing_fees of this LineItem.

        Fees for filing  # noqa: E501

        :param filing_fees: The filing_fees of this LineItem.  # noqa: E501
        :type filing_fees: float
        """

        self._filing_fees = filing_fees

    @property
    def service_fees(self):
        """Gets the service_fees of this LineItem.  # noqa: E501

        Applicable service fees  # noqa: E501

        :return: The service_fees of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._service_fees

    @service_fees.setter
    def service_fees(self, service_fees):
        """Sets the service_fees of this LineItem.

        Applicable service fees  # noqa: E501

        :param service_fees: The service_fees of this LineItem.  # noqa: E501
        :type service_fees: float
        """

        self._service_fees = service_fees

    @property
    def future_effective_fees(self):
        """Gets the future_effective_fees of this LineItem.  # noqa: E501

        Future effective fees  # noqa: E501

        :return: The future_effective_fees of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._future_effective_fees

    @future_effective_fees.setter
    def future_effective_fees(self, future_effective_fees):
        """Sets the future_effective_fees of this LineItem.

        Future effective fees  # noqa: E501

        :param future_effective_fees: The future_effective_fees of this LineItem.  # noqa: E501
        :type future_effective_fees: float
        """

        self._future_effective_fees = future_effective_fees

    @property
    def priority_fees(self):
        """Gets the priority_fees of this LineItem.  # noqa: E501

        Applicable processing fees  # noqa: E501

        :return: The priority_fees of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._priority_fees

    @priority_fees.setter
    def priority_fees(self, priority_fees):
        """Sets the priority_fees of this LineItem.

        Applicable processing fees  # noqa: E501

        :param priority_fees: The priority_fees of this LineItem.  # noqa: E501
        :type priority_fees: float
        """

        self._priority_fees = priority_fees

    @property
    def processing_fees(self):
        """Gets the processing_fees of this LineItem.  # noqa: E501

        Applicable processing fees  # noqa: E501

        :return: The processing_fees of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._processing_fees

    @processing_fees.setter
    def processing_fees(self, processing_fees):
        """Sets the processing_fees of this LineItem.

        Applicable processing fees  # noqa: E501

        :param processing_fees: The processing_fees of this LineItem.  # noqa: E501
        :type processing_fees: float
        """

        self._processing_fees = processing_fees

    @property
    def description(self):
        """Gets the description of this LineItem.  # noqa: E501

        Description of the fee item  # noqa: E501

        :return: The description of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LineItem.

        Description of the fee item  # noqa: E501

        :param description: The description of this LineItem.  # noqa: E501
        :type description: float
        """

        self._description = description

    @property
    def gst(self):
        """Gets the gst of this LineItem.  # noqa: E501

        Applicable gst of the fee item  # noqa: E501

        :return: The gst of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._gst

    @gst.setter
    def gst(self, gst):
        """Sets the gst of this LineItem.

        Applicable gst of the fee item  # noqa: E501

        :param gst: The gst of this LineItem.  # noqa: E501
        :type gst: float
        """

        self._gst = gst

    @property
    def pst(self):
        """Gets the pst of this LineItem.  # noqa: E501

        Applicable pst of the fee item  # noqa: E501

        :return: The pst of this LineItem.  # noqa: E501
        :rtype: float
        """
        return self._pst

    @pst.setter
    def pst(self, pst):
        """Sets the pst of this LineItem.

        Applicable pst of the fee item  # noqa: E501

        :param pst: The pst of this LineItem.  # noqa: E501
        :type pst: float
        """

        self._pst = pst

    @property
    def status_code(self):
        """Gets the status_code of this LineItem.  # noqa: E501

        Line item status  # noqa: E501

        :return: The status_code of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this LineItem.

        Line item status  # noqa: E501

        :param status_code: The status_code of this LineItem.  # noqa: E501
        :type status_code: str
        """
        allowed_values = ["DRAFT", "IN_PROGRESS", "CREATED", "COMPLETED", "PARTIAL", "FAILED", "REFUNDED", "CANCELLED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

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
        if not isinstance(other, LineItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineItem):
            return True

        return self.to_dict() != other.to_dict()
