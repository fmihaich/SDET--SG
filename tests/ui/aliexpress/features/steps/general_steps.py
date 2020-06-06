import logging
from behave import step

from tests.ui.aliexpress.page_objects.aliexpress_home_page import AliexpressHomePage


@step('I navigate to Aliexpress home page')
def navigate_to_aliexpress_page(context):
    aliexpress_url = AliexpressHomePage.url
    logging.info('Aliexpress home page URL: "{0}"'.format(aliexpress_url))
    context.browser = context.browser.go_to(aliexpress_url)
    context.current_page = AliexpressHomePage(context.browser)
