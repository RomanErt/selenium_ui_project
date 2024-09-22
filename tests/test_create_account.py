def test_required_field_error_messages_displayed(customer_account_create):
    customer_account_create.open_page()
    customer_account_create.verify_required_field_error_messages_displayed()


def test_password_strength_meter_updates_correctly(customer_account_create):
    customer_account_create.open_page()
    customer_account_create.verify_password_strength_meter_updates_correctly()


def test_confirm_password_error_correct_if_passwords_do_not_match(customer_account_create):
    customer_account_create.open_page()
    customer_account_create.verify_password_confirmation_error_message()
