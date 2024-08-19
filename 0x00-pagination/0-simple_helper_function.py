#!/usr/bin/env python3
"""
Module of a simple helper function for pagination.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end
    indices for items on a specific page.

    Args:
        page (int)
        page_size (int)

    Returns:
        Tuple[int,int]
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end

