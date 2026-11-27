# 3946. Maximum Number of Items From Sale I (Medium)

https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

Buy items within a budget. The first copy of an item also gives you a free copy of every other item whose factor is a multiple of its factor. Maximize total copies.

- only the first copy of each item matters for the bonus, every extra copy is worth exactly 1
- so first copies = 0/1 knapsack, value of item i = number of items whose factor is a multiple of f_i (counting itself)
- leftover budget goes to the cheapest item, `(budget - spent) // min_price`
- answer = max over spent of `dp[spent] + leftover // cheapest`
- multiples count: bucket items by factor, then loop f, 2f, 3f... up to max factor (harmonic sum, cheap)
- gotcha: two items with the same factor both give each other a free copy
- checked against a brute force on small random inputs

O(n * budget + F log F) time, O(budget + F) space, F = max factor.
