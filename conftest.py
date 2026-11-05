import pytest
from utils.test_data import generate_customer_data

BASE_URL = "https://demo.guru99.com/telecom/index.html"

@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage
    page.goto(BASE_URL)
    return HomePage(page)

@pytest.fixture
def customer_page(home_page):
    from pages.customer_page import CustomerPage
    home_page.click_add_customer()
    return CustomerPage(home_page.page)

@pytest.fixture
def customer_data(home_page):
    return generate_customer_data()

