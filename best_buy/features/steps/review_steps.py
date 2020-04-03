from behave import given, when, then


@when('Click on router')
def click_on_router(context):
    context.app.product_page.click_on_product()


@when('Click on "Reviews" button')
def click_on_reviews_button(context):
    context.app.product_page.click_on_reviews()


@then('User can see {text} button')
def verify_write_review_button(context, text):
    context.app.product_page.verify_review_button(text)
