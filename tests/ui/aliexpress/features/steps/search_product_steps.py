import logging

from behave import step

from tests.ui.aliexpress.page_objects.product_details_page import ProductDetailsPage
from tests.ui.aliexpress.page_objects.search_result_page import SearchResultPage


@step('I search for "{product}" product')
def search_for(context, product):
    logging.info('Searching for product: "{0}"'.format(product))
    search_result_driver = context.current_page.search_product(product)
    context.current_page = SearchResultPage(search_result_driver)


@step('I click on "{view_option}" view option')
def click_on_view_option(context, view_option):
    search_result_page = context.current_page
    search_result_page.click_on_view_option_btn(view_option)


@step('I select the result page number "{page_number:d}"')
def select_page_result(context, page_number):
    if page_number < 1:
        raise RuntimeError('Page number shall be greater than 1')
    search_result_page = context.current_page
    search_result_page.select_page(page_number)


@step('I click on the product number "{product_number:d}" of the current result page')
def click_on_product(context, product_number):
    search_result_page = context.current_page
    context.selected_product_title = search_result_page.get_product_title(product_number)
    product_details_driver = search_result_page.select_product(product_number)
    logging.info('Selected product title (search result): {0}'.format(context.selected_product_title))
    context.current_page = ProductDetailsPage(driver=product_details_driver)
