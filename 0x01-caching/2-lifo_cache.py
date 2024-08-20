#!/usr/bin/python3
"""
LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching
    system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Inits the cache.
        """
        super().__init__()
        self.last_key = None

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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.last_key = key

    def get(self, key):
        """
        Retrieves an item.

        Args:
            key

        Returns:
            Value linked to a key or None.
        """
        return self.cache_data.get(key)

