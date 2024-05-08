#!/usr/bin/env python3
"""A class LFUCache that inherits from BaseCaching module and is
a caching system
"""

from base_caching import BaseCaching
from collections import defaultdict
from datetime import datetime


class LFUCache(BaseCaching):
    """LFU caching algorithm implementation."""
    def __init__(self):
        """Initializer."""
        super().__init__()
        self.frequency = defaultdict(int)  # Dictionary store for frequent key
        self.last_used = {}  # Dictionary store for last used time of each key

    def put(self, key, item):
        """
        Put an item into the cache.

        Args:
            key: Key of the item to be cached.
            item: Item to be cached.

        Returns:
            None
        """
        if key is None or item is None:
            return

        # Discard least frequently used item if cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = min(self.frequency, key=lambda k:
                              (self.frequency[k], self.last_used[k]))
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            del self.last_used[discard_key]
            print("DISCARD:", discard_key)

        # Add item to cache and update frequency and last used time
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.last_used[key] = datetime.now()

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key: Key of the item to retrieve.

        Returns:
            Item corresponding to the key if present in the cache, else None
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and last used time of the key
        self.frequency[key] += 1
        self.last_used[key] = datetime.now()
        return self.cache_data[key]
