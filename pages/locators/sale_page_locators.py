from selenium.webdriver.common.by import By


women_hoodies_and_sweatshirts_loc = (
    By.XPATH, "//a[contains(@href, '/hoodies-and-sweatshirts-women.html') and contains(text(), "
              "'Hoodies and Sweatshirts')]"
)
women_jackets_loc = (
    By.XPATH, "//a[contains(@href, '/jackets-women.html') and contains(text(), 'Jackets')]"
)
women_tees_loc = (By.XPATH, "//a[contains(@href, '/tees-women.html') and contains(text(), 'Tees')]")
women_bras_tanks_loc = (By.XPATH, "//a[contains(@href, '/tanks-women.html') and contains(text(), 'Bras & Tanks')]")
women_pants_loc = (By.XPATH, "//a[contains(@href, '/pants-women.html') and contains(text(), 'Pants')]")
women_shorts_loc = (By.XPATH, "//a[contains(@href, '/shorts-women.html') and contains(text(), 'Shorts')]")

men_hoodies_and_sweatshirts_loc = (
    By.XPATH, "//a[contains(@href, '/hoodies-and-sweatshirts-men.html') and contains(text(), "
              "'Hoodies and Sweatshirts')]"
)
men_jackets_loc = (By.XPATH, "//a[contains(@href, '/jackets-men.html') and contains(text(), 'Jackets')]")
men_tees_loc = (By.XPATH, "//a[contains(@href, '/tees-men.html') and contains(text(), 'Tees')]")
men_pants_loc = (By.XPATH, "//a[contains(@href, '/pants-men.html') and contains(text(), 'Pants')]")
men_shorts_loc = (By.XPATH, "//a[contains(@href, '/shorts-men.html') and contains(text(), 'Shorts')]")

shop_women_deals_loc = (By.CSS_SELECTOR, "img[src*='/pub/media/wysiwyg/sale/sale-main.jpg']")
shop_men_deals_loc = (By.CSS_SELECTOR, "img[src*='/pub/media/wysiwyg/sale/sale-mens.jpg']")
shop_luma_gear_loc = (By.CSS_SELECTOR, "img[src*='/pub/media/wysiwyg/sale/sale-gear.jpg']")
