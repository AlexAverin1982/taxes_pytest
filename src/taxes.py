def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, discount: float = 0, precision: int = 2) -> float:
    """Функция должна вычислять стоимость товара с учетом налога"""

    if not (isinstance(price, float) or isinstance(price, int)):
        raise TypeError("Цена должна быть целым или дробным неотрицательным числом")

    if not (isinstance(tax_rate, float) or isinstance(tax_rate, int)):
        raise TypeError("Процент налога должен быть целым или дробным положительным числом меньше 100")

    if price <= 0:
        raise ValueError("Неверная цена")

    if (tax_rate < 0) or (tax_rate >= 100):
        raise ValueError("Неверный налоговый процент")

    if (discount < 0) or (discount >= 100):
        raise ValueError("Неверное значение процента скидки")

    if not isinstance(precision, int):
        raise TypeError("Число цифр после запятой должно быть целочисленным")

    result = price * (tax_rate / 100 + 1) * (1 - discount / 100)
    return round(result, precision)

# print(calculate_taxes([10], '0'))
