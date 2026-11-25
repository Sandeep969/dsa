# 10. Valid Palindrome (Easy)

https://leetcode.com/problems/valid-palindrome/

Check if a string reads the same both ways once you drop non-alphanumeric chars and ignore case.

- brute force: build a cleaned lowercase string and compare it with its reverse, O(n) but extra O(n) space
- key idea: two pointers from both ends, skip junk chars on each side, compare lowercased chars
- move only one pointer per skip step so the l < r check stays correct
- digits count, so "0P" is false (easy to miss if you only check letters)
- empty string or all punctuation is a palindrome

O(n) time, O(1) space.
