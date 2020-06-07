import logging

from behave import step

from tests.ui.aliexpress.page_objects.search_result_page import SearchResultPage


@step('I search for "{product}" product')
def search_for(context, product):
    logging.info('Searching for product: "{0}"'.format(product))
    search_result_driver = context.current_page.search_product(product)
    context.current_page = SearchResultPage(search_result_driver)


@step('I click on "list" view option')
def click_on_view_option(context):
    search_result_page = context.current_page
    search_result_page.click_on_list_view()


@step('I click on "gallery" view option')
def click_on_gallery_option(context):
    search_result_page = context.current_page
    search_result_page.click_on_gallery_view()


@step('I select the result page number "{page_number:d}"')
def select_page_result(context, page_number):
    search_result_page = context.current_page
    search_result_page.scroll_to_bottom()
    search_result_page.click_on_page_number(page_number)


@step('I click on the product number "{product_number}" of the current result page')
def click_on_product(context, product_number):
    search_result_page = context.current_page
    search_result_page.select_product(product_number)
