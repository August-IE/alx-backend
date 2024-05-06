#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Optional, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Returns hyperlinked page information."""
        indexed_data = self.indexed_dataset()
        total_rows = len(indexed_data)

        assert index is None or (isinstance(index, int)
                                 and 0 <= index < total_rows)

        if index is None:
            index = 0

        # Adjust index if rows are deleted
        while index not in indexed_data:
            index += 1

        next_index = min(index + page_size, total_rows)
        page_data = [indexed_data[i] for i in range(index, next_index)]

        return {
            "index": index,
            "next_index": next_index if next_index < total_rows else None,
            "page_size": len(page_data),
            "data": page_data
        }
