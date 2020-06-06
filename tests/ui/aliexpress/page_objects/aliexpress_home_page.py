from tests.ui.aliexpress.config.config import get_config
from tests.ui.aliexpress.page_objects.base_page import BasePage


class AliexpressHomePage(BasePage):
    url = get_config().get('aliexpress', 'host')
