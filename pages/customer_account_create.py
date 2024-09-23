from pages.locators import customer_account_create_locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class CustomerAccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 5)

    def click_create_an_account_button(self):
        self.find(loc.create_an_account_button_loc).click()

    def input_password(self, password):
        self.find(loc.password_field).send_keys(password)

    def clear_password_field(self):
        self.find(loc.password_field).clear()

    def input_password_and_confirm_password(self, password, confirm_password):
        self.find(loc.password_field).send_keys(password)
        self.find(loc.confirm_password_field).send_keys(confirm_password)

    def verify_password_strength_meter_text(self, password_meter_text):
        password_strength_meter = self.find(loc.password_strength_meter)
        assert password_strength_meter.text == password_meter_text

    def verify_password_error_text(self, password_error_text):
        confirm_password_error = self.find(loc.confirm_password_error_loc)
        assert confirm_password_error.text == password_error_text

    def verify_first_name_required_error_is_displayed(self):
        assert self.find(loc.first_name_req_error_loc).is_displayed()

    def verify_last_name_required_error_is_displayed(self):
        assert self.find(loc.last_name_req_error_loc).is_displayed()

    def verify_email_required_error_is_displayed(self):
        assert self.find(loc.email_address_req_error_loc).is_displayed()

    def verify_password_required_error_is_displayed(self):
        assert self.find(loc.password_req_error_loc).is_displayed()

    def verify_confirm_password_required_error_is_displayed(self):
        assert self.find(loc.confirm_password_error_loc).is_displayed()
