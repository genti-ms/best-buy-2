class Product:
    """
    Class representing a product in the store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new product with name, price, and quantity.

        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity of the product in stock. Must be >= 0.

        Raises:
            ValueError: If the name is empty or the price is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def show(self):
        """
        Returns a string representation of the product's details.

        Returns:
            str: The product's name, price, and quantity.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def update_quantity(self, amount):
        """
        Updates the product quantity by the given amount. Can be negative.

        Args:
            amount (int): The amount to change the quantity by.

        Notes:
            If quantity becomes zero or less, the product is marked inactive.
        """
        self.quantity += amount
        if self.quantity <= 0:
            self.quantity = 0
            self.active = False

    def purchase(self, amount):
        """
        Purchases a given amount of the product.

        Args:
            amount (int): Number of units to purchase.

        Returns:
            str: Confirmation message of the purchase.

        Raises:
            ValueError: If the requested amount exceeds available quantity.
        """
        if amount > self.quantity:
            raise ValueError("Not enough stock to complete purchase")
        self.quantity -= amount
        if self.quantity == 0:
            self.active = False
        return f"Purchased {amount} of {self.name}"
