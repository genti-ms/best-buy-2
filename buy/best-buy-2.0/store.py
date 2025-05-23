class Store:
    """
    A class that represents the store and its operations.
    """

    def __init__(self, product_list):
        """
        Initializes the store with a list of products.

        Args:
            product_list (list): A list of Product objects.
        """
        self.products = product_list

    def get_all_products(self):
        """
        Returns a list of all products in the store.

        Returns:
            list: A list of all products.
        """
        return self.products

    @staticmethod
    def get_total_quantity(products):
        """
        Returns the total quantity of all products in the store.

        Args:
            products (list): A list of Product objects.

        Returns:
            int: Total quantity of items.
        """
        return sum(product.quantity for product in products)

    @staticmethod
    def order(shopping_list):
        """
        Processes the order and returns the total cost.

        Args:
            shopping_list (list): A list of tuples containing product and quantity.

        Returns:
            float: The total cost of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity < quantity:
                raise ValueError(f"Not enough stock for {product.name}.")
            product.quantity -= quantity
            total_price += product.price * quantity
        return total_price
