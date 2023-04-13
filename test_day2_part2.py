import pytest
from day2_part2 import find_inputs_for_output


def test_find_inputs_for_output():
    assert find_inputs_for_output("day2_data.txt", 19690720) == 6249

