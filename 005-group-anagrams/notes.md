# 5. Group Anagrams (Medium)

https://leetcode.com/problems/group-anagrams/

Group the strings in a list so that every group holds words made of the same letters.

- brute force: compare every pair of words with a sort or a count, roughly O(n^2 * k)
- key idea: two words are anagrams exactly when their sorted letters match, so the sorted string works as a dict key
- use defaultdict(list) and append each word under its key, then return the values
- gotcha: the output order doesn't matter, but the test check has to sort the groups before comparing
- empty string is a valid input, it just goes into its own group
- counting letters into a 26-slot tuple as the key is faster for long words, O(n * k) total

O(n * k log k) time, where n is the number of words and k the max length. O(n * k) space.
