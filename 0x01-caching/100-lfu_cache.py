#!/usr/bin/python3
"""
LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """
    It uses the Least Frequently Used (LFU) algorithm to manage the cache.
    """

    def __init__(self):
        """
        Inits the cache with the parent class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_freq = defaultdict(int)

    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
            key
            item

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.usage_freq.values())
                least_used = [k for k, v in self.usage_freq.items() if v == min_freq]

                if len(least_used) > 1:
                    for k in self.cache_data:
                        if k in least_used:
                            discarded_key = k
                            break
                else:
                    discarded_key = least_used[0]

                del self.cache_data[discarded_key]
                del self.usage_freq[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.usage_freq[key] = 1

        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieves an item from the cache

        Args:
            key

        Returns:
            Value of the item linked to the key
        """
        if key is not None and key in self.cache_data:
            # Increment the frequency since it was accessed
            self.usage_freq[key] += 1
            # Move the key to the end to maintain LRU order
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

