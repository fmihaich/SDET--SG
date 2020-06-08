from selenium.webdriver.common.by import By

from tests.ui.aliexpress.config.config import get_config
from tests.ui.aliexpress.utils.decorators import close_new_user_discount
from tests.ui.aliexpress.page_objects.base_aliexpress_page import BaseAliexpressPage
from tests.ui.aliexpress.page_objects.search_result_page import SearchResultPage


class AliexpressHomePage(BaseAliexpressPage):
    url = get_config().get('aliexpress', 'host')
    search_input_locator = (By.ID, 'search-key')
    search_btn_locator = (By.XPATH, '//input[@class="search-button"]')

    def __init__(self, driver):
        close_user_discount_btn_locator = (By.XPATH, '//div[@class="ui-window-content"]/a')
        super().__init__(driver, close_user_discount_locator=close_user_discount_btn_locator)

    @close_new_user_discount
    def search_product(self, product):
        self.fill_textbox(locator=self.search_input_locator, text_input=product)
        return self.click_on_search()

    def click_on_search(self):
        self.click_on(locator=self.search_btn_locator)
        self.wait_until_loaded(locator=SearchResultPage.search_container_locator)
        return self.driver
