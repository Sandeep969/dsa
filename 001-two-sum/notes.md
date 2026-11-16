# 1. Two Sum (Easy)

https://leetcode.com/problems/two-sum/

Find indices of two numbers that add up to target.

- brute force: check every pair, O(n^2)
- better: for each x, the number I need is `target - x`. keep a dict of value -> index for
  everything seen so far and check it before inserting x
- checking before inserting matters, otherwise `[3]` with target 6 would match 3 with itself
- [3, 3] still works because the first 3 is already in the dict when we reach the second one

O(n) time, O(n) space.

Could also sort + two pointers in O(n log n) but then you lose the original indices.
