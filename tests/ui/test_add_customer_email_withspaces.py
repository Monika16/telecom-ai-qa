# AC-021: Verify email containing spaces is rejected

def test_add_customer_email_withspaces(customer_data, customer_page):
    customer_data["email"] = "john example@test.com"
    customer_page.fill_form(customer_data)
    email = customer_page.page.locator("#email")
    customer_page.submit_form()

    # Verify browser email validation
    is_valid = email.evaluate(
        "(element) => element.validity.valid"
    )

    assert is_valid is False

    # Verify email format mismatch
    type_mismatch = email.evaluate(
        "(element) => element.validity.typeMismatch"
    )

    assert type_mismatch is True
