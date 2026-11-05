from utils.dialog_handler import handle_dialog

# AC-017: Submit the form with Email empty and all other fields valid
def test_add_customer_without_email(customer_data, customer_page):
   customer_data["email"] = ""
   customer_page.fill_form(customer_data)
   validation_text = customer_page.page.locator("form").text_content()
   assert "Email-ID must not be blank" in validation_text
   customer_page.page.on("dialog", handle_dialog)
   customer_page.submit_form()
