# coding: utf-8

"""
    Impower ERP

     # Setup  Enquire a `Bearer Token` from Api Support  # Authentication  Use API calls with an `Authorization: Bearer TOKEN` header  # Webhooks  The application supports sending secured notification events to registered endpoints.  The events one may receive are sent as  ``` POST https://your.webhook.url/path/somewhere Authorization: Bearer TOKEN  {   \"connectionId\": 0,   \"entityType\": \"properties|contacts|invoices|etc.\",   \"entityId\": 0,   \"eventType\": \"CREATE|UPDATE|DELETE\" } ```  <!-- Style overrides --> <style> code {   display: block; } </style>   # noqa: E501

    OpenAPI spec version: 2.201.52181d67
    Contact: support+api@impower.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PropertyDto(object):
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
        'created': 'datetime',
        'id': 'int',
        'name': 'str',
        'property_hr_id': 'str',
        'state': 'str',
        'type': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'name': 'name',
        'property_hr_id': 'propertyHrId',
        'state': 'state',
        'type': 'type',
        'updated': 'updated'
    }

    def __init__(self, created=None, id=None, name=None, property_hr_id=None, state=None, type=None, updated=None):  # noqa: E501
        """PropertyDto - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._id = None
        self._name = None
        self._property_hr_id = None
        self._state = None
        self._type = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if property_hr_id is not None:
            self.property_hr_id = property_hr_id
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this PropertyDto.  # noqa: E501

        Creation time of the property instance.  # noqa: E501

        :return: The created of this PropertyDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PropertyDto.

        Creation time of the property instance.  # noqa: E501

        :param created: The created of this PropertyDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this PropertyDto.  # noqa: E501

        ID of the property instance.  # noqa: E501

        :return: The id of this PropertyDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PropertyDto.

        ID of the property instance.  # noqa: E501

        :param id: The id of this PropertyDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PropertyDto.  # noqa: E501

        Name of the property instance.  # noqa: E501

        :return: The name of this PropertyDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyDto.

        Name of the property instance.  # noqa: E501

        :param name: The name of this PropertyDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def property_hr_id(self):
        """Gets the property_hr_id of this PropertyDto.  # noqa: E501

        Human readable id of the property instance.  # noqa: E501

        :return: The property_hr_id of this PropertyDto.  # noqa: E501
        :rtype: str
        """
        return self._property_hr_id

    @property_hr_id.setter
    def property_hr_id(self, property_hr_id):
        """Sets the property_hr_id of this PropertyDto.

        Human readable id of the property instance.  # noqa: E501

        :param property_hr_id: The property_hr_id of this PropertyDto.  # noqa: E501
        :type: str
        """

        self._property_hr_id = property_hr_id

    @property
    def state(self):
        """Gets the state of this PropertyDto.  # noqa: E501

        Current state of the property.  1. DRAFT - property not activated yet, therefore no bookings/bank orders/reports can be generated.  2. READY - property has been activated and can be used for bookings/bank orders/reports generation.  3. DISABLED - property has been deactivated, and can no longer generate bookings/bank orders/reports.   # noqa: E501

        :return: The state of this PropertyDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PropertyDto.

        Current state of the property.  1. DRAFT - property not activated yet, therefore no bookings/bank orders/reports can be generated.  2. READY - property has been activated and can be used for bookings/bank orders/reports generation.  3. DISABLED - property has been deactivated, and can no longer generate bookings/bank orders/reports.   # noqa: E501

        :param state: The state of this PropertyDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "READY", "DISABLED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def type(self):
        """Gets the type of this PropertyDto.  # noqa: E501

        Administration type of the property. OWNER - Home Owner Association. RENTAL - Tenant Management.  # noqa: E501

        :return: The type of this PropertyDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyDto.

        Administration type of the property. OWNER - Home Owner Association. RENTAL - Tenant Management.  # noqa: E501

        :param type: The type of this PropertyDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "RENTAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this PropertyDto.  # noqa: E501

        Update time of the property instance.  # noqa: E501

        :return: The updated of this PropertyDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PropertyDto.

        Update time of the property instance.  # noqa: E501

        :param updated: The updated of this PropertyDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if issubclass(PropertyDto, dict):
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
        if not isinstance(other, PropertyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
