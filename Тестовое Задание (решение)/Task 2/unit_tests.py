import pytest

from aqa_task.numerology import number_analysis


def test_basic():
  test_input = [1, 2, 3, 4, 5]
  test1_result = number_analysis(*test_input)

  assert test1_result.min == 1
  assert test1_result.max == 5
  assert test1_result.avg == 3
  assert test1_result.sum == 15
  assert test1_result.even_cnt == 2
  assert test1_result.odd_cnt == 3
  
def test_float():
  test_input_float = [1, 2, 3.2, 4, 5]

  with pytest.raises(ValueError):
    number_analysis(*test_input_float)

def test_empty():
  test_input_empty = []

  with pytest.raises(ValueError):
    number_analysis(*test_input_empty)

def test_non_number():
  test_input_non_number = [1, 2, 'three', 4, 5]

  with pytest.raises(ValueError):
    number_analysis(*test_input_non_number)
    