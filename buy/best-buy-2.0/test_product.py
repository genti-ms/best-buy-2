import pytest
from products import Product



def test_create_normal_product():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.active == True

def test_create_product_invalid_details():
    # Leerer Name sollte Exception werfen
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    # Negativer Preis sollte Exception werfen
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_product_becomes_inactive_when_quantity_zero():
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.purchase(1)
    assert p.quantity == 0
    assert p.active == False

def test_product_purchase_modifies_quantity_and_returns_correct_output():
    p = Product("MacBook Air M2", price=1450, quantity=10)
    result = p.purchase(3)
    assert p.quantity == 7
    assert result == "Purchased 3 of MacBook Air M2"

def test_purchase_more_than_quantity_raises_exception():
    p = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        p.purchase(10)
