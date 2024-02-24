# 1. You are working on a codebase for managing online orders. Currently, the Order
# class has the following functionalities:
# a. Storing order details (customer info, items, shipping address)
# b. Calculating total order cost (including taxes and discounts)
# c. Validating order data (checking item availability, customer address etc.)
# d. Sending order confirmation emails to customers
# e. Updating inventory levels after order processing
# Question: Write a Program (WAP) on how you would refactor the Order class to
# follow the Single Responsibility Principle (SRP). Name your program s.py.
# ● Each listed functionality represents a distinct responsibility.
# ● SRP suggests separating each responsibility into its own class or module.
# ● Think about how different functionalities interact and depend on each other.
# ● Consider the impact on code readability, maintainability, and reusability


class Order:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.price
        return total_cost

    def validate_order(self):
        print("Validating order...")

    def send_confirmation_email(self):
        print("Sending confirmation email...")

    def update_inventory(self):
        print("Updating inventory...")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderProcessor:
    def process_order(self, order):
        order.validate_order()
        order.calculate_total_cost()
        order.send_confirmation_email()
        order.update_inventory()