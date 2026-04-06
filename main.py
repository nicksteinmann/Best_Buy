import products
import store


def start(best_buy):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            active_products = best_buy.get_all_products()
            for index, product in enumerate(active_products, start=1):
                print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")

        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")

        elif choice == "3":
            shopping_list = []
            active_products = best_buy.get_all_products()

            print("------")
            for index, product in enumerate(active_products, start=1):
                print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                product_choice = input("Which product # do you want? ")
                quantity_choice = input("What amount do you want? ")

                if product_choice == "" or quantity_choice == "":
                    break

                try:
                    product_index = int(product_choice) - 1
                    amount = int(quantity_choice)

                    if product_index < 0 or product_index >= len(active_products):
                        print("Error adding product!")
                        print()
                        continue

                    shopping_list.append((active_products[product_index], amount))
                    print("Product added to list!")
                    print()

                except ValueError:
                    print("Error adding product!")
                    print()

            try:
                total_price = best_buy.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total_price}")
            except Exception as e:
                print(f"Error while making order: {e}")

        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
