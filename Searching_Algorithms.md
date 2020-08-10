------------Searching Algorithms------------

Objectives

- Describe what a searching algorithm is
- Implement linear search on arrays
- Implement binary search on sorted arrays
- Implement a naive string searching algorithm
- Implement the KMP string searching algorithm

A searching algorithm looks for a specific value/item (can be in an array, string, dictionary, etc.) and may return the index, or the item itself. If the value/item is not found, it may return -1.

Linear Search

A searching alogrithm that goes through each item in an array (or other iterable), starting from the first index up to the last. (many methods and functions in python are using linear search!)

Time Complexity (linear search)

Looking at the worst case (if item is not in array or is the very last index), as the length of input n grows, the time grows roughly in proportion to n. This means if the array is 5000 elements long, then it will have to go through each of the indices until it finds the correct item. Of course, the best case is if the first index is the correct item every time (O(1)). As a result, the time complexity of the linear search algorithm is O(n), hence the name, linear search!

Binary Search

Another searching algorithm that uses the DIVIDE AND CONQUER method.

- Binary Search is a much faster form of search.
- Rather than eliminating one element at a time, you can eliminate HALF of the remaining elements at a time.
- Binary search only works on SORTED ARRAYS! (iterables)

Time Complexity

The best case would mean that the middle point chosen of the sorted array is the value we are looking for (O(1)). However, the worst case would mean that every time the array size is doubled, we add one extra step (size 32 is 2^5, size 64 becomes 2^6). Therefore, the time complexity of Binary Search (worst or average case) is O(log n)

Naive String Search

A searching algorithm that searches for sub-strings within a string.

Ex. Find "omg" ---> "owmomgzomg" (2 matches)
Ex. Find "haha" ---> "He said haha out loud!" (1 match)
