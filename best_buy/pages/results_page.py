from best_buy.pages import Page
from selenium.webdriver.common.by import By


class ResultsPage(Page):
    HEADER_TEXT = (By.XPATH, "//h1[@class='search-title']")

    def verify_header_result(self, expected_text: str):
        # wait for header message appear
        self.wait_for_element_appear(*self.HEADER_TEXT)
        self.verify_element_text(expected_text, *self.HEADER_TEXT)
