#!/usr/bin/env python3
'''
Create a class FIFOCache that inherits from BaseCaching
and is a caching system
'''

from base_caching import BaseCaching



class FIFOCache(BaseCaching):
    '''
    FIFOCache class implements a FIFO caching system where the oldest
    added item is discarded if the cache exceeds its size limit.
    '''

    def __init__(self):
        '''
        Initialize the cache and call the parent class initializer
        '''
        super().__init__()

        # List to maintain the order of inserted keys
        self.order = []

    def put(self, key: str, item: any) -> None:
        '''
        Add the item to the cache using the given key.
        If the cache exceeds the MAX_ITEMS limit, discard the oldest item.
        '''
        if key is not None and item is not None:
            # If the key exists, we update the value but not the order
            if key not in self.cache_data:
                self.order.append(key)  # Keep track of the order

            self.cache_data[key] = item  # Insert or update the item in cache
            
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO: Remove the first inserted item
                first_key = self.order.pop(0)  # Get and remove the first key
                del self.cache_data[first_key]  # Remove from cache_data
                print(f"DISCARD: {first_key}")  # Print the discarded key

    def get(self, key: str) -> any:
        '''
        Retrieve the value from the cache for the given key.
        '''
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)  # Return the cached item for the key
        