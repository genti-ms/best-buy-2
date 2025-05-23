import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_create_normal_product():
    """
    Test creating a normal Product with valid parameters.
    Verifies attributes and that the product is active.
    """
    p = Product("Laptop", 1000, 10)
    assert p.name == "Laptop"
    assert p.price == 1000
    assert p.quantity == 10
    assert p.active is True
    assert "Laptop" in p.show()

def test_create_product_invalid():
    """
    Test that creating a Product with invalid parameters
    (empty name, negative price, negative quantity) raises ValueError.
    """
    with pytest.raises(ValueError):
        Product("", 1000, 10)  # empty name
    with pytest.raises(ValueError):
        Product("Laptop", -5, 10)  # negative price
    with pytest.raises(ValueError):
        Product("Laptop", 1000, -1)  # negative quantity

def test_product_purchase_reduces_quantity_and_inactive():
    """
    Test that purchasing a Product reduces its quantity correctly
    and deactivates the product when quantity reaches zero.
    """
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
    """
    Test that purchasing more items than available quantity
    raises a ValueError.
    """
    p = Product("Keyboard", 50, 3)
    with pytest.raises(ValueError):
        p.purchase(4)

def test_nonstocked_product_quantity_always_zero():
    """
    Test that NonStockedProduct always has quantity zero
    and its string representation indicates it is non-stocked.
    """
    np = NonStockedProduct("Windows License", 120)
    assert np.quantity == 0
    assert "Non-stocked" in np.show()

def test_nonstocked_product_purchase():
    """
    Test purchasing a NonStockedProduct returns the correct message
    and does not change the quantity.
    """
    np = NonStockedProduct("Windows License", 120)
    result = np.purchase(5)
    assert result == "Purchased 5 of Windows License (Non-stocked product)"
    assert np.quantity == 0  # quantity never changes

def test_limited_product_purchase_within_limit():
    """
    Test purchasing a LimitedProduct within its maximum allowed quantity
    reduces stock correctly and returns confirmation.
    """
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    result = lp.purchase(1)
    assert lp.quantity == 99
    assert result == "Purchased 1 of Shipping"

def test_limited_product_purchase_above_limit_raises():
    """
    Test that attempting to purchase more than the maximum allowed
    quantity for a LimitedProduct raises a ValueError.
    """
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    with pytest.raises(ValueError):
        lp.purchase(2)

def test_limited_product_show_contains_limit():
    """
    Test that the string representation of a LimitedProduct
    includes the maximum purchase limit.
    """
    lp = LimitedProduct("Shipping", 10, 100, maximum=1)
    assert "Limited to 1" in lp.show()
