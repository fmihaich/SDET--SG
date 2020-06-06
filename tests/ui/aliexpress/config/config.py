import logging
import os

from configparser import ConfigParser
from os.path import abspath, dirname

DEFAULT_SUIT_ENV = "PDR_DOCKER"


def get_config():
    env = os.getenv("TEST_ENV", DEFAULT_SUIT_ENV)
    config_dir = abspath(dirname(__file__))
    config_file_path = os.path.join(config_dir, "{0}.cfg".format(env.upper()))

    if not os.path.exists(config_file_path):
        raise RuntimeError('Config file does not exist: "{0}"'.format(config_file_path))

    config = ConfigParser()
    config.read(config_file_path)
    return config
