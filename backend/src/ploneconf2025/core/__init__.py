"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "20251014.0"

PACKAGE_NAME = "ploneconf2025.core"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
