#!/usr/bin/env python3
'''
Create a class MRUCache that inherits from BaseCaching
and is a caching system
'''

from base_caching import BaseCaching
from collections import OrderedDict


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
        Use OrderedDict to maintain insertion order and allow MRU tracking.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: any) -> None:
        '''
        Add the item to the cache using the given key.
        If the cache exceeds the MAX_ITEMS limit,
        discard the most recently used item.
        '''
        if key is None or item is None:
            return

        # If key already exists, update its value and move it to the end (most recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        # Add the item to the cache
        self.cache_data[key] = item

        # If cache exceeds max limit, remove the MRU item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last used item (the MRU one)
            discarded_key, _ = self.cache_data.popitem(last=False)  # Remove the first inserted item
            print(f"DISCARD: {discarded_key}")

    def get(self, key: str) -> any:
        '''
        Retrieve the value from the cache for the given key.
        Move the key to the end to mark it as most recently used.
        '''
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
