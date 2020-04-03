from behave import given, when, then


@when('Click "Create account"')
def click_create_account_button(context):
    context.app.registration_page.click_on_create_account_button()


@when('Enter {data} in First name field')
def enter_first_name(context, data):
    context.app.registration_page.enter_frst_name(data)


@when('Enter {data} in Last name field')
def enter_first_name(context, data):
    context.app.registration_page.enter_lst_name(data)


@when('Enter {data} in Email address field')
def enter_Email(context, data):
    context.app.registration_page.enter_email(data)


@when('Enter {data} in Passwords field')
def enter_Password(context, data):
    context.app.registration_page.enter_password(data)


@when('Enter {data} in Confirm Password field')
def confirm_Password(context, data):
    context.app.registration_page.enter_confirm_password(data)


@when('Enter {data} in Phone Number field')
def enter_phone_number(context, data):
    context.app.registration_page.enter_phone_number(data)


@when('Click submit')
def click_submit(context):
    context.app.registration_page.click_submit_button()


@then('User can see message {title_text}')
def verify_successfully_registration(context, title_text):
    context.app.registration_page.verify_header_result(title_text)
