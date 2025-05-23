from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    Abstract base class for promotions.

    Attributes:
        name (str): Name of the promotion.
    """

    def __init__(self, name):
        """
        Initializes a Promotion instance.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the promotion to a product purchase.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity being purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Applies a percentage discount to the total price.

    Attributes:
        percent (float): Discount percentage (e.g., 20 for 20% off).
    """

    def __init__(self, name, percent):
        """
        Initializes a PercentDiscount promotion.

        Args:
            name (str): Name of the promotion.
            percent (float): Percentage discount to apply.
        """
        super().__init__(name)
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply percentage discount to product purchase.

        Args:
            product (Product): The product instance.
            quantity (int): Quantity being purchased.

        Returns:
            float: Total price after discount.
        """
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount


class SecondHalfPrice(Promotion):
    """
    For every two items, the second is half price.
    """

    def apply_promotion(self, product, quantity):
        """
        Apply "second item at half price" promotion.

        Args:
            product (Product): The product instance.
            quantity (int): Quantity being purchased.

        Returns:
            float: Total price after applying the promotion.
        """
        full_price_count = (quantity + 1) // 2  # Number of full price items
        half_price_count = quantity // 2       # Number of half price items
        total = (full_price_count * product.price) + (half_price_count * product.price * 0.5)
        return total


class ThirdOneFree(Promotion):
    """
    Buy 2, get 1 free promotion.
    """

    def apply_promotion(self, product, quantity):
        """
        Apply "buy 2, get 1 free" promotion.

        Args:
            product (Product): The product instance.
            quantity (int): Quantity being purchased.

        Returns:
            float: Total price after applying the promotion.
        """
        group_of_three = quantity // 3
        remainder = quantity % 3
        total_price = (group_of_three * 2 * product.price) + (remainder * product.price)
        return total_price
