from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from best_buy.app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    # context.driver = webdriver.Firefox(executable_path='drivers/geckodriver')
    # context.driver = webdriver.Safari()
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)
    context.wait = WebDriverWait(context, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()