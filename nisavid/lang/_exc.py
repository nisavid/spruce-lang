"""Exceptions."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import exceptions as _exceptions


class Error(RuntimeError):
    pass


class TypeError(_exceptions.TypeError, Error):

    def __init__(self, type, expected_type_displayname,
                 expected_type_description=None, message=None, *args):
        super(TypeError, self).__init__(type, expected_type_displayname,
                                        expected_type_description, message,
                                        *args)
        self._expected_type_displayname = expected_type_displayname
        self._expected_type_description = expected_type_description
        self._message = message
        self._type = type

    def __str__(self):
        message = 'invalid {} type {!r}'.format(self.expected_type_displayname,
                                                self.type)
        if self.message:
            message += ': ' + self.message
        if self.expected_type_description:
            message += '; expecting ' + self.expected_type_description
        return message

    @property
    def expected_type_displayname(self):
        return self._expected_type_displayname

    @property
    def expected_type_description(self):
        return self._expected_type_description

    @property
    def message(self):
        return self._message

    @property
    def type(self):
        return self._type


class ConversionTypeError(TypeError, Error):
    def __str__(self):
        message = 'cannot convert type {!r} to {}'\
                      .format(self.type, self.expected_type_displayname)
        if self.message:
            message += ': ' + self.message
        if self.expected_type_description:
            message += '; expecting ' + self.expected_type_description
        return message


class ValueError(_exceptions.ValueError, Error):

    def __init__(self, value, expected_type_displayname,
                 expected_value_description=None, message=None, *args):
        super(ValueError, self).__init__(value, expected_type_displayname,
                                         expected_value_description, message,
                                         *args)
        self._expected_type_displayname = expected_type_displayname
        self._expected_value_description = expected_value_description
        self._message = message
        self._value = value

    def __str__(self):
        message = 'invalid {} {!r}'.format(self.expected_type_displayname,
                                           self.value)
        if self.message:
            message += ': ' + self.message
        if self.expected_value_description:
            message += '; expecting ' + self.expected_value_description
        return message

    @property
    def expected_type_displayname(self):
        return self._expected_type_displayname

    @property
    def expected_value_description(self):
        return self._expected_value_description

    @property
    def message(self):
        return self._message

    @property
    def value(self):
        return self._value


class ConversionValueError(ValueError, Error):
    def __str__(self):
        message = 'cannot convert {!r} to {}'\
                      .format(self.value, self.expected_type_displayname)
        if self.message:
            message += ': ' + self.message
        if self.expected_value_description:
            message += '; expecting ' + self.expected_value_description
        return message
