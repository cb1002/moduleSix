class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}"

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            total_items = self.get_num_items_in_cart()
            total_cost = self.get_cost_of_cart()
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {total_items}")
            for item in self.cart_items:
                print(item.print_item_cost())
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_price}, {item.item_quantity}")

def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """
    option = ''
    while option != 'q':
        option = input(menu).lower()
        if option == 'a':
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter the item name: ")
            new_item.item_price = float(input("Enter the item price: "))
            new_item.item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(new_item)
        elif option == 'r':
            item_name = input("Enter the name of the item to remove: ")
            cart.remove_item(item_name)
        elif option == 'c':
            item_name = input("Enter the item name to modify: ")
            updated_item = ItemToPurchase()
            updated_item.item_name = item_name
            updated_item.item_price = float(input("Enter the new item price: "))
            updated_item.item_quantity = int(input("Enter the new item quantity: "))
            cart.modify_item(updated_item)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()

def main():
    shopping_cart = ShoppingCart("Bruce Springsteen", "July 4, 2024")
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()