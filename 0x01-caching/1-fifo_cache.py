#!/usr/bin/python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching
    system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Inits the cache with the parent class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key
            item
        Returns:
            None
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        Returns:
            Value or None
        """
        return self.cache_data.get(key)

