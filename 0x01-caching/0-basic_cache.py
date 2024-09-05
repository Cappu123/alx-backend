#!/usr/bin/env python3
"""
The CaseCaching class imported"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """representation of an object to store and 
    retrieve items from a dictionary """

    def put(self, key, item):
        """adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
