class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if not self.is_active():
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
