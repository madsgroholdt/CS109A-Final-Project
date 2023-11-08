# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.base_stream import BaseStream  # noqa: F401,E501

class AltitudeStream(BaseStream):
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
        'data': 'list[float]'
    }
    if hasattr(BaseStream, "swagger_types"):
        swagger_types.update(BaseStream.swagger_types)

    attribute_map = {
        'data': 'data'
    }
    if hasattr(BaseStream, "attribute_map"):
        attribute_map.update(BaseStream.attribute_map)

    def __init__(self, data=None, *args, **kwargs):  # noqa: E501
        """AltitudeStream - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        if data is not None:
            self.data = data
        BaseStream.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this AltitudeStream.  # noqa: E501

        The sequence of altitude values for this stream, in meters  # noqa: E501

        :return: The data of this AltitudeStream.  # noqa: E501
        :rtype: list[float]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AltitudeStream.

        The sequence of altitude values for this stream, in meters  # noqa: E501

        :param data: The data of this AltitudeStream.  # noqa: E501
        :type: list[float]
        """

        self._data = data

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
        if issubclass(AltitudeStream, dict):
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
        if not isinstance(other, AltitudeStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
