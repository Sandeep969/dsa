# 3. Valid Anagram (Easy)

https://leetcode.com/problems/valid-anagram/

Check if two strings use exactly the same letters the same number of times.

- brute force: sort both and compare, O(n log n)
- key idea: count chars, +1 for s and -1 for t, everything should end at 0
- check lengths first, different lengths can never be anagrams
- doing both strings in one zip loop keeps it to a single dict
- `Counter(s) == Counter(t)` is the lazy version and totally fine
- follow up with unicode: dict handles it, a fixed size-26 array would not

O(n) time, O(k) space where k is number of distinct chars (O(1) for lowercase only).
