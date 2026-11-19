# 4. Majority Element (Easy)

https://leetcode.com/problems/majority-element/

Return the value that appears more than n/2 times. It is guaranteed to exist.

- brute force: count each value with a loop or dict, O(n^2) or O(n) space
- sorting: the majority always sits at index n//2 after sorting, O(n log n)
- key idea: boyer-moore voting. keep a candidate and a counter, match adds 1, mismatch subtracts 1, reset candidate when counter hits 0
- works because the majority can't be cancelled out by everything else combined
- the final candidate is the answer only because the problem guarantees a majority exists

O(n) time, O(1) space.
