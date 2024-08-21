# coding: utf-8

"""
    Speech Services API version 3.2

    Speech Services API version 3.2.  # noqa: E501

    OpenAPI spec version: 3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BaseModelProperties(object):
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
        'deprecation_dates': 'BaseModelDeprecationDates',
        'features': 'BaseModelFeatures',
        'charge_for_adaptation': 'bool'
    }

    attribute_map = {
        'deprecation_dates': 'deprecationDates',
        'features': 'features',
        'charge_for_adaptation': 'chargeForAdaptation'
    }

    def __init__(self, deprecation_dates=None, features=None, charge_for_adaptation=None, _configuration=None):  # noqa: E501
        """BaseModelProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deprecation_dates = None
        self._features = None
        self._charge_for_adaptation = None
        self.discriminator = None

        if deprecation_dates is not None:
            self.deprecation_dates = deprecation_dates
        if features is not None:
            self.features = features
        if charge_for_adaptation is not None:
            self.charge_for_adaptation = charge_for_adaptation

    @property
    def deprecation_dates(self):
        """Gets the deprecation_dates of this BaseModelProperties.  # noqa: E501


        :return: The deprecation_dates of this BaseModelProperties.  # noqa: E501
        :rtype: BaseModelDeprecationDates
        """
        return self._deprecation_dates

    @deprecation_dates.setter
    def deprecation_dates(self, deprecation_dates):
        """Sets the deprecation_dates of this BaseModelProperties.


        :param deprecation_dates: The deprecation_dates of this BaseModelProperties.  # noqa: E501
        :type: BaseModelDeprecationDates
        """

        self._deprecation_dates = deprecation_dates

    @property
    def features(self):
        """Gets the features of this BaseModelProperties.  # noqa: E501


        :return: The features of this BaseModelProperties.  # noqa: E501
        :rtype: BaseModelFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BaseModelProperties.


        :param features: The features of this BaseModelProperties.  # noqa: E501
        :type: BaseModelFeatures
        """

        self._features = features

    @property
    def charge_for_adaptation(self):
        """Gets the charge_for_adaptation of this BaseModelProperties.  # noqa: E501

        A value indicating whether model adaptation is charged.  # noqa: E501

        :return: The charge_for_adaptation of this BaseModelProperties.  # noqa: E501
        :rtype: bool
        """
        return self._charge_for_adaptation

    @charge_for_adaptation.setter
    def charge_for_adaptation(self, charge_for_adaptation):
        """Sets the charge_for_adaptation of this BaseModelProperties.

        A value indicating whether model adaptation is charged.  # noqa: E501

        :param charge_for_adaptation: The charge_for_adaptation of this BaseModelProperties.  # noqa: E501
        :type: bool
        """

        self._charge_for_adaptation = charge_for_adaptation

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
        if issubclass(BaseModelProperties, dict):
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
        if not isinstance(other, BaseModelProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseModelProperties):
            return True

        return self.to_dict() != other.to_dict()
