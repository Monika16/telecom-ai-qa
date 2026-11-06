#AC-028: Double-click the Submit button during customer creation
def test_add_customer_double_click(customer_page,customer_data):
    customer_page.fill_form(customer_data)
    customer_page.page.locator("[name='submit']").dblclick()
    customer_page.page.wait_for_load_state("load")
    customer_id = customer_page.page.locator("//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3").inner_text()
    assert customer_id.strip() != ""
