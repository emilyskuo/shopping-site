"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        """Instantiate a Customer"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Representation of a Customer"""

        return f"<Customer: {self.first_name}, {self.last_name}"


def read_customer_data(filepath):
    """Read customer data from file and return dictionary"""

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first_name, last_name, email, password) = line.strip().split("|")

            customers[email] = Customer(first_name, last_name, email, password)

    return customers
