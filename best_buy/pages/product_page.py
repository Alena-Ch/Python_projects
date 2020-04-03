from best_buy.pages import Page
import selenium.webdriver.common.by


class ProductPage(Page):
    ROUTER = (
        selenium.webdriver.common.by.By.XPATH,
        "//a[text()='NETGEAR - Nighthawk Dual-Band AC1900 Router with 24 x 8 DOCSIS 3.0 Cable Modem - Black']")
    REVIEWS = (selenium.webdriver.common.by.By.XPATH, "//span[text()='Reviews']")
    WRITE_REVIEW_BUTTON = (selenium.webdriver.common.by.By.XPATH, "//a[@class='btn btn-secondary v-medium write-a-review']")

    SMART_WATCH = (selenium.webdriver.common.by.By.XPATH, "//ol[@class='sku-item-list']//li[@class='sku-item'][1]//h4[@class='sku-header']/a")
    # or
    # SMART_WATCH =(By.CSS_SELECTOR, "#main-results .sku-item-list .sku-item:nth-child(2) .sku-title a")

    ADD_TO_CART = (selenium.webdriver.common.by.By.XPATH, "//button[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']")
    ALERT = (selenium.webdriver.common.by.By.XPATH, "//div[@class='c-modal-grid col-xs-10']")

    GO_TO_CART_LINK = (selenium.webdriver.common.by.By.XPATH, "//span[@class='cart-nav-text'] ")
    PROMPT_WINDOW = (selenium.webdriver.common.by.By.XPATH, "//div[@class='c-modal-grid col-xs-10']")
    ITEM_COUNT_TEXT = (selenium.webdriver.common.by.By.XPATH, "//span[@class='item-count']")
    ITEM_LIST = (selenium.webdriver.common.by.By.XPATH, "//ol[@class='sku-item-list']")

    def click_on_product(self):
        self.click(*self.ROUTER)

    def click_on_reviews(self):
        self.click(*self.REVIEWS)

    def click_on_product_link(self):
        self.click(*self.SMART_WATCH)

    def click_on_add_to_cart_button(self):
        self.wait_for_element_appear(*self.ADD_TO_CART)
        self.click(*self.ADD_TO_CART)
        # close prompt window
        self.find_element(*self.PROMPT_WINDOW)
        self.wait_for_element_click(*self.GO_TO_CART_LINK)

    def verify_review_button(self, expected_text: str):
        self.wait_for_element_located(*self.WRITE_REVIEW_BUTTON)
        self.verify_element_text(expected_text, *self.WRITE_REVIEW_BUTTON)

    def print_suggestions(self, text: str):
        self.print_element_text(text, *self.ITEM_COUNT_TEXT)

    def wait_for_suggestions(self):
        self.wait_for_element_located(*self.ITEM_LIST)

    def count_and_print_suggestions(self):
        self.print_number_of_list_elements(*self.ITEM_LIST)
