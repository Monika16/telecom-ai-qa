from utils.dialog_handler import handle_dialog

# AC-020: Enter invalid email format
def test_add_customer_invalid_email(customer_data, customer_page):
   customer_data["email"] = "john123"
   customer_page.fill_form(customer_data)
   validation_text = customer_page.page.locator("form").text_content()
   assert "Email-ID is not valid" in validation_text
