import pytest
from selenium import webdriver
from pages.sale_page import SalePage
from pages.customer_account_create import CustomerAccountCreate
from pages.collections_eco_friendly import CollectionsEcoFriendly


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def customer_account_create(driver):
    return CustomerAccountCreate(driver)


@pytest.fixture()
def collections_eco_friendly(driver):
    return CollectionsEcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
