#!/usr/bin/env python3
"""
Module that creates a simple function that paginates based on
current page and page size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    A simple function that paginates based on current page and page size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
