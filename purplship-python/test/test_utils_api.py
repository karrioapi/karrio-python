# coding: utf-8

"""
    PurplShip Multi-carrier API

    PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@purplship.com
    Generated by: https://github.com/purplship-api/purplship-codegen.git
"""


from __future__ import absolute_import

import unittest

import purplship
from purplship.api.utils import Utils  # noqa: E501
from purplship.rest import ApiException


class TestUtils(unittest.TestCase):
    """Utils unit test stubs"""

    def setUp(self):
        self.api = purplship.api.utils.Utils()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_reference(self):
        """Test case for get_reference

        """
        pass

    def test_print_label(self):
        """Test case for print_label

        """
        pass


if __name__ == '__main__':
    unittest.main()
