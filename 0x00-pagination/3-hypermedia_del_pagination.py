#!/usr/bin/env python3
"""
Hypermedia pagination module with deletion capabilities.
"""

import csv
from typing import List, Dict


class Server:
    """
    PaginateS a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Handles cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at posn 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary.

        Args:
            index (int): The start index of the page.
            page_size (int): The number of items to display per page.

        Returns:
            Dict: A dictionary containing the current index, next index,
                  page size, and the data.
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset())

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        next_index = index

        while len(data) < page_size and next_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }

