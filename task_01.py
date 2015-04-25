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


class NonZeroError(NumberError):
    """An exception class.
        Attributes:
            None
    """
    pass
