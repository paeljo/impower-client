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

class UnitDto(object):
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
        'floor': 'str',
        'id': 'int',
        'position': 'str',
        'property_id': 'int',
        'type': 'str',
        'unit_hr_id': 'str',
        'unit_rank': 'int',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'floor': 'floor',
        'id': 'id',
        'position': 'position',
        'property_id': 'propertyId',
        'type': 'type',
        'unit_hr_id': 'unitHrId',
        'unit_rank': 'unitRank',
        'updated': 'updated'
    }

    def __init__(self, created=None, floor=None, id=None, position=None, property_id=None, type=None, unit_hr_id=None, unit_rank=None, updated=None):  # noqa: E501
        """UnitDto - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._floor = None
        self._id = None
        self._position = None
        self._property_id = None
        self._type = None
        self._unit_hr_id = None
        self._unit_rank = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if floor is not None:
            self.floor = floor
        if id is not None:
            self.id = id
        if position is not None:
            self.position = position
        if property_id is not None:
            self.property_id = property_id
        if type is not None:
            self.type = type
        if unit_hr_id is not None:
            self.unit_hr_id = unit_hr_id
        if unit_rank is not None:
            self.unit_rank = unit_rank
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this UnitDto.  # noqa: E501

        Creation time of the unit instance.  # noqa: E501

        :return: The created of this UnitDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UnitDto.

        Creation time of the unit instance.  # noqa: E501

        :param created: The created of this UnitDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def floor(self):
        """Gets the floor of this UnitDto.  # noqa: E501

        Floor the unit is located on.  # noqa: E501

        :return: The floor of this UnitDto.  # noqa: E501
        :rtype: str
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        """Sets the floor of this UnitDto.

        Floor the unit is located on.  # noqa: E501

        :param floor: The floor of this UnitDto.  # noqa: E501
        :type: str
        """

        self._floor = floor

    @property
    def id(self):
        """Gets the id of this UnitDto.  # noqa: E501

        ID of the unit instance.  # noqa: E501

        :return: The id of this UnitDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnitDto.

        ID of the unit instance.  # noqa: E501

        :param id: The id of this UnitDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def position(self):
        """Gets the position of this UnitDto.  # noqa: E501

        Position of the unit within the floor.  # noqa: E501

        :return: The position of this UnitDto.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UnitDto.

        Position of the unit within the floor.  # noqa: E501

        :param position: The position of this UnitDto.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def property_id(self):
        """Gets the property_id of this UnitDto.  # noqa: E501

        ID of the property instance the unit belongs to.  # noqa: E501

        :return: The property_id of this UnitDto.  # noqa: E501
        :rtype: int
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this UnitDto.

        ID of the property instance the unit belongs to.  # noqa: E501

        :param property_id: The property_id of this UnitDto.  # noqa: E501
        :type: int
        """

        self._property_id = property_id

    @property
    def type(self):
        """Gets the type of this UnitDto.  # noqa: E501

        Purpose the unit is used for.APARTMENT - unit used for residential purposes. PARKING - unit used for parking purposes. COMMERCIAL - unit used for business/commercial purposes. OTHER - unit used for other purposes.  # noqa: E501

        :return: The type of this UnitDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnitDto.

        Purpose the unit is used for.APARTMENT - unit used for residential purposes. PARKING - unit used for parking purposes. COMMERCIAL - unit used for business/commercial purposes. OTHER - unit used for other purposes.  # noqa: E501

        :param type: The type of this UnitDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["APARTMENT", "PARKING", "OTHER", "COMMERCIAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unit_hr_id(self):
        """Gets the unit_hr_id of this UnitDto.  # noqa: E501

        Human readable id of the unit instance.  # noqa: E501

        :return: The unit_hr_id of this UnitDto.  # noqa: E501
        :rtype: str
        """
        return self._unit_hr_id

    @unit_hr_id.setter
    def unit_hr_id(self, unit_hr_id):
        """Sets the unit_hr_id of this UnitDto.

        Human readable id of the unit instance.  # noqa: E501

        :param unit_hr_id: The unit_hr_id of this UnitDto.  # noqa: E501
        :type: str
        """

        self._unit_hr_id = unit_hr_id

    @property
    def unit_rank(self):
        """Gets the unit_rank of this UnitDto.  # noqa: E501

        The rank defines the order how units are displayed on the UI / Reports. The user may update it in the UI.  # noqa: E501

        :return: The unit_rank of this UnitDto.  # noqa: E501
        :rtype: int
        """
        return self._unit_rank

    @unit_rank.setter
    def unit_rank(self, unit_rank):
        """Sets the unit_rank of this UnitDto.

        The rank defines the order how units are displayed on the UI / Reports. The user may update it in the UI.  # noqa: E501

        :param unit_rank: The unit_rank of this UnitDto.  # noqa: E501
        :type: int
        """

        self._unit_rank = unit_rank

    @property
    def updated(self):
        """Gets the updated of this UnitDto.  # noqa: E501

        Update time of the unit instance.  # noqa: E501

        :return: The updated of this UnitDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UnitDto.

        Update time of the unit instance.  # noqa: E501

        :param updated: The updated of this UnitDto.  # noqa: E501
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
        if issubclass(UnitDto, dict):
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
        if not isinstance(other, UnitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
