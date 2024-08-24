#!/usr/bin/env python3
"""Module parameterizes a unit test"""

from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """Class parameterizes a unit test"""

    @parameterized.expand([
        ({"a": 1}, 'a', 1),
        ({"a": {"b": 2}}, 'a', {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Method parameterizes a unit test"""
        self.assertEqual(access_nested_map(nested_map, path), result)
