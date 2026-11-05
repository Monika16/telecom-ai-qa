
# AC-001: Add customer with all valid details
def test_add_customer(customer_page, customer_data):
    customer_page.fill_form(customer_data)
    customer_page.submit_form()