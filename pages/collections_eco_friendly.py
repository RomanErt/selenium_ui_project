from pages.locators import collections_eco_friendly_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils import project_ec


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 5)

    def verify_item_added_to_compare(self):
        first_item = self.find(loc.first_item_loc)
        compare_button = self.find(loc.compare_button_loc)

        ActionChains(self.driver).move_to_element(first_item).click(compare_button).perform()
        self.wait.until(EC.visibility_of_element_located(loc.item_in_compare_products_loc))
        first_item_name = (self.find(loc.first_item_loc)).text
        assert (self.find(loc.item_in_compare_products_loc)).text == first_item_name

        you_added_item_banner = self.find(loc.you_added_item_banner_loc)
        assert you_added_item_banner.is_displayed()

    def verify_product_images_load(self):
        first_product_image = self.find(loc.first_product_image_loc)
        fifth_product_image = self.find(loc.fifth_product_image_loc)

        assert project_ec.image_is_loaded(first_product_image)
        assert project_ec.image_is_loaded(fifth_product_image)

    def verify_erin_recommends_options(self):
        erin_recommends = self.find(loc.erin_recommends_loc)
        erin_recommends.click()

        erin_recommends_yes = self.find(loc.erin_recommends_yes_loc)
        erin_recommends_no = self.find(loc.erin_recommends_no_loc)
        assert erin_recommends_yes.is_displayed() and erin_recommends_yes.is_enabled()
        assert erin_recommends_no.is_displayed() and erin_recommends_no.is_enabled()
