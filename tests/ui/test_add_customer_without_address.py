
from utils.dialog_handler import handle_dialog

# AC-018: Submit the form with Address empty and all other fields valid
def test_add_customer_without_telephone(customer_page,customer_data):
    customer_data["addr"]= ""
    customer_page.fill_form(customer_data)
    validation_text = customer_page.page.locator("form").text_content()
    assert "Address Field must not be blank" in validation_text
