from behave import given, when, then


@when('Click on Sign In button')
def click_on_sign_in_button(context):
    context.app.main_page.click_sign_in_button()


@when('Click Sign In')
def click_on_sign_in_button(context):
    context.app.main_page.click_sign_in()
