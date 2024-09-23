def test_item_added_to_comparison_success(collections_eco_friendly):
    collections_eco_friendly.open_page()
    collections_eco_friendly.add_item_to_compare()
    collections_eco_friendly.verify_item_successfully_added_to_compare()


def test_product_images_loaded(collections_eco_friendly):
    collections_eco_friendly.open_page()
    collections_eco_friendly.verify_product_images_load()


def test_erin_recommends_shopping_options(collections_eco_friendly):
    collections_eco_friendly.open_page()
    collections_eco_friendly.click_erin_recommends_menu_option()
    collections_eco_friendly.verify_erin_recommends_submenu_options_clickable()
