#!/usr/bin/python3
"""
BasicCache module that implements a basic caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching and provides a basic cache
    mechanism where items are added without any limit or eviction policy.
    """

    def __init__(self):
        """
        Initialize the BasicCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache with a specific key.

        Args:
            key (str): The key to store the item under.
            item (Any): The item to store in the cache.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        Args:
            key (str): The key to retrieve the item by.

        Returns:
            Any: The item stored in the cache, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
