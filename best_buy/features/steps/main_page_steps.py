from behave import given, when


@given('Open Best Buy main page')
def open_best_buy_main_page(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)


@when('Click account button')
def click_account_button(context):
    context.app.main_page.click_on_account_button()


@when('Click cart icon')
def click_cart_icon(context):
    context.app.main_page.click_on_cart_icon()


@when('Return to product search page')
def return_to_product_search_page(context):
    context.app.main_page.click_on_logo_icon()


@when('Print {product} number')
def print_suggestions_number(context, product):
    context.app.product_page.print_suggestions(product)


@when('Wait for product suggestions')
def wait_for_product_suggestions(context,):
    context.app.product_page.wait_for_suggestions()


@when('Count suggestions')
def count_suggestions(context,):
    context.app.product_page.count_and_print_suggestions()

