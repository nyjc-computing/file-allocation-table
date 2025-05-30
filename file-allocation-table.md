# Background

Computer memory is volatile; any data left in memory is lost when the computer is restarted. Data that is to be retained across restarts must be stored in permanent storage media, such as a hard disk.

A hard disk, in a computer system, is organised into clusters, each storing a certain amount of data. For example, a 4 GiB hard disk stores 4,294,967,296 bytes, which can be grouped into 4,194,304 clusters of 1 KiB each.

## Hard disk operations

The hard disk is a simple device, essentially only supporting two operations: **read** and **write**. It writes a whole cluster at a go, and reads a whole cluster at a go; partial reads and writes are not possible.

    Simulation in Python of writing data for the string
    "Hello" to cluster 5:

    >>> disk.write(5, "Hello".encode("ascii")
    >>> disk.read(5)
    b'Hello\x00\x00\x00\x00\x00 ... <to end of cluster data>'

However, the hard disk does not carry out any organising of files or directories; the disk has no concept of files or filenames, only clusters and bytes.

## Filesystems

The operating system (OS) must manage the translation from files and filenames to clusters and bytes, through a program called a **filesystem**.

A filesystem must keep track of which clusters are used and which are unused, and which files are using which clusters.

# File Allocation Table

A well-known and common filesystem called FAT uses a **f**ile **a**llocation **t**able to track these clusters. The file allocation table implements linked lists of clusters to keep track of each file's data on the disk.

FAT is highly popular on portable storage devices, such as flash drives and external hard disks. In this project, we will simulate the operation of a simplified FAT filesystem to understand how it works.

## Layout

A disk using the FAT filesystem is organised into three sections:

1. a reserved section containing data about the cluster size and other metadata (not simulated)
2. The file allocation table (represented in `filesystem.py`)
3. The data clusters (represented in `disk.py`)

We will focus on (2) and (3) for this project, simulating a disk of 256 (2^8 - 2) clusters, with each cluster storing 256 (2^8) bytes.

## File Allocation Table

The file allocation table for this simulation has 255 entries, with each entry consisting of the following fields:

- **Index:** int (`0 - 254`)  
  The index of the entry. This also corresponds to the address of the data cluster, i.e. entry 10 of the file allocation table stores information about the data in cluster 10.

- **Filename:** str  
  The filename of the entry. In the actual file allocation table there would be a maximum length limit on the filename, but we will not simulate that here.

- **Cluster:** int `(0 - 255)`  
  Indicates the index of the next cluster. This functions like the `next` attribute of a linked list.
  If an entry represents the last cluster of the file, it has the special value `255` (`0xFF` in hexadecimal).

- **Size**: int `(0 - 255)`
  Represents the amount of space (in bits) taken up by a file within the cluster.
  A value of `255` means all the space in the cluster is used up.
  Leftover space cannot be used by any other files.

An actual file allocation table contains many more fields, such as fields to store the file size and date/time of file creation, but we will not simulate these.

File allocation table representation:

| Index |  Filename | Cluster | Size |
|-------|-----------|---------|------|
|    0  |           |     5   |
|    1  | FILE1.TXT |     2   |  255 |
|    2  |           |     4   |  255 |
|    3  | FILE2.TXT |     7   |  255 |
|    4  |           |   255   |  113 |
|    5  |           |     8   |
|    6  | FILE3.TXT |   255   |  127 |
|    7  |           |   255   |   97 |
|    8  |   ...     |   ...   |  ... |
|  ...  |   ...     |   ...   |  ... |

This file allocation table describes three files:

1. `FILE1.TXT` stored in clusters 1, 2, 4
2. `FILE2.TXT` stored in clusters 3 & 7
3. `FILE3.TXT` stored in cluster 6 only

The entries `0` and `255` are reserved and not used for storing cluster records.

## Data Clusters

The data section of the disk is organised into 256 clusters, with the first and last cluster (address `0` and `255`) unused. The address of the cluster corresponds with the index of its entry in the file allocation table.

# Free Space List

In FAT, when storing a file, the first available entry (after index 0) is used.

The entry at `0` is thus special: `0` serves as a free space pointer to the head of a free space (linked) list.  
The tail of the free space list points to entry `255`, which is also a special value (since it is used to indicate the final cluster of a file).

These two values can be accessed via the `disk` module as `disk.HEAD` and `disk.TAIL` respectively.

# Further reading

[File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table) [Wikipedia]

[File Allocation Ssytem](https://www.ntfs.com/fat-allocation.htm) [NTFS.com]