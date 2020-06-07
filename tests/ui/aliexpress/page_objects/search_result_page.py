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

    def move_to_page_selector(self):
        self.scroll_to_bottom()
        self.move_page_up()
        for _ in range(3):
            try:
                self.wait_until_clickable(locator=self.page_number_locator)
            except:
                self.move_page_up()

    @close_new_user_discount
    def click_on_page_number(self, page_number):
        page_number_buttons = self.get_web_elements(locator=self.page_number_locator)
        page_index = page_number - 1

        if page_index >= len(page_number_buttons):
            raise NotImplementedError(
                'Interaction with "Next Page" button is necessary to reach {0} page'.format(page_number))

        page_number_buttons[page_index].click()
        from time import sleep
        sleep(3)

    def select_product(self, product_number):
        windows_handler_count = len(self.get_window_handlers())
        second_product = self.get_web_element(self.second_product_locator)
        self.click_on(locator=self.product_link_locator, web_element=second_product)
        self.wait_until_window_handlers_greater_than(windows_handler_count)
        return self.switch_to_new_window()
