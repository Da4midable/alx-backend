#!/usr/bin/env python3


import csv
import math
from typing import List, Tuple
index_range = __import__('0-simple_helper_function').index_range


def index_range(page: int, page_size: int) -> Tuple:
    """
    A simple function that paginates based on current page and page size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """function returns appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "Page and page_size must be greater than 0."

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(data):
            return []
        return data[start_index:end_index]
