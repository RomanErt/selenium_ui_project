from selenium.webdriver.common.by import By

password_field = (By.ID, 'password')
confirm_password_field = (By.ID, 'password-confirmation')
password_strength_meter = (By.ID, 'password-strength-meter-container')


create_an_account_button_loc = (By.CSS_SELECTOR, '.action.submit.primary')

first_name_req_error_loc = (By.CSS_SELECTOR, '#firstname-error.mage-error')
last_name_req_error_loc = (By.CSS_SELECTOR, '#lastname-error.mage-error')
email_address_req_error_loc = (By.CSS_SELECTOR, '#email_address-error.mage-error')
password_req_error_loc = (By.CSS_SELECTOR, '#password-error.mage-error')
confirm_password_error_loc = (By.CSS_SELECTOR, '#password-confirmation-error.mage-error')
