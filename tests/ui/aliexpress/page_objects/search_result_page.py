from selenium.webdriver.common.by import By

from tests.ui.aliexpress.utils.decorators import close_new_user_discount
from tests.ui.aliexpress.page_objects.base_aliexpress_page import BaseAliexpressPage
from selenium.common.exceptions import ElementClickInterceptedException


DEFAULT_VIEW = "list"


class SearchResultPage(BaseAliexpressPage):
    search_container_locator = (By.XPATH, '//div[@class="product-container"]')
    view_option_btn_locator = (By.XPATH, '//*[contains(@class, "svg-icon m ")]')
    page_number_locator = (By.XPATH, '//div[@class="next-pagination-list"]/button')
    gallery_first_row_products_locator = (By.XPATH, '//ul[@class="list-items"]/div[1]/li')
    product_link_xpath = '//ul[@class="list-items"]/{view_div}li[{product_order}]//*/div[@class="item-title-wrap"]/a'

    def __init__(self, driver):
        self.current_view = DEFAULT_VIEW
        close_user_discount_btn_locator = (By.XPATH, '//a[@class="next-dialog-close"]')
        super().__init__(driver, close_user_discount_locator=close_user_discount_btn_locator)

    def close_discount(self):
        self.scroll_to_top()
        super().close_discount()

    @close_new_user_discount
    def click_on_view_option_btn(self, view_option):
        view_buttons = self.get_web_elements(locator=self.view_option_btn_locator)
        if not view_buttons:
            raise ElementClickInterceptedException()
        expected_view_btn = next((btn for btn in view_buttons if view_option in btn.get_attribute("innerHTML")), None)
        expected_view_btn.click()
        self.current_view = view_option
        first_product_link_locator = self._get_product_link_locator(product_number=1)
        self.wait_until_loaded(locator=first_product_link_locator)

    @close_new_user_discount
    def select_page(self, page_number):
        first_product_locator = self._get_product_link_locator(product_number=1)
        first_product = self.get_web_element(locator=first_product_locator)
        self._move_to_page_selector()
        self._click_on_page_number(page_number)
        self.wait_until_web_element_is_different(locator=first_product_locator, base_web_element=first_product)

    @close_new_user_discount
    def select_product(self, product_number):
        windows_handler_count = len(self.get_window_handlers())
        self.click_on(locator=self._get_product_link_locator(product_number))
        self.wait_until_window_handlers_greater_than(windows_handler_count)
        return self.switch_to_new_window()

    def get_product_title(self, product_number):
        return \
            self.get_element_attribute(locator=self._get_product_link_locator(product_number), attribute_name="title")

    def _move_to_page_selector(self):
        self.scroll_to_bottom()
        self.move_page_up()
        for _ in range(3):
            try:
                self.wait_until_clickable(locator=self.page_number_locator)
            except:
                self.move_page_up()

    def _click_on_page_number(self, page_number):
        page_number_buttons = self.get_web_elements(locator=self.page_number_locator)
        page_index = page_number - 1
        if page_index >= len(page_number_buttons):
            raise NotImplementedError(
                'Interaction with "Next Page" button is necessary to reach {0} page'.format(page_number))
        page_number_buttons[page_index].click()

    def _get_product_link_locator(self, product_number):
        if self.current_view != DEFAULT_VIEW:
            div_num, li_num = self._get_product_position_in_gallery(product_number)
            view_div = 'div[{0}]/'.format(div_num)
        else:
            view_div = ''
            li_num = product_number
        product_link_locator = (By.XPATH, self.product_link_xpath.format(view_div=view_div, product_order=li_num))
        return product_link_locator

    def _get_product_position_in_gallery(self, product_number):
        first_row_products = self.get_web_elements(locator=self.gallery_first_row_products_locator)
        row_product_count = len(first_row_products)
        div_num = int((product_number - 1)/row_product_count) + 1
        li_num = product_number % row_product_count if product_number % row_product_count != 0 else row_product_count
        return div_num, li_num
