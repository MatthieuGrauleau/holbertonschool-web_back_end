#!/usr/bin/env python3
"""The function should return a tuple of size two containing
a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.

    :param page: The current page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple (start index, end index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
