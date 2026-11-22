# 7. Product of Array Except Self (Medium)

https://leetcode.com/problems/product-of-array-except-self/

For each index, return the product of every other element, without using division.

- brute force: for each i multiply everything else, O(n^2)
- division trick (total / nums[i]) is banned and also breaks on zeros anyway
- key idea: answer[i] = (product of stuff left of i) * (product of stuff right of i)
- first pass left to right fills res with prefix products, second pass right to left
  keeps a running `right` product and multiplies it in
- shift by one matters: res[i] uses nums[0..i-1], so update `right` after multiplying
- zeros just fall out naturally, no special casing needed

O(n) time, O(1) extra space (output array doesn't count).
