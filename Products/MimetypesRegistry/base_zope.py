"""some common utilities
"""

FB_REGISTRY = None

# base class
from ExtensionClass import Base
from Acquisition import aq_base

# logging function
import logging

logger = logging.getLogger('PortalTransforms')

def log(msg, severity=logging.INFO, id='PortalTransforms'):
    logger.log(severity, msg)

# directory where template for the ZMI are located
import os.path
_www = os.path.join(os.path.dirname(__file__), 'www')
skins_dir = os.path.join(os.path.dirname(__file__), 'skins')

# list and dict classes to use
from Globals import PersistentMapping as DictClass
try:
    from ZODB.PersistentList import PersistentList as ListClass
except ImportError:
    from persistent.list import PersistentList as ListClass

from Interface import Interface, Attribute

def implements(object, interface):
    return interface.isImplementedBy(object)

from zExceptions import BadRequest

__all__ = ('Base', 'log', 'DictClass', 'ListClass', 'aq_base',
           'Interface', 'Attribute', 'implements', 'skins_dir', '_www',
           'BadRequest', )
