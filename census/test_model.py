import pytest
from . import Census
from .models import Citizen


@pytest.fixture
def census():
    return Census([
        Citizen(name='Grace', age=66),
        Citizen(name='Guido', age=42)])


def test_sum(census):
    assert census.sum() == 2


def test_average_age(census):
    assert census.average_age() == 54.0
