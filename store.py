from products import Product


class Store:
    def __init__(self, product_list):
        if not isinstance(product_list, list):
            raise TypeError("Product list must be a list.")
        for product in product_list:
            if not isinstance(product, Product):
                raise TypeError("All items in product list must be Product instances.")

        self.product_list = product_list

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance.")

        self.product_list.append(product)

    def remove_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance.")
        if product not in self.product_list:
            raise ValueError("Product does not exist in store.")

        self.product_list.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list.")

        total_price = 0

        for item in shopping_list:
            if not isinstance(item, tuple):
                raise TypeError("Each shopping list item must be a tuple.")

            if len(item) != 2:
                raise ValueError("Each shopping list item must contain product and quantity.")

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError("Shopping list product must be a Product instance.")
            if not isinstance(quantity, int):
                raise TypeError("Shopping list quantity must be an integer.")

            total_price += product.buy(quantity)

        return total_price
