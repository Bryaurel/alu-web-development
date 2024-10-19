#!/usr/bin/env python3
'''
Create a class MRUCache that inherits from BaseCaching
and is a caching system
'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache class implements an MRU caching system.
    If the number of items in cache exceeds the limit,
    it discards the most recently used item.
    MRU: Most Recently Used
    '''
    def __init__(self):
        '''
        Initialize the cache and call the parent class initializer.
        '''
        super().__init__()
        self.usage_order = []  # List to track access order

    def put(self, key, item):
        '''
        Add the item to the cache using the given key.
        If the cache exceeds the MAX_ITEMS limit,
        discard the most recently used item.
        '''
        if key is None or item is None:
            return

        # If key already exists, update its value and mark it as mru
        if key in self.cache_data:
            self.usage_order.remove(key)

        # Add the item to the cache
        self.cache_data[key] = item
        self.usage_order.append(key)

        # If cache exceeds max limit, remove the MRU item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last accessed (most recently used) item
            mru_key = self.usage_order.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        '''
        Retrieve the value from the cache for the given key.
        Mark the key as most recently used.
        '''
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as most recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
