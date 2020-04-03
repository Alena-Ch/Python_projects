from best_buy.pages.base_page import Page
from selenium.webdriver.common.by import By


class RegistrationPage(Page):
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='am-create-account__button btn btn-tertiary']")
    FIRST_NAME = (By.ID, "fld-firstName")
    LAST_NAME = (By.ID, "fld-lastName")
    EMAIL = (By.ID, "fld-e")
    PASSWORD = (By.ID, "fld-p1")
    CONFIRM_PASSWORD = (By.ID, "fld-p2")
    PHONE_NUMBER = (By.ID, "fld-phone")
    CREATE_AN_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, "//button[@class='cia-form__submit-button js-submit-button']")
    HI_USER_TEXT = (By.XPATH, "//span[@class='flyBtn logged_user_name']")
    USER_NAME_BUTTON = (By.XPATH, "//div[@class='BtnTxt']")

    def click_on_create_account_button(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)

    def enter_frst_name(self, text: str):
        self.input(text, *self.FIRST_NAME)

    def enter_lst_name(self, text: str):
        self.input(text, *self.LAST_NAME)

    def enter_email(self, text: str):
        self.input(text, *self.EMAIL)

    def enter_password(self, text: str):
        self.input(text, *self.PASSWORD)

    def enter_confirm_password(self, text: str):
        self.input(text, *self.CONFIRM_PASSWORD)

    def enter_phone_number(self, text: str):
        self.input(text, *self.PHONE_NUMBER)

    def click_submit_button(self):
        self.click(*self.CREATE_AN_ACCOUNT_SUBMIT_BUTTON)

    def verify_header_result(self, expected_text: str):
        self.wait_for_element_appear(*self.USER_NAME_BUTTON)
        self.verify_element_text(expected_text, *self.HI_USER_TEXT)
