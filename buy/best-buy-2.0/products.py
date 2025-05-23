class Product:
    """
    Class representing a product in the store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        """
        Shows the details of the product.

        Returns:
            str: The product details as a string.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def update_quantity(self, amount):
        """
        Update the quantity of the product.

        Args:
            amount (int): The amount to be added/subtracted from the product quantity.
        """
        self.quantity += amount
