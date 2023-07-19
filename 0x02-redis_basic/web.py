#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps


def count_and_cache_calls(fn):
    """
    Decorator to track the number of times a URL is 
    accessed and cache the result.

    Args:
        fn (Callable): The function to be wrapped.

    Returns:
        Callable: The wrapped function.
    """
    @wraps(fn)
    def wrapper(url):
        """
        Wrapped function that tracks the URL access
        count and caches the result.

        Args:
            url (str): The URL to fetch the HTML content.

        Returns:
            str: The HTML content of the URL.
        """
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
    """
    Fetches the HTML content of the specified URL.

    Args:
        url (str): The URL to fetch the HTML content.

    Returns:
        str: The HTML content of the URL.
    """
    # Fetch the HTML content using requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    return ""  
