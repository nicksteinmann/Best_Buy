class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
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
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
