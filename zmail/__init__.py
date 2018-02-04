"""
zmail.__init__
~~~~~~~~~~~~
Zmail allows you to send and get email as possible as it can be.
"""
import logging
from .api import encode_mail, decode_mail, server
from .settings import __level__, __status__

# Define logger.
logger = logging.getLogger('zmail')

sh = logging.StreamHandler()
fmt = logging.Formatter('[%(levelname)s] %(message)s')
sh.setFormatter(fmt)
logger.addHandler(sh)

logger.setLevel(__level__)