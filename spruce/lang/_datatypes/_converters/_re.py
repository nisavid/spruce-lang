"""Regular expression converters."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import re as _re

from . import _core as _converters_core


@_converters_core.converter('regular expression')
def regex(value):
    return _re.compile(value)
