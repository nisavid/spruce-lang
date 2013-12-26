"""String converters."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

from . import _core as _converters_core


@_converters_core.converter('hexadecimal integer')
def hex_int(value):
    return int(value, base=16)


@_converters_core.converter('string')
def string(value):
    return unicode(value)
