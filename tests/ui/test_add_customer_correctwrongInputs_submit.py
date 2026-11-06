from utils.dialog_handler import handle_dialog

# AC-030: Correct invalid form data and submit again
def test_add_customer_correctwrongInputs_submit(customer_page,customer_data):
    customer_data["email"] = "johnexample.com"
    customer_page.fill_form(customer_data)
    customer_page.page.on("dialog", handle_dialog)
    customer_page.submit_form()

    validation_text = customer_page.page.locator("form").text_content()
    assert "Email-ID is not valid" in validation_text

    customer_page.page.locator("#email").fill("john@example.com")
    customer_page.page.on("dialog", handle_dialog)
    customer_page.submit_form()
    customer_page.page.wait_for_load_state("load")
    customer_id_locator = customer_page.page.locator("//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3")
    print("Customer_id: ",customer_id_locator.inner_text())