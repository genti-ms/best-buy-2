import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_create_normal_product():
    p = Product("Laptop", 1000, 10)
    assert p.name == "Laptop"
    assert p.price == 1000
    assert p.quantity == 10
    assert p.active is True
    assert "Laptop" in p.show()

def test_create_product_invalid():
    with pytest.raises(ValueError):
        Product("", 1000, 10)  # empty name
    with pytest.raises(ValueError):
        Product("Laptop", -5, 10)  # negative price
    with pytest.raises(ValueError):
        Product("Laptop", 1000, -1)  # negative quantity

def test_product_purchase_reduces_quantity_and_inactive():
    p = Product("Mouse", 20, 2)
    result = p.purchase(1)
    assert p.quantity == 1
    assert result == "Purchased 1 of Mouse"
    assert p.active is True

    result = p.purchase(1)
    assert p.quantity == 0
    assert p.active is False
    assert result == "Purchased 1 of Mouse"

def test_product_purchase_more_than_quantity_raises():
    p = Product("Keyboard", 50, 3)
    with pytest.raises(ValueError):
        p.purchase(4)

def test_nonstocked_product_quantity_always_zero():
    np = NonStockedProduct("Windows License", 120)
    assert np.quantity == 0
    assert "Non-stocked" in np.show()

def test_nonstocked_product_purchase():
    np = NonStockedProduct("Windows License", 120)
    result = np.purchase(5)
    assert result == "Purchased 5 of Windows License (Non-stocked product)"
    assert np.quantity == 0  # quantity never changes

def test_limited_product_purchase_within_limit():
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    result = lp.purchase(1)
    assert lp.quantity == 99
    assert result == "Purchased 1 of Shipping"

def test_limited_product_purchase_above_limit_raises():
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    with pytest.raises(ValueError):
        lp.purchase(2)

def test_limited_product_show_contains_limit():
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    assert "Limited to 1" in lp.show()
