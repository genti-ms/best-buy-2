import pytest
from products import Product
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

@pytest.fixture
def sample_product():
    """
    Fixture that provides a sample Product instance
    with name 'TestProduct', price 100, and quantity 100.
    """
    return Product("TestProduct", price=100, quantity=100)

def test_percent_discount(sample_product):
    """
    Test the PercentDiscount promotion with a 20% discount
    on a quantity of 5 products.
    Expected total price: 5 * 100 * 0.8 = 400.
    """
    promo = PercentDiscount("20% off", percent=20)
    total_price = promo.apply_promotion(sample_product, 5)
    assert total_price == 400

def test_second_half_price_even(sample_product):
    """
    Test the SecondHalfPrice promotion for an even quantity (4).
    Expected price: 2 full price + 2 half price = 300.
    """
    promo = SecondHalfPrice("Second Half Price")
    total_price = promo.apply_promotion(sample_product, 4)
    assert total_price == 300

def test_second_half_price_odd(sample_product):
    """
    Test the SecondHalfPrice promotion for an odd quantity (5).
    Expected price: 3 full price + 2 half price = 400.
    """
    promo = SecondHalfPrice("Second Half Price")
    total_price = promo.apply_promotion(sample_product, 5)
    assert total_price == 400

def test_third_one_free_exact(sample_product):
    """
    Test the ThirdOneFree promotion for exact multiples (6).
    Expected price: pay for 4 items (2 groups * 2), get 2 free = 400.
    """
    promo = ThirdOneFree("Buy 2 get 1 free")
    total_price = promo.apply_promotion(sample_product, 6)
    assert total_price == 400

def test_third_one_free_remainder(sample_product):
    """
    Test the ThirdOneFree promotion with remainder items (7).
    Expected price: pay for 5 items (2 groups * 2 + 1 extra) = 500.
    """
    promo = ThirdOneFree("Buy 2 get 1 free")
    total_price = promo.apply_promotion(sample_product, 7)
    assert total_price == 500

def test_percent_discount_invalid_percent():
    """
    Test that PercentDiscount raises a ValueError
    when initialized with an invalid percentage (> 100).
    """
    with pytest.raises(ValueError):
        PercentDiscount("Invalid", percent=150)  # Percent must be between 0 and 100
