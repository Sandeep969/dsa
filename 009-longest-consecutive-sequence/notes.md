# 9. Longest Consecutive Sequence (Medium)

https://leetcode.com/problems/longest-consecutive-sequence/

Length of the longest run of consecutive integers in an unsorted array, needs to be O(n).

- brute force: sort and walk the array counting runs, O(n log n), doesn't meet the O(n) ask
- key idea: put everything in a set. a number starts a run only if `x - 1` is not in the set,
  so only count forward from those starting points
- each number gets visited at most twice (once in the loop, once while extending a run),
  which is why it's still O(n) even with the inner while
- loop over the set, not nums, otherwise lots of duplicates of a run start redo the same work
- duplicates don't count towards length, the set handles that for free
- empty input returns 0

O(n) time, O(n) space.
