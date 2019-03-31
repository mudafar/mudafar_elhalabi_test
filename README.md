# This repo includes the solution for the technical test.  

Note:  Time spent: 1 day

## Question A: 
Solution can be found in `overlap.py`.

The provided function `is_lines_segments_overlap()` handles the following cases:
- Sorted values as the provided in the example.
- Unsorted values, e.g: x1 > x2

## Question B: 
Solution can be found in `version_checker.py`

The solution given in `version_checker()` can handle the given example and any  valid nested sub-versions, e.g:
- 1, 2
- 1.1 , 1.2
- 1.1.4.2, 1.1.55.1
- 1.2v,  1.23v 


Note: also the version input can includes the letter `v` as it maybe common in some nomenclature.

 

## Question C: 

Solution can be found in `tlru.py` 

For this question I just built the base structure aka- `class` to manage a time aware least
recently used cache, that is with time expiration.

The class include its required sub-classes and the most fundamentals test cases.  


The `class`  `TimeAwareLeastRecentlyUsed` includes two methods:
- `put(key, value)`: insert a new value.
- `get(key)`: get the value for the given key if exist else return `None`.