from best_buy.pages import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShoppingCartPage(Page):
    ADD_TO_CART_BUTTON = (
        By.XPATH, "//button[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']")
    SHOPPING_CART_MESSAGE = (By.XPATH, "//h2[@class='empty-cart__info-title']")
    SHOPPING_CART_ICON_DOT = (By.XPATH, "//div[@class='dot']")
    CHANGE_QUANTITY_BUTTON = (
        By.XPATH, "//div[@class='cart-item__quantity-block col-xs-1']//select[@class='c-dropdown v-medium']")

    def change_quantity_in_shopping_cart(self, option):
        self.wait_for_element_appear(*self.CHANGE_QUANTITY_BUTTON)
        select = Select(self.find_element(*self.CHANGE_QUANTITY_BUTTON))
        select.select_by_visible_text(option)

    def verify_shopping_cart_message(self, expected_text: str):
        self.verify_element_text(expected_text, *self.SHOPPING_CART_MESSAGE)

    def verify_shopping_cart_contain_product(self, expected_text: str):
        self.wait_for_element_appear(*self.SHOPPING_CART_ICON_DOT)
        self.click(*self.SHOPPING_CART_ICON_DOT)
        self.verify_element_text(expected_text, *self.SHOPPING_CART_ICON_DOT)
