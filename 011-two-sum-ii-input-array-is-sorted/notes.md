# 11. Two Sum II - Input Array Is Sorted (Medium)

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Same as two sum but the array is sorted, answer is 1-indexed and you're supposed to use constant extra space.

- brute force: every pair, O(n^2). the hashmap from two sum works too but uses O(n) space
- key idea: pointers at both ends. sum too small means move left up, too big means move right down
- why it's safe: if numbers[l] + numbers[r] < target, numbers[l] can't pair with anything left of r either, so drop it
- gotcha: return indices + 1, easy to forget
- l < r (not <=) so we never use the same element twice
- exactly one answer is guaranteed so the fallback return never really happens

O(n) time, O(1) space.
