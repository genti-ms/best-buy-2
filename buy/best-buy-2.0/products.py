class Product:
    """
    Represents a general product in the store.

    Attributes:
        name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity of the product in stock.
        active (bool): Whether the product is active (available).
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance.

        Args:
            name (str): The product's name.
            price (float): The product's price.
            quantity (int): The available quantity in stock.

        Raises:
            ValueError: If name is empty or price is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def show(self):
        """
        Returns a string with product details.

        Returns:
            str: Details of the product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def purchase(self, amount):
        """
        Purchases a given amount of the product, reducing stock.

        Args:
            amount (int): The quantity to purchase.

        Returns:
            str: Confirmation message.

        Raises:
            ValueError: If amount is greater than available quantity.
        """
        if amount > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")
        self.quantity -= amount
        if self.quantity == 0:
            self.active = False
        return f"Purchased {amount} of {self.name}"


class NonStockedProduct(Product):
    """
    Represents a non-stocked (digital or service) product.

    Quantity is always zero and cannot be changed.
    """

    def __init__(self, name, price):
        """
        Initializes a NonStockedProduct with quantity fixed to zero.

        Args:
            name (str): The product's name.
            price (float): The product's price.
        """
        super().__init__(name, price, quantity=0)

    def show(self):
        """
        Returns product details indicating it is non-stocked.

        Returns:
            str: Details of the non-stocked product.
        """
        return f"{self.name} (Non-stocked), Price: ${self.price}"

    def purchase(self, amount):
        """
        Allows purchase of any amount (no stock to reduce).

        Args:
            amount (int): The quantity to purchase.

        Returns:
            str: Confirmation message.
        """
        return f"Purchased {amount} of {self.name} (Non-stocked product)"


class LimitedProduct(Product):
    """
    Represents a product that can only be purchased up to a limited amount per order.

    Attributes:
        maximum (int): Maximum quantity allowed per order.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a LimitedProduct.

        Args:
            name (str): The product's name.
            price (float): The product's price.
            quantity (int): Available quantity in stock.
            maximum (int): Max quantity allowed per order.

        Raises:
            ValueError: If maximum is less than 1.
        """
        if maximum < 1:
            raise ValueError("Maximum must be at least 1.")
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """
        Returns product details indicating the purchase limit.

        Returns:
            str: Details of the limited product.
        """
        return f"{self.name} (Limited to {self.maximum} per order), Price: ${self.price}, Quantity: {self.quantity}"

    def purchase(self, amount):
        """
        Purchases a given amount with check against the maximum allowed per order.

        Args:
            amount (int): The quantity to purchase.

        Returns:
            str: Confirmation message.

        Raises:
            ValueError: If amount exceeds the maximum per order.
        """
        if amount > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of {self.name} per order.")
        return super().purchase(amount)
