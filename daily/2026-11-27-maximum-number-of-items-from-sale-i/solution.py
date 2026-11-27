# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
from itertools import product
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        top = max(f for f, _ in items)
        cnt = [0] * (top + 1)
        for f, _ in items:
            cnt[f] += 1

        # buying the first copy of item i gets 1 + (other items whose factor is a multiple of f_i)
        dp = [0] * (budget + 1)  # 0/1 knapsack over "first copy" of each item
        for f, p in items:
            gain = sum(cnt[m] for m in range(f, top + 1, f))  # includes itself, which is the +1
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + gain)

        # any extra copy is worth exactly 1, so spend leftover on the cheapest item
        cheapest = min(p for _, p in items)
        return max(dp[b] + (budget - b) // cheapest for b in range(budget + 1))


def brute(items, budget):
    n, best = len(items), 0
    for counts in product(range(budget + 1), repeat=n):
        if sum(c * p for c, (_, p) in zip(counts, items)) > budget:
            continue
        total = sum(counts)
        for i in range(n):
            if counts[i]:
                total += sum(1 for j in range(n) if j != i and items[j][0] % items[i][0] == 0)
        best = max(best, total)
    return best


if __name__ == "__main__":
    import random

    s = Solution()
    assert s.maximumSaleItems([[6, 2], [2, 6], [3, 4]], 9) == 4
    assert s.maximumSaleItems([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8) == 10
    assert s.maximumSaleItems([[5, 10]], 3) == 0          # can't afford anything
    assert s.maximumSaleItems([[1, 1]], 5) == 5
    assert s.maximumSaleItems([[2, 3], [2, 3]], 3) == 2   # same factor still counts as j != i
    assert s.maximumSaleItems([[1, 5], [7, 1], [9, 1]], 5) == 5

    random.seed(1)
    for _ in range(300):
        items = [[random.randint(1, 8), random.randint(1, 4)] for _ in range(random.randint(1, 3))]
        budget = random.randint(1, 6)
        assert s.maximumSaleItems(items, budget) == brute(items, budget), (items, budget)
    print("ok")
