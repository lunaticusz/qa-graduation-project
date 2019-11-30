import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_added_to_cart()
