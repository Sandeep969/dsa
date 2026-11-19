# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore voting: a candidate survives as long as it outnumbers the rest
        candidate, count = None, 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([1]) == 1
    assert s.majorityElement([6, 5, 5]) == 5
    assert s.majorityElement([-1, -1, 0, -1]) == -1
    assert s.majorityElement([0, 0, 0, 1, 1]) == 0
    assert s.majorityElement([7, 7, 7, 7, 1, 2, 3]) == 7
    print("ok")
