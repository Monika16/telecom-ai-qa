# AC-014: Refresh the page after successful customer creation
def test_add_customer_refresh(customer_page,customer_data):
    customer_page.fill_form(customer_data)
    customer_page.submit_form()
    customer_page.page.wait_for_load_state("load")
    customer_id_before = customer_page.page.locator("//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3").inner_text()
    customer_page.page.reload()
    customer_id_after = customer_page.page.locator("//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3").inner_text()
    assert customer_id_before == customer_id_after
