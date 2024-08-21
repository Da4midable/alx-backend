#!/usr/bin/python3
"""
LIFOCache module that implements a LIFO caching system.
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class inherits from BaseCaching and provides a basic cache
    mechanism where items are added with LIFO replacement policy.
    """

    def __init__(self):
        """Initialises LIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache with a specific key.
        Removes first item put in cache (LIFO algorithm)

        Args:
            key (str): The key to store the item under.
            item (Any): The item to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

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
