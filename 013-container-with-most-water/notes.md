# 13. Container With Most Water (Medium)

https://leetcode.com/problems/container-with-most-water/

Pick two lines so the water trapped between them (width times the shorter height) is as big as possible.

- brute force: try every pair, O(n^2)
- key idea: start with the widest pair and move pointers inward
- always move the shorter side. keeping it and moving the taller one only shrinks width,
  and the height is still capped by the short wall, so those pairs can never win
- on ties it doesn't matter which side moves
- no sorting here, positions matter

O(n) time, O(1) space.
