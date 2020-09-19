from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_element_text(self, *locator):
        self.driver.find_element(*locator).text

    def print_element_text(self, text: str, *locator):
        e = self.driver.find_element(*locator).text
        print(e)

    def print_number_of_list_elements(self, *locator):
        e = self.driver.find_elements(*locator)
        print(len(e))

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_located(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_text_to_be_present_in_element_value(self, text, *locator):
        self.driver.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    def verify_items_in_list(self, expected_text: str, *locator):
        actual_text = self.driver.find_elements(*locator)
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_element_count(self, expected_value: int, *locator):
        actual_value = int(len(self.driver.find_elements(*locator)))
        assert actual_value == expected_value, f'Expected {expected_value} elements, but got {actual_value} elements'

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'





