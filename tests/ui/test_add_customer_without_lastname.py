from utils.dialog_handler import handle_dialog

# AC-016: Submit form with empty Last Name
def test_add_customer_without_lastname(customer_page,customer_data):
    customer_data["lname"]= ""
    customer_page.fill_form(customer_data)
    validation_text = customer_page.page.locator("form").text_content()
    assert "Customer name must not be blank" in validation_text
    customer_page.page.on("dialog", handle_dialog)
    customer_page.submit_form()
