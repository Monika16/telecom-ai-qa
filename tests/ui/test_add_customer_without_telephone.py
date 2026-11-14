
from utils.dialog_handler import handle_dialog

# AC-019: Submit the form with Telephone no. empty and all other fields valid
def test_add_customer_without_address(customer_page,customer_data):
    customer_data["phno"]= ""
    customer_page.fill_form(customer_data)
    validation_text = customer_page.page.locator("form").text_content()
    assert "Mobile no must not be blank" in validation_text
