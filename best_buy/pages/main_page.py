from best_buy.pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT_FIELD = (By.ID, "gh-search-input")
    SEARCH_ICON = (By.XPATH, "//button[@class='header-search-button']")
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='utility-navigation-list-item'][1]")
    SIGN_IN_BUTTON = (By.XPATH, "// button[@class='lam-signIn__button btn btn-secondary']")
    SING_IN = (By.XPATH,
               "// button[@class='btn btn-secondary btn-lg btn-block btn-leading-ficon cia-form__controls__submit '] ")
    LOGO_ICON = (By.XPATH, "//div[@class='bby-logo-lv']")
    CART_ICON = (By.XPATH, "//div[@class='bby-cart lv']")

    PROMPT_ALERT_DO_NOT_MISS_CLOSE_BUTTON = (By.XPATH, "//button[@class='close']")
    PROMPT_ALERT_DO_NOT_MISS = (
        By.XPATH, "//div[@class='modal fade email-submission-modal in']//div[@class='modal-content']")

    def open(self):
        self.open_page('https://www.bestbuy.com/')

    def search_product(self, text: str):
        # close the Prompt Alert------------------------------------
        self.wait_for_element_appear(*self.PROMPT_ALERT_DO_NOT_MISS)
        self.click(*self.PROMPT_ALERT_DO_NOT_MISS_CLOSE_BUTTON)
        # ----------------------------------------------------------

        self.input(text, *self.SEARCH_INPUT_FIELD)
        # self.wait_for_element_click(*self.SEARCH_ICON)
        self.wait_for_text_to_be_present_in_element_value(text, *self.SEARCH_INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_on_account_button(self):
        self.click(*self.ACCOUNT_BUTTON)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def click_sign_in(self):
        self.click(*self.SING_IN)

        # close the Prompt Alert------------------------------------
        self.wait_for_element_appear(*self.PROMPT_ALERT_DO_NOT_MISS)
        self.click(*self.PROMPT_ALERT_DO_NOT_MISS_CLOSE_BUTTON)
        # ----------------------------------------------------------

    def click_on_logo_icon(self):
        self.wait_for_element_located(*self.LOGO_ICON)
        self.click(*self.LOGO_ICON)