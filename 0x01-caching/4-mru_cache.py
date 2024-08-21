#!/usr/bin/env python3
"""
MRUCache module that implements an MRU caching system.
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCaching and provides a basic cache
    mechanism where items are added with MRU replacement policy.
    """

    def __init__(self):
        """Initialises LIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache with a specific key.
        Removes the most recently used item put in cache (MRU algorithm)

        Args:
            key (str): The key to store the item under.
            item (Any): The item to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                discarded_mru_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {discarded_mru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache by its key.

        Args:
            key (str): The key to retrieve the item by.

        Returns:
            Any: The item stored in the cache, or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
