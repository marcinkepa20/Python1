import pytest
from main import the_sum

def test_add():
    assert the_sum(2,2) == 4


def test_addMore():
    assert the_sum(100,2) == 102





