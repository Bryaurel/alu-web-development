#!/usr/bin/env python3
'''
Create a class BasicCache that inherits from BaseCaching
and implements a basic caching system with no limit.
'''

from base_caching import BaseCaching

class BaseCaching(BaseCaching):
    '''
    This caching system doesn't have limit
    '''


    def put(self, key: str, item: any) -> None:
        '''
        Add the item to the cache using the given key.
        
        Args:
        key (str): The key for the item.
        item (any): The item to be cached.

        If either key or item is None, do nothing.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item  # Assign the item value to the dictionnary key
        else:
            return  # Do nothing if key or item is None

    def get(self, key: str) -> any:
        '''
        Retrieve the value from the cache for the given key.
        
        Args:
        key (str): The key to look up in the cache.

        Returns:
        The value associated with the key, or None if the key is None or not in the cache.
        '''
        if key is None or key not in self.cache:
            return None  # Return None if key is None or doesn't exist in cache

        return self.cache_data.get(key)  # Return the cached item for the key
