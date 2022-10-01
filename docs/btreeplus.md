
# btreeplus - B+-Tree 

`btreeplus` provides core methods for searching, inserting, and deleting data for a 
[`B+Tree`](https://en.wikipedia.org/wiki/B%2B_tree) 

for expert reading: 
[B-tree_and_UB-tree](http://www.scholarpedia.org/article/B-tree_and_UB-tree)


# how to use

reading, inserting and deleting is done via `Context` class which is responsable for caching, preventing clashes,
and in-memory index manipulation prior writing all changes finally to the heap.
class methods using a `Context` have `_ctx` as naming convention.
if no ctx is provided a ctx is created on the fly and closed properly at the end.

refer also to test cases in [`tests`](https://github.com/kr-g/dryades/blob/main/tests)


# memory / file layout / limitations

see [`btreecore`](./btreecore.md) for layout and limitations

    
