Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Vending Machine Program
... 
... # Menu: Dictionary with item codes, names, and prices
... menu = {
...     '1': {'name': 'Coke', 'price': 1.50},
...     '2': {'name': 'Pepsi', 'price': 1.40},
...     '3': {'name': 'Water', 'price': 1.00},
...     '4': {'name': 'Chips', 'price': 2.00},
...     '5': {'name': 'Chocolate', 'price': 2.50}
... }
... 
... def display_menu():
...     """Displays the vending machine menu."""
...     print("\n--- VENDING MACHINE MENU ---")
...     for code, item in menu.items():
...         print(f"[{code}] {item['name']} - ${item['price']:.2f}")
... 
... def get_user_selection():
...     """Prompts the user to select an item."""
...     while True:
...         code = input("\nEnter the code of the item you want to buy: ")
...         if code in menu:
...             return code
...         else:
...             print("Invalid selection. Please try again.")
... 
... def process_payment(price):
...     """Processes payment and returns the change."""
...     print(f"Total amount due: ${price:.2f}")
...     while True:
...         try:
...             amount = float(input("Enter your payment: $"))
...             if amount >= price:
...                 change = amount - price
...                 print(f"Payment accepted! Your change is ${change:.2f}")
...                 return change
...             else:
...                 print("Insufficient payment. Please enter more money.")
...         except ValueError:
...             print("Invalid input. Please enter a valid amount.")
... 
... def dispense_item(item_name):
...     """Dispenses the selected item."""
...     print(f"Dispensing {item_name}... Enjoy your snack or drink!")
... 
... def main():
...     """Main function to run the vending machine."""
...     print("Welcome to the Vending Machine!")
...     display_menu()
...     code = get_user_selection()
...     item = menu[code]
...     process_payment(item['price'])
...     dispense_item(item['name'])
... 
... # Run the vending machine
... if __name__ == "__main__":
...     main()
