import pytest


@pytest.fixture
def simple_ab():
    return [1, 2, 4]


@pytest.fixture
def supply_url():
    return "https://reqres.in/api"
