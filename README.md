**Prerequisites:** Linked List (using array implementation)

# Instructions

## Research filesystem

1. Read the description of the file allocation table in `file-allocation-table.md`.

## Implement filesystem

`disk.py` has been implemented for you.  
- `disk.read(address: int) -> bytes`  
  Reads raw binary data from the disk cluster at the given address.
- `disk.write(address: int, cluster_data: bytes)`  
  Writes raw binary data to the disk cluster at the given address.
- `disk.ADDR_LIMIT`  
  The address of the last disk cluster.
- `disk.CLUSTER_SIZE`  
  The size of each cluster in the disk.

The above constants should be used wherever required, instead of using hardcoded values.  

The above methods should be used for all disk reads and writes; the disk storage should not be directly accessed.  

You should not need to refer to the source code in `disk.py` to be able to use it.


2. Using the constants and functions from `disk`, implement the following functions in `filesystem.py`:
   - `_index_of(filename) -> index[int]`  
     Searches for and returns the first entry index of the filename.
   - `_next_free() -> index[int]`  
     Retrieves the index of the next free entry from the free space list.
   - `disk_space() -> bytes_free[int]`  
     Returns the number of bytes available in the free clusters of the disk.
   - `save(filename, data: str)`  
     Saves `strdata` to the disk with the given `filename`.
     All saved data is assumed to be in ASCII text format.  
     (Reminder: Python strings must be `.encode()`d to `bytes` before being passed to `disk.write()`.)
   - `load(filename) -> text[str]`  
     Loads the text data for `filename`.  
     Remember to truncate the unused bytes from the data in the cluster.  
     (Reminder: bytes from `disk.read()` have to be `.decode()`d back into text.)
   - `delete(filename)`  
     This deletes the entries for `filename` from the file allocation table.  
     Note that the data in the disk clusters for `filename` need not be cleared; the clusters are simply marked as free in the file allocation table, and data in them is ignored.

You may implement any other helper functions as necessary. Prefix them with an underscore (`_`), following `_index_of()` and other helper functions, to mark them as non-public functions.

## Test filesystem

Some test data has been provided in the files `file1.txt`, `file2.txt`, and `file3.txt`.

In `main.py`,

3. Display the free space in the filesystem.
4. Save the data from each file into the filesystem, using uppercase versions of the filenames (e.g. `FILE1.TXT`).  
   As each file is saved, display the following information with appropriate labels:
   - File size (number of characters in the text file data)
   - Remaining disk space (in bytes)
5. Read each file from the filesystem, and verify that its contents are unchanged from the original.
6. Delete the files in reverse order (i.e. if you saved `file1.txt` first and `file3.txt` last, then delete `FILE3.txt` first and `FILE1.txt` last).  
   As each file is deleted, display the following information with appropriate labels:
   - Remaining disk space (in bytes)  
   
   Verify that the values match up with those from Step 4.  
   You can also use the unit tests, which carry out the above steps, to verify.

Nice! You have simulated a simple filesystem 🎉
