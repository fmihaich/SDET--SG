from tests.ui.aliexpress.page_objects.base_page import BasePage


class BaseAliexpressPage(BasePage):

    def __init__(self, driver, close_user_discount_locator):
        self.close_user_discount_locator = close_user_discount_locator
        super().__init__(driver)

    def close_new_user_discount(self):
        active_element = self.driver.switch_to.active_element
        self.click_on(locator=self.close_user_discount_locator, web_element=active_element)
