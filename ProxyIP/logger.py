#!/usr/bin/env python
# coding=utf-8

import logging


def get_logger():
    """
    create log instance
    """
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    logger = logging.getLogger("monitor")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = get_logger()
