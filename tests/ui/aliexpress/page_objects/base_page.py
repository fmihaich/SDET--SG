from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator))
        btn = driver.find_element(*locator)
        btn.click()

    def wait_until_loaded(self, locator, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def get_web_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_web_elements(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located(locator))
        return self.driver.find_elements(*locator)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
