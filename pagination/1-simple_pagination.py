#!/usr/bin/env python3
"""The function should return a tuple of size two containing
a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters."""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (list of rows) corresponding to the given
        page number and page size.

        :param page: The current page number (1-indexed)
        :param page_size: The number of items per page
        :return: A list of lists containing the data for the requested page.
        """
        "page must be a positive integer"
        assert isinstance(page, int) and page > 0
        "page_size must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
