"""Converters miscellany."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import __builtin__

from . import _core as _converters_core


@_converters_core.converter('boolean value')
def bool(value):
    return __builtin__.bool(value)
