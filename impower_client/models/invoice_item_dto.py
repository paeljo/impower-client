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

class InvoiceItemDto(object):
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
        'account_code': 'str',
        'account_id': 'int',
        'account_name': 'str',
        'amount': 'float',
        'booking_text': 'str',
        'created': 'datetime',
        'id': 'int',
        'labor_cost_amount': 'float',
        'labor_cost_type': 'str',
        'updated': 'datetime',
        'vat_amount': 'float',
        'vat_percentage': 'float'
    }

    attribute_map = {
        'account_code': 'accountCode',
        'account_id': 'accountId',
        'account_name': 'accountName',
        'amount': 'amount',
        'booking_text': 'bookingText',
        'created': 'created',
        'id': 'id',
        'labor_cost_amount': 'laborCostAmount',
        'labor_cost_type': 'laborCostType',
        'updated': 'updated',
        'vat_amount': 'vatAmount',
        'vat_percentage': 'vatPercentage'
    }

    def __init__(self, account_code=None, account_id=None, account_name=None, amount=None, booking_text=None, created=None, id=None, labor_cost_amount=None, labor_cost_type=None, updated=None, vat_amount=None, vat_percentage=None):  # noqa: E501
        """InvoiceItemDto - a model defined in Swagger"""  # noqa: E501
        self._account_code = None
        self._account_id = None
        self._account_name = None
        self._amount = None
        self._booking_text = None
        self._created = None
        self._id = None
        self._labor_cost_amount = None
        self._labor_cost_type = None
        self._updated = None
        self._vat_amount = None
        self._vat_percentage = None
        self.discriminator = None
        if account_code is not None:
            self.account_code = account_code
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if amount is not None:
            self.amount = amount
        if booking_text is not None:
            self.booking_text = booking_text
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if labor_cost_amount is not None:
            self.labor_cost_amount = labor_cost_amount
        if labor_cost_type is not None:
            self.labor_cost_type = labor_cost_type
        if updated is not None:
            self.updated = updated
        if vat_amount is not None:
            self.vat_amount = vat_amount
        if vat_percentage is not None:
            self.vat_percentage = vat_percentage

    @property
    def account_code(self):
        """Gets the account_code of this InvoiceItemDto.  # noqa: E501

        Account code of the booking item.  # noqa: E501

        :return: The account_code of this InvoiceItemDto.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this InvoiceItemDto.

        Account code of the booking item.  # noqa: E501

        :param account_code: The account_code of this InvoiceItemDto.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def account_id(self):
        """Gets the account_id of this InvoiceItemDto.  # noqa: E501

        Account id of the booking item.  # noqa: E501

        :return: The account_id of this InvoiceItemDto.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvoiceItemDto.

        Account id of the booking item.  # noqa: E501

        :param account_id: The account_id of this InvoiceItemDto.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this InvoiceItemDto.  # noqa: E501

        Account name of the booking item.  # noqa: E501

        :return: The account_name of this InvoiceItemDto.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this InvoiceItemDto.

        Account name of the booking item.  # noqa: E501

        :param account_name: The account_name of this InvoiceItemDto.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def amount(self):
        """Gets the amount of this InvoiceItemDto.  # noqa: E501

        Amount corresponding to the booking item.  # noqa: E501

        :return: The amount of this InvoiceItemDto.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceItemDto.

        Amount corresponding to the booking item.  # noqa: E501

        :param amount: The amount of this InvoiceItemDto.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def booking_text(self):
        """Gets the booking_text of this InvoiceItemDto.  # noqa: E501

        Booking text of the booking item.  # noqa: E501

        :return: The booking_text of this InvoiceItemDto.  # noqa: E501
        :rtype: str
        """
        return self._booking_text

    @booking_text.setter
    def booking_text(self, booking_text):
        """Sets the booking_text of this InvoiceItemDto.

        Booking text of the booking item.  # noqa: E501

        :param booking_text: The booking_text of this InvoiceItemDto.  # noqa: E501
        :type: str
        """

        self._booking_text = booking_text

    @property
    def created(self):
        """Gets the created of this InvoiceItemDto.  # noqa: E501

        Creation time of the invoice item.  # noqa: E501

        :return: The created of this InvoiceItemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InvoiceItemDto.

        Creation time of the invoice item.  # noqa: E501

        :param created: The created of this InvoiceItemDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this InvoiceItemDto.  # noqa: E501

        Unique identifier of the booking item.  # noqa: E501

        :return: The id of this InvoiceItemDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceItemDto.

        Unique identifier of the booking item.  # noqa: E501

        :param id: The id of this InvoiceItemDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labor_cost_amount(self):
        """Gets the labor_cost_amount of this InvoiceItemDto.  # noqa: E501

        Amount relevant for income tax declaration according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html).  # noqa: E501

        :return: The labor_cost_amount of this InvoiceItemDto.  # noqa: E501
        :rtype: float
        """
        return self._labor_cost_amount

    @labor_cost_amount.setter
    def labor_cost_amount(self, labor_cost_amount):
        """Sets the labor_cost_amount of this InvoiceItemDto.

        Amount relevant for income tax declaration according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html).  # noqa: E501

        :param labor_cost_amount: The labor_cost_amount of this InvoiceItemDto.  # noqa: E501
        :type: float
        """

        self._labor_cost_amount = labor_cost_amount

    @property
    def labor_cost_type(self):
        """Gets the labor_cost_type of this InvoiceItemDto.  # noqa: E501

        Depending on the selected type: percentages of the amounts will be reported on the 35a annexes of multiple reports according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html).   Ex: Housemoney Settlement (Hausgeldabrechnung) or Opscost Report (Nebenkostenabrechnung).   1. HOUSEHOLD_RELATED_SERVICES - haushaltsnahe Dienstleistungen  2. TECHNICIAN_SERVICE - haushaltsnahe Handwerkerleistungen  3. MARGINAL_EMPLOYMENT - haushaltsnahe geringfügige Beschäftigungsverhältnisse  4. INSURABLE_EMPLOYMENT - sozialversicherungspflichtigen haushaltsnahen Beschäftigungsverhältnissen  # noqa: E501

        :return: The labor_cost_type of this InvoiceItemDto.  # noqa: E501
        :rtype: str
        """
        return self._labor_cost_type

    @labor_cost_type.setter
    def labor_cost_type(self, labor_cost_type):
        """Sets the labor_cost_type of this InvoiceItemDto.

        Depending on the selected type: percentages of the amounts will be reported on the 35a annexes of multiple reports according to the Income Tax Act: [Einkommenstueregesetz EStG 35a](https://www.gesetze-im-internet.de/estg/__35a.html).   Ex: Housemoney Settlement (Hausgeldabrechnung) or Opscost Report (Nebenkostenabrechnung).   1. HOUSEHOLD_RELATED_SERVICES - haushaltsnahe Dienstleistungen  2. TECHNICIAN_SERVICE - haushaltsnahe Handwerkerleistungen  3. MARGINAL_EMPLOYMENT - haushaltsnahe geringfügige Beschäftigungsverhältnisse  4. INSURABLE_EMPLOYMENT - sozialversicherungspflichtigen haushaltsnahen Beschäftigungsverhältnissen  # noqa: E501

        :param labor_cost_type: The labor_cost_type of this InvoiceItemDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOUSEHOLD_RELATED_SERVICES", "TECHNICIAN_SERVICE", "MARGINAL_EMPLOYMENT", "INSURABLE_EMPLOYMENT"]  # noqa: E501
        if labor_cost_type not in allowed_values:
            raise ValueError(
                "Invalid value for `labor_cost_type` ({0}), must be one of {1}"  # noqa: E501
                .format(labor_cost_type, allowed_values)
            )

        self._labor_cost_type = labor_cost_type

    @property
    def updated(self):
        """Gets the updated of this InvoiceItemDto.  # noqa: E501

        Last update time of the invoice item.  # noqa: E501

        :return: The updated of this InvoiceItemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this InvoiceItemDto.

        Last update time of the invoice item.  # noqa: E501

        :param updated: The updated of this InvoiceItemDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def vat_amount(self):
        """Gets the vat_amount of this InvoiceItemDto.  # noqa: E501

        Corresponding vat amount of the booking item.  # noqa: E501

        :return: The vat_amount of this InvoiceItemDto.  # noqa: E501
        :rtype: float
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this InvoiceItemDto.

        Corresponding vat amount of the booking item.  # noqa: E501

        :param vat_amount: The vat_amount of this InvoiceItemDto.  # noqa: E501
        :type: float
        """

        self._vat_amount = vat_amount

    @property
    def vat_percentage(self):
        """Gets the vat_percentage of this InvoiceItemDto.  # noqa: E501

        Corresponding vat percentage of the vat amount of the total amount.  # noqa: E501

        :return: The vat_percentage of this InvoiceItemDto.  # noqa: E501
        :rtype: float
        """
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, vat_percentage):
        """Sets the vat_percentage of this InvoiceItemDto.

        Corresponding vat percentage of the vat amount of the total amount.  # noqa: E501

        :param vat_percentage: The vat_percentage of this InvoiceItemDto.  # noqa: E501
        :type: float
        """

        self._vat_percentage = vat_percentage

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
        if issubclass(InvoiceItemDto, dict):
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
        if not isinstance(other, InvoiceItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
