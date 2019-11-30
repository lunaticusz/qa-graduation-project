from pages.locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_be_button_add_to_cart()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button 'Add to basket' is not presented"

    def should_be_added_to_cart(self):
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        assert self.is_element_present(*ProductPageLocators.TITLE_IN_PRODUCT_INFO), "Product title is not presented in product info"
        assert self.is_element_present(*ProductPageLocators.TITLE_IN_SUCCESS_MESSAGE), "Message with title is not presented"

        title_in_product_info = self.get_element_text(*ProductPageLocators.TITLE_IN_PRODUCT_INFO)
        title_in_success_message = self.get_element_text(*ProductPageLocators.TITLE_IN_SUCCESS_MESSAGE)
        assert title_in_product_info == title_in_success_message, "Product title is not correct in success message"

        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_PRODUCT_INFO), "Product price is not presented in product info"
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_SUCCESS_MESSAGE), "Message with price is not presented"

        price_in_product_info = self.get_element_text(*ProductPageLocators.PRICE_IN_PRODUCT_INFO)
        price_in_success_message = self.get_element_text(*ProductPageLocators.PRICE_IN_SUCCESS_MESSAGE)
        assert price_in_product_info == price_in_success_message, "Product price is not correct in success message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TITLE_IN_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.TITLE_IN_SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
