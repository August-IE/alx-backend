#!/usr/bin/env python3
"""Implementing a method named get_page that takes two integers page with
default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple, Optional, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


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
        """Retrieves a page of data."""
        assert isinstance(page, int) and isinstance(page_size, int)
        "Verifies both arguments are integers."
        assert page > 0 and page_size > 0
        "Verifies both arguments are greater than 0."
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Returns hyperlinked page information."""
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
