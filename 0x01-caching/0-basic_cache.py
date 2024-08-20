#!/usr/bin/python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching
    and provides basic put and get operations without any limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache with the provided key.

        Args:
            key (str): The key for the item to be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        Args:
            key (str): The key for the item to be retrieved.

        Returns:
            The value of the item linked to the key, or None if the key is not found.
        """
        return self.cache_data.get(key)

