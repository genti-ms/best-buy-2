class Store:
    """
    A class that represents the store and its operations.
    Manages a list of Product objects, supports adding/removing products,
    calculating total inventory, and processing customer orders.
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
            list: The current list of Product objects in the store.
        """
        return self.products

    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: Total number of items in stock across all products.
        """
        return sum(product.quantity for product in self.products)

    def add_product(self, product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to be removed.
        """
        self.products.remove(product)

    def order(self, shopping_list):
        """
        Processes an order consisting of multiple products and quantities.
        Reduces stock and returns the total cost.

        Args:
            shopping_list (list): A list of tuples (Product, quantity) representing the customer's order.

        Returns:
            float: The total cost of all purchased items.

        Raises:
            ValueError: If a product does not have enough quantity in stock.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.price * quantity
            product.purchase(quantity)
        return total_price
