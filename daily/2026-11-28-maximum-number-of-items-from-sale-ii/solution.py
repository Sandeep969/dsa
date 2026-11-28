# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
from itertools import product
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        top = max(f for f, _ in items)
        cnt = [0] * (top + 1)
        for f, _ in items:
            cnt[f] += 1
        multiples = [0] * (top + 1)
        for f in range(1, top + 1):
            if cnt[f]:
                multiples[f] = sum(cnt[m] for m in range(f, top + 1, f))

        # buying c copies of item i is worth c + min(c, d_i), so the first d_i copies count double
        cheapest = min(p for _, p in items)
        doubles = sorted((p, multiples[f] - 1) for f, p in items if p <= 2 * cheapest)
        left, k = budget, 0
        for p, d in doubles:
            take = min(d, left // p)
            k += take
            left -= take * p
            if take < d:
                break  # can't afford this price anymore, later ones cost more
        # whatever is left goes to single-value copies of the cheapest item
        return 2 * k + left // cheapest


def brute(items, budget):
    n, best = len(items), 0
    for counts in product(range(budget + 1), repeat=n):
        if sum(c * p for c, (_, p) in zip(counts, items)) > budget:
            continue
        total = sum(counts)
        for i in range(n):
            d = sum(1 for j in range(n) if j != i and items[j][0] % items[i][0] == 0)
            total += min(counts[i], d)
        best = max(best, total)
    return best


if __name__ == "__main__":
    import random

    s = Solution()
    assert s.maximumSaleItems([[1, 6], [2, 4], [3, 5]], 19) == 5
    assert s.maximumSaleItems([[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 35) == 7
    assert s.maximumSaleItems([[1, 5]], 3) == 0         # can't afford anything
    assert s.maximumSaleItems([[1, 1]], 5) == 5         # nothing to get for free
    assert s.maximumSaleItems([[1, 2], [1, 2]], 10) == 7  # each pair gives one free copy max
    assert s.maximumSaleItems([[1, 10], [2, 3]], 10) == 3  # double copy too pricey vs singles
    assert s.maximumSaleItems([[1, 10**9]] * 3, 10**9) == 2

    random.seed(7)
    for _ in range(400):
        n = random.randint(1, 3)
        items = [[random.randint(1, n), random.randint(1, 5)] for _ in range(n)]
        budget = random.randint(1, 8)
        assert s.maximumSaleItems(items, budget) == brute(items, budget), (items, budget)
    print("ok")
