from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def image_is_loaded(self, image):
        self.driver.execute_script(
            "return arguments[0].complete && typeof arguments[0]"
            ".naturalWidth != 'undefined' && arguments[0].naturalWidth > 0",
            image
        )
        return self.image_is_loaded(image)
