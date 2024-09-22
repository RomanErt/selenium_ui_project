def test_women_deals_categories_are_clickable(sale_page):
    sale_page.open_page()
    sale_page.verify_women_deals_categories_clickable()


def test_men_deals_categories_are_clickable(sale_page):
    sale_page.open_page()
    sale_page.verify_men_deals_categories_clickable()


def test_banner_images_loaded(sale_page):
    sale_page.open_page()
    sale_page.verify_banner_images_load()
