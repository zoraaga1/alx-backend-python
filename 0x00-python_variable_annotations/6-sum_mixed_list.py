#!/usr/bin/env python3
"""
script that returns the sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union [int, float]]) -> float:
  """
  returns the sum of a list of floats and integers
  """
  return sum(mxd_lst)
