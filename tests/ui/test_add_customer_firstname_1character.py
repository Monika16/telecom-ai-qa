from playwright.async_api import expect


def test_add_customer_firstname_1character(customer_page,customer_data):
    customer_data["fname"] = "C"
    customer_page.fill_form(customer_data)
    customer_page.submit_form()
    customer_page.page.wait_for_load_state("load")
    customer_id = customer_page.page.locator(
        "//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3"
    ).inner_text()

    assert customer_id.strip() != ""


