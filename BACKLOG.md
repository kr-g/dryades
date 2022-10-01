
Check
[`CHANGELOG`](./CHANGELOG.md)
for latest ongoing, or upcoming news.


# BACKLOG

##  heapfile

- acid atomic handling -> bimfile
  - journal file support
  - write before-image integration
- compact heap, reorg methods
- convert (encode/decode) of standard types (refactor from btree project)


## dllfile

- more testcases
- refactor heapfile handling
  - calc of offset to write to in [`pyheapfile`](https://github.com/kr-g/pyheapfile/)
  - check boundery
  - from_buffer/to_buffer methods
  
## btreecore

- more testcases
- convert (encode/decode) of standard types (refactor to heap file project)


## btreeplus

- refactor Context to pybtreecore
- refactor core methods of bplustree to btreecore
- refactor test cases



# OPEN ISSUES

refer to [issues](https://github.com/kr-g/dryades/issues)


# LIMITATIONS

-
