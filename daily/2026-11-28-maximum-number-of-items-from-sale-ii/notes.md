# 3947. Maximum Number of Items From Sale II (Medium)

https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

Same sale as part i, but now every bought copy can earn one free item, each (i, j) pair only once. Maximize total copies within budget.

- brute force: try every count vector and add up the free copies, exponential
- d_i = how many other items have a factor that is a multiple of f_i. count via harmonic loop over multiples
- buying c copies of item i gives c + min(c, d_i). so item i has d_i "double" copies at price p_i, the rest are worth 1
- any single-value copy is best bought at the cheapest price m
- a double copy at price p beats spending p on singles only when p <= 2m, and taking cheaper doubles first is always fine
- so: sort doubles by price, grab as many as fit while p <= 2m, then dump the leftover into singles at m
- budget is 1e9 so no knapsack this time, the greedy works because every copy is worth 1 or 2
- checked against brute force on small random inputs

O(n log n) time, O(n) space.
