#!/usr/bin/python3
"""A class BasicCache that inherits from Basiccaching and is
a caching system"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system without limit"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
