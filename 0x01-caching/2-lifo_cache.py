#!/usr/bin/python3
"""A class LIFOCache that inherits from Basiccaching and is
a caching system"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''A caching system that inherits from BaseCaching'''

    def __init__(self):
        '''Initializer'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assigns item value for the key to the dictionary self.cache_data.'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        '''Returns the linked key value in self.cache_data.'''
        return self.cache_data.get(key, None)
