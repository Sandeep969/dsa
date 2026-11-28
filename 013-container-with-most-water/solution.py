# https://leetcode.com/problems/container-with-most-water/
import random
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        best = 0
        while lo < hi:
            best = max(best, (hi - lo) * min(height[lo], height[hi]))
            # the shorter wall is the limit, moving the taller one can't help
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return best


def brute(height):
    n = len(height)
    return max(
        (j - i) * min(height[i], height[j]) for i in range(n) for j in range(i + 1, n)
    )


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([0, 0]) == 0
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    assert s.maxArea([1, 2, 1]) == 2
    assert s.maxArea([1, 2, 4, 3]) == 4
    for _ in range(300):
        h = [random.randint(0, 10) for _ in range(random.randint(2, 9))]
        assert s.maxArea(h) == brute(h), h
    print("ok")
