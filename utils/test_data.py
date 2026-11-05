import random
import string

def generate_customer_data():
    number = random.randint(1000,9999)

    return {
        "fname": f"John{number}",
        "lname": f"Doe{number}",
        "email": f"john{number}@example.com",
        "addr": f"{number} Main Street",
        "phno": f"98765{number}"
    }