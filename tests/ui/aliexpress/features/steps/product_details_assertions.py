from behave import step
from hamcrest import assert_that, greater_than_or_equal_to


@step('I see there are at least "{product_count:d}" available product to buy')
def check_at_least_product_count(context, product_count):
    product_details_page = context.current_page
    available_units = product_details_page.get_product_available_units()
    assert_that(available_units, greater_than_or_equal_to(product_count))
