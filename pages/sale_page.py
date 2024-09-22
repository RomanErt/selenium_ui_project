from pages.locators import sale_page_locators as loc
from pages.base_page import BasePage
from utils import project_ec
from selenium.webdriver.support.ui import WebDriverWait


class SalePage(BasePage):
    page_url = '/sale.html'

    def verify_women_deals_categories_clickable(self):
        hoodies_and_sweatshirts = self.find(loc.women_hoodies_and_sweatshirts_loc)
        jackets = self.find(loc.women_jackets_loc)
        tees = self.find(loc.women_tees_loc)
        bras_tanks = self.find(loc.women_bras_tanks_loc)
        pants = self.find(loc.women_bras_tanks_loc)
        shorts = self.find(loc.women_shorts_loc)
        assert hoodies_and_sweatshirts.is_enabled() and hoodies_and_sweatshirts.is_displayed()
        assert jackets.is_enabled() and jackets.is_displayed()
        assert tees.is_enabled() and tees.is_displayed()
        assert bras_tanks.is_enabled() and bras_tanks.is_displayed()
        assert pants.is_enabled() and pants.is_displayed()
        assert shorts.is_enabled() and shorts.is_displayed()

    def verify_men_deals_categories_clickable(self):
        hoodies_and_sweatshirts = self.find(loc.men_hoodies_and_sweatshirts_loc)
        jackets = self.find(loc.men_jackets_loc)
        tees = self.find(loc.men_tees_loc)
        pants = self.find(loc.men_pants_loc)
        shorts = self.find(loc.men_shorts_loc)
        assert hoodies_and_sweatshirts.is_enabled() and hoodies_and_sweatshirts.is_displayed()
        assert jackets.is_enabled() and jackets.is_displayed()
        assert tees.is_enabled() and tees.is_displayed()
        assert pants.is_enabled() and pants.is_displayed()
        assert shorts.is_enabled() and shorts.is_displayed()

    def verify_banner_images_load(self):
        wait = WebDriverWait(self.driver, 5)

        wait.until(project_ec.image_is_loaded(loc.shop_women_deals_loc))
        assert project_ec.image_is_loaded(loc.shop_women_deals_loc)
        assert project_ec.image_is_loaded(loc.shop_men_deals_loc)
        assert project_ec.image_is_loaded(loc.shop_luma_gear_loc)
