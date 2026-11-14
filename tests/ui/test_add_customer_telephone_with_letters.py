
# AC-022: Verify telephone field does not accept letters

def test_add_customer_telephone_with_letters(customer_page, customer_data):
    customer_data["phno"]= "98765abcd1"
    customer_page.fill_form(customer_data)
    customer_page.page.locator("#telephoneno").press("Tab")
    validation_text = customer_page.page.locator("form").text_content()
    assert "Characters are not allowed" in validation_text

