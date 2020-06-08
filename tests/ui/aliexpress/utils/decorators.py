import functools
import logging

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


def close_new_user_discount(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except (ElementClickInterceptedException, TimeoutException):
            logging.warning('Caught an exception in {0}'.format(f.__name__))
            ali_express_page = args[0]
            ali_express_page.close_discount()
            return f(*args, **kwargs)
    return func
