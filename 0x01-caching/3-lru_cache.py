#!/usr/bin/python3
"""A class LRUCache that inherits from Basiccaching and is
a caching system"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''A caching system that inherits from BaseCaching'''

    def __init__(self):
        '''Initializer'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assigns item value for the key to the dictionary self.cache_data'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

        self.cache_data[key] = item

    def get(self, key):
        '''Returns the linked key value in self.cache_data.'''
        if key is not None:
            if key in self.cache_data:
                value = self.cache_data.pop(key)
                self.cache_data[key] = value
                return value
        return None
