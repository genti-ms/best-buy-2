import pytest
from products import Product
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

@pytest.fixture
def sample_product():
    return Product("TestProduct", price=100, quantity=100)

def test_percent_discount(sample_product):
    promo = PercentDiscount("20% off", percent=20)
    total_price = promo.apply_promotion(sample_product, 5)  # 5 * 100 = 500, 20% off = 400
    assert total_price == 400

def test_second_half_price_even(sample_product):
    promo = SecondHalfPrice("Second Half Price")
    total_price = promo.apply_promotion(sample_product, 4)
    # 2 full price + 2 half price: 2*100 + 2*50 = 300
    assert total_price == 300

def test_second_half_price_odd(sample_product):
    promo = SecondHalfPrice("Second Half Price")
    total_price = promo.apply_promotion(sample_product, 5)
    # 3 full price + 2 half price: 3*100 + 2*50 = 400
    assert total_price == 400

def test_third_one_free_exact(sample_product):
    promo = ThirdOneFree("Buy 2 get 1 free")
    total_price = promo.apply_promotion(sample_product, 6)
    # 2 groups of 3: pay for 4 items (2*2), free 2
    assert total_price == 400

def test_third_one_free_remainder(sample_product):
    promo = ThirdOneFree("Buy 2 get 1 free")
    total_price = promo.apply_promotion(sample_product, 7)
    # 2 groups of 3 + 1 item: pay for 4 + 1 = 5 items
    assert total_price == 500

def test_percent_discount_invalid_percent():
    with pytest.raises(ValueError):
        PercentDiscount("Invalid", percent=150)  # Percent must be between 0 and 100
