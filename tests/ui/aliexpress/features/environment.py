import logging
import os
import shutil

from time import time

from tests.ui.aliexpress.config.config import get_config
from tests.ui.aliexpress.utils.browser import Browser, DEFAULT_BROWSER


def before_all(context):
    suite_config = get_config()
    browser_name = os.getenv('BROWSER', DEFAULT_BROWSER).lower()
    context.suit_output_dir = os.path.join(os.path.abspath(suite_config.get('output', 'path')), browser_name)
    _create_directory(dir_path=context.suit_output_dir)

    context.config.setup_logging(filename=os.path.join(context.suit_output_dir, suite_config.get('log', 'file_name')),
                                 format='%(asctime)s [%(levelname)s] - %(message)s',
                                 level=suite_config.get('log', 'level'))
    logging.info('-------------------- TEST SUITE INITIALIZED --------------------\n')


def before_feature(context, feature):
    logging.info('-------------------- BEFORE FEATURE --------------------')
    logging.info('Feature: {0}'.format(feature.name))
    logging.info('---------------------------------------------------------\n')


def before_scenario(context, scenario):
    logging.info('-------------------- BEFORE SCENARIO --------------------')
    logging.info('Scenario: {0}'.format(scenario.name))
    logging.info('---------------------------------------------------------\n')

    scenario_dir_name = scenario.name.replace(' ', '_')
    context.scenario_dir = os.path.join(os.path.abspath(context.suit_output_dir), scenario_dir_name)
    _create_directory(dir_path=context.scenario_dir)

    context.browser = Browser()


def after_step(context, step):
    context.browser.get_screenshot_as_file(
        os.path.join(context.scenario_dir, "{}_{}.png".format(int(time()), step.name.replace(' ', '_'))))


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.browser.save_screenshot(
            os.path.join(context.scenario_dir, "{}_{}_failed.png".format(int(time()), scenario.name.replace(' ', '_'))))

    if hasattr(context, "browser"):
        context.browser.close()


def _create_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, ignore_errors=True)
    os.makedirs(dir_path)
