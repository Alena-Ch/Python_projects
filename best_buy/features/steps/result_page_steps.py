from behave import then


@then('Search result for {product} is shown')
def verify_result(context, product):
    context.app.results_page.verify_header_result(product)


@then('Verify {title_text} page is opened')
def verify_SignIn_page(context, title_text):
    context.app.results_page.verify_SignIn_page_is_open(title_text)


@then('Suggestions for {product} are shown')
def verify_result(context, product):
    context.app.results_page.verify_header_result(product)



