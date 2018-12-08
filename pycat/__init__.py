import pkg_resources
__version__ = pkg_resources.require("pycat")[0].version

from .pycat import *
