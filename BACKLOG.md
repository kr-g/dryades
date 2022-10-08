
Check
[`CHANGELOG`](./CHANGELOG.md)
for latest ongoing, or upcoming news.


# BACKLOG

##  heapfile

- acid atomic handling 
  - journal file support
  - write before-image integration -> bimfile
- compact heap, reorg methods
- convert (encode/decode) of standard types (refactor from btree)


## dllfile

- more testcases
- refactor heapfile handling
  - calc of offset to write to in `heapfile`
  - check boundery
  - from_buffer/to_buffer methods
  
  
## btreecore

- more testcases
- convert (encode/decode) of standard types (refactor to heap file project)


## btreeplus

- refactor Context to btreecore
- refactor core methods of bplustree to btreecore
- refactor test cases


## common

- hexdump tool rework in all submodules!!!
-



# OPEN ISSUES

refer to [issues](https://github.com/kr-g/dryades/issues)


# LIMITATIONS

-
