from selenium.webdriver.common.by import By

from tests.ui.aliexpress.utils.decorators import close_new_user_discount
from tests.ui.aliexpress.page_objects.base_aliexpress_page import BaseAliexpressPage
from selenium.common.exceptions import ElementClickInterceptedException


class SearchResultPage(BaseAliexpressPage):
    search_container_locator = (By.XPATH, '//div[@class="product-container"]')
    view_option_btn_locator = (By.XPATH, '//*[contains(@class, "svg-icon m ")]')
    page_number_locator = (By.XPATH, '//div[@class="next-pagination-list"]/button')
    second_product_locator = (By.XPATH, '//ul[@class="list-items"]/div[1]/li[@class="list-item"][2]')
    product_link_locator = (By.XPATH, '//div[@class="item-title-wrap"]/a')

    def __init__(self, driver):
        close_user_discount_btn_locator = (By.XPATH, '//a[@class="next-dialog-close"]')
        super().__init__(driver, close_user_discount_locator=close_user_discount_btn_locator)

    def click_on_list_view(self):
        self.click_on_view_option_btn(view_option='iconlist')

    def click_on_gallery_view(self):
        self.click_on_view_option_btn(view_option='icongallery')

    @close_new_user_discount
    def click_on_view_option_btn(self, view_option):
        view_buttons = self.get_web_elements(locator=self.view_option_btn_locator)
        if not view_buttons:
            raise ElementClickInterceptedException()
        expected_view_btn = next((btn for btn in view_buttons if view_option in btn.get_attribute("innerHTML")), None)
        expected_view_btn.click()
        from time import sleep
        sleep(3)

    @close_new_user_discount
    def click_on_page_number(self, page_number):
        if page_number < 1:
            raise RuntimeError('Page number shall be greater than 1')
        page_number_buttons = self.get_web_elements(locator=self.page_number_locator)
        page_index = page_number - 1

        if page_index >= len(page_number_buttons):
            raise NotImplementedError(
                'Interaction with "Next Page" button is necessary to reach {0} page'.format(page_number))

        page_number_buttons[page_index].click()
        from time import sleep
        sleep(5)

    def select_product(self, product_number):
        second_product = self.get_web_element(self.second_product_locator)
        self.click_on(locator=self.product_link_locator, web_element=second_product)
        from time import sleep
        sleep(3)
