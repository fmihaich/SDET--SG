from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_textbox(self, locator, text_input):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        textbox = self.driver.find_element(*locator)
        textbox.click()
        textbox.clear()
        textbox.send_keys(text_input)

    def click_on(self, locator, web_element=None):
        driver = web_element if web_element else self.driver
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))
        btn = driver.find_element(*locator)
        btn.click()

    def get_element_text(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text.strip()

    def get_element_attribute(self, locator, attribute_name, web_element=None):
        element = self.get_web_element(locator, web_element)
        return element.get_attribute(name=attribute_name)

    def wait_until_loaded(self, locator, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def wait_until_clickable(self, locator, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))

    def get_web_element(self, locator, web_element=None):
        driver = web_element if web_element else self.driver
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
        return driver.find_element(*locator)

    def get_web_elements(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located(locator))
        return self.driver.find_elements(*locator)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def move_page_up(self):
        body = self.driver.find_element_by_css_selector('body')
        body.click()
        body.send_keys(Keys.PAGE_UP)

    def get_window_handlers(self):
        return self.driver.window_handles

    def wait_until_window_handlers_greater_than(self, handlers_count):
        for _ in range(40):
            windows_handlers = self.get_window_handlers()
            if len(windows_handlers) > handlers_count:
                return
            sleep(0.25)
        raise TimeoutError('New element was not loaded')

    def wait_until_web_element_is_different(self, locator, base_web_element):
        for _ in range(40):
            current_web_element = self.get_web_element(locator)
            if current_web_element != base_web_element:
                return
            sleep(0.25)
        raise TimeoutError('New element was not loaded\nPage url: {0}'.format(self.driver.current_url))

    def switch_to_new_window(self):
        new_window = self.get_window_handlers()[-1]
        self.driver.switch_to.window(new_window)
        return self.driver
