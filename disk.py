############################### 72 chars ###############################
"""disk.py
This module simulates the operations that can be performed on a disk.

Errors
------
- InvalidAddressError
- InvalidDataError
- ClusterSizeExceededError

Constants
---------
- ZERO
  The byte representing zero

Functions
---------
- write(addr, data)
- read(addr) -> data

Each element in `_storage` represents a cluster that holds part of a file
(simulated here as bytes) with a maximum size of 256 bytes.
"""

ADDR_LIMIT = 255
CLUSTER_SIZE = 256
ZERO = bytes('\0', "ascii")


class DiskError(Exception):
    """Base class for all disk errors."""


class InvalidAddressError(DiskError):
    """Raised when an invalid address is used for reading or writing."""


class InvalidDataError(DiskError):
    """Raised when invalid data is passed for writing."""


class ClusterSizeExceededError(DiskError):
    """Raised when the data written to the cluster exceeds its size."""


# The storage object here is meant to be mutated using functions
# in this module only. It should not be mutated by other functions.
# Initialise storage with 0s
_storage = [(ZERO * CLUSTER_SIZE) for i in range(CLUSTER_SIZE)]


def _rightpad(data: bytes, padchar: bytes = ZERO) -> bytes:
    """Pad data with padchar until it reaches CLUSTER_SIZE.

    Raises ClusterSizeExceededError if data is already longer than
    CLUSTER_SIZE.

    Returns: [bytes] the padded data
    """
    padsize = CLUSTER_SIZE - len(data)
    return data + padchar * padsize


def write(addr: int, data: bytes) -> None:
    """Writes the data to the cluster at address addr.

    Raises InvalidAddressError if addr is invalid.

    Raises InvalidDataError if data is not bytes.

    Raises ClusterSizeExceededError if data exceeds cluster size.
    """
    if addr < 0 or addr > ADDR_LIMIT:
        raise InvalidAddressError(f"[{addr}]: Not a valid address")
    if not isinstance(data, bytes):
        raise InvalidDataError(f"expected bytes, not {type(data)}")
    if len(data) > CLUSTER_SIZE:
        breakpoint()
        raise ClusterSizeExceededError("Data too large")
    _storage[addr] = _rightpad(data)


def read(addr: int) -> bytes:
    """Read the data from the cluster at address addr.

    Raises InvalidAddressError if addr is invalid.
    
    Returns: [bytes] The data read from the cluster at addr.
    """
    if addr < 0 or addr > ADDR_LIMIT:
        raise InvalidAddressError(f"[{addr}]: Not a valid address")
    return _storage[addr]
