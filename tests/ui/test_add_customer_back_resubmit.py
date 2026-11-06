#AC-029: Navigate back from the confirmation page and submit the form again

def test_add_customer_back_resubmit(customer_page,customer_data):
    customer_page.fill_form(customer_data)
    customer_page.submit_form()

    customer_page.page.wait_for_load_state("load")
    customer_id_locator = customer_page.page.locator("//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3")
    first_customer_id = customer_id_locator.inner_text()
    #print(first_customer_id)
    customer_page.page.go_back(wait_until="load")

    customer_page.trigger_field_events()

    customer_page.submit_form()
    customer_page.page.wait_for_load_state("load")

    sec_customer_id = customer_id_locator.inner_text()
    #print(sec_customer_id)

    assert first_customer_id != sec_customer_id


