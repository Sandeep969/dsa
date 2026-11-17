# 2. Contains Duplicate (Easy)

https://leetcode.com/problems/contains-duplicate/

Return true if any value shows up more than once in the array.

- brute force: compare every pair, O(n^2)
- sorting works too, then duplicates sit next to each other, O(n log n) and no extra space
- key idea: walk once with a set, if x is already in it we're done
- early return means we often stop before reading the whole array
- one-liner `len(set(nums)) != len(nums)` is fine but always builds the full set

O(n) time, O(n) space.
