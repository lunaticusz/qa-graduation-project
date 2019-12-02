import pytest
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_added_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()

    # Добавляем товар в корзину
    page.add_to_cart()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()

    # Добавляем товар в корзину
    page.add_to_cart()

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, BasePageLocators.LOGIN_LINK)
    login_page.should_be_login_page()
