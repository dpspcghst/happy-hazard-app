# -*- coding: utf-8 -*-

"""
random.org clone
~~~~~~~~~~~~~~~~~~~

A basic clone of random.org.

:copyright: © 2021-present demiurge
:license: MIT, see LICENSE for more details.

"""

__title__ = "random.org-clone"
__author__ = "deepspaceghost"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present demiurge"
__version__ = "0.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging

from collections import namedtuple

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=0, minor=0, micro=0, releaselevel="in development", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
