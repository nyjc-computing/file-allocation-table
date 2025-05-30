"""filesystem.py
This module holds error classes used by filesystem.py.

Errors
------
- DiskFullError
- InsufficientDiskSpace
- FileNotFoundError
"""
__all__ = ['DiskFullError', 'FileNotFoundError', 'InsufficientDiskSpace']

class DiskFullError(Exception):
    """Raised when the disk has been fully filled."""


class FileNotFoundError(Exception):
    """Raised when a filename cannot be found in the
    file allocation table.
    """


class InsufficientDiskSpace(Exception):
    """Raised when attempting to store more data than available
    disk space.
    """
