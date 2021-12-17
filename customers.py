"""Customers at Hackbright."""
import melons

class Customer(Melon):
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
    """Convenience method to show information about melon in console."""

    return (
        f"<Customer: {self.first_name, {self.last_name}, {self.email}, {self.password}>"
    )
    
def read_customer_file(filepath):
    customers = {}
    with open(filepath) as file:
        for line in file:
            (
            first_name,
            last_name,
            email,
            password
            ) = line.strip().split("|")
        new_customer = Customer(first_name, last_name, email, password)
        customers[email] = new_customer
    return customers

def get_by_email(email):
    return customers[email]


customers = read_customer_file('customers.txt')