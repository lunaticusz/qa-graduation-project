# Команда для запуска:
# pytest -v --tb=line --language=en test_main_page.py
# pytest -v --tb=line --language=en -m login_guest test_main_page.py
import pytest
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()

    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()

    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()

    # Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()

    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()
