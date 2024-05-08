#!/usr/bin/env python3
"""A class LFUCache that inherits from BaseCaching module and is
a caching system
"""

from base_caching import BaseCaching
from collections import defaultdict
from datetime import datetime


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)
        self.last_used = {}

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = min(self.frequency, key=lambda k:
                              (self.frequency[k], self.last_used[k]))
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            del self.last_used[discard_key]
            print("DISCARD:", discard_key)
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.last_used[key] = datetime.now()

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.last_used[key] = datetime.now()
        return self.cache_data[key]
