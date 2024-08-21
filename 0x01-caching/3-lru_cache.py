#!/usr/bin/python3
"""
LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Inits the cache with the parent class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
            key
            item

        Returns:
            None
        """
        if key is not None and item is not None:
            # If key exists, move it to the end to show it was recently used
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the first item (least recently used)
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item.

        Args:
            key.

        Returns:
            Value.
        """
        if key is not None and key in self.cache_data:
            # Move key to the end to show it was recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

