
# bimfile - before image file (BIM File) - copy on write

`bimfile` implements [`copy-on-write`](https://en.wikipedia.org/wiki/Copy-on-write) 
for file based resources

before a change to a file is written all changes are recorded in another file.


# memory / file layout

## header record

| name | size (bytes) | description |
| --- | --- | --- | 
| blen | xpos | original size of file prior changes |
| mark | xpos | 0xdeafbeef as start marker |
| magick | 4 | 0xdeafbeef as magic marker |

## change record

| name | size / value | description |
| --- | --- | --- | 
| fpos | xpos | pointer to file change |
| blen | xpos | size of change segment |
| magick | 4 | 0xdeafbeef as magic marker |

a list of change records is stored as continuously stream after the header record


## limitation

- xpos (default) == 8 bytes ==> 2**(8*8) 
== 18.446.744.073.709.551.616 bytes total file size (default)
- the default can be changed by creating `BeforeImageFile` with a different `link_size`
- 


