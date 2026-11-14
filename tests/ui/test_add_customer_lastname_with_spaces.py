import pytest
from utils.dialog_handler import handle_dialog

#AC-011: Enter leading spaces in a required text field
#AC-012: Enter trailing spaces in a required text field
@pytest.mark.parametrize(
    "last_name, expected_output",
    [
        ("      John","First character can not have space"),
        ("John        ",""),
    ]
)
def test_add_customer_lasttname_with_spaces(customer_page,customer_data,last_name,expected_output):
    customer_data["lname"]= last_name
    customer_page.fill_form(customer_data)
    validation_text = customer_page.page.locator("form").text_content()
    if expected_output:
        assert expected_output in validation_text
    else:
        customer_page.submit_form()

        customer_id = customer_page.page.locator(
            "//*[@id='main']/div/div/table/tbody/tr[1]/td[2]/h3"
        ).inner_text()

        assert customer_id.strip() != ""