import pytest

from src.taxes import calculate_taxes, calculate_tax


# from tests.conftest import zero_prices_zero_tax


def test_calculate_taxes():
    assert calculate_taxes([1.0, 2.4, 3.7, 9], 14) == [
        1.1400000000000001,
        2.7359999999999998,
        4.218,
        10.26,
    ]


def test_negative_tax_rate():
    with pytest.raises(ValueError) as e:
        calculate_taxes([1.4, 32.4, 3.7, 19.2], -1.7)

    assert str(e.value) == "Неверный налоговый процент"


def test_negative_prices():
    with pytest.raises(ValueError) as e:
        calculate_taxes([-1.4, -32.4, 3.7, -19.2], 1)

    assert str(e.value) == "Неверная цена"


def test_zero_price():
    with pytest.raises(ValueError) as e:
        calculate_taxes([0, ], 2)

    assert str(e.value) == "Неверная цена"


def test_none():
    with pytest.raises(TypeError) as e:
        calculate_taxes(None, None)
    assert str(e.value) == "'<' not supported between instances of 'NoneType' and 'int'"


def test_str_taxrate():
    with pytest.raises(TypeError) as e:
        calculate_taxes([10], 'some_string')
    assert str(e.value) == "'<' not supported between instances of 'str' and 'int'"


def test_empty_prices(zero_prices_zero_tax):
    with pytest.raises(ValueError) as e:
        calculate_taxes(zero_prices_zero_tax[0], zero_prices_zero_tax[1])
    assert str(e.value) == "Неверная цена"


@pytest.mark.parametrize('prices, tax_rate, expected',
                         [([1, 1, 1], 0, [1, 1, 1]), ([100, 200, 300], 0.5, [100.5, 201.0, 301.5])])
def test_params(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calc_tax(tax_fixture1):
    assert calculate_tax(tax_fixture1[0], tax_fixture1[1]) == 10.5


@pytest.mark.parametrize('price, tax_rate, expected', [(100, 10, 110.0), (50, 5, 52.5),
                                                       (105, 1, 106.05)])
def test_calc_taxes_params(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_negative_price_tax():
    with pytest.raises(ValueError) as e:
        calculate_tax(-100, 1)
        assert str(e.value) == "Неверная цена"


def test_negative_tax():
    with pytest.raises(ValueError) as e:
        calculate_tax(100, -10)
        assert str(e.value) == "Неверный налоговый процент"


def test_overtax():
    with pytest.raises(ValueError) as e:
        calculate_tax(100, 200)
        assert str(e.value) == "Неверный налоговый процент"
