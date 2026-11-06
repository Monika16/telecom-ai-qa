import random
import string

def generate_customer_data():
    number = random.randint(1000,9999)

    rand_first = ''.join(random.choices(string.ascii_lowercase, k=6))
    rand_last = ''.join(random.choices(string.ascii_lowercase, k=6))

    return {
        "fname": rand_first.capitalize(),
        "lname": rand_last.capitalize(),
        "email": f"john{number}@example.com",
        "addr": f"{number} Main Street",
        "phno": f"98765{number}"
    }