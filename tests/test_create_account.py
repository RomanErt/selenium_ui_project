from test_data import (weak_password, medium_password, strong_password, very_strong_password, weak_password_message,
                       medium_password_message, strong_password_message, very_strong_password_message, password,
                       confirm_password, confirm_password_dont_match_error)


def test_required_field_error_messages_displayed(customer_account_create):
    customer_account_create.open_page()
    customer_account_create.click_create_an_account_button()

    customer_account_create.verify_first_name_required_error_is_displayed()
    customer_account_create.verify_last_name_required_error_is_displayed()
    customer_account_create.verify_email_required_error_is_displayed()
    customer_account_create.verify_password_required_error_is_displayed()
    customer_account_create.verify_confirm_password_required_error_is_displayed()


def test_password_strength_meter_updates_correctly(customer_account_create):
    customer_account_create.open_page()

    customer_account_create.input_password(weak_password)
    customer_account_create.verify_password_strength_meter_text(weak_password_message)
    customer_account_create.clear_password_field()

    customer_account_create.input_password(medium_password)
    customer_account_create.verify_password_strength_meter_text(medium_password_message)
    customer_account_create.clear_password_field()

    customer_account_create.input_password(strong_password)
    customer_account_create.verify_password_strength_meter_text(strong_password_message)
    customer_account_create.clear_password_field()

    customer_account_create.input_password(very_strong_password)
    customer_account_create.verify_password_strength_meter_text(very_strong_password_message)


def test_confirm_password_error_correct_if_passwords_do_not_match(customer_account_create):
    customer_account_create.open_page()
    customer_account_create.input_password_and_confirm_password(password, confirm_password)
    customer_account_create.click_create_an_account_button()
    customer_account_create.verify_password_error_text(confirm_password_dont_match_error)
