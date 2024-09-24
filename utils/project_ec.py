def image_is_loaded(locator):
    def _predicate(driver):
        image = driver.find_element(*locator)
        is_loaded = driver.execute_script(
            "return arguments[0].complete && "
            "typeof arguments[0].naturalWidth != 'undefined' && "
            "arguments[0].naturalWidth > 0",
            image
        )
        return is_loaded
    return _predicate
