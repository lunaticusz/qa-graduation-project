import time
import pytest
from pages.basket_page import BasketPage
from pages.locators import BasePageLocators, LoginPageLocators, ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
    page.open()
    page.add_to_cart()
    page.should_be_added_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
    page.open()

    # Добавляем товар в корзину
    page.add_to_cart()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
    page.open()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, BasePageLocators.LOGIN_LINK)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
    page.open()

    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()

    # Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()

    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        login_page.open()
        login_page.should_be_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = "F34SEsesc#2"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
        page.open()

        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PROMO_LINK)
        page.open()
        page.add_to_cart()
        page.should_be_added_to_cart()
