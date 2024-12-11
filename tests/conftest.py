import pytest


@pytest.fixture
def zero_prices_zero_tax():
    return [0, 0, 0], 0


@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.fixture
def tax_fixture1():
    return 10, 5
