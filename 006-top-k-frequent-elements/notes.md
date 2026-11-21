# 6. Top K Frequent Elements (Medium)

https://leetcode.com/problems/top-k-frequent-elements/

Return the k most frequent values in an array.

- brute force: count everything, sort the (value, count) pairs by count, take k. O(n log n)
- heap: keep a min-heap of size k while counting, O(n log k)
- key idea: counts are capped at n, so bucket the values by their count. walk the buckets from high to low and stop once you have k
- gotcha: the answer can come back in any order, so sort it if the checker wants a fixed order
- make the bucket list size n + 1 so a value appearing n times still has a slot

O(n) time, O(n) space.
