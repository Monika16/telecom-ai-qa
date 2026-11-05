import pytest
from utils.dialog_handler import handle_dialog

#AC-011: Enter leading spaces in a required text field
#AC-012: Enter trailing spaces in a required text field
@pytest.mark.parametrize(
    "first_name, expected_output",
    [
        ("      John","First character can not have space"),
        ("John        ",""),
    ]
)
def test_add_customer_firstname_with_spaces(customer_page,customer_data,first_name,expected_output):
    customer_data["fname"]= first_name
    customer_page.fill_form(customer_data)
    validation_text = customer_page.page.locator("form").text_content()
    assert  expected_output in validation_text
    customer_page.page.on("dialog", handle_dialog)
    customer_page.submit_form()
