import products
import store


def list_products(best_buy):
    """Displays all active products in the store."""
    print("------")
    active_products = best_buy.get_all_products()
    for index, product in enumerate(active_products, start=1):
        print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")


def show_total_quantity(best_buy):
    """Displays the total quantity of all products in the store."""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def show_products(products_list):
    """Displays a numbered list of products."""
    print("------")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")


def get_reserved_quantity(shopping_list, selected_product):
    """Returns how many units of a product are already in the shopping list."""
    reserved_quantity = 0
    for product, quantity in shopping_list:
        if product == selected_product:
            reserved_quantity += quantity
    return reserved_quantity


def get_valid_product(active_products):
    """Prompts the user for a valid product number and returns the selected product."""
    while True:
        product_choice = input("Which product # do you want? ")

        if product_choice == "":
            return None

        try:
            product_index = int(product_choice) - 1
        except ValueError:
            print("Error adding product! Please enter a valid product number.")
            print()
            continue

        if product_index < 0 or product_index >= len(active_products):
            print("Error adding product! Product number does not exist.")
            print()
            continue

        return active_products[product_index]


def get_valid_quantity(selected_product, shopping_list):
    """Prompts the user for a valid quantity for the selected product."""
    reserved_quantity = get_reserved_quantity(shopping_list, selected_product)
    available_left = selected_product.quantity - reserved_quantity

    if available_left == 0:
        print("Error adding product! No items left available for this order.")
        print()
        return None

    while True:
        quantity_choice = input("What amount do you want? ")

        if quantity_choice == "":
            return None

        try:
            amount = int(quantity_choice)
        except ValueError:
            print("Error adding product! Please enter a valid quantity.")
            print()
            continue

        if amount <= 0:
            print("Error adding product! Quantity must be greater than 0.")
            print()
            continue

        if amount > available_left:
            print(f"Error adding product! Only {available_left} item(s) left available for this order.")
            print()
            continue

        return amount


def make_order(best_buy):
    """Handles the order flow: product selection, validation, and checkout."""
    shopping_list = []
    active_products = best_buy.get_all_products()

    show_products(active_products)
    print("When you want to finish order, press Enter.")

    while True:
        selected_product = get_valid_product(active_products)

        if selected_product is None:
            break

        amount = get_valid_quantity(selected_product, shopping_list)

        if amount is None:
            continue

        shopping_list.append((selected_product, amount))
        print("Product added to list!")
        print()

    if not shopping_list:
        print("Order cancelled.")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as error:
        print(f"Error while making order: {error}")
    except TypeError as error:
        print(f"Error while making order: {error}")


def quit_program(best_buy):
    """Stops the program."""
    return False


def start(best_buy):
    """Runs the store menu loop."""
    menu_actions = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order,
        "4": quit_program
    }

    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        action = menu_actions.get(choice)

        if action is None:
            print("Invalid choice, please try again.")
            continue

        result = action(best_buy)
        if result is False:
            break


def main():
    """Creates the store and starts the program."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
