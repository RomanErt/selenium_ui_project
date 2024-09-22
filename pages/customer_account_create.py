from pages.locators import customer_account_create_locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerAccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 5)

    def verify_required_field_error_messages_displayed(self):
        create_account_button = self.find(loc.create_an_account_button_loc)
        create_account_button.click()

        first_name_required_error = self.find(loc.first_name_req_error_loc)
        last_name_required_error = self.find(loc.last_name_req_error_loc)
        email_required_error = self.find(loc.email_address_req_error_loc)
        password_required_error = self.find(loc.password_req_error_loc)
        confirm_password_required_error = self.find(loc.confirm_password_error_loc)

        self.wait.until(EC.visibility_of_element_located(loc.password_req_error_loc))

        assert first_name_required_error.is_displayed()
        assert last_name_required_error.is_displayed()
        assert email_required_error.is_displayed()
        assert password_required_error.is_displayed()
        assert confirm_password_required_error.is_displayed()

    def verify_password_strength_meter_updates_correctly(self):
        weak_password = 'weakpass'
        medium_password = 'Medium!1'
        strong_password = 'StrongPas!'
        very_strong_password = 'StrongPass!'

        password_field = self.find(loc.password_field)
        password_strength_meter = self.find(loc.password_strength_meter)
        password_field.send_keys(weak_password)
        self.wait.until(EC.visibility_of_element_located(loc.password_req_error_loc))
        assert password_strength_meter.text == 'Password Strength: Weak'
        password_field.clear()

        password_field.send_keys(medium_password)
        assert password_strength_meter.text == 'Password Strength: Medium'
        password_field.clear()

        password_field.send_keys(strong_password)
        assert password_strength_meter.text == 'Password Strength: Strong'
        password_field.clear()

        password_field.send_keys(very_strong_password)
        assert password_strength_meter.text == 'Password Strength: Very Strong'

    def verify_password_confirmation_error_message(self):
        password_field = self.find(loc.password_field)
        confirm_password_field = self.find(loc.confirm_password_field)

        password_field.send_keys('MyPassword')
        confirm_password_field.send_keys('mypassword')

        self.find(loc.create_an_account_button_loc).click()
        self.wait.until(EC.visibility_of_element_located(loc.confirm_password_error_loc))

        confirm_password_error = self.find(loc.confirm_password_error_loc)

        assert confirm_password_error.text == 'Please enter the same value again.'
