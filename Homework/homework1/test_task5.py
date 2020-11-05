from typing import List

import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, 2, -4, 5, 6, -9, 0], 1, 6),
        ([-1, 2, -4, 5, 6, -9, 0], 2, 11),
        ([-1, 2, -4, 5, 6, -9, 0], 3, 11),
        ([-1, 2, -4, 5, 6, -9, 0], 4, 11),
        ([-1, 2, -4, 5, 6, -9, 0], 5, 11),
        ([-1, 2, -4, 5, 6, -9, 0], 6, 11),
        ([-1, 2, -4, 5, 6, -9, 0], 7, 11),
        ([4, -4, 5, -4, 3, 2, 1], 1, 5),
        ([4, -4, 5, -4, 3, 2, 1], 2, 5),
        ([4, -4, 5, -4, 3, 2, 1], 3, 6),
        ([4, -4, 5, -4, 3, 2, 1], 4, 6),
        ([4, -4, 5, -4, 3, 2, 1], 5, 7),
        ([4, -4, 5, -4, 3, 2, 1], 6, 7),
        ([4, -4, 5, -4, 3, 2, 1], 7, 7),
        ([5], 1, 5),
        ([], 0, 404),
        ([1, 2], 5, 404),
        ([1, 2, 3], 0, 404),
        ([1, 1, 1, 1, 1, 1, 1], 5, 5),
        ([-1, -1, -1, -1, -1, -1, -1], 5, -1),
        ([0, 0, 0, 0, 0, 0, 1], 7, 1),
        ([-1, 0, 0, 0, 0, 0, 0], 7, 0),
        ([1, 0, 0, 0, 0, 0, 1], 7, 2),
        ([1, 0, 0, 0, 0, 0, 1], 4, 1),
    ],
)
def test_find_maximal_subarray_sum(
    value1: List[int], value2: int, expected_result: int
):
    actual_result = find_maximal_subarray_sum(value1, value2)

    assert actual_result == expected_result
