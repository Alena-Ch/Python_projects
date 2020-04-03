from behave import given, when, then


@when('Choose product and click it')
def click_product(context):
    context.app.product_page.click_on_product_link()


@when('Add product to shopping cart')
def add_product_to_shopping_cart(context):
    context.app.product_page.click_on_add_to_cart_button()


@when('Change quantity from 1 to {option}')
def change_quantity_in_cart(context, option):
    context.app.shopping_cart_page.change_quantity_in_shopping_cart(option)


@then('User sees message {title_text}')
def verify_shopping_cart(context, title_text):
    context.app.shopping_cart_page.verify_shopping_cart_message(title_text)


@then('Verify cart contains {number} product')
def verify_cart_contain_product(context, number):
    context.app.shopping_cart_page.verify_shopping_cart_contain_product(number)


