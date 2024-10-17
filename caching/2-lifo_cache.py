#!/usr/bin/env python3
'''
Create a class LIFOCache that inherits from BaseCaching
and is a caching system
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache class implements a LIFO caching system where the most
    recently added item is discarded if the cache exceeds its size limit.
    '''

    def __init__(self):
        '''
        Initialize the cache and call the parent class initializer.
        '''
        super().__init__()
        self.last_key = None  # Keep track of the last inserted key

    def put(self, key: str, item: any) -> None:
        '''
        Add the item to the cache using the given key.
        If the cache exceeds the MAX_ITEMS limit,
        discard the last item added.
        '''
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # LIFO: Remove the last inserted item when the cache is full
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]
            
            # Insert or update the item in the cache
            self.cache_data[key] = item
            self.last_key = key  # Update the last inserted key

    def get(self, key: str) -> any:
        '''
        Retrieve the value from the cache for the given key.
        '''
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
