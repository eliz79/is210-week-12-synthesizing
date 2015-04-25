#! usr/bin/env python
# -*- coding: utf-8 -*-
"""A tree of class exceptions."""


class BaseError(Exception):
    """An exception class.
        Attributes:
            None
    """
    pass


class StringError(BaseError, TypeError):
    """An exception class.
        Attributes:
            None
    """
    pass


class NumberError(BaseError, TypeError):
    """An exception class.
        Attributes:
            None
    """
    pass


class NoneZeroError(NumberError):
    """An exception class.
        Attributes:
            None
    """
    pass
