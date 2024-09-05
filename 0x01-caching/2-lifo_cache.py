#!/usr/bin/env python3
"""
importing parent class or caching module"""
from base_caching import BaseCaching
from collections import OrderedDict

class LIFOCache(BaseCaching):
    """Represents an object that allows storing andd
    retrieving items from a dictioary with a LIFO
    removal mechanism when the limit is reached
    """

    def __init__(self):
        """intitialization of the cache"""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns a value to a key
        pops last item if item > max possible 
        number of item in the parent class"""

        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key,_ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key
        """
        return self.cache_data.get(key, None)
