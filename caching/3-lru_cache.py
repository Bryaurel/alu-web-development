#!/usr/bin/env python3
'''
Create a class LRUCache that inherits from BaseCaching
and is a caching system
'''

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''
    LRUCache class implements an LRU caching system.
    If the number of items in cache exceeds the limit,
    it discards the least recently used item.
    LRU: Least Recently Used
    '''
    def __init__(self):
        '''
        Initialize the cache and call the parent class initializer.
        Use OrderedDict to maintain insertion order and allow LRU tracking.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put (self, key: str, item: any) -> None:
        '''
        Add the item to the cache using the given key.
        If the cache exceeds the MAX_ITEMS limit,
        discard the least recently used item.
        '''
        if key is None or item is None:
            return
        '''
        If key already exists, update its value
        and move it to the end (most recently used)
        '''
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        
        # Add the item to the cache
        self.cache_data[key] = item

        # If cache exceeds max limit, remove the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first inserted item (the least recently used one)
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key: str) -> any:
        '''
        Retrieve the value from the cache for the given key.
        Move the key to the end to mark it as recently used.
        '''
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
