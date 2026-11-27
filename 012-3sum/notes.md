# 12. 3Sum (Medium)

https://leetcode.com/problems/3sum/

Find all unique triplets in the array that add up to zero.

- brute force: three nested loops plus a set to dedupe, O(n^3)
- key idea: sort, then fix the first number and run two sum ii (two pointers) on the rest
- if the sum is too small move lo up, too big move hi down
- duplicates are the annoying part. skip a repeated first value, and after a match skip
  repeated lo values. hi takes care of itself since lo moved
- early break once nums[i] > 0, everything to the right is positive too
- sorting in place is fine here since we return values, not indices

O(n^2) time, O(1) extra space ignoring the output (sort aside).
