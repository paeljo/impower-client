# coding: utf-8

"""
    Impower ERP

     # Setup  Enquire a `Bearer Token` from Api Support  # Authentication  Use API calls with an `Authorization: Bearer TOKEN` header  # Webhooks  The application supports sending secured notification events to registered endpoints.  The events one may receive are sent as  ``` POST https://your.webhook.url/path/somewhere Authorization: Bearer TOKEN  {   \"connectionId\": 0,   \"entityType\": \"properties|contacts|invoices|etc.\",   \"entityId\": 0,   \"eventType\": \"CREATE|UPDATE|DELETE\" } ```  <!-- Style overrides --> <style> code {   display: block; } </style>   # noqa: E501

    OpenAPI spec version: 2.201.52181d67
    Contact: support+api@impower.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import impower_client
from impower_client.models.contact_dto import ContactDto  # noqa: E501
from impower_client.rest import ApiException


class TestContactDto(unittest.TestCase):
    """ContactDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContactDto(self):
        """Test ContactDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = impower_client.models.contact_dto.ContactDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
