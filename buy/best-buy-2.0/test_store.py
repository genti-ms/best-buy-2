import pytest
from store import Store
from products import Product


def test_add_and_remove_product():
    """
    Tests that a product can be added to and removed from the store.
    """
    product = Product("iPhone", 999, 10)
    store = Store([])
    store.add_product(product)
    assert product in store.get_all_products()
    store.remove_product(product)
    assert product not in store.get_all_products()


def test_get_total_quantity():
    """
    Tests that the total quantity of all products is calculated correctly.
    """
    p1 = Product("iPhone", 999, 10)
    p2 = Product("MacBook", 1999, 5)
    store = Store([p1, p2])
    assert store.get_total_quantity() == 15


def test_successful_order():
    """
    Tests that a successful order returns the correct total price
    and updates the product quantities.
    """
    p1 = Product("iPhone", 1000, 10)
    p2 = Product("MacBook", 2000, 5)
    store = Store([p1, p2])
    total = store.order([(p1, 2), (p2, 1)])
    assert total == 4000
    assert p1.quantity == 8
    assert p2.quantity == 4


def test_order_raises_exception_on_insufficient_stock():
    """
    Tests that an exception is raised when trying to order
    more quantity than is in stock.
    """
    p1 = Product("iPhone", 1000, 2)
    store = Store([p1])
    with pytest.raises(ValueError):
        store.order([(p1, 5)])
