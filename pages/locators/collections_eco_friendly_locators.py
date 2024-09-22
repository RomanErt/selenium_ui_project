from selenium.webdriver.common.by import By

first_item_loc = (By.XPATH, '//*[@class="product-item-link"][1]')
compare_button_loc = (By.XPATH, '//*[@class="action tocompare"][1]')
item_in_compare_products_loc = (By.CSS_SELECTOR, "a.product-item-link[data-bind*='href: product_url']")
you_added_item_banner_loc = (By.CSS_SELECTOR, ".message-success.success.message")

first_product_image_loc = (By.XPATH, '//*[@class="product-image-photo"]')
fifth_product_image_loc = (By.XPATH, '(//*[@class="product-image-photo"])[5]')

erin_recommends_loc = (By.XPATH, '(//*[@class="filter-options-title"])[7]')
erin_recommends_yes_loc = (By.XPATH, "//a[contains(@href, '/collections/eco-friendly.html?erin_recommends=1')]")
erin_recommends_no_loc = (By.XPATH, "//a[contains(@href, '/collections/eco-friendly.html?erin_recommends=0')]")
