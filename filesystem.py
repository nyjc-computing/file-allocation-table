"""filesystem.py
This module holds the file allocation table and the cluster data.

Errors
------
- DiskFullError
- FileNotFoundError
- InsufficientDiskSpace

Classes
-------
- FileEntry

Globals
-------
- table: list
  `table` is a Python list with 256 indexes, representing the
  file allocation table.
  Each element in `table` is an instance of the FileEntry class.
- HEAD: int
  The head of the free space linked list.
- TAIL: int
  The tail of the free space linked list.

Functions
--------
- is_full() -> bool
- disk_space() -> int
- save(filename, strdata) -> int
- load(filename) -> str
- delete(filename) -> None
"""

# Builtin imports
from dataclasses import dataclass

# Local imports
import disk
from error import (DiskFullError, FileNotFoundError, InsufficientDiskSpace)


@dataclass
class FileEntry:
    """Represents an entry in the file allocation table.
    No validation is done upon setting the attributes.
    """
    __slots__ = ('index', 'filename', 'cluster', 'size')
    index: int
    filename: str
    cluster: int
    size: int


# Initialise file allocation table
# Each entry.cluster points to the next entry, except the last entry
# which points to itself. Last entry should not be used.
table = []

# Indexes of head and tail of free space list
# Do not modify these constants.
HEAD = 0
TAIL = disk.ADDR_LIMIT


def _init():
    # Reset filesystem
    global table
    table = [
        FileEntry(index=i,
                  filename='',
                  cluster=i + (1 if i < disk.ADDR_LIMIT else 0),
                  size=0) for i in range(disk.ADDR_LIMIT + 1)
    ]


def _index_of(filename: str) -> int:
    """Searches for filename in the file allocation table.
    A linear search algorithm is used.
    
    Returns: [int] the entry index of the first cluster if found,
    otherwise returns TAIL
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


def _next_free() -> int:
    """Gets the index of the next free entry, and removes the entry
    from the free space list.
    
    Raises DiskFullError if disk is full.

    Returns: [int] index of next free entry in file allocation table
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


def disk_space() -> int:
    """Count the number of free clusters (excluding HEAD and TAIL).

    Returns the total free space in the clusters, in bytes.
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


def delete(filename: str) -> None:
    """Mark the clusters used by the file as freed.
    
    Raises FileNotFoundError if filename is not found.
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


def load(filename: str) -> str:
    """Load the data for filename from disk, and returns it
    as a string.
    
    Raises FileNotFoundError if filename is not found.

    Returns: [str] text data of file
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


def save(filename: str, strdata: str) -> int:
    """Save the file data to the disk as filename.
    
    Raises InsufficientDiskSpace if there is insufficient disk space,
    without writing the file to disk.
    
    Returns: [int] number of clusters used
    """
    # Remove the line below and write your code here
    raise NotImplementedError("function not implemented")


_init()