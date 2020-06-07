import logging

from behave import step
from hamcrest import assert_that, contains_string, greater_than_or_equal_to


@step('I see the selected product details')
def check_current_product_details(context):
    product_details_page = context.current_page
    product_description = product_details_page.get_product_description()
    logging.info('Product description: {0}'.format(product_description))
    assert_that(product_description, contains_string(context.selected_product_title))


@step('I see there are at least "{product_count:d}" available product to buy')
def check_at_least_product_count(context, product_count):
    product_details_page = context.current_page
    available_units = product_details_page.get_product_available_units()
    logging.info('Available units: {0}'.format(available_units))
    assert_that(available_units, greater_than_or_equal_to(product_count))
