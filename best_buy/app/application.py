
from best_buy.pages.main_page import MainPage
from best_buy.pages.product_page import ProductPage
from best_buy.pages.registration_page import RegistrationPage
from best_buy.pages.results_page import ResultsPage
from best_buy.pages.shopping_cart_page import ShoppingCartPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)

        self.results_page = ResultsPage(self.driver)

        self.registration_page = RegistrationPage(self.driver)

        self.shopping_cart_page = ShoppingCartPage(self.driver)

        self.product_page = ProductPage(self.driver)
