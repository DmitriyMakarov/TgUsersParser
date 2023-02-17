# -*- coding: utf-8 -*-

import os.path
import logging
import shutil
from res.strings import error_messages


config_path = '../res/config/config.ini'
fconfig_path = '../res/examples/.src/fconfig'


init_logger = logging.getLogger(__name__)
init_logger.setLevel(logging.INFO)
init_logger_handler = logging.FileHandler(f'../logs/{__name__}.log', mode='w')
init_logger_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
init_logger_handler.setFormatter(init_logger_formatter)
init_logger.addHandler(init_logger_handler)
init_logger.info(f"Testing the custom logger for module {__name__}...")


def copy_config_example():
    shutil.copy(fconfig_path, '../fconfig')


def config_exist():
    try:
        config = open(config_path)
    except:
        init_logger.exception(error_messages.init_errors['noconfig_RU'])
        print(error_messages.init_errors['noconfig_RU'])
        copy_config_example()
        return False
    return True

print(config_exist())