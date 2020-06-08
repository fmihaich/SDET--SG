from selenium.webdriver.common.by import By

from tests.ui.aliexpress.page_objects.base_aliexpress_page import BaseAliexpressPage
from tests.ui.aliexpress.utils.decorators import close_new_user_discount


class ProductDetailsPage(BaseAliexpressPage):
    product_title_locator = (By.XPATH, '//h1[@class="product-title-text"]')
    product_availability_locator = (By.XPATH, '//div[@class="product-quantity-tip"]')

    def __init__(self, driver):
        close_user_discount_btn_locator = (By.XPATH, '//a[@class="next-dialog-close"]')
        super().__init__(driver, close_user_discount_locator=close_user_discount_btn_locator)

    @close_new_user_discount
    def get_product_description(self):
        return self.get_element_text(locator=self.product_title_locator)

    @close_new_user_discount
    def get_product_available_units(self):
        available_product_text = self.get_element_text(locator=self.product_availability_locator)
        # Text example: "74120 pieces available"
        product_count = available_product_text.split(' ')[0]
        return int(product_count)
