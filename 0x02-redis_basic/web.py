#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
import time
from functools import wraps

def count_and_cache_calls(fn):
    @wraps(fn)
    def wrapper(url):
        # Create a Redis client
        r = redis.Redis(host='localhost', port=6379, db=0)

        # Increment the count of the URL accessed
        count_key = f"count:{url}"
        r.incr(count_key)

        # Get the cached HTML content if available
        cached_content = r.get(url)
        if cached_content:
            return cached_content.decode('utf-8')

        # Call the original function
        content = fn(url)

        # Cache the HTML content with a 10-second expiration time
        r.setex(url, 10, content)
        return content

    return wrapper

@count_and_cache_calls
def get_page(url: str) -> str:
    # Fetch the HTML content using requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    return ""  # Return an empty string if the request fails or the URL is not accessible
