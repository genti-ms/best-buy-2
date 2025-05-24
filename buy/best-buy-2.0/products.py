class Product:
    """
    Represents a basic product in the store with price, quantity, and optional promotion.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a product with name, price, and quantity.

        Args:
            name (str): Name of the product.
            price (float): Price per unit (must be non-negative).
            quantity (int): Initial stock quantity (must be non-negative).
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self._promotion = None

    def is_active(self):
        """
        Returns whether the product is active (available for purchase).

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Marks the product as active."""
        self.active = True

    def deactivate(self):
        """Marks the product as inactive."""
        self.active = False

    def set_promotion(self, promotion):
        """
        Sets a promotion for the product.

        Args:
            promotion (Promotion): A promotion object.
        """
        self._promotion = promotion

    def get_promotion(self):
        """
        Gets the promotion set on the product.

        Returns:
            Promotion or None: The promotion object or None if not set.
        """
        return self._promotion

    def show(self):
        """
        Returns a string representation of the product for display.

        Returns:
            str: Product details.
        """
        promo = f" [Promotion: {self._promotion.name}]" if self._promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo}"

    def purchase(self, amount):
        """
        Purchases a given amount of the product, applying promotion if any.

        Args:
            amount (int): Quantity to purchase.

        Returns:
            float: Total price after promotion (if applicable).
        """
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if amount > self.quantity:
            raise ValueError(f"Not enough stock for '{self.name}'.")

        if self._promotion:
            total_price = self._promotion.apply_promotion(self, amount)
        else:
            total_price = self.price * amount

        self.quantity -= amount
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    A product that is always available and not stock-limited (e.g., digital goods).
    """

    def __init__(self, name, price):
        """
        Initializes a non-stocked product.

        Args:
            name (str): Product name.
            price (float): Product price (must be non-negative).
        """
        super().__init__(name, price, quantity=0)

    def show(self):
        """
        Returns a string representation of the non-stocked product.

        Returns:
            str: Product details.
        """
        promo = f" [Promotion: {self._promotion.name}]" if self._promotion else ""
        return f"{self.name}, Price: {self.price}, (Non-stocked){promo}"

    def purchase(self, amount):
        """
        Allows unlimited purchases of the product.

        Args:
            amount (int): Quantity to "purchase".

        Returns:
            float: Total price after promotion (if any).
        """
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if self._promotion:
            return self._promotion.apply_promotion(self, amount)
        return self.price * amount


class LimitedProduct(Product):
    """
    A product that limits the quantity per purchase.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a limited product.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Available stock.
            maximum (int): Max quantity per purchase.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """
        Returns a string representation of the limited product.

        Returns:
            str: Product details.
        """
        promo = f" [Promotion: {self._promotion.name}]" if self._promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}{promo}"

    def purchase(self, amount):
        """
        Purchases a quantity of the product within allowed maximum.

        Args:
            amount (int): Quantity to purchase.

        Returns:
            float: Total price after promotion (if applicable).
        """
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if amount > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of '{self.name}'.")
        if amount > self.quantity:
            raise ValueError(f"Not enough stock for '{self.name}'.")

        if self._promotion:
            total_price = self._promotion.apply_promotion(self, amount)
        else:
            total_price = self.price * amount

        self.quantity -= amount
        if self.quantity == 0:
            self.deactivate()

        return total_price
